# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(670, 478)
        self.tietokantaLineEdit = QLineEdit(Dialog)
        self.tietokantaLineEdit.setObjectName(u"tietokantaLineEdit")
        self.tietokantaLineEdit.setGeometry(QRect(330, 210, 125, 25))
        font = QFont()
        font.setPointSize(12)
        self.tietokantaLineEdit.setFont(font)
        self.passwordLineEdit = QLineEdit(Dialog)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(330, 310, 125, 25))
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.porttiLabel = QLabel(Dialog)
        self.porttiLabel.setObjectName(u"porttiLabel")
        self.porttiLabel.setGeometry(QRect(170, 160, 100, 20))
        font1 = QFont()
        font1.setPointSize(14)
        self.porttiLabel.setFont(font1)
        self.tietokantaLabel = QLabel(Dialog)
        self.tietokantaLabel.setObjectName(u"tietokantaLabel")
        self.tietokantaLabel.setGeometry(QRect(170, 210, 100, 20))
        self.tietokantaLabel.setFont(font1)
        self.porttiLineEdit = QLineEdit(Dialog)
        self.porttiLineEdit.setObjectName(u"porttiLineEdit")
        self.porttiLineEdit.setGeometry(QRect(330, 160, 125, 25))
        self.porttiLineEdit.setFont(font)
        self.kayttajatunnusLabel = QLabel(Dialog)
        self.kayttajatunnusLabel.setObjectName(u"kayttajatunnusLabel")
        self.kayttajatunnusLabel.setGeometry(QRect(170, 260, 140, 20))
        self.kayttajatunnusLabel.setFont(font1)
        self.palvelinLineEdit = QLineEdit(Dialog)
        self.palvelinLineEdit.setObjectName(u"palvelinLineEdit")
        self.palvelinLineEdit.setGeometry(QRect(330, 110, 125, 25))
        self.palvelinLineEdit.setFont(font)
        self.tallennaPushButton = QPushButton(Dialog)
        self.tallennaPushButton.setObjectName(u"tallennaPushButton")
        self.tallennaPushButton.setGeometry(QRect(350, 360, 90, 25))
        self.tallennaPushButton.setFont(font1)
        self.KayttajatunnusLineEdit = QLineEdit(Dialog)
        self.KayttajatunnusLineEdit.setObjectName(u"KayttajatunnusLineEdit")
        self.KayttajatunnusLineEdit.setGeometry(QRect(330, 260, 125, 25))
        self.KayttajatunnusLineEdit.setFont(font)
        self.palvelinLabel = QLabel(Dialog)
        self.palvelinLabel.setObjectName(u"palvelinLabel")
        self.palvelinLabel.setGeometry(QRect(170, 110, 100, 20))
        self.palvelinLabel.setFont(font1)
        self.passwordLabel = QLabel(Dialog)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(170, 310, 100, 20))
        self.passwordLabel.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.porttiLabel.setText(QCoreApplication.translate("Dialog", u"Portti", None))
        self.tietokantaLabel.setText(QCoreApplication.translate("Dialog", u"Tietokanta", None))
        self.kayttajatunnusLabel.setText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.tallennaPushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
        self.palvelinLabel.setText(QCoreApplication.translate("Dialog", u"Palvelin", None))
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Salasana", None))
    # retranslateUi

