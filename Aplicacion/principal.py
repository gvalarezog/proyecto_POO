import sys

from PySide6.QtWidgets import QApplication, QMainWindow

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
from Logica.nueva_persona import NuevaPersona

app = QApplication()
vtn_nueva_persona = NuevaPersona()
vtn_nueva_persona.show()
sys.exit(app.exec())
