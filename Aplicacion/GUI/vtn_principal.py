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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(694, 411)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tb_personas = QTableWidget(self.centralwidget)
        if (self.tb_personas.columnCount() < 6):
            self.tb_personas.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tb_personas.setObjectName(u"tb_personas")
        self.tb_personas.setGeometry(QRect(30, 20, 621, 281))
        self.tb_personas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_personas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_personas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btn_actualizar = QPushButton(self.centralwidget)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(280, 320, 75, 23))
        self.btn_refrescar = QPushButton(self.centralwidget)
        self.btn_refrescar.setObjectName(u"btn_refrescar")
        self.btn_refrescar.setGeometry(QRect(570, 320, 75, 23))
        self.btn_nuevo = QPushButton(self.centralwidget)
        self.btn_nuevo.setObjectName(u"btn_nuevo")
        self.btn_nuevo.setGeometry(QRect(94, 320, 101, 23))
        self.btn_eliminar = QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(420, 320, 75, 23))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.mnb_menu = QMenuBar(vtn_principal)
        self.mnb_menu.setObjectName(u"mnb_menu")
        self.mnb_menu.setGeometry(QRect(0, 0, 694, 21))
        vtn_principal.setMenuBar(self.mnb_menu)
        self.stb_estado = QStatusBar(vtn_principal)
        self.stb_estado.setObjectName(u"stb_estado")
        vtn_principal.setStatusBar(self.stb_estado)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Bienvenidos a Persona Cargar", None))
        ___qtablewidgetitem = self.tb_personas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("vtn_principal", u"ID", None));
        ___qtablewidgetitem1 = self.tb_personas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("vtn_principal", u"Nombre", None));
        ___qtablewidgetitem2 = self.tb_personas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("vtn_principal", u"Apellido", None));
        ___qtablewidgetitem3 = self.tb_personas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("vtn_principal", u"Cedula", None));
        ___qtablewidgetitem4 = self.tb_personas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("vtn_principal", u"Email", None));
        ___qtablewidgetitem5 = self.tb_personas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("vtn_principal", u"Sexo", None));
        self.btn_actualizar.setText(QCoreApplication.translate("vtn_principal", u"Actualizar", None))
        self.btn_refrescar.setText(QCoreApplication.translate("vtn_principal", u"Refrescar", None))
        self.btn_nuevo.setText(QCoreApplication.translate("vtn_principal", u"Nueva Persona", None))
        self.btn_eliminar.setText(QCoreApplication.translate("vtn_principal", u"Eliminar", None))
    # retranslateUi

