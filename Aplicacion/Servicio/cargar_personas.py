from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from Aplicacion.Datos.persona_dao import PersonaDAO
from Aplicacion.Dominio.persona import Persona
from Aplicacion.GUI.vtn_principal_cargar import Ui_vtn_principal_cargar
from Aplicacion.Servicio.nueva_persona import NuevaPersona


class CargarPersonas(QMainWindow):
    def __init__(self):
        super(CargarPersonas, self).__init__()
        self.personas = None
        self.persona_escogida = None
        self.vtn_hija = None
        self.ui = Ui_vtn_principal_cargar()
        self.ui.setupUi(self)
        self.cargar()
        self.ui.tb_personas.clicked.connect(self.escoger_persona)
        self.ui.btn_actualizar.clicked.connect(self.actualizar)
        self.ui.btn_refrescar.clicked.connect(self.cargar)
        self.ui.btn_nuevo.clicked.connect(self.nuevo)
        self.ui.btn_eliminar.clicked.connect(self.eliminar)

    def cargar(self):
        self.ui.tb_personas.clearContents()
        while (self.ui.tb_personas.rowCount() > 0):
            self.ui.tb_personas.removeRow(0)

        self.personas = PersonaDAO.seleccionar()
        data = []
        for persona in self.personas:
            data.append((str(persona.id), persona.nombre, persona.apellido, persona.cedula, persona.email, persona.sexo))
        fila = 0
        for registro in data:
            columna = 0
            self.ui.tb_personas.insertRow(fila)
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                self.ui.tb_personas.setItem(fila, columna, celda)
                columna += 1
            fila += 1

    def escoger_persona(self):
        fila = self.ui.tb_personas.currentRow()
        self.ui.tb_personas.selectRow(fila)
        id = self.ui.tb_personas.item(fila, 0).text()
        nombre = self.ui.tb_personas.item(fila, 1).text()
        apellido = self.ui.tb_personas.item(fila, 2).text()
        cedula = self.ui.tb_personas.item(fila, 3).text()
        email = self.ui.tb_personas.item(fila, 4).text()
        sexo = self.ui.tb_personas.item(fila, 5).text()
        self.persona_escogida = Persona(id=id, nombre=nombre, cedula=cedula, apellido=apellido, email=email, sexo=sexo)
        print(self.persona_escogida)

    def actualizar(self):
        if not self.persona_escogida:
            QMessageBox.warning(self, 'Advertencia', 'Debe escoger una persona.')
        else:
            self.vtn_hija = NuevaPersona(persona=self.persona_escogida)
            self.vtn_hija.show()

    def nuevo(self):
        self.vtn_hija = NuevaPersona()
        self.vtn_hija.show()

    def eliminar(self):
        if not self.persona_escogida:
            QMessageBox.warning(self, 'Advertencia', 'Debe escoger una persona.')
        else:
            button = QMessageBox.question(self,"Eliminar Persona","Desea eliminar la persona escogida?" )
            if button == QMessageBox.Yes:
                respuesta = PersonaDAO.eliminar_por_cedula(self.persona_escogida)
                if respuesta['exito']:
                    QMessageBox.information(self, 'Información', 'Se ha eliminado la persona.')
                    self.cargar()
            else:
                self.cargar()
