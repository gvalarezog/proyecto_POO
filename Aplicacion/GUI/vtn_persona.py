# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_persona.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_vtn_persona(object):
    def setupUi(self, vtn_persona):
        if not vtn_persona.objectName():
            vtn_persona.setObjectName(u"vtn_persona")
        vtn_persona.setWindowModality(Qt.ApplicationModal)
        vtn_persona.resize(500, 299)
        vtn_persona.setMaximumSize(QSize(500, 299))
        self.mni_archivo = QAction(vtn_persona)
        self.mni_archivo.setObjectName(u"mni_archivo")
        self.mni_abrir = QAction(vtn_persona)
        self.mni_abrir.setObjectName(u"mni_abrir")
        self.mni_cerrar = QAction(vtn_persona)
        self.mni_cerrar.setObjectName(u"mni_cerrar")
        self.mni_acerca_de = QAction(vtn_persona)
        self.mni_acerca_de.setObjectName(u"mni_acerca_de")
        self.centralwidget = QWidget(vtn_persona)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(70, 70, 61, 20))
        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(140, 70, 211, 20))
        self.txt_nombre.setMaxLength(50)
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(70, 100, 61, 20))
        self.txt_apellido = QLineEdit(self.centralwidget)
        self.txt_apellido.setObjectName(u"txt_apellido")
        self.txt_apellido.setGeometry(QRect(140, 100, 211, 20))
        self.txt_apellido.setMaxLength(50)
        self.btn_guardar = QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(90, 210, 75, 23))
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(140, 130, 211, 20))
        self.txt_email.setMaxLength(100)
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(70, 140, 47, 13))
        self.lbl_sexo = QLabel(self.centralwidget)
        self.lbl_sexo.setObjectName(u"lbl_sexo")
        self.lbl_sexo.setGeometry(QRect(70, 170, 47, 13))
        self.cb_sexo = QComboBox(self.centralwidget)
        self.cb_sexo.addItem("")
        self.cb_sexo.addItem("")
        self.cb_sexo.addItem("")
        self.cb_sexo.setObjectName(u"cb_sexo")
        self.cb_sexo.setGeometry(QRect(140, 170, 211, 22))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(70, 30, 51, 16))
        self.txt_cedula = QLineEdit(self.centralwidget)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(140, 30, 211, 20))
        self.txt_cedula.setMaxLength(10)
        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(190, 210, 75, 23))
        self.btn_consultar = QPushButton(self.centralwidget)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setGeometry(QRect(370, 30, 75, 23))
        self.btn_actualizar = QPushButton(self.centralwidget)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(290, 210, 75, 23))
        self.btn_eliminar = QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(380, 210, 75, 23))
        vtn_persona.setCentralWidget(self.centralwidget)
        self.stb_estado = QStatusBar(vtn_persona)
        self.stb_estado.setObjectName(u"stb_estado")
        vtn_persona.setStatusBar(self.stb_estado)
        QWidget.setTabOrder(self.txt_cedula, self.btn_consultar)
        QWidget.setTabOrder(self.btn_consultar, self.txt_nombre)
        QWidget.setTabOrder(self.txt_nombre, self.txt_apellido)
        QWidget.setTabOrder(self.txt_apellido, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.cb_sexo)
        QWidget.setTabOrder(self.cb_sexo, self.btn_guardar)
        QWidget.setTabOrder(self.btn_guardar, self.btn_limpiar)

        self.retranslateUi(vtn_persona)

        QMetaObject.connectSlotsByName(vtn_persona)
    # setupUi

    def retranslateUi(self, vtn_persona):
        vtn_persona.setWindowTitle(QCoreApplication.translate("vtn_persona", u"Persona", None))
        self.mni_archivo.setText(QCoreApplication.translate("vtn_persona", u"Nuevo", None))
        self.mni_abrir.setText(QCoreApplication.translate("vtn_persona", u"Abrir", None))
        self.mni_cerrar.setText(QCoreApplication.translate("vtn_persona", u"Cerrar", None))
        self.mni_acerca_de.setText(QCoreApplication.translate("vtn_persona", u"Acerca de...", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_persona", u"Nombre:*", None))
#if QT_CONFIG(tooltip)
        self.txt_nombre.setToolTip(QCoreApplication.translate("vtn_persona", u"Ingrese su nombre", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_persona", u"Apellido:*", None))
        self.btn_guardar.setText(QCoreApplication.translate("vtn_persona", u"Insertar", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_persona", u"Email:*", None))
        self.lbl_sexo.setText(QCoreApplication.translate("vtn_persona", u"Sexo:*", None))
        self.cb_sexo.setItemText(0, QCoreApplication.translate("vtn_persona", u"Seleccionar opci\u00f3n", None))
        self.cb_sexo.setItemText(1, QCoreApplication.translate("vtn_persona", u"Masculino", None))
        self.cb_sexo.setItemText(2, QCoreApplication.translate("vtn_persona", u"Femenino", None))

        self.lbl_cedula.setText(QCoreApplication.translate("vtn_persona", u"Cedula:*", None))
        self.btn_limpiar.setText(QCoreApplication.translate("vtn_persona", u"Limpiar", None))
        self.btn_consultar.setText(QCoreApplication.translate("vtn_persona", u"Consultar", None))
        self.btn_actualizar.setText(QCoreApplication.translate("vtn_persona", u"Actualizar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("vtn_persona", u"Eliminar", None))
    # retranslateUi

