#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
import twitter
import io
import json
from flask import request


app = Flask(__name__)
GoogleMaps(app)
lista_final = []

#Funcion: inicio de sesion con la APP de Twitter
#Accion: Realiza una conexión con la APP de Twitter y devuelve su variable
#Para evitar intrusiones, nosotros hemos quitado nuestras credenciales para la subida a GitHub
#Es necesario que coloque sus credenciales para la prueba del programa
def inicio_sesion():
	CONSUMER_KEY = 'c8x7H5zljiA16UVqWU3EOqiv2'
	CONSUMER_SECRET = 'rQbk505hueBLKuYW3XzUih1T1BLBUpkx24Uf9MYuzDZXVSFrtp'
	OAUTH_TOKEN = '346838383-8lNRR1Hy5zIhzQcDZRKv9gcIEKqHcgkAsbwtWsmC'
	OAUTH_TOKEN_SECRET = 'a2dta5sj2UeYax66tqbpADf1SN7HBJNp3A7SS5IRB7UDG'

	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api

#Funcion: Buscar tweets en la red
#Accion: Realiza una busqueda basada en un texto, sobre un area geolocalizada (España aproximadamente) y con una cantidad máxima de lectura de 100 tweets
def buscar_tweets(texto):
	usuario = inicio_sesion()
	listado_tweets = usuario.search.tweets(q=texto,geocode='36.516380894202264,-6.282446299999947,500km',count=100)
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
@app.route("/buscar", methods=['POST'])
def buscar():
	datos = request.form['text']
	lista_tweets = buscar_tweets(datos)
	guardar_json('contenedor',lista_tweets)
	fich = leer_json('contenedor.json')
	lista_final = recorrer_tweets(fich)
	mymap = Map(
		identifier="view-side",
		lat=40.3450396,
		lng=-3.6517684,
		zoom=6,
		markers=lista_final,
		style="height:800px;width:800px;margin:0;"
	) 
	return render_template('mapa.html', mymap=mymap)

@app.route("/")
def index():
	return render_template('index.html')


#lista_tweets = buscar_tweets()

#datos = leer_json('contenedor.json')
#lista_final = recorrer_tweets(datos)

#Ejecutamos la App
if __name__ == "__main__":
     app.run(debug=True)
     
    
