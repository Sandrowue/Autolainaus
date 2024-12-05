import os # Polkumääritykset
import sys # Käynnistysargumentit
import json 
import dbOperations

from PySide6 import QtWidgets
from Autolainaus import Ui_MainWindow
from Settings_dialog import Ui_Dialog as Settings_Dialog
from About_dialog import Ui_Dialog as About_Dialog


import cipher

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            with open('settings.json', 'rt') as settingsFile:
                self.currentSettings = json.load(settingsFile)

                encryptedPassword = self.currentSettings['password']
                print('Tietokannan salattu salasana: ', encryptedPassword)
                
                plainPassword = cipher.decryptString(encryptedPassword)
                print('Selväkielinen salasana on', plainPassword)
                
        except Exception as e:
            self.openSettingsDialog()
            
            

        # Ohjelmoidut signaalit
        # Asetukset-valikon muokkaa toiminto avaa Asetukset-dialogi-ikkunan
        self.ui.actionMuokkaa.triggered.connect(self.openSettingsDialog)
        self.ui.actionTietoja_ohjelmasta.triggered.connect(self.openAboutDialog)

    # Ohjelmoidut Slotit
    # Dialogien avausmetodit
    def openSettingsDialog(self):
        self.saveSettingsDialog = SaveSettingsDialog()
        self.saveSettingsDialog.setWindowTitle('Palvelinasetukset')
        self.saveSettingsDialog.exec()

    def openAboutDialog(self):
        self. aboutDialog = AboutWindow()
        self.aboutDialog.setWindowTitle('Tietoja ohjelmasta')
        self.aboutDialog.exec()

    # Asetusten tallennusikkunan luokka
class SaveSettingsDialog(QtWidgets.QDialog, Settings_Dialog):
    def __init__(self):
        super().__init__()

        self.ui = Settings_Dialog()
        self.ui.setupUi(self)

        self.currentSettings = {}
        
        
        try:
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            self.ui.palvelinLineEdit.setText(self.currentSettings['server'])
            self.ui.porttiLineEdit.setText(self.currentSettings['port'])
            self.ui.tietokantaLineEdit.setText(self.currentSettings['database'])
            self.ui.KayttajatunnusLineEdit.setText(self.currentSettings['userName'])
            self.ui.vanhaSalasanaLineEdit.setText(self.currentSettings['password'])
            

            self.ui.vaihdaSalasanapushButton.setEnabled(False)
            self.ui.tallennaPushButton.clicked.connect(self.saveUserToJsonFile)
            self.ui.uusiSalasanaLineEdit.textEdited.connect(self.ui.vaihdaSalasanapushButton.setEnabled(True))
            self.ui.vaihdaSalasanapushButton.clicked.connect(self.savePasswordToJsonFile)
        
        except Exception as e:
            self.openInfo()
            
            self.ui.tallennaPushButton.clicked.connect(self.saveAllToJsonFile)

            self.ui.vanhaSalasanaLineEdit.setEnabled(False)
            self.ui.vaihdaSalasanapushButton.setEnabled(False)

 

    def saveAllToJsonFile(self):

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.palvelinLineEdit.text()
        port = self.ui.porttiLineEdit.text()
        database = self.ui.tietokantaLineEdit.text() 
        userName = self.ui.KayttajatunnusLineEdit.text()
        newPassword = self.ui.uusiSalasanaLineEdit.text()

        # Muutetaan merkkijono tavumuotoon (byte, merkisö UTF-8)
        plainTextPassword = newPassword

        # Salataan ja muunnetaan tavalliseksi merkkijonoksi, jotta JSON-tallennus onnistuu
        encryptedPassword = cipher.encryptString(plainTextPassword)

        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName,
            'password': encryptedPassword
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto ja korjataan asetukset
        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)


    def saveUserToJsonFile(self):

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.palvelinLineEdit.text()
        port = self.ui.porttiLineEdit.text()
        database = self.ui.tietokantaLineEdit.text() 
        userName = self.ui.KayttajatunnusLineEdit.text()
        
        
        
        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName, 
            'password': self.currentSettings['password']    
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto ja korjataan asetukse

        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)
        
            
    def savePasswordToJsonFile(self):

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        newPassword = self.ui.uusiSalasanaLineEdit.text()

        # Muutetaan merkkijono tavumuotoon (byte, merkisö UTF-8)
        plainTextPassword = newPassword

        # Salataan ja muunnetaan tavalliseksi merkkijonoksi, jotta JSON-tallennus onnistuu
        encryptedPassword = cipher.encryptString(plainTextPassword)

        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': self.currentSettings['server'],
            'port': self.currentSettings['port'],
            'database': self.currentSettings['database'],
            'userName': self.currentSettings['userName'],
            'password': encryptedPassword
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto ja korjataan asetukset
        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)               

    # Avataan Message Box
    def openInfo(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle('Huomautus!')
        msgBox.setText('settings.json tiedosto puuttuu!')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

class AboutWindow(QtWidgets.QDialog, About_Dialog):
    def __init__(self):
        super().__init__()
        
        self.ui = About_Dialog()

        self.ui.setupUi(self)

if __name__ == "__main__":
    # Luodaan sovellus ja setetaan tyyliksi Fusion
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fosion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.setWindowTitle('Autolainauksen hallinta')
    window.show()

    app.exec()