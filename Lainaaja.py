# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lainaaja.ui'
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
        MainWindow.resize(990, 756)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lainaaPushButton = QPushButton(self.centralwidget)
        self.lainaaPushButton.setObjectName(u"lainaaPushButton")
        self.lainaaPushButton.setGeometry(QRect(150, 90, 100, 30))
        font = QFont()
        font.setPointSize(14)
        self.lainaaPushButton.setFont(font)
        self.palautaPushButton = QPushButton(self.centralwidget)
        self.palautaPushButton.setObjectName(u"palautaPushButton")
        self.palautaPushButton.setGeometry(QRect(460, 90, 100, 30))
        self.palautaPushButton.setFont(font)
        self.hetuLabel = QLabel(self.centralwidget)
        self.hetuLabel.setObjectName(u"hetuLabel")
        self.hetuLabel.setGeometry(QRect(150, 290, 150, 25))
        self.hetuLabel.setFont(font)
        self.rekisteriNrLabel = QLabel(self.centralwidget)
        self.rekisteriNrLabel.setObjectName(u"rekisteriNrLabel")
        self.rekisteriNrLabel.setGeometry(QRect(470, 290, 150, 25))
        self.rekisteriNrLabel.setFont(font)
        self.ajokorttiLineEdit = QLineEdit(self.centralwidget)
        self.ajokorttiLineEdit.setObjectName(u"ajokorttiLineEdit")
        self.ajokorttiLineEdit.setGeometry(QRect(150, 190, 225, 25))
        self.ajokorttiLineEdit.setFont(font)
        self.avainLineEdit = QLineEdit(self.centralwidget)
        self.avainLineEdit.setObjectName(u"avainLineEdit")
        self.avainLineEdit.setGeometry(QRect(460, 190, 225, 25))
        self.avainLineEdit.setFont(font)
        self.tilaLabel = QLabel(self.centralwidget)
        self.tilaLabel.setObjectName(u"tilaLabel")
        self.tilaLabel.setGeometry(QRect(290, 20, 175, 25))
        self.tilaLabel.setFont(font)
        self.naytaTiedotPushButton = QPushButton(self.centralwidget)
        self.naytaTiedotPushButton.setObjectName(u"naytaTiedotPushButton")
        self.naytaTiedotPushButton.setGeometry(QRect(290, 90, 125, 30))
        self.naytaTiedotPushButton.setFont(font)
        self.okPushButton = QPushButton(self.centralwidget)
        self.okPushButton.setObjectName(u"okPushButton")
        self.okPushButton.setGeometry(QRect(320, 250, 75, 30))
        self.okPushButton.setFont(font)
        self.alkuunPushButton = QPushButton(self.centralwidget)
        self.alkuunPushButton.setObjectName(u"alkuunPushButton")
        self.alkuunPushButton.setGeometry(QRect(150, 400, 125, 30))
        self.alkuunPushButton.setFont(font)
        self.alkuLabel = QLabel(self.centralwidget)
        self.alkuLabel.setObjectName(u"alkuLabel")
        self.alkuLabel.setGeometry(QRect(150, 340, 225, 25))
        self.alkuLabel.setFont(font)
        self.paattyminenLabel = QLabel(self.centralwidget)
        self.paattyminenLabel.setObjectName(u"paattyminenLabel")
        self.paattyminenLabel.setGeometry(QRect(470, 340, 225, 25))
        self.paattyminenLabel.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 990, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ajokorttiLineEdit.textEdited.connect(self.hetuLabel.setText)
        self.avainLineEdit.textEdited.connect(self.rekisteriNrLabel.setText)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lainaaPushButton.setText(QCoreApplication.translate("MainWindow", u"Lainaa", None))
        self.palautaPushButton.setText(QCoreApplication.translate("MainWindow", u"Palauta", None))
        self.hetuLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.rekisteriNrLabel.setText(QCoreApplication.translate("MainWindow", u"Rekisterinumero", None))
        self.ajokorttiLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue ajokortin viivakoodi", None))
        self.avainLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue avaimen viivakoodi", None))
        self.tilaLabel.setText(QCoreApplication.translate("MainWindow", u"Tila", None))
        self.naytaTiedotPushButton.setText(QCoreApplication.translate("MainWindow", u"N\u00e4yt\u00e4 tiedot", None))
        self.okPushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.alkuunPushButton.setText(QCoreApplication.translate("MainWindow", u"Palaa Alkuun", None))
        self.alkuLabel.setText(QCoreApplication.translate("MainWindow", u"Lainauksen alku", None))
        self.paattyminenLabel.setText(QCoreApplication.translate("MainWindow", u"Lainauksen p\u00e4\u00e4ttyminen", None))
    # retranslateUi

