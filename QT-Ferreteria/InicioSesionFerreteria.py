# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InicioSesionFerreteria.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 306)

        ################################
        font = QtGui.QFont()
        font.setPointSize(12)
        ############Lo anterio no es necesario
        Dialog.setFont(font)
        self.gtbSesion = QtWidgets.QGroupBox(Dialog)
        self.gtbSesion.setGeometry(QtCore.QRect(0, 0, 401, 251))
        #gtbSesion
        self.gtbSesion.setObjectName("gtbSesion")

        ########################################################3
        self.lblUsuario = QtWidgets.QLabel(self.gtbSesion)
        self.lblUsuario.setGeometry(QtCore.QRect(10, 40, 111, 21))
        #######################################
        font = QtGui.QFont()
        font.setPointSize(14)
        #############LO anterio no es necesario
        self.lblUsuario.setFont(font)
        #lblUsuario
        self.lblUsuario.setObjectName("lblUsuario")

        #######################################################
        self.lblContrasena = QtWidgets.QLabel(self.gtbSesion)
        self.lblContrasena.setGeometry(QtCore.QRect(10, 100, 141, 21))
        ######################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        ################Lo anterio no es necesario
        self.lblContrasena.setFont(font)
        #lblContrasena
        self.lblContrasena.setObjectName("lblContrasena")

        ###########################################################
        self.lblNombre = QtWidgets.QLabel(self.gtbSesion)
        self.lblNombre.setGeometry(QtCore.QRect(10, 160, 111, 21))
        #################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        ##############Lo anterio no es necesario
        self.lblNombre.setFont(font)
        #lblNombre
        self.lblNombre.setObjectName("lblNombre")

        ####################################################
        self.lblRol = QtWidgets.QLabel(self.gtbSesion)
        self.lblRol.setGeometry(QtCore.QRect(10, 220, 111, 21))
        ####################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        #####################Lo anterio no es necesario
        self.lblRol.setFont(font)
        #lblRol
        self.lblRol.setObjectName("lblRol")

        ########################################################
        self.leUsuario = QtWidgets.QLineEdit(self.gtbSesion)
        self.leUsuario.setGeometry(QtCore.QRect(150, 30, 221, 31))
        ##########################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        #######################Lo anterio no es necesario
        self.leUsuario.setFont(font)
        #leUsuario
        self.leUsuario.setObjectName("leUsuario")

        ###############################################################
        self.leContrasena = QtWidgets.QLineEdit(self.gtbSesion)
        self.leContrasena.setGeometry(QtCore.QRect(150, 90, 221, 31))
        ##################################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        ########################Lo anterior no es necesario
        self.leContrasena.setFont(font)
        #leContrasena
        self.leContrasena.setObjectName("leContrasena")

        #########################################################
        self.leNombre = QtWidgets.QLineEdit(self.gtbSesion)
        self.leNombre.setEnabled(False)
        self.leNombre.setGeometry(QtCore.QRect(150, 150, 221, 31))
        ##############################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        ####################Lo anterio no es necesario
        self.leNombre.setFont(font)
        #leNombre
        self.leNombre.setObjectName("leNombre")

        #########################################################
        self.leRol = QtWidgets.QLineEdit(self.gtbSesion)
        self.leRol.setEnabled(False)
        self.leRol.setGeometry(QtCore.QRect(150, 210, 221, 31))
        ######################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        #################Lo anterior no es necesario
        self.leRol.setFont(font)
        #LeRol
        self.leRol.setObjectName("leRol")

        ##################################################
        self.pbIniciar = QtWidgets.QPushButton(Dialog)
        self.pbIniciar.setGeometry(QtCore.QRect(260, 250, 111, 51))
        #######################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        #####################Lo anterior no es necesario
        self.pbIniciar.setFont(font)
        #pbIniciar
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/aceptar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbIniciar.setIcon(icon)
        self.pbIniciar.setIconSize(QtCore.QSize(24, 24))
        self.pbIniciar.setObjectName("pbIniciar")


        #########################################################
        self.pbCancelar = QtWidgets.QPushButton(Dialog)
        self.pbCancelar.setGeometry(QtCore.QRect(10, 250, 131, 51))
        #################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        ###########Lo anterior no es necesario
        self.pbCancelar.setFont(font)
        #pbCancelar
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
        self.pbIniciar.setText(_translate("Dialog", "Iniciar"))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
