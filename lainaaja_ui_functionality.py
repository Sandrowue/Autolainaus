import os
import sys

from PySide6 import QtWidgets

from Lainaaja import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia seupUi
        self.ui.setupUi(self)

        # Ohjelman käynnistyksessä piilotetaan tarpeettomat elementit
        self.ui.ajokorttiLineEdit.hide()
        self.ui.hetuLabel.hide()
        self.ui.avainLineEdit.hide()
        self.ui.rekisteriNrLabel.hide()
        self.ui.tilaLabel.hide()

        # OHJELMOIDUT SIGNAALIT

        # Kun Tulosta-painiketta on klikattu, kutsutaan updatePrintedLabel metodi

        self.ui.lainaaPushButton.clicked.connect(self.activateLender)

        # OHJELMOIDUT SLOTIT

    def activateLender(self):
        self.ui.tilaLabel.show()
        self.ui.tilaLabel.setText('AUTON LAINAUS')
        self.ui.ajokorttiLineEdit.show()
        self.ui.ajokorttiLineEdit.setFocus()
        self.ui.hetuLabel.show()
        self.ui.statusbar.showMessage('Skannaa ajokortin!')
        self.ui.palautaPushButton.hide()
        
# LUODAAN VARSINAINEN SOVELLUS

app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
windows = MainWindow()
windows.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä (event loop)
app.exec()