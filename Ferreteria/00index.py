#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Title-Project: Ferreteria
Code: Principal
@uthor: José Vidal Cardona Rosas
About: Work in back-end for the control of web page
"""
# Importamos la librería
from flask import Flask, render_template, request, flash, redirect, url_for
#from flask import Flask, render_template,request,session,g,redirect,url_for,flash
import webbrowser

# Creamos el objeto de flask que nos servira para lanzar el servidor
# y la página web
app = Flask(__name__)


# Establece llave secreta
app.secret_key = "Eladiv"

#Indicamos la ruta para la página principal, que corresponde a la ruta donde
# nosotros estamos corriendo el archivo
@app.route("/")
# Definimos la función para la ruta de la página principal
def index():
    return (render_template("index.html"))


##############################################################################
"""
Apartado: REALIZAR VENTAS
"""
@app.route("/Realizar-Venta")
def RealizarVenta():
    import functions
    total, state_query = functions.total_sale()
    #print("EL TOTAL: {0} Y EL ESTADO: {1}".format(total, state_query))
    if state_query == False:
        message = "Algo a fallado a la hora de realizar la suma"
        return (render_template("RealizarVenta.html", longitud = 0, precioTotal = total, error = message))
    else:
        return (render_template("RealizarVenta.html", longitud = 0, precioTotal = total))


@app.route("/Realizar-Venta/ControlVenta", methods = ['POST'])
def ControlVenta():
    import functions
    code = request.form['product_code']
    try:
        add_by_code = request.form['adding']
        add_by_code = str(add_by_code)
        #-------------AÑADIR ATRIBUTOS POR CODIGO------------------------------------#
        if add_by_code == "AddCode":
            try:
                mydata, state = functions.add_fast_parameters(code)
                total, state_query = functions.total_sale()
                #print("MIS DATOS: {0} - SU ESTADO: {1}\nMY QUERY: {2} - SU ESTADO: {3}".format(mydata, state, total, state_query))
                if state == True and state_query == True:
                    return (render_template("RealizarVenta.html", producto = mydata, longitud = len(mydata[0]), precioTotal = total))
                elif state == False :
                    error = str(mydata)
                    message = ("{0}".format(mydata))
                    #message = "Hubo un error en alguna de las dos funciones, revisalo"
                    return (render_template("RealizarVenta.html", error = message, longitud = 0, precioTotal = total))
            except:
                return("<h1> ¡Ups! Parece que este error en CONTROLVENTA no lo vio el administrador</h1>")
        else:
            return("<h1>¡Hiuston, tenemos un problema, el valor del botón adding no es correcto!</h1>")

    except:
        try:
            add_carrito = request.form['btn_carrito']
            add_carrito = str(add_carrito)
            #-------------------AÑADIR EL PRODUCTO AL CARRITO DE COMPRAS-----------------#
            if add_carrito == "addCar":

                try:
                    name = request.form['product_name']
                    quantity = request.form['product_quantity']
                    unity = request.form['product_unity']
                    price_sale = request.form['sale_price']

                    if name == "d" or quantity == "d" or unity == "d" or price_sale == "d" or name == " " or quantity == " " or unity == " " or price_sale == " ":
                        total, state_query = functions.total_sale()
                        if state_query == True:
                            message == "Por favor introduce todos los datos"
                            return (render_template("RealizarVenta.html", error = message, longitud = 0, precioTotal = total))
                        else:
                            return ("<h1>Vaya, parece que hay un error en state_query y no llenaste todos los campos</h1>")

                    else:
                        mydata, state = functions.add_to_car(code, name, quantity, unity, price_sale)
                        total, state_query = functions.total_sale()
                        #print("MIS DATOS PAL CARRO: {0} - SU ESTADO: {1}\nMY QUERY: {2} - SU ESTADO: {3}".format(mydata, state, total, state_query))
                        if state == True and state_query == True:
                            error = str(mydata)
                            message = ("{0}".format(mydata))
                            #message = "Producto añadido al carrito correctamente"
                            return (render_template("RealizarVenta.html", longitud = 0, precioTotal = total, error = message))
                        elif state == False :
                            error = str(mydata)
                            message = ("{0}".format(mydata))
                            return (render_template("RealizarVenta.html", error = message, longitud = 0, precioTotal = total))
                except:
                    # Debo de controlar más este error añadiendo mejor un mensaje
                    return("<h1> ¡Ups! Parece que este error al AÑADIRALCARRITO no lo vio el administrador</h1>")
            else:
                return("<h1>¡Hiuston, tenemos un problema, el valor del botón carrito no es correcto!</h1>")

        except:
            return("<h1> We're working a lot but we have an error :( in request btn_carrito</h1>")


##############################################################################
"""
Apartado: INVENTARIO
"""
@app.route("/Inventario")
def Inventario():
    import functions
    # Función para desplegar la lista de inventario
    mydata, state = functions.desplegar_lista_inventario()
    #print("mydata en Inventario", mydata)
    if state == True:
        return (render_template("Inventario.html", productos = mydata))
    if state == False:
        #print(mydata)
        mydata = str(mydata)
        message = ("{0}".format(mydata))
        return (render_template("Inventario.html", error = message, productos = []))
    else:
        return ("<h1>¡Ups! Parece que este error en INVENTARIO no lo habíamos contemplado. Por favor contacte al administrador</h1>")

#---FUNCION PARA *FILTRAR* LA LISTA DE ARTICULOS EN EL INVENTARIO------------#
@app.route("/Inventario/FilterInventario", methods = ['POST'])
def FilterInventario():
    import functions
    letter = request.form['valuesLetter']
    letter = letter.lower()
    #print(letter)
    mydata, state = functions.desplegar_lista_inventario_letra(letter)
    #print(mydata)
    if state == True:
        return (render_template("Inventario.html", productos = mydata))
    if state == False:
        mydata = str(mydata)
        message =("{0}".format(mydata))
        return (render_template("Inventario.html", error = message, productos = []))
    else:
        return ("<h1>¡Ups! Parece que este error en FILTERINVENTARIO no lo habíamos contemplado. Por favor contacte al administrador</h1>")

#---FUNCION PARA *BUSCAR* ARTICULOS POR NOMBRE EN EL INVENTARIO--------------#
@app.route("/Inventario/SearchInventario", methods = ['POST'])
def SearchInventario():
    import functions
    word = request.form['searching']
    word = str(word)
    #print("myword:",word, type(word))
    word = word.lower()
    mydata, state = functions.buscar_articulo_nombre(word)
    if state == True:
        return (render_template("Inventario.html", productos = mydata))
    if state == False:
        mydata = str(mydata)
        message = ("{0}".format(mydata))
        return (render_template("Inventario.html", error = message, productos = []))
    else:
        return("<h1>¡Ups! Parece que este error en SEARCHINVENTARIO no lo habíamos contemplado. Por favor contacte al administrador</h1>")

##############################################################################
"""
Apartado: Actualizar El Inventario
"""
@app.route("/Inventario/Actualizar-Inventario")
def InventarioActualizar():
    return (render_template("InventarioActualizar.html", longitud = 0))

#----FUNCION PARA CONTROLAR EL TIPO DE *OPERACION* A REALIZAR-------
#----*OPERACION: Añadir, Eliminar y Actualizar
@app.route("/Inventario/Actualizar-Inventario/Administrar", methods = ['POST'])
def Administrar():
    import functions
    code = request.form['product_code']
    #En el código de try intentamos la búsqueda por Código
    #Si no se presiona la búsqueda por código
    #entonces hacemos la peticion de la operacion: añadir, eliminar o actualizar
    try:
        search_by_code = request.form['search']
        search_by_code = str(search_by_code)
        #-------------BUSQUEDA POR CODIGO------------------------------------#
        if search_by_code == 'SearchCode':

            mydata, state = functions.busqueda_por_codigo(code)
            if state == True:
                #print(len(mydata[0]))
                return (render_template("InventarioActualizar.html", producto = mydata, longitud = len(mydata[0])))
            elif state == False:
                error = str(mydata)
                message = ("{0}".format(mydata))
                return (render_template("InventarioActualizar.html", error = message, longitud = 0))
        else:
            return("<h1> ¡Ups! Parece que este error en ADMINISTRAR no lo vio el administrador</h1>")

    except:
        operation = request.form['Operations']
        if operation == 'off':
            message = "off-Debes elegir la operación que deseas realizar"
            return (render_template("InventarioActualizar.html", error = message, longitud = 0))

        #-----------------OPERACION AÑADIR-----------------------------------#
        elif operation == 'add':
            try:
                name = request.form['product_name']
                name = name.lower()
                specifications = request.form['product_specifications']
                quantity = request.form['product_quantity']
                unity = request.form['product_unity']
                price = request.form['product_price']

                mydata, state = functions.add_producto(code, name, specifications, quantity, unity, price)
                if state == True:
                    #print(len(mydata[0]))
                    message = "Producto Añadido Correctamente"
                    return (render_template("InventarioActualizar.html", error = message, producto = mydata, longitud = len(mydata[0])))
                elif state == False:
                    error = str(mydata)
                    message = ("{0}".format(mydata))
                    return (render_template("InventarioActualizar.html", error = message, longitud = 0))
            except:
                message = "add-Debes introducir todos los valores del producto"
                return (render_template("InventarioActualizar.html", error = message, longitud = 0))

        #--------OPERACION ELIMINAR------------------------------------------#
        elif operation == 'delete':
            # Para eliminar basta con introducir el código del producto
            mydata, state = functions.eliminar_por_codigo(code)
            if state == False:
                error = str(mydata)
                message = ("{0}".format(mydata))
                return (render_template("InventarioActualizar.html", error = message, longitud = 0))
            elif state == True:
                error = str(mydata)
                message = ("{0}".format(mydata))
                return (render_template("InventarioActualizar.html", error = message, longitud = 0))
                # En caso de error en la eliminación, descomentar lo comentado. NOTA PARA MI
                #message = "Producto Eliminado Correctamente"
                #return (render_template("InventarioActualizar.html", error = message, producto = mydata, longitud = len(mydata[0])))

        elif operation == 'update':
            # La dejamos pendiente
            try:
                name = request.form['product_name']
                name = name.lower()
                specifications = request.form['product_specifications']
                quantity = request.form['product_quantity']
                unity = request.form['product_unity']
                price = request.form['product_price']

                mydata, state = functions.update_producto(code, name, specifications, quantity, unity, price)
                if state == False:
                    error = str(mydata)
                    message = ("{0}".format(mydata))
                    return (render_template("InventarioActualizar.html", error = message, longitud = 0))
                elif state == True:
                    error = str(mydata)
                    message = ("{0}".format(mydata))
                    return (render_template("InventarioActualizar.html", error = message, longitud = 0))
            except:
                return ("<h1>¡ups! Este error no lo vi-update</h1>")

##############################################################################
"""
Apartado: Contacto
"""
@app.route("/Contacto")
def Contacto():
    return (render_template("Contacto.html"))



######################### FUNCION PRINCIPAL ##################################
if __name__ == "__main__":
    # Ejecutamos el objeto
    #webbrowser.open_new_tab('http://127.0.0.1:5000/')
    app.run(debug=True)
