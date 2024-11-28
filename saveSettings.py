import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-muunnokset

from PySide6 import QtWidgets # Qt-vimpaimet
from Autolainaus_settings import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow-ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    # Määritellään oliomuodostin ja kutsutaan yliluokan muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Luetaan asetustietosto Python-sanakirjaksi
        self.currentSettings = {}
        try:
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            self.ui.palvelinLineEdit.setText(self.currentSettings['server'])
            self.ui.porttiLineEdit.setText(self.currentSettings['port'])
            self.ui.tietokantaLineEdit.setText(self.currentSettings['database'])
            self.ui.KayttajatunnusLineEdit.setText(self.currentSettings['userName'])
            self.ui.passwordLineEdit.setText(self.currentSettings['password'])
        except Exception as e:
            self.openWarning()
        # Kun Tallenna-painiketta on klikattu, kutsutaan saveToJsonFile-metodia
        self.ui.tallennaPushButton.clicked.connect(self.saveToJsonFile)

        # Tallennetaan käyttöliittymään syötetyt asetukset tiedostoon
    def saveToJsonFile(self):

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.palvelinLineEdit.text()
        port = self.ui.porttiLineEdit.text()
        database = self.ui.tietokantaLineEdit.text() 
        userName = self.ui.KayttajatunnusLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        # Lisää tähän salasanan kryptaus

        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName,
            'password': password
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto ja korjataan asetukset
        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)

    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle('Huomautus!')
        msgBox.setText('settings.json tiedosto puuttuu!')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

if __name__ == "__main__":

    # Luodaan sovellus
    app = QtWidgets.QApplication(sys.argv)

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    windows = MainWindow()
    windows.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()