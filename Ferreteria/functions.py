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


# Cargamos las credenciales de manera global
# para que todos las puedan usar
with open('credentialsDB.json') as file:
    credentials = json.load(file)

# Seleccionamos las credenciales
userDB = credentials["credentials"][0]["user"]
passwordDB = credentials["credentials"][0]["password"]
hostDB = credentials["credentials"][0]["host"]
nameDB = credentials["credentials"][0]["database"]

"""
###############################
######### FUNCIONES ###########
###############################
######### INVENTARIO ##########
###############################
"""

##############################################################################
"""
Función: DESPLEGAR LOS PRODUCTOS DEL INVENTARIO
"""
def desplegar_lista_inventario():
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        query = ('SELECT * FROM Inventario;')
        cursor.execute(query)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordDLI", False)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existDLI", False)
        else:
            return(err, False)

        return ("No fue posible desplegar la lista", False)


    mydata = []
    #datos = cursor.fetchall()
    for (ID, Nombre, Especificaciones, Cantidad, Unidad, Precio) in cursor:
        mydata.append([ID, Nombre, Especificaciones, Cantidad, Unidad, Precio])

    cnx.commit()
    cnx.close()
    return (mydata, True)

##############################################################################
"""
Función: DESPLEGAR LOS PRODUCTOS POR LETRA
"""
def desplegar_lista_inventario_letra(letter):
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        query = ('SELECT * FROM Inventario WHERE  Nombre_Producto LIKE %s"%";')
        cursor.execute(query, (letter,))
        datos = cursor.fetchall()
        #print(datos)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordDLIL", False)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existDLIL", False)
        else:
            return (err, False)

        return ("No fue posible filtrar la lista por letra", False)

    mydata = []
    for (ID, Nombre, Especificaciones, Cantidad, Unidad, Precio) in datos:
        mydata.append([ID, Nombre, Especificaciones, Cantidad, Unidad, Precio])

    cnx.commit()
    cnx.close()
    #print(mydata)
    return (mydata, True)

##############################################################################
"""
FUNCION: BUSCAR POR NOMBRE
"""
def buscar_articulo_nombre(word):
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        query = ("SELECT * FROM Inventario WHERE Nombre_Producto = %s;")
        cursor.execute(query,(word,))
        #datos = cursor.fetchone()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordBAN", False)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existBAN", False)
        else:
            return (err, False)

        return ("No fue posible hacer la búsqueda por nombre", False)

    mydata = []
    for (ID, Nombre, Especificaciones, Cantidad, Unidad, Precio) in cursor:
        mydata.append([ID, Nombre, Especificaciones, Cantidad, Unidad, Precio])

    cnx.commit()
    cnx.close()
    print(mydata)
    return (mydata, True)

##############################################################################
"""
#############################################################
Las siguiente funciones serán para realizar las operaciones #
elementales: Añadir, Modificar y Eliminar####################
#########################################
"""
##############################################################################
"""
FUNCION: BUSQUEDA MEDIANTE CODIGO
"""
def busqueda_por_codigo(code):
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        query = ("SELECT * FROM Inventario WHERE ID_Producto = %s;")
        cursor.execute(query,(code,))
        #datos = cursor.fetchone()

        #print("dats", cursor)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordBPC", False)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existBPC", False)
        else:
            return (err, False)

        return ("No fue posible hacer la búsqueda por código", False)

    mydata = []
    for (ID, Nombre, Especificaciones, Cantidad, Unidad, Precio) in cursor:
        mydata.append([ID, Nombre, Especificaciones, Cantidad, Unidad, Precio])

    cnx.commit()
    cnx.close()

    if len(mydata) == 0:
        return("No se encontro un producto con ese código", False)
    else:
        #print("mydata:", mydata)
        return (mydata, True)

##############################################################################
"""
FUNCION: ELIMINAR PRODUCTO DEL INVENTARIO
"""
def eliminar_por_codigo(code):
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        #DELETE FROM PE_Empleado WHERE Sueldo >= 10000;
        query = ("DELETE FROM Inventario WHERE ID_Producto = %s;")
        cursor.execute(query,(code,))
        #datos = cursor.fetchone()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordEPC", False)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existEPC", False)
        else:
            return (err, False)

        return ("No fue posible eliminar el producto", False)

    cnx.commit()
    cnx.close()
    return ("Producto eliminado correctamente", True)

##############################################################################
"""
FUNCION: AÑADIR PRODUCTO AL INVENTARIO
"""
def add_producto(code, name, specifications, quantity, unity, price):
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        data_query = (code, name, specifications, quantity, unity, price)
        #INSERT INTO ex2_Asignatura (Clave, Nombre, Semestre, Creditos, Clave_Plan, Tipo) VALUES ('0117','Pensamiento del ambiente','0',6,'1800', 'Optativa');
        query = ("INSERT INTO Inventario (ID_Producto, Nombre_Producto, Especificaciones_Producto, Cantidad_Producto,  Unidad_Producto, Precio_Producto) VALUES (%s, %s, %s, %s, %s, %s);")
        cursor.execute(query, data_query)
        #datos = cursor.fetchone()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordAP", False)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existAP", False)
        else:
            return (err, False)

        return ("No fue posible añadir el producto", False)

    cnx.commit()
    cnx.close()
    return ("Producto añadido correctamente", True)

##############################################################################
"""
FUNCION: MODIFICAR PRODUCTO DEL INVENTARIO
"""
# --------------------LA DEJAMOS PENDIENTE-----------------------------------#


#UPDATE tabla SET columna = valor [WHERE condiciones];
def update_producto(code, name, specifications, quantity, unity, price):
    # Haremos algunas manipulaciones en los datos para formar la query & data_query
    columnas_query = {"Nombre_Producto": name, "Especificaciones_Producto": specifications,
     "Cantidad_Producto": quantity, "Unidad_Producto": unity, "Precio_Producto": price}

    values = columnas_query.values() #Obtenemos los valores de cada clave
    values = list(values)
    print("VALORES:", values)
    changes = values.count("") # Contamos cuantos valores con cero hay
    print("Cabmios:", changes)
    if changes == 3:
        # Si hay tres valores con cero significa que solo es una columna en la query
        for key, value in columnas_query.items():
            #key_by_value = list(columnas_query.keys())[list(columnas_query.values()).index(value)]
            #print(key_by_value)
            if  value != '':
                #my_query = "UPDATE inventario SET %s = %s WHERE ID_Producto = %s;"
                print(key, value, code)
                data_query = (key, str(value), code)
                break

    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        print("mis datos consulta: ", data_query)
        query = ("UPDATE inventario SET %s = %s WHERE ID_Producto = %s;")
        cursor.execute(query, data_query)
        cursor.execute(my_query)
        #datos = cursor.fetchone()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordUP", False)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existUP", False)
        else:
            return (err, False)

        return ("No fue posible actualizar el producto", False)

    cnx.commit()
    cnx.close()
    return ("Producto actualizado correctamente", True)

##############################################################################

"""
FUNCION: RELLENAR PARAMETROS EN VENTA
"""
def add_fast(code):
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor()
        query = ("SELECT ID_Producto, Nombre_Producto, Cantidad_Producto, Unidad_Producto FROM Inventario WHERE ID_Producto = %s;")
        cursor.execute(query,(code,))
        try:
            query2 = ("SELECT SUM(Precio_Total) FROM Carrito;")
            cursor2.execute(query2)
            total = 0
            for value in cursor2:
                print(value)
                total = float(value[0])
        except:
            total = 0

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordBPC", False, total == 0)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existBPC", False, total == 0)
        else:
            return (err, False, total == 0)

        return ("No fue posible hacer la búsqueda por código", False, total == 0)

    mydata = []
    for (ID, Nombre, Cantidad, Unidad) in cursor:
        mydata.append([ID, Nombre, Cantidad, Unidad])


    cnx.commit()
    cnx.close()

    if len(mydata) == 0:
        return("No se encontro un producto con ese código", False, total)
    else:
        return (mydata, True, total)

"""
FUNCION: PARA AÑADIR AL CARRITO
"""
def add_to_car(code, name, quantity, unity, price):
    try:
        cnx = mysql.connector.connect(user=userDB, password=passwordDB, host=hostDB, database=nameDB)
        cursor = cnx.cursor(); cursor2 = cnx.cursor()
        data_query = (code, name, quantity, unity, price)
        #INSERT INTO ex2_Asignatura (Clave, Nombre, Semestre, Creditos, Clave_Plan, Tipo) VALUES ('0117','Pensamiento del ambiente','0',6,'1800', 'Optativa');
        query = ("INSERT INTO Carrito (ID_Producto, Nombre_Producto, Cantidad,  Unidad, Precio_Total) VALUES (%s, %s, %s, %s, %s);")
        cursor.execute(query, data_query)
        try:
            query2 = ("SELECT SUM(Precio_Total) FROM Carrito;")
            cursor2.execute(query2)
            total = 0
            for value in cursor2:
                total = float(value[0])
        except:
            total = 0

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return ("Something is wrong with your user name or passwordAP", False, total == 0)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return ("Database does not existAP", False, total == 0)
        else:
            return (err, False, total == 0)

        return ("No fue posible añadir el producto al carrito", False, total == 0)

    cnx.commit()
    cnx.close()
    return ("Producto añadido al carrito correctamente", True, total)
