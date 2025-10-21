# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sora_API.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Sora2_API(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 300)
        Form.setMinimumSize(QSize(600, 400))
        Form.setMaximumSize(QSize(1920, 1080))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.Image_Adress = QLineEdit(Form)
        self.Image_Adress.setObjectName(u"Image_Adress")
        self.Image_Adress.setFont(font)

        self.horizontalLayout_3.addWidget(self.Image_Adress)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 56))
        self.label_2.setMaximumSize(QSize(16777215, 500))
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.Prompt_Text = QTextEdit(Form)
        self.Prompt_Text.setObjectName(u"Prompt_Text")
        self.Prompt_Text.setMinimumSize(QSize(0, 100))
        self.Prompt_Text.setMaximumSize(QSize(16777215, 1500))
        font1 = QFont()
        font1.setPointSize(15)
        self.Prompt_Text.setFont(font1)

        self.horizontalLayout_2.addWidget(self.Prompt_Text)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.Submit_Button = QPushButton(Form)
        self.Submit_Button.setObjectName(u"Submit_Button")
        self.Submit_Button.setMinimumSize(QSize(0, 24))

        self.verticalLayout.addWidget(self.Submit_Button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 56))
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.Out_Put = QLineEdit(Form)
        self.Out_Put.setObjectName(u"Out_Put")
        self.Out_Put.setFont(font)
        self.Out_Put.setReadOnly(True)

        self.horizontalLayout.addWidget(self.Out_Put)

        self.Download_Button = QPushButton(Form)
        self.Download_Button.setObjectName(u"Download_Button")

        self.horizontalLayout.addWidget(self.Download_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Sora2_API", u"Form", None))
        self.label.setText(QCoreApplication.translate("Sora2_API", u"\u56fe\u7247\u5730\u5740\uff1a", None))
        self.Image_Adress.setPlaceholderText(QCoreApplication.translate("Sora2_API", u"\u8bf7\u8f93\u5165\u56fe\u7247\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("Sora2_API", u"\u751f\u6210\u8981\u6c42\uff1a", None))
        self.Prompt_Text.setPlaceholderText(QCoreApplication.translate("Sora2_API", u"\u8bf7\u8f93\u5165\u4f60\u7684\u751f\u6210\u8981\u6c42", None))
        self.Submit_Button.setText(QCoreApplication.translate("Sora2_API", u"\u63d0\u4ea4", None))
        self.label_3.setText(QCoreApplication.translate("Sora2_API", u"\u751f\u6210\u7ed3\u679c\uff1a", None))
        self.Out_Put.setPlaceholderText(QCoreApplication.translate("Sora2_API", u"\u751f\u6210\u6210\u529f\u8fd4\u56deurl\uff0c\u5931\u8d25\u5219\u8fd4\u56de\u9519\u8bef\u4fe1\u606f", None))
        self.Download_Button.setText(QCoreApplication.translate("Sora2_API", u"\u4e0b\u8f7d\u89c6\u9891", None))
    # retranslateUi

