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
        self.ui.naytaTiedotPushButton.hide()
        self.ui.tilaLabel.setText('VALITSE TOIMINTO')

        # OHJELMOIDUT SIGNAALIT

        # Kun Tulosta-painiketta on klikattu, kutsutaan updatePrintedLabel metodi

        self.ui.lainaaPushButton.clicked.connect(self.activateLend)
        self.ui.ajokorttiLineEdit.returnPressed.connect(self.activateAvain)
        self.ui.avainLineEdit.returnPressed.connect(self.tilaValmis)
        self.ui.palautaPushButton.clicked.connect(self.activateReturn)
        self.ui.naytaTiedotPushButton.clicked.connect(self.tiedot)

        # OHJELMOIDUT SLOTIT

    def activateLend(self):
        self.ui.tilaLabel.setText('AUTON LAINAUS')
        self.ui.ajokorttiLineEdit.show()
        self.ui.ajokorttiLineEdit.setFocus()
        self.ui.hetuLabel.hide()
        self.ui.statusbar.showMessage('Skannaa ajokortin!')
        self.ui.palautaPushButton.hide()
        self.ui.lainaaPushButton.hide()
        

    def activateAvain(self):
        self.ui.ajokorttiLineEdit.hide()
        self.ui.hetuLabel.hide()
        self.ui.avainLineEdit.show()
        self.ui.avainLineEdit.setFocus()
        self.ui.rekisteriNrLabel.hide()

    def tilaValmis(self):
        self.ui.avainLineEdit.hide()
        self.ui.rekisteriNrLabel.hide()
        self.ui.naytaTiedotPushButton.show()
        self.ui.tilaLabel.setText('VALMIS')

    def activateReturn(self):
        self.ui.tilaLabel.setText('AUTON PALAUTUS')
        self.ui.avainLineEdit.show()
        self.ui.avainLineEdit.setFocus()
        self.ui.rekisteriNrLabel.show()
        self.ui.lainaaPushButton.hide()
        self.ui.palautaPushButton.hide()

    def tiedot(self):
        self.ui.hetuLabel.show() 
        self.ui.rekisteriNrLabel.show()
        self.ui.naytaTiedotPushButton.hide()
# LUODAAN VARSINAINEN SOVELLUS

app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
windows = MainWindow()
windows.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä (event loop)
app.exec()