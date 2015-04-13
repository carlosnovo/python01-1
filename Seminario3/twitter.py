#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
import twitter
import io
import json

app = Flask(__name__)
GoogleMaps(app)
lista_final = []

#Funcion: inicio de sesion con la APP de Twitter
#Accion: Realiza una conexión con la APP de Twitter y devuelve su variable
#Para evitar intrusiones, nosotros hemos quitado nuestras credenciales para la subida a GitHub
#Es necesario que coloque sus credenciales para la prueba del programa
def inicio_sesion():
	CONSUMER_KEY = 'consumer key'
	CONSUMER_SECRET = 'consumer secret'
	OAUTH_TOKEN = 'clave token'
	OAUTH_TOKEN_SECRET = 'clave token secret'

	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api

#Funcion: Buscar tweets en la red
#Accion: Realiza una busqueda basada en un texto, sobre un area geolocalizada (España aproximadamente) y con una cantidad máxima de lectura de 100 tweets
def buscar_tweets():
	listado_tweets = usuario.search.tweets(q='Real Madrid',geocode='36.516380894202264,-6.282446299999947,500km',count=100)
	return listado_tweets

#Función para grabar la información en formato JSON
def guardar_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def leer_json(filename):
    return json.loads(open(filename).read())

#Funcion: Recorre los tweets leidos que cumplen las condiciones antes expuestas
#Accion: Devuelve una lista con las geolocalizaciones de dichos tweets.
def recorrer_tweets(fichero):
	lista = []
	for estado in fichero["statuses"]:
	 	 if estado["coordinates"]!= None:
		 	 coordenadas = estado["coordinates"]
			 xy=[coordenadas.values()[1][1] , coordenadas.values()[1][0]]
			 lista.append(xy)
	return lista


#Creamos el Mapa con los valores que queramos
@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=40.45,
        lng=3.75,
        markers=lista_final,
        style="height:600px;width:600px;margin:0", 
        zoom=4
    )
    return render_template('template2.html', mymap=mymap)


usuario = inicio_sesion()
lista_tweets = buscar_tweets()
guardar_json('contenedor',lista_tweets)
datos = leer_json('contenedor.json')
lista_final = recorrer_tweets(datos)

#Ejecutamos la App
if __name__ == "__main__":
     app.run(debug=True)
     
    
