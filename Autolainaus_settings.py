# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autolainaus_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(675, 496)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.palvelinLabel = QLabel(self.centralwidget)
        self.palvelinLabel.setObjectName(u"palvelinLabel")
        self.palvelinLabel.setGeometry(QRect(80, 40, 100, 20))
        font = QFont()
        font.setPointSize(14)
        self.palvelinLabel.setFont(font)
        self.porttiLabel = QLabel(self.centralwidget)
        self.porttiLabel.setObjectName(u"porttiLabel")
        self.porttiLabel.setGeometry(QRect(80, 90, 100, 20))
        self.porttiLabel.setFont(font)
        self.tietokantaLabel = QLabel(self.centralwidget)
        self.tietokantaLabel.setObjectName(u"tietokantaLabel")
        self.tietokantaLabel.setGeometry(QRect(80, 140, 100, 20))
        self.tietokantaLabel.setFont(font)
        self.kayttajatunnusLabel = QLabel(self.centralwidget)
        self.kayttajatunnusLabel.setObjectName(u"kayttajatunnusLabel")
        self.kayttajatunnusLabel.setGeometry(QRect(80, 190, 140, 20))
        self.kayttajatunnusLabel.setFont(font)
        self.passwordLabel = QLabel(self.centralwidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(80, 240, 100, 20))
        self.passwordLabel.setFont(font)
        self.palvelinLineEdit = QLineEdit(self.centralwidget)
        self.palvelinLineEdit.setObjectName(u"palvelinLineEdit")
        self.palvelinLineEdit.setGeometry(QRect(240, 40, 125, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.palvelinLineEdit.setFont(font1)
        self.porttiLineEdit = QLineEdit(self.centralwidget)
        self.porttiLineEdit.setObjectName(u"porttiLineEdit")
        self.porttiLineEdit.setGeometry(QRect(240, 90, 125, 25))
        self.porttiLineEdit.setFont(font1)
        self.tietokantaLineEdit = QLineEdit(self.centralwidget)
        self.tietokantaLineEdit.setObjectName(u"tietokantaLineEdit")
        self.tietokantaLineEdit.setGeometry(QRect(240, 140, 125, 25))
        self.tietokantaLineEdit.setFont(font1)
        self.KayttajatunnusLineEdit = QLineEdit(self.centralwidget)
        self.KayttajatunnusLineEdit.setObjectName(u"KayttajatunnusLineEdit")
        self.KayttajatunnusLineEdit.setGeometry(QRect(240, 190, 125, 25))
        self.KayttajatunnusLineEdit.setFont(font1)
        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(240, 240, 125, 25))
        self.passwordLineEdit.setFont(font1)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.tallennaPushButton = QPushButton(self.centralwidget)
        self.tallennaPushButton.setObjectName(u"tallennaPushButton")
        self.tallennaPushButton.setGeometry(QRect(260, 290, 90, 25))
        self.tallennaPushButton.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 675, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.palvelinLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
        self.porttiLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
        self.tietokantaLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.kayttajatunnusLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
        self.tallennaPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
    # retranslateUi

