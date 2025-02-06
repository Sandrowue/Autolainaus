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
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)
                print(self.currentSettings)

                encryptedPassword = self.currentSettings['password']
                print('Tietokannan salattu salasana: ', encryptedPassword)
                
                plainPassword = cipher.decryptString(encryptedPassword)
                print('Selväkielinen salasana on', plainPassword)
                
            # Päivitetään yhdistelmäruutjen arvot ohjelman käynnistyksen yhteydessä
            

        except Exception as e:
            print(str(e))
            self.openSettingsDialog()
            
        self.refreshUi()

        # OHJELMOIDUT SIGNAALIT
        # Valikkotoiminnot
        self.ui.actionMuokkaa.triggered.connect(self.openSettingsDialog)
        self.ui.actionTietoja_ohjelmasta.triggered.connect(self.openAboutDialog)

        # Välilehtien vaihdot päivittävät comboxit
        self.ui.tabWidget.currentChanged.connect(self.updateCombox)

        # Painikkeet
        self.ui.tallennaRyhmatPushButton.clicked.connect(self.saveGroup)
        self.ui.tallennaLainaajatPushButton.clicked.connect(self.savePerson)
        self.ui.tallennaAutotPushButton.clicked.connect(self.saveCar)
        

    # OHJELMOIDUT SLOTIT

    # Valikkotoimintojen slotit

    # Dialogien avausmetodit
    def openSettingsDialog(self):
        self.saveSettingsDialog = SaveSettingsDialog()
        self.saveSettingsDialog.setWindowTitle('Palvelinasetukset')
        self.saveSettingsDialog.exec()

    def openAboutDialog(self):
        self. aboutDialog = AboutWindow()
        self.aboutDialog.setWindowTitle('Tietoja ohjelmasta')
        self.aboutDialog.exec()

    # Yleinen käyttöliittymän verestys (refresh)
    def refreshUi(self):
        self.updateCombox()
        self.updateLainaajaTableWidget()
        self.updateAutoTableWidget()
        self.updateGroupTableWidget()

    # PAINIKKEIDEN SLOTIT
    
    # Ryhmän valinta -ruudun arvojen päivitys
    def updateCombox(self):
        dbSettings = self.currentSettings
        dbConnection = dbOperations.DbConnection(dbSettings)
        
        # Tehdään lista lainaaja
        groupList = dbConnection.readChosenColumnFormTable('ryhma', 'ryhma')
        simpleList = []
        for tuple in groupList:
            simpleList.append(tuple[0])
        self.ui.ryhmaComboBox.clear()
        self.ui.ryhmaComboBox.addItems(simpleList)
        
    # Lainaajat-taulukon päivitys
    def updateLainaajaTableWidget(self):
        dbSettings = self.currentSettings
        dbConnection = dbOperations.DbConnection(dbSettings)
        tableData = dbConnection.readAllColumnsFromTable('lainaaja')
        print('Lainaajataulun tiedot:', tableData)
        headerRow = ['Henkilötunnus', 'Etunimi', 'Sukunimi', 'Ryhmä', 'Ajokortti', 'Sähköposti']
        self.ui.lainaajatTableWidget.setHorizontalHeaderLabels(headerRow)
        for row in range(len(tableData)): # Luetaan listaa riveittäin
            for column in range(len(tableData[row])): # Luetaan monikkoa sarakkeittain
            # Muutetaan merkkijonoksi ja QTableWidgetItem-olioksi
                data = QtWidgets.QTableWidgetItem(str(tableData[row][column]))
                self.ui.lainaajatTableWidget.setItem(row, column, data)
    
    # Autot-taulukon päivitys
    def updateAutoTableWidget(self):
        dbSettings = self.currentSettings
        dbConnection = dbOperations.DbConnection(dbSettings)
        tableData = dbConnection.readAllColumnsFromTable('auto')
        print('Autotaulun tiedot:', tableData)
        headerRow = ['Rekisterinumero', 'Malli', 'Merkki', 'Vuosimalli', 'Henkilömäärä']
        self.ui.autoluetteloTableWidget.setHorizontalHeaderLabels(headerRow)

    # Ryhmät-taulukon päivitys
    def updateGroupTableWidget(self):
        dbSettings = self.currentSettings
        dbConnection = dbOperations.DbConnection(dbSettings)
        tableData = dbConnection.readAllColumnsFromTable('ryhma')
        print('Ryhmataulun tiedot:', tableData)
        headerRow = ['ryhma', 'vastuuhenkilo']
        self.ui.ryhmatTableWidget.setHorizontalHeaderLabels(headerRow)

    # Ryhmän tallennus

    def saveCar(self):
        dbSettings = self.currentSettings
        tableName = 'auto'

        rekisterinumero = self.ui.rekisterinumeroLineEdit.text()
        malli = self.ui.malliLineEdit.text()
        merkki = self.ui.merkkiLineEdit.text()
        vuosimalli = self.ui.vuosimalliLineEdit.text()
        henkilomaara = self.ui.henkilomaaraLineEdit.text()

        groupDictionary = {
            'rekisterinumero': rekisterinumero,
            'malli': malli,
            'merkki': merkki,
            'vuosimalli': vuosimalli,
            'henkilomaara': henkilomaara
        }

        dbConnection = dbOperations.DbConnection(dbSettings)

        try:
            dbConnection.addToTable(tableName, groupDictionary)
        except Exception as e:
            print('Virheilmoitus', str(e))
            self.openWarning('Virhe!', f'Toiminto keskeytyi! {e}')

    def savePerson(self):
        dbSettings = self.currentSettings
        tableName = 'lainaaja'
        
        hetu = self.ui.henkilotunnusLineEdit.text()
        etunimi = self.ui.etunimiLineEdit.text()
        sukunimi = self.ui.sukunimiLineEdit.text()
        ryhma = self.ui.ryhmaComboBox.currentText()
        ajokortti = self.ui.ajoneuvoluokkaLineEdit.text()
        sahkoposti = self.ui.sahkopostiLineEdit.text()

        groupDictionary = {
            'hetu': hetu,
            'etunimi': etunimi,
            'sukunimi': sukunimi,
            'ryhma': ryhma,
            'ajokorttiluokka': ajokortti,
            'sahkoposti': sahkoposti
        }

        dbConnection = dbOperations.DbConnection(dbSettings)
        

        try:
            dbConnection.addToTable(tableName, groupDictionary)
            self.updateLainaajaTableWidget()
        except Exception as e:
            print('Virheilmoitus', str(e))
            self.openWarning('Virhe!', f'Toiminto keskeytyi! {e}')

    def saveGroup(self):
        # Määritellään tietokanta-asetukset
        dbSettings = self.currentSettings
        print('Tiedokannan asetukset on:', dbSettings)
        # Määritellään tallennusmetodin vaatimat parametrit
        tableName = 'ryhma'

        group = self.ui.ryhmaLineEdit_2.text()
        responsiblePerson = self.ui.vastuuhenkiloLineEdit.text()
        groupDictionary  = {'ryhma': group,
                            'vastuuhenkilo': responsiblePerson}
        
        # Luodaan tietokantayhteys-olio
        dbConnection = dbOperations.DbConnection(dbSettings)

        # Kutsutaan tallennusmetodia
        try:
            dbConnection.addToTable(tableName, groupDictionary)
        except Exception as e:
            print('Virheilmoitus', str(e))
            self.openWarning('Virhe!', f'Toiminto keskeytyi! {e}')

    def openWarning(self, title: str, text: str) -> None:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

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
            
            self.ui.vaihdaSalasanapushButton.setEnabled(False)
            self.ui.tallennaPushButton.clicked.connect(self.saveUserToJsonFile)

            # if self.ui.vanhaSalasanaLineEdit.text() == self.currentSettings['password']:
            self.ui.uusiSalasanaLineEdit.textEdited.connect(self.enableVaihdaSalasana)
            self.ui.vaihdaSalasanapushButton.clicked.connect(self.savePasswordToJsonFile)
        
        except Exception as e:
            self.openInfo()
            
            self.ui.tallennaPushButton.clicked.connect(self.saveAllToJsonFile)

            self.ui.vanhaSalasanaLineEdit.hide()
            self.ui.vaihdaSalasanapushButton.hide()
            self.ui.vanhaSalasanaLabel.hide()

    def enableVaihdaSalasana(self):
        if self.ui.vanhaSalasanaLineEdit.text() == cipher.decryptString(self.currentSettings['password']):
            self.ui.vaihdaSalasanapushButton.setEnabled(True)

    def saveAllToJsonFile(self):

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.palvelinLineEdit.text()
        port = self.ui.porttiLineEdit.text()
        database = self.ui.tietokantaLineEdit.text() 
        userName = self.ui.KayttajatunnusLineEdit.text()
        newPassword = self.ui.uusiSalasanaLineEdit.text()

        # Salataan ja muunnetaan tavalliseksi merkkijonoksi, jotta JSON-tallennus onnistuu
        encryptedPassword = cipher.encryptString(newPassword)

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

        with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                actualSettings = json.loads(jsonData)

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.palvelinLineEdit.text()
        port = self.ui.porttiLineEdit.text()
        database = self.ui.tietokantaLineEdit.text() 
        userName = self.ui.KayttajatunnusLineEdit.text()
        password = actualSettings['password']
        
        
        
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

        # Avataan asetustiedosto ja korjataan asetukse

        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)
        
            
    def savePasswordToJsonFile(self):

        with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                actualSettings = json.loads(jsonData)

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        newPassword = self.ui.uusiSalasanaLineEdit.text()

        # Salataan ja muunnetaan tavalliseksi merkkijonoksi, jotta JSON-tallennus onnistuu
        encryptedPassword = cipher.encryptString(newPassword)

        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': actualSettings['server'],
            'port': actualSettings['port'],
            'database': actualSettings['database'],
            'userName': actualSettings['userName'],
            'password': encryptedPassword
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto ja korjataan asetukset
        if self.ui.vanhaSalasanaLineEdit.text() == cipher.decryptString(actualSettings['password']):
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
    app.setStyle('fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.setWindowTitle('Autolainauksen hallinta')
    window.show()

    app.exec()