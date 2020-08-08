#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Title-Project: Ferreteria
Code: Principal
@uthor: José Vidal Cardona Rosas
About: Work in back-end for the control of web page
"""
# Importamos la librería
from flask import Flask, render_template, request
import json
import webbrowser
import mysql.connector
from mysql.connector import errorcode
# Cargamos las credenciales
with open('credentialsDB.json') as file:
    credentials = json.load(file)

# Seleccionamos las credenciales
userDB = credentials["credentials"][0]["user"]
passwordDB = credentials["credentials"][0]["password"]
hostDB = credentials["credentials"][0]["host"]
nameDB = credentials["credentials"][0]["database"]

# Creamos el objeto de flask que nos servira para lanzar el servidor
# y la página web
app = Flask(__name__)

#Indicamos la ruta para la página principal, que corresponde a la ruta donde
# nosotros estamos corriendo el archivo
@app.route("/")
# Definimos la función para la ruta de la página principal
def index():
    return (render_template("index.html"))

########################################################################
"""
Apartado: REALIZAR VENTAS
"""
@app.route("/Realizar-Venta")
def RealizarVenta():
    return (render_template("RealizarVenta.html"))

########################################################################
"""
Apartado: VENTAS DEL DÍA
"""
@app.route("/Ventas-Del-Dia")
def VentasDelDia():
    return (render_template("VentasDelDia.html"))

########################################################################
"""
Apartado: INVENTARIO
"""
@app.route("/Inventario")
def Inventario():
    import functions
    # Función para desplegar la lista de invetnario
    mydata = functions.desplegar_lista_inventario()
    return (render_template("Inventario.html", productos = mydata))


@app.route("/Inventario/Actualizar-Inventario")
def InventarioActualizar():
    return (render_template("InventarioActualizar.html"))

#----FUNCIONES PARA *DESPLEGAR* LA LISTA DE ARTICULOS EN EL INVENTARIO------------
@app.route("/Inventario/filterInventario", methods = ['POST'])
def filterInventario():
	mydata = Processing.displayGroup(cnx)
	return render_template("groups.html", dataSet = mydata)


########################################################################
"""
Apartado: Contacto
"""
@app.route("/Contacto")
def Contacto():
    return (render_template("Contacto.html"))



# Función principal
if __name__ == "__main__":
    # Ejecutamos el objeto
    #webbrowser.open_new_tab('http://127.0.0.1:5000/')
    app.run(debug=True)
