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
        self.ui.lainausAvainLineEdit.returnPressed.connect(self.lainaaTilaValmis)
        self.ui.naytaLainausTiedotPushButton.clicked.connect(self.lainausTiedot)
        self.ui.okLainaaPushButton.clicked.connect(self.saveLendingData)
        
        self.ui.palautaPushButton.clicked.connect(self.activateReturn)
        self.ui.palautusAvainLineEdit.returnPressed.connect(self.palautaTilaValmis)
        self.ui.naytaPalautusTiedotPushButton.clicked.connect(self.palautusTiedot)
        
        self.ui.alkuunPushButton.clicked.connect(self.startView)

        # OHJELMOIDUT SLOTIT

    def setInitialElements(self):
        self.ui.ajokorttiLineEdit.hide()
        self.ui.hetuLabel.hide()
        self.ui.lainausAvainLineEdit.hide()
        self.ui.palautusAvainLineEdit.hide()
        self.ui.rekisteriNrLabel.hide()
        self.ui.naytaLainausTiedotPushButton.hide()
        self.ui.naytaPalautusTiedotPushButton.hide()
        self.ui.okLainaaPushButton.hide()
        self.ui.alkuunPushButton.hide()
        self.ui.alkuLabel.hide()
        self.ui.paattyminenLabel.hide()
        self.ui.tilaLabel.setText('VALITSE TOIMINTO')
        self.ui.nimiLabel.hide()
        self.ui.autoLabel.hide()
        self.ui.vapaatAutotTableWidget.hide()
        self.ui.vapaatAutotTitlelabel.hide()
        self.ui.okPalautaPushButton.hide()
        
    def startView(self):
        self.ui.lainaaPushButton.show()
        self.ui.palautaPushButton.show()
        self.ui.ajokorttiLineEdit.hide()
        self.ui.ajokorttiLineEdit.setText('')
        self.ui.hetuLabel.hide()
        self.ui.lainausAvainLineEdit.hide()
        self.ui.lainausAvainLineEdit.setText('')
        self.ui.palautusAvainLineEdit.setText('')
        self.ui.rekisteriNrLabel.setText('')
        self.ui.rekisteriNrLabel.hide()
        self.ui.naytaLainausTiedotPushButton.hide()
        self.ui.naytaPalautusTiedotPushButton.hide()
        self.ui.okLainaaPushButton.hide()
        self.ui.alkuunPushButton.hide()
        self.ui.alkuLabel.hide()
        self.ui.paattyminenLabel.hide()
        self.ui.tilaLabel.setText('VALITSE TOIMINTO')
        self.ui.nimiLabel.hide()
        self.ui.autoLabel.hide()
        self.ui.vapaatAutotTableWidget.hide()
        self.ui.vapaatAutotTitlelabel.hide()
        self.ui.okPalautaPushButton.hide()

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
        self.ui.lainausAvainLineEdit.show()
        self.ui.lainausAvainLineEdit.setFocus()
        self.ui.rekisteriNrLabel.hide()

    def activateReturn(self):
        self.ui.tilaLabel.setText('AUTON PALAUTUS')
        self.ui.palautusAvainLineEdit.show()
        self.ui.alkuunPushButton.show()
        self.ui.palautusAvainLineEdit.setFocus()
        self.ui.rekisteriNrLabel.show()
        self.ui.lainaaPushButton.hide()
        self.ui.palautaPushButton.hide()    

    def lainaaTilaValmis(self):
        self.ui.lainausAvainLineEdit.hide()
        self.ui.rekisteriNrLabel.hide()
        self.ui.naytaLainausTiedotPushButton.show()
        self.ui.okLainaaPushButton.show()
        self.ui.tilaLabel.setText('VALMIS')

    def palautaTilaValmis(self):
        self.ui.palautusAvainLineEdit.hide()
        self.ui.rekisteriNrLabel.hide()
        self.ui.naytaPalautusTiedotPushButton.show()
        self.ui.okPalautaPushButton.show()
        self.ui.tilaLabel.setText('VALMIS')

    def lainausTiedot(self):
        self.ui.hetuLabel.show() 
        self.ui.rekisteriNrLabel.show()
        self.ui.alkuLabel.show()
        self.ui.alkuLabel.setText(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        self.ui.nimiLabel.show()
        self.ui.autoLabel.show()
        self.ui.naytaLainausTiedotPushButton.hide()

        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['Password'] = plainTextPassword

        try:
            dbConnection = dbOperations.DbConnection(dbSettings)
            valitutKolumnit = dbConnection.readChosenColumnFormTable('lainaaja', 'hetu, etunimi, sukunimi')
            print(valitutKolumnit)
            for tuple in valitutKolumnit:
                print(tuple[1] + ' ' + tuple[2])
                if tuple[0] == self.ui.hetuLabel.text():
                    self.ui.nimiLabel.setText(tuple[1] + ' ' + tuple[2])
        except Exception as e:
            title = 'Tuntematon Henkilötunnus!'
            text = 'Lainaajan henkilötunnus ei löytynyt tietokannasta! Ota yhteyttä hekilökuntaan.'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)

        try:
            dbConnection = dbOperations.DbConnection(dbSettings)
            valitutKolumnit = dbConnection.readChosenColumnFormTable('auto', 'rekisterinumero, merkki, malli')
            for tuple in valitutKolumnit:
                print(tuple[1] + ' ' + tuple[2])
                if tuple[0] == self.ui.rekisteriNrLabel.text():
                    self.ui.autoLabel.setText(tuple[1] + ' ' + tuple[2])
        except Exception as e:
            title = 'Tuntematon Rekisterinumero!'
            text = 'Auton Rekisterinumero ei löytynyt tietokannasta! Ota yhteyttä hekilökuntaan.'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)

    def palautusTiedot(self):
        self.ui.hetuLabel.show() 
        self.ui.hetuLabel.setText('huuhaaa')
        self.ui.rekisteriNrLabel.show()
        self.ui.rekisteriNrLabel.setText('Hallo')
        self.ui.alkuLabel.show()
        self.ui.alkuLabel.setText('hii')
        self.ui.paattyminenLabel.show()
        self.ui.paattyminenLabel.setText(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        self.ui.nimiLabel.show()
        self.ui.autoLabel.show()
        self.ui.naytaPalautusTiedotPushButton.hide()

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


