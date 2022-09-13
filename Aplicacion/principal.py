import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from Aplicacion.Servicio.cargar_personas import CargarPersonas
from GUI.vtn_principal import Ui_vtn_principal

# def guardar():
#     print ('Se hizo clic en el boton guardar')
#
# app = QApplication()
# ventanaPrincipal = QMainWindow()
# ventanaInterna = Ui_vtn_principal()
# ventanaInterna.setupUi(ventanaPrincipal)
# ventanaInterna.btn_guardar.clicked.connect(guardar)
# ventanaPrincipal.show()
#
# sys.exit(app.exec())
from Servicio.nueva_persona import NuevaPersona

app = QApplication()
vtn_principal = CargarPersonas()
vtn_principal.show()
# vtn_nueva_persona = NuevaPersona()
# vtn_nueva_persona.show()
sys.exit(app.exec())
