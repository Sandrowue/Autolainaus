# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autolainaus.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(889, 642)
        self.actionMuokkaa = QAction(MainWindow)
        self.actionMuokkaa.setObjectName(u"actionMuokkaa")
        self.actionTietoja_ohjelmasta = QAction(MainWindow)
        self.actionTietoja_ohjelmasta.setObjectName(u"actionTietoja_ohjelmasta")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 911, 591))
        self.lainaajat = QWidget()
        self.lainaajat.setObjectName(u"lainaajat")
        self.henkilotunnusLabel = QLabel(self.lainaajat)
        self.henkilotunnusLabel.setObjectName(u"henkilotunnusLabel")
        self.henkilotunnusLabel.setGeometry(QRect(30, 20, 150, 25))
        font = QFont()
        font.setPointSize(14)
        self.henkilotunnusLabel.setFont(font)
        self.etunimiLabel = QLabel(self.lainaajat)
        self.etunimiLabel.setObjectName(u"etunimiLabel")
        self.etunimiLabel.setGeometry(QRect(30, 60, 150, 25))
        self.etunimiLabel.setFont(font)
        self.sukunimiLabel = QLabel(self.lainaajat)
        self.sukunimiLabel.setObjectName(u"sukunimiLabel")
        self.sukunimiLabel.setGeometry(QRect(30, 110, 150, 25))
        self.sukunimiLabel.setFont(font)
        self.ryhmaLabel = QLabel(self.lainaajat)
        self.ryhmaLabel.setObjectName(u"ryhmaLabel")
        self.ryhmaLabel.setGeometry(QRect(30, 160, 150, 25))
        self.ryhmaLabel.setFont(font)
        self.ajoneuvoluokkaLabel = QLabel(self.lainaajat)
        self.ajoneuvoluokkaLabel.setObjectName(u"ajoneuvoluokkaLabel")
        self.ajoneuvoluokkaLabel.setGeometry(QRect(30, 210, 150, 25))
        self.ajoneuvoluokkaLabel.setFont(font)
        self.henkilotunnusLineEdit = QLineEdit(self.lainaajat)
        self.henkilotunnusLineEdit.setObjectName(u"henkilotunnusLineEdit")
        self.henkilotunnusLineEdit.setGeometry(QRect(200, 20, 150, 25))
        self.henkilotunnusLineEdit.setFont(font)
        self.etunimiLineEdit = QLineEdit(self.lainaajat)
        self.etunimiLineEdit.setObjectName(u"etunimiLineEdit")
        self.etunimiLineEdit.setGeometry(QRect(200, 60, 150, 25))
        self.etunimiLineEdit.setFont(font)
        self.sukunimiLineEdit = QLineEdit(self.lainaajat)
        self.sukunimiLineEdit.setObjectName(u"sukunimiLineEdit")
        self.sukunimiLineEdit.setGeometry(QRect(200, 110, 150, 25))
        self.sukunimiLineEdit.setFont(font)
        self.ajoneuvoluokkaLineEdit = QLineEdit(self.lainaajat)
        self.ajoneuvoluokkaLineEdit.setObjectName(u"ajoneuvoluokkaLineEdit")
        self.ajoneuvoluokkaLineEdit.setGeometry(QRect(200, 210, 150, 25))
        self.ajoneuvoluokkaLineEdit.setFont(font)
        self.lainaajatLabel = QLabel(self.lainaajat)
        self.lainaajatLabel.setObjectName(u"lainaajatLabel")
        self.lainaajatLabel.setGeometry(QRect(30, 310, 200, 25))
        self.lainaajatLabel.setFont(font)
        self.lainaajatTableWidget = QTableWidget(self.lainaajat)
        self.lainaajatTableWidget.setObjectName(u"lainaajatTableWidget")
        self.lainaajatTableWidget.setGeometry(QRect(30, 341, 600, 225))
        self.tallennaLainaajatPushButton = QPushButton(self.lainaajat)
        self.tallennaLainaajatPushButton.setObjectName(u"tallennaLainaajatPushButton")
        self.tallennaLainaajatPushButton.setGeometry(QRect(460, 210, 100, 30))
        self.tallennaLainaajatPushButton.setFont(font)
        self.viivakoodiPushButton = QPushButton(self.lainaajat)
        self.viivakoodiPushButton.setObjectName(u"viivakoodiPushButton")
        self.viivakoodiPushButton.setGeometry(QRect(460, 160, 100, 30))
        self.viivakoodiPushButton.setFont(font)
        self.ryhmaComboBox = QComboBox(self.lainaajat)
        self.ryhmaComboBox.setObjectName(u"ryhmaComboBox")
        self.ryhmaComboBox.setGeometry(QRect(200, 160, 150, 25))
        self.sahkopostiLineEdit = QLineEdit(self.lainaajat)
        self.sahkopostiLineEdit.setObjectName(u"sahkopostiLineEdit")
        self.sahkopostiLineEdit.setGeometry(QRect(200, 260, 150, 25))
        self.sahkopostiLabel = QLabel(self.lainaajat)
        self.sahkopostiLabel.setObjectName(u"sahkopostiLabel")
        self.sahkopostiLabel.setGeometry(QRect(30, 260, 150, 25))
        self.sahkopostiLabel.setFont(font)
        self.tabWidget.addTab(self.lainaajat, "")
        self.autot = QWidget()
        self.autot.setObjectName(u"autot")
        self.merkkiLabel = QLabel(self.autot)
        self.merkkiLabel.setObjectName(u"merkkiLabel")
        self.merkkiLabel.setGeometry(QRect(30, 20, 150, 25))
        self.merkkiLabel.setFont(font)
        self.malliLabel = QLabel(self.autot)
        self.malliLabel.setObjectName(u"malliLabel")
        self.malliLabel.setGeometry(QRect(30, 70, 150, 25))
        self.malliLabel.setFont(font)
        self.vuosimalliLabel = QLabel(self.autot)
        self.vuosimalliLabel.setObjectName(u"vuosimalliLabel")
        self.vuosimalliLabel.setGeometry(QRect(30, 120, 150, 25))
        self.vuosimalliLabel.setFont(font)
        self.rekisterinumeroLabel = QLabel(self.autot)
        self.rekisterinumeroLabel.setObjectName(u"rekisterinumeroLabel")
        self.rekisterinumeroLabel.setGeometry(QRect(30, 170, 150, 25))
        self.rekisterinumeroLabel.setFont(font)
        self.henkilomaaraLabel = QLabel(self.autot)
        self.henkilomaaraLabel.setObjectName(u"henkilomaaraLabel")
        self.henkilomaaraLabel.setGeometry(QRect(30, 220, 150, 25))
        self.henkilomaaraLabel.setFont(font)
        self.autoluetteloLabel = QLabel(self.autot)
        self.autoluetteloLabel.setObjectName(u"autoluetteloLabel")
        self.autoluetteloLabel.setGeometry(QRect(30, 280, 150, 25))
        self.autoluetteloLabel.setFont(font)
        self.autoluetteloTableWidget = QTableWidget(self.autot)
        self.autoluetteloTableWidget.setObjectName(u"autoluetteloTableWidget")
        self.autoluetteloTableWidget.setGeometry(QRect(30, 310, 600, 225))
        self.merkkiLineEdit = QLineEdit(self.autot)
        self.merkkiLineEdit.setObjectName(u"merkkiLineEdit")
        self.merkkiLineEdit.setGeometry(QRect(200, 20, 150, 25))
        self.merkkiLineEdit.setFont(font)
        self.malliLineEdit = QLineEdit(self.autot)
        self.malliLineEdit.setObjectName(u"malliLineEdit")
        self.malliLineEdit.setGeometry(QRect(200, 70, 150, 25))
        self.malliLineEdit.setFont(font)
        self.vuosimalliLineEdit = QLineEdit(self.autot)
        self.vuosimalliLineEdit.setObjectName(u"vuosimalliLineEdit")
        self.vuosimalliLineEdit.setGeometry(QRect(200, 120, 150, 25))
        self.vuosimalliLineEdit.setFont(font)
        self.rekisterinumeroLineEdit = QLineEdit(self.autot)
        self.rekisterinumeroLineEdit.setObjectName(u"rekisterinumeroLineEdit")
        self.rekisterinumeroLineEdit.setGeometry(QRect(200, 170, 150, 25))
        self.rekisterinumeroLineEdit.setFont(font)
        self.henkilomaaraLineEdit = QLineEdit(self.autot)
        self.henkilomaaraLineEdit.setObjectName(u"henkilomaaraLineEdit")
        self.henkilomaaraLineEdit.setGeometry(QRect(200, 220, 150, 25))
        self.henkilomaaraLineEdit.setFont(font)
        self.tallennaAutotPushButton = QPushButton(self.autot)
        self.tallennaAutotPushButton.setObjectName(u"tallennaAutotPushButton")
        self.tallennaAutotPushButton.setGeometry(QRect(460, 220, 100, 30))
        self.tallennaAutotPushButton.setFont(font)
        self.tabWidget.addTab(self.autot, "")
        self.ryhmat = QWidget()
        self.ryhmat.setObjectName(u"ryhmat")
        self.ryhmaLabel_2 = QLabel(self.ryhmat)
        self.ryhmaLabel_2.setObjectName(u"ryhmaLabel_2")
        self.ryhmaLabel_2.setGeometry(QRect(30, 30, 150, 25))
        self.ryhmaLabel_2.setFont(font)
        self.vastuuhenkiloLabel = QLabel(self.ryhmat)
        self.vastuuhenkiloLabel.setObjectName(u"vastuuhenkiloLabel")
        self.vastuuhenkiloLabel.setGeometry(QRect(30, 80, 150, 25))
        self.vastuuhenkiloLabel.setFont(font)
        self.ryhmaLineEdit_2 = QLineEdit(self.ryhmat)
        self.ryhmaLineEdit_2.setObjectName(u"ryhmaLineEdit_2")
        self.ryhmaLineEdit_2.setGeometry(QRect(210, 30, 150, 25))
        self.vastuuhenkiloLineEdit = QLineEdit(self.ryhmat)
        self.vastuuhenkiloLineEdit.setObjectName(u"vastuuhenkiloLineEdit")
        self.vastuuhenkiloLineEdit.setGeometry(QRect(210, 80, 150, 25))
        self.ryhmatTableWidget = QTableWidget(self.ryhmat)
        if (self.ryhmatTableWidget.columnCount() < 2):
            self.ryhmatTableWidget.setColumnCount(2)
        if (self.ryhmatTableWidget.rowCount() < 7):
            self.ryhmatTableWidget.setRowCount(7)
        self.ryhmatTableWidget.setObjectName(u"ryhmatTableWidget")
        self.ryhmatTableWidget.setGeometry(QRect(30, 180, 600, 225))
        self.ryhmatTableWidget.setRowCount(7)
        self.ryhmatTableWidget.setColumnCount(2)
        self.ryhmat_label = QLabel(self.ryhmat)
        self.ryhmat_label.setObjectName(u"ryhmat_label")
        self.ryhmat_label.setGeometry(QRect(30, 150, 170, 25))
        self.ryhmat_label.setFont(font)
        self.tallennaRyhmatPushButton = QPushButton(self.ryhmat)
        self.tallennaRyhmatPushButton.setObjectName(u"tallennaRyhmatPushButton")
        self.tallennaRyhmatPushButton.setGeometry(QRect(450, 80, 100, 30))
        self.tallennaRyhmatPushButton.setFont(font)
        self.tabWidget.addTab(self.ryhmat, "")
        self.raportit = QWidget()
        self.raportit.setObjectName(u"raportit")
        self.raporttiComboBox = QComboBox(self.raportit)
        self.raporttiComboBox.setObjectName(u"raporttiComboBox")
        self.raporttiComboBox.setGeometry(QRect(30, 80, 150, 25))
        self.raporttiComboBox.setFont(font)
        self.esikatseluTableWidget = QTableWidget(self.raportit)
        self.esikatseluTableWidget.setObjectName(u"esikatseluTableWidget")
        self.esikatseluTableWidget.setGeometry(QRect(30, 280, 600, 225))
        self.alkaaLabel = QLabel(self.raportit)
        self.alkaaLabel.setObjectName(u"alkaaLabel")
        self.alkaaLabel.setGeometry(QRect(30, 140, 150, 25))
        self.alkaaLabel.setFont(font)
        self.paattyylabel = QLabel(self.raportit)
        self.paattyylabel.setObjectName(u"paattyylabel")
        self.paattyylabel.setGeometry(QRect(240, 140, 150, 25))
        self.paattyylabel.setFont(font)
        self.tulostaPushButton = QPushButton(self.raportit)
        self.tulostaPushButton.setObjectName(u"tulostaPushButton")
        self.tulostaPushButton.setGeometry(QRect(440, 220, 100, 30))
        self.tulostaPushButton.setFont(font)
        self.esikatseluLabel = QLabel(self.raportit)
        self.esikatseluLabel.setObjectName(u"esikatseluLabel")
        self.esikatseluLabel.setGeometry(QRect(30, 250, 150, 25))
        self.esikatseluLabel.setFont(font)
        self.raporttiLabel = QLabel(self.raportit)
        self.raporttiLabel.setObjectName(u"raporttiLabel")
        self.raporttiLabel.setGeometry(QRect(30, 30, 150, 25))
        self.raporttiLabel.setFont(font)
        self.alkaaDateEdit = QDateEdit(self.raportit)
        self.alkaaDateEdit.setObjectName(u"alkaaDateEdit")
        self.alkaaDateEdit.setGeometry(QRect(30, 180, 150, 25))
        self.alkaaDateEdit.setFont(font)
        self.alkaaDateEdit.setCalendarPopup(True)
        self.paattyyDateEdit = QDateEdit(self.raportit)
        self.paattyyDateEdit.setObjectName(u"paattyyDateEdit")
        self.paattyyDateEdit.setGeometry(QRect(240, 180, 150, 25))
        self.paattyyDateEdit.setFont(font)
        self.paattyyDateEdit.setCalendarPopup(True)
        self.tabWidget.addTab(self.raportit, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 889, 21))
        self.menuAsetukset = QMenu(self.menubar)
        self.menuAsetukset.setObjectName(u"menuAsetukset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAsetukset.menuAction())
        self.menuAsetukset.addAction(self.actionMuokkaa)
        self.menuAsetukset.addAction(self.actionTietoja_ohjelmasta)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionMuokkaa.setText(QCoreApplication.translate("MainWindow", u"Muokkaa...", None))
#if QT_CONFIG(shortcut)
        self.actionMuokkaa.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionTietoja_ohjelmasta.setText(QCoreApplication.translate("MainWindow", u"Tietoja ohjelmasta...", None))
        self.henkilotunnusLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.etunimiLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.sukunimiLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.ryhmaLabel.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4", None))
        self.ajoneuvoluokkaLabel.setText(QCoreApplication.translate("MainWindow", u"Ajoneuvoluokka", None))
        self.lainaajatLabel.setText(QCoreApplication.translate("MainWindow", u"Rekister\u00f6idyt lainaajat", None))
        self.tallennaLainaajatPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.viivakoodiPushButton.setText(QCoreApplication.translate("MainWindow", u"Viivakoodi", None))
        self.sahkopostiLabel.setText(QCoreApplication.translate("MainWindow", u"S\u00e4hk\u00f6posti", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lainaajat), QCoreApplication.translate("MainWindow", u"Lainaajat", None))
        self.merkkiLabel.setText(QCoreApplication.translate("MainWindow", u"Merkki", None))
        self.malliLabel.setText(QCoreApplication.translate("MainWindow", u"Malli", None))
        self.vuosimalliLabel.setText(QCoreApplication.translate("MainWindow", u"Vuosimalli", None))
        self.rekisterinumeroLabel.setText(QCoreApplication.translate("MainWindow", u"Rekisterinumero", None))
        self.henkilomaaraLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6m\u00e4\u00e4r\u00e4", None))
        self.autoluetteloLabel.setText(QCoreApplication.translate("MainWindow", u"Autoluettelo", None))
        self.tallennaAutotPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.autot), QCoreApplication.translate("MainWindow", u"Autot", None))
        self.ryhmaLabel_2.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4n nimi", None))
        self.vastuuhenkiloLabel.setText(QCoreApplication.translate("MainWindow", u"Vastuuhenkil\u00f6", None))
        self.ryhmat_label.setText(QCoreApplication.translate("MainWindow", u"Tallennetut ryhm\u00e4t", None))
        self.tallennaRyhmatPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ryhmat), QCoreApplication.translate("MainWindow", u"Ryhm\u00e4t", None))
        self.alkaaLabel.setText(QCoreApplication.translate("MainWindow", u"Alkaa", None))
        self.paattyylabel.setText(QCoreApplication.translate("MainWindow", u"P\u00e4\u00e4ttyy", None))
        self.tulostaPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.esikatseluLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.raporttiLabel.setText(QCoreApplication.translate("MainWindow", u"Raportti", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.raportit), QCoreApplication.translate("MainWindow", u"Raportit", None))
        self.menuAsetukset.setTitle(QCoreApplication.translate("MainWindow", u"Asetukset", None))
    # retranslateUi

