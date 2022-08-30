# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(424, 299)
        self.mni_archivo = QAction(vtn_principal)
        self.mni_archivo.setObjectName(u"mni_archivo")
        self.mni_abrir = QAction(vtn_principal)
        self.mni_abrir.setObjectName(u"mni_abrir")
        self.mni_cerrar = QAction(vtn_principal)
        self.mni_cerrar.setObjectName(u"mni_cerrar")
        self.mni_acerca_de = QAction(vtn_principal)
        self.mni_acerca_de.setObjectName(u"mni_acerca_de")
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(70, 30, 61, 20))
        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(140, 30, 211, 20))
        self.txt_nombre.setMaxLength(50)
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(70, 60, 61, 20))
        self.txt_apellido = QLineEdit(self.centralwidget)
        self.txt_apellido.setObjectName(u"txt_apellido")
        self.txt_apellido.setGeometry(QRect(140, 60, 211, 20))
        self.txt_apellido.setMaxLength(50)
        self.btn_guardar = QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(90, 210, 75, 23))
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(140, 90, 211, 20))
        self.txt_email.setMaxLength(100)
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(70, 100, 47, 13))
        self.lbl_sexo = QLabel(self.centralwidget)
        self.lbl_sexo.setObjectName(u"lbl_sexo")
        self.lbl_sexo.setGeometry(QRect(70, 160, 47, 13))
        self.cb_sexo = QComboBox(self.centralwidget)
        self.cb_sexo.addItem("")
        self.cb_sexo.addItem("")
        self.cb_sexo.addItem("")
        self.cb_sexo.setObjectName(u"cb_sexo")
        self.cb_sexo.setGeometry(QRect(140, 160, 211, 22))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(70, 130, 47, 13))
        self.txt_cedula = QLineEdit(self.centralwidget)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(140, 120, 211, 20))
        self.txt_cedula.setMaxLength(10)
        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(270, 210, 75, 23))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.mnb_menu_principal = QMenuBar(vtn_principal)
        self.mnb_menu_principal.setObjectName(u"mnb_menu_principal")
        self.mnb_menu_principal.setGeometry(QRect(0, 0, 424, 21))
        self.mnu_archivo = QMenu(self.mnb_menu_principal)
        self.mnu_archivo.setObjectName(u"mnu_archivo")
        self.mnu_ayuda = QMenu(self.mnb_menu_principal)
        self.mnu_ayuda.setObjectName(u"mnu_ayuda")
        vtn_principal.setMenuBar(self.mnb_menu_principal)
        self.stb_estado = QStatusBar(vtn_principal)
        self.stb_estado.setObjectName(u"stb_estado")
        vtn_principal.setStatusBar(self.stb_estado)
        QWidget.setTabOrder(self.txt_nombre, self.txt_apellido)
        QWidget.setTabOrder(self.txt_apellido, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.txt_cedula)
        QWidget.setTabOrder(self.txt_cedula, self.cb_sexo)
        QWidget.setTabOrder(self.cb_sexo, self.btn_guardar)
        QWidget.setTabOrder(self.btn_guardar, self.btn_limpiar)

        self.mnb_menu_principal.addAction(self.mnu_archivo.menuAction())
        self.mnb_menu_principal.addAction(self.mnu_ayuda.menuAction())
        self.mnu_archivo.addAction(self.mni_archivo)
        self.mnu_archivo.addAction(self.mni_abrir)
        self.mnu_archivo.addAction(self.mni_cerrar)
        self.mnu_ayuda.addAction(self.mni_acerca_de)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Mi Primer GUI v1", None))
        self.mni_archivo.setText(QCoreApplication.translate("vtn_principal", u"Nuevo", None))
        self.mni_abrir.setText(QCoreApplication.translate("vtn_principal", u"Abrir", None))
        self.mni_cerrar.setText(QCoreApplication.translate("vtn_principal", u"Cerrar", None))
        self.mni_acerca_de.setText(QCoreApplication.translate("vtn_principal", u"Acerca de...", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"Nombre:*", None))
#if QT_CONFIG(tooltip)
        self.txt_nombre.setToolTip(QCoreApplication.translate("vtn_principal", u"Ingrese su nombre", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_principal", u"Apellido:*", None))
        self.btn_guardar.setText(QCoreApplication.translate("vtn_principal", u"Guardar", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_principal", u"Email:*", None))
        self.lbl_sexo.setText(QCoreApplication.translate("vtn_principal", u"Sexo:*", None))
        self.cb_sexo.setItemText(0, QCoreApplication.translate("vtn_principal", u"Seleccionar opci\u00f3n", None))
        self.cb_sexo.setItemText(1, QCoreApplication.translate("vtn_principal", u"Masculino", None))
        self.cb_sexo.setItemText(2, QCoreApplication.translate("vtn_principal", u"Femenino", None))

        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"Cedula:*", None))
        self.btn_limpiar.setText(QCoreApplication.translate("vtn_principal", u"Limpiar", None))
        self.mnu_archivo.setTitle(QCoreApplication.translate("vtn_principal", u"Archivo", None))
        self.mnu_ayuda.setTitle(QCoreApplication.translate("vtn_principal", u"Ayuda", None))
    # retranslateUi

