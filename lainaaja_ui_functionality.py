import os
import sys
import datetime 
import json

from PySide6 import QtWidgets

from Lainaaja import Ui_MainWindow
import dbOperations
import cipher

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia seupUi
        self.ui.setupUi(self)

        try: 
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)
            self.plainTextPassword = cipher.decryptString(self.currentSettings['password'])
        except Exception as error:
            title = 'Asetustiedosto saattaa puuttua!'
            text = 'Tietokannan asetusten luku ein onnistunut'
            detailedText = str(error)
            self.openWarning(title, text, detailedText)

        self.setInitialElements()

        # Ohjelman käynnistyksessä piilotetaan tarpeettomat elementit
        
        # OHJELMOIDUT SIGNAALIT

        # Kun Tulosta-painiketta on klikattu, kutsutaan updatePrintedLabel metodi

        self.ui.lainaaPushButton.clicked.connect(self.activateLend)
        self.ui.ajokorttiLineEdit.returnPressed.connect(self.activateAvain)
        self.ui.avainLineEdit.returnPressed.connect(self.tilaValmis)
        self.ui.palautaPushButton.clicked.connect(self.activateReturn)
        self.ui.naytaTiedotPushButton.clicked.connect(self.tiedot)
        self.ui.alkuunPushButton.clicked.connect(self.startView)
        self.ui.okPushButton.clicked.connect(self.saveLendingData)

        # OHJELMOIDUT SLOTIT

    def setInitialElements(self):
        self.ui.ajokorttiLineEdit.hide()
        self.ui.hetuLabel.hide()
        self.ui.avainLineEdit.hide()
        self.ui.rekisteriNrLabel.hide()
        self.ui.naytaTiedotPushButton.hide()
        self.ui.okPushButton.hide()
        self.ui.alkuunPushButton.hide()
        self.ui.alkuLabel.hide()
        self.ui.paattyminenLabel.hide()
        self.ui.tilaLabel.setText('VALITSE TOIMINTO')

    def startView(self):
        self.ui.lainaaPushButton.show()
        self.ui.palautaPushButton.show()
        self.ui.ajokorttiLineEdit.hide()
        self.ui.ajokorttiLineEdit.setText('')
        self.ui.hetuLabel.hide()
        self.ui.avainLineEdit.hide()
        self.ui.avainLineEdit.setText('')
        self.ui.rekisteriNrLabel.hide()
        self.ui.naytaTiedotPushButton.hide()
        self.ui.okPushButton.hide()
        self.ui.alkuunPushButton.hide()
        self.ui.alkuLabel.hide()
        self.ui.paattyminenLabel.hide()
        self.ui.tilaLabel.setText('VALITSE TOIMINTO')

    def activateLend(self):
        self.ui.tilaLabel.setText('AUTON LAINAUS') 
        self.ui.ajokorttiLineEdit.show()
        self.ui.alkuunPushButton.show()
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
        self.ui.okPushButton.show()
        self.ui.tilaLabel.setText('VALMIS')

    def activateReturn(self):
        self.ui.tilaLabel.setText('AUTON PALAUTUS')
        self.ui.avainLineEdit.show()
        self.ui.alkuunPushButton.show()
        self.ui.avainLineEdit.setFocus()
        self.ui.rekisteriNrLabel.show()
        self.ui.lainaaPushButton.hide()
        self.ui.palautaPushButton.hide()

    def tiedot(self):
        self.ui.hetuLabel.show() 
        self.ui.rekisteriNrLabel.show()
        self.ui.alkuLabel.show()
        self.ui.alkuLabel.setText(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        print(datetime.datetime.now())
        self.ui.paattyminenLabel.show()
        self.ui.naytaTiedotPushButton.hide()

    def saveLendingData(self):
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['Password'] = plainTextPassword

        try:
            dbConnection = dbOperations.DbConnection(dbSettings)
            ssn = self.ui.hetuLabel.text()
            key = self.ui.rekisteriNrLabel.text()
            dataDictionary = {'hetu': ssn,
                              'rekisterinumero': key}
            dbConnection.addToTable('lainaus', dataDictionary)
            
            self.startView()
            self.ui.statusbar.showMessage('Auton lainaustiedot tallenettiin', 5000)
        except Exception as e:
            title = 'Lainaustietojen tallentaminen ei onnistunut'
            text = 'Ajokortin tai rekisterinumertiedot virheelliset! Ota yhteyttä hekilökuntaan.'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)

    def openWarning(self, title: str, text: str, detailedText: str) -> None:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setDetailedText(detailedText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()
# LUODAAN VARSINAINEN SOVELLUS

app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
windows = MainWindow()
windows.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä (event loop)
app.exec()


