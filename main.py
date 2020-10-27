# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ventana import *
import sys, var, events

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi()

    '''
    Conexión de eventos con los objetos
    '''
    var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
    var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())