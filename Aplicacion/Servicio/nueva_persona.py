import re

from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QMessageBox


from Aplicacion.Datos.archivo import Archivo
from Aplicacion.Datos.persona_dao import PersonaDAO
from Aplicacion.Dominio.persona import Persona
from Aplicacion.GUI.vtn_principal import Ui_vtn_principal


class NuevaPersona(QMainWindow):
    def __init__(self):
        super(NuevaPersona, self).__init__()
        self.persona = None
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.txt_cedula.setToolTip('Ingrese solo números')
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_formulario)

    def guardar(self):

        if self.validar_formulario():
            self.capturar_datos()
            respuesta = PersonaDAO.insertar(self.persona)
            if respuesta['exito']:
            # if Archivo.guardar(objeto=self.persona):
                self.limpiar_formulario()
                self.ui.stb_estado.showMessage('Ingreso exitoso.', 3000)
                print(self.persona)
            else:
                # self.ui.stb_estado.showMessage('Fallo el ingreso.', 3000)

                QMessageBox.critical(self, 'Error', f"Error al guardar la información \n{respuesta['mensaje']}")
        else:
            QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos.')

    def limpiar_formulario(self):
        self.ui.txt_nombre.setText('')
        self.ui.txt_apellido.setText('')
        self.ui.txt_cedula.setText('')
        self.ui.txt_email.setText('')
        self.ui.cb_sexo.setCurrentText('Seleccionar opción')

    def validar_formulario(self):
        return (self.ui.txt_nombre.text() != '' and self.ui.txt_apellido.text() != '' and
        len(self.ui.txt_cedula.text()) == 10 and self.validar_email(self.ui.txt_email.text()) and
        self.ui.cb_sexo.currentText() != 'Seleccionar opción')

    def capturar_datos(self):
        self.persona = Persona()
        self.persona.nombre = self.ui.txt_nombre.text().capitalize()
        self.persona.apellido = self.ui.txt_apellido.text().capitalize()
        self.persona.email = self.ui.txt_email.text()
        self.persona.cedula = self.ui.txt_cedula.text()
        self.persona.sexo = self.ui.cb_sexo.currentText()

    def validar_email(self, email):
        # expresionRegular = r'(^[\w]+)@([\w]+)' + '{2,3}'
        expresionRegular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.search(expresionRegular, email)
