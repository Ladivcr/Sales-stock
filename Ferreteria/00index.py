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
    return (render_template("RealizarVenta.html", longitud = 0, precioTotal = 0))


@app.route("/Realizar-Venta/AddToCar", methods = ['POST'])
def AddToCar():
    import functions
    code = request.form['product_code']
    try:
        add_by_code = request.form['adding']
        add_by_code = str(add_by_code)
        #-------------AÑADIR ATRIBUTOS POR CODIGO------------------------------------#
        if add_by_code == "AddCode":
            try:
                mydata, state, total = functions.add_fast(code)
                if state == True:
                    return (render_template("RealizarVenta.html", producto = mydata, longitud = len(mydata[0]), precioTotal = total))
                elif state == False:
                    error = str(mydata)
                    message = ("{0}".format(mydata))
                    return (render_template("RealizarVenta.html", error = message, longitud = 0, precioTotal = total))
            except:
                return("<h1> ¡Ups! Parece que este error en ADMINISTRAR no lo vio el administrador</h1>")

    except:
        try:
            carrito = request.form['btn_carrito']
            if carrito == 'addCar':
                name = request.form['product_name']
                name = name.lower()
                quantity = request.form['product_quantity']
                unity = request.form['product_unity']
                price = request.form['sale_price']

                if name == "d" or quantity == "d" or unity == "d" or price == "d":
                    message = "Por favor introduzca todos los datos"
                    return (render_template("RealizarVenta.html", error = message, longitud = 0, total =0))
                else:
                    mydata, state, total = functions.add_to_car(code, name, quantity, unity, price)
                    if state == True:
                        return (render_template("RealizarVenta.html", producto = mydata, longitud = len(mydata[0]), precioTotal = total))
                    elif state == False:
                        error = str(mydata)
                        message = ("{0}".format(mydata))
                        return (render_template("RealizarVenta.html", error = message, longitud = 0, precioTotal = total))

        except:
            return("<h1>sad</h1>")


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
