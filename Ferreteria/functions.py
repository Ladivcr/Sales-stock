#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Title-Project: Ferreteria
Code: Secondary
@uthor: José Vidal Cardona Rosas
About: Work in back-end for the control of web page
"""

# Importamos la librería
from flask import Flask, render_template,request,session,g,redirect,url_for,flash
import json
import webbrowser
import mysql.connector
from mysql.connector import errorcode


# Cargamos las credenciales de manera global para que todos
# las puedan usar
with open('credentialsDB.json') as file:
    credentials = json.load(file)

# Seleccionamos las credenciales
userDB = credentials["credentials"][0]["user"]
passwordDB = credentials["credentials"][0]["password"]
hostDB = credentials["credentials"][0]["host"]
nameDB = credentials["credentials"][0]["database"]


def añadir_al_inventario(IDProducto, NombreProducto, Especificaciones, CantidadProducto, Precio):
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        print("Conexión exitosa!\n")
        query = ("INSERT INTO inventario(ID_Producto, Nombre_Producto, Especificaciones_Producto, Cantidad_Producto, Precio_Producto) VALUES(%s, %s, %s ,%s ,%s)")
        data_query = (IDProducto, NombreProducto, Especificaciones, CantidadProducto, Precio)
        cursor.execute(query,data_query)
        cnx.commit()
        print("Querys efectuadas correctamente...")
        cnx.close()
        return (True)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:

            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("Error: ",err)
        return False

def desplegar_lista_inventario():
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        query = ('SELECT * FROM inventario;')
        cursor.execute(query)
    except:
        return("<h1> Algo a fallado al realizar la consulta a Inventario. Por favor contacte al administrador</h1>")

    mydata = []
    #datos = cursor.fetchall()
    for (ID, Nombre, Especificaciones, Cantidad, Precio) in cursor:
        #mydata2[hashtag]=[quantity, str(date)]
        mydata.append([ID, Nombre, Especificaciones, Cantidad, Precio])

    cnx.commit()
    cnx.close()
    return(mydata)
