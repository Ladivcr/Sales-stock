# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InicioSesionFerreteria.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# Definimos una función para desplegar
# un meessage box
def fnMensaje(sMensaje, sInformacion):
    #Crea un message Box
    msg = QMessageBox()

    # Establece el icono
    msg.setIcon(QMessageBox.Information)

    # Coloca el mensaje a desplegar
    msg.setText(sMensaje)
    msg.setInformativeText(sInformacion)
    msg.setWindowTitle("Mensaje informativo")
    #msg.setDetailedText("The details are as follow:")
    msg.setStandardButtons(QMessageBox.Ok)

    # Ejecuta el MessageBox
    msg.exec_()
    return()



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 306)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)

        self.gtbSesion = QtWidgets.QGroupBox(Dialog)
        self.gtbSesion.setGeometry(QtCore.QRect(0, 0, 401, 251))
        self.gtbSesion.setObjectName("gtbSesion")


        self.lblUsuario = QtWidgets.QLabel(self.gtbSesion)
        self.lblUsuario.setGeometry(QtCore.QRect(10, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setObjectName("lblUsuario")


        self.lblContrasena = QtWidgets.QLabel(self.gtbSesion)
        self.lblContrasena.setGeometry(QtCore.QRect(10, 100, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblContrasena.setFont(font)
        self.lblContrasena.setObjectName("lblContrasena")


        self.lblNombre = QtWidgets.QLabel(self.gtbSesion)
        self.lblNombre.setGeometry(QtCore.QRect(10, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")


        self.lblRol = QtWidgets.QLabel(self.gtbSesion)
        self.lblRol.setGeometry(QtCore.QRect(10, 220, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblRol.setFont(font)
        self.lblRol.setObjectName("lblRol")


        self.leUsuario = QtWidgets.QLineEdit(self.gtbSesion)
        self.leUsuario.setGeometry(QtCore.QRect(150, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leUsuario.setFont(font)
        self.leUsuario.setText("")
        self.leUsuario.setMaxLength(100)
        self.leUsuario.setObjectName("leUsuario")
        # Establece la función Enter
        self.leUsuario.returnPressed.connect(self.fnProcesaEnter)

        # Establece la función para saber si se presionauna tecla
        self.leUsuario.keyPressEvent = self.keyPressEvent

        # Establece la función para procesar el cambio de texto
        self.leUsuario.textChanged.connect(self.fnProcesarCambioTexto)

        self.leContrasena = QtWidgets.QLineEdit(self.gtbSesion)
        self.leContrasena.setGeometry(QtCore.QRect(150, 90, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leContrasena.setFont(font)
        self.leContrasena.setMaxLength(100)
        self.leContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leContrasena.setObjectName("leContrasena")
        # Establece la función Enter
        self.leContrasena.returnPressed.connect(self.fnProcesaEnter)

        # Establece el control de evento para cuando se presiona una Tecla
        self.leContrasena.keyPressEvent = self.keyPressEvent

        # Establece la función para procesar el cambio de texto
        self.leContrasena.textChanged.connect(self.fnProcesarCambioTexto)


        self.leNombre = QtWidgets.QLineEdit(self.gtbSesion)
        self.leNombre.setEnabled(True)
        self.leNombre.setGeometry(QtCore.QRect(150, 150, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.leNombre.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leNombre.setFont(font)
        self.leNombre.setReadOnly(True)
        self.leNombre.setObjectName("leNombre")


        self.leRol = QtWidgets.QLineEdit(self.gtbSesion)
        self.leRol.setEnabled(True)
        self.leRol.setGeometry(QtCore.QRect(150, 210, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.leRol.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leRol.setFont(font)
        self.leRol.setReadOnly(True)
        self.leRol.setObjectName("leRol")


        self.pbIniciar = QtWidgets.QPushButton(Dialog)
        self.pbIniciar.setGeometry(QtCore.QRect(230, 250, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pbIniciar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/aceptar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbIniciar.setIcon(icon)
        self.pbIniciar.setIconSize(QtCore.QSize(24, 24))
        self.pbIniciar.setObjectName("pbIniciar")

        # Asocia el keyPressEvent
        self.pbIniciar.keyPressEvent = self.keyPressEvent

        # Controla el evento click
        #self.pbIniciar.clicked.connect(self.fnValidaDatos)
        self.pbIniciar.clicked.connect(self.fnProcesaClickAceptar)




        self.pbCancelar = QtWidgets.QPushButton(Dialog)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 250, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pbCancelar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/cancelar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancelar.setIcon(icon1)
        self.pbCancelar.setIconSize(QtCore.QSize(24, 24))
        self.pbCancelar.setObjectName("pbCancelar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Inicio de sesión"))
        self.gtbSesion.setTitle(_translate("Dialog", " Usuario Y Contraseña"))
        self.lblUsuario.setText(_translate("Dialog", "Usuario:"))
        self.lblContrasena.setText(_translate("Dialog", "Contraseña:"))
        self.lblNombre.setText(_translate("Dialog", "Nombre:"))
        self.lblRol.setText(_translate("Dialog", "Rol:"))
        self.leNombre.setText(_translate("Dialog", "Unknow"))
        self.leRol.setText(_translate("Dialog", "Unknow"))
        self.pbIniciar.setText(_translate("Dialog", "Iniciar"))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar"))

    """
    Función para procesar el Enter
    """
    def fnProcesaEnter(self):
        print("Haz presionado enter")

        #Verifica si tiene el foco del Usuario
        if (self.leUsuario.hasFocus()):
            # Manda el foco al Password
            print("Foco en Password")
            self.leContrasena.setFocus()
        else:
            # El foco lo tiene Password
            print("Foco a Aceptar")
            # Manda el foco al boton de Aceptar
            self.pbIniciar.setFocus()

    """
    Función para detectar cambios
    """
    def fnProcesarCambioTexto(self):
        # verifica si el usuario tiene el Foco
        if (self.leUsuario.hasFocus()):
            # manda el foco al Password
            print("Cambio de texto en usuario:", self.leUsuario.text())

        else:
            # El foco lo tiene Password
            print("Cambio de texto en Password:", self.leContrasena.text())

    # Se ha presionado una tecla
    def keyPressEvent(self, event):
        # Mensaje
        print("Tecla presionada:", event.text())
        if (self.leUsuario.hasFocus()):
            print("Presionaste una tecla en usuario")

            # Evitamos el 5
            if (event.text()!= "1"):
                return (QtWidgets.QLineEdit.keyPressEvent(self.leUsuario, event))

        elif (self.leContrasena.hasFocus()):
            print("Presionaste una tecla en contrasena")
            if (event.text()!="1"):
                return (QtWidgets.QLineEdit.keyPressEvent(self.leContrasena, event))

        else:
            #Mensaje
            print("Se presiono una tecla en el botón aceptar")

            #Verifica que sea Enter
            if (event.key() == QtCore.Qt.key_Return):
                # Llama la función para validar fnValidaDatos
                self.fnValidaDatos()

    # Funcion para procesar el click del botón de aceptar
    def fnProcesaClickAceptar(self):
        if(self.pbIniciar.hasFocus()):
            # Llama a la función de validar fnValidaDatos
            self.fnValidaDatos()

    # Función para validar datos
    def fnValidaDatos(self):

        # Variable para el Mensaje
        sMensaje = ""

        # Valida el usuario
        if (len(self.leUsuario.text())==0):
            # Coloca el dato en el mensaje
            sMensaje = "El usuario\n"

            # Coloca el foco en el Usuario
            self.leUsuario.setFocus()

        # Valida el Password
        if (len(self.leContrasena.text())==0):
            # Verifica si debe colocar el foco
            if (len(sMensaje)==0):
                # Coloca el Foco
                self.leContrasena.setFocus()

            # Agrego el dato en el mensaje
            sMensaje = sMensaje + "El Password"

        # Verifica si debe desplegar el mensade de error
        if (len(sMensaje)>0):
            #Actualiza el Mensaje
            sMensaje="Revise los siguientes datos:\n" + sMensaje
            # Despliega el MessageBox
            fnMensaje(sMensaje, "El usuario y la contraseña no pueden quedar vacios")
            # Hay error en los datos
            return (False)
        else:
            # Despliega el MessageBox
            fnMensaje("Los datos están correctos", "La aplicación intentara el acceso")
            # Los datos están correctos
            return (True)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
