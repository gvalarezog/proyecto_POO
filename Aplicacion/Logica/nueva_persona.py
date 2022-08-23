from PySide6.QtWidgets import QMainWindow, QMessageBox

from Aplicacion.Datos.archivo import Archivo
from Aplicacion.Dominio.persona import Persona
from Aplicacion.GUI.vtn_principal import Ui_vtn_principal


class NuevaPersona(QMainWindow):
    def __init__(self):
        super(NuevaPersona, self).__init__()
        self.persona = None
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.txt_cedula.setToolTip('Ingrese solo números')
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_formulario)

    def guardar(self):
        # nombre = self.ui.txt_nombre.text().capitalize()
        # apellido = self.ui.txt_apellido.text().capitalize()
        # cedula =  self.ui.txt_cedula.text()
        # email = self.ui.txt_email.text()
        # sexo = self.ui.cb_sexo.currentText()
        # # self.persona = Persona(nombre=nombre, apellido=apellido, cedula=cedula, email=email, sexo=sexo)

        if self.validar_formulario():
            self.capturar_datos()
            if Archivo.guardar(objeto=self.persona):
                self.limpiar_formulario()
                self.ui.stb_estado.showMessage('Ingreso exitoso.', 3000)
                print(self.persona)
            else:
                # self.ui.stb_estado.showMessage('Fallo el ingreso.', 3000)
                QMessageBox.critical(self, 'Error', 'Error al guardar la información')
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
        self.ui.txt_cedula.text() != '' and self.ui.txt_email.text() != '' and
        self.ui.cb_sexo.currentText() != 'Seleccionar opción')

    def capturar_datos(self):
        self.persona = Persona()
        self.persona.nombre = self.ui.txt_nombre.text().capitalize()
        self.persona.apellido = self.ui.txt_apellido.text().capitalize()
        self.persona.email = self.ui.txt_email.text()
        self.persona.cedula = self.ui.txt_cedula.text()
        self.persona.sexo = self.ui.cb_sexo.currentText()



