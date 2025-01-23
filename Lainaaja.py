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
        MainWindow.resize(992, 756)
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
        self.palautaPushButton.setGeometry(QRect(460, 100, 100, 30))
        self.palautaPushButton.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 270, 150, 16))
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 270, 150, 25))
        self.label_2.setFont(font)
        self.ajokorttiLineEdit = QLineEdit(self.centralwidget)
        self.ajokorttiLineEdit.setObjectName(u"ajokorttiLineEdit")
        self.ajokorttiLineEdit.setGeometry(QRect(150, 190, 225, 25))
        self.ajokorttiLineEdit.setFont(font)
        self.avainLineEdit = QLineEdit(self.centralwidget)
        self.avainLineEdit.setObjectName(u"avainLineEdit")
        self.avainLineEdit.setGeometry(QRect(460, 190, 225, 25))
        self.avainLineEdit.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 992, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ajokorttiLineEdit.textEdited.connect(self.label.setText)
        self.avainLineEdit.textEdited.connect(self.label_2.setText)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lainaaPushButton.setText(QCoreApplication.translate("MainWindow", u"Lainaa", None))
        self.palautaPushButton.setText(QCoreApplication.translate("MainWindow", u"Palauta", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rekisterinumero", None))
        self.ajokorttiLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue ajokortin viivakoodi", None))
        self.avainLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue avaimen viivakoodi", None))
    # retranslateUi

