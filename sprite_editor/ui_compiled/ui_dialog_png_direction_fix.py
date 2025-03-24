# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_png_direction_fix.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DialogPngDirectionFix(object):
    def setupUi(self, DialogPngDirectionFix):
        if not DialogPngDirectionFix.objectName():
            DialogPngDirectionFix.setObjectName(u"DialogPngDirectionFix")
        DialogPngDirectionFix.resize(951, 187)
        self.horizontalLayout = QHBoxLayout(DialogPngDirectionFix)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(DialogPngDirectionFix)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_select_png_dir = QPushButton(self.widget_2)
        self.pushButton_select_png_dir.setObjectName(u"pushButton_select_png_dir")
        self.pushButton_select_png_dir.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_select_png_dir)

        self.lineEdit_json_dir = QLineEdit(self.widget_2)
        self.lineEdit_json_dir.setObjectName(u"lineEdit_json_dir")
        self.lineEdit_json_dir.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.lineEdit_json_dir)

        self.pushButton_open_dir = QPushButton(self.widget_2)
        self.pushButton_open_dir.setObjectName(u"pushButton_open_dir")
        self.pushButton_open_dir.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_open_dir)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox_flip_left_right = QRadioButton(self.widget_5)
        self.checkBox_flip_left_right.setObjectName(u"checkBox_flip_left_right")

        self.horizontalLayout_4.addWidget(self.checkBox_flip_left_right)

        self.checkBox_flip_top_down = QRadioButton(self.widget_5)
        self.checkBox_flip_top_down.setObjectName(u"checkBox_flip_top_down")
        self.checkBox_flip_top_down.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_flip_top_down)

        self.checkBox_rotate_90 = QRadioButton(self.widget_5)
        self.checkBox_rotate_90.setObjectName(u"checkBox_rotate_90")

        self.horizontalLayout_4.addWidget(self.checkBox_rotate_90)

        self.checkBox_rotate_180 = QRadioButton(self.widget_5)
        self.checkBox_rotate_180.setObjectName(u"checkBox_rotate_180")

        self.horizontalLayout_4.addWidget(self.checkBox_rotate_180)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_start = QPushButton(self.widget_4)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(120, 30))
        self.pushButton_start.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_start)

        self.pushButton_save_settings = QPushButton(self.widget_4)
        self.pushButton_save_settings.setObjectName(u"pushButton_save_settings")
        self.pushButton_save_settings.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_save_settings)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(DialogPngDirectionFix)

        QMetaObject.connectSlotsByName(DialogPngDirectionFix)
    # setupUi

    def retranslateUi(self, DialogPngDirectionFix):
        DialogPngDirectionFix.setWindowTitle(QCoreApplication.translate("DialogPngDirectionFix", u"Png\u56fe\u7247\u7ffb\u8f6c\u4fee\u590d", None))
        self.pushButton_select_png_dir.setText(QCoreApplication.translate("DialogPngDirectionFix", u"\u9009\u62e9PNG\u76ee\u5f55", None))
        self.lineEdit_json_dir.setPlaceholderText(QCoreApplication.translate("DialogPngDirectionFix", u"\u5728\u6b64\u5904\u8f93\u5165\u6216\u70b9\u51fb\u53f3\u4fa7\u6309\u94ae\u9009\u62e9 Json \u76ee\u5f55", None))
        self.pushButton_open_dir.setText(QCoreApplication.translate("DialogPngDirectionFix", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.checkBox_flip_left_right.setText(QCoreApplication.translate("DialogPngDirectionFix", u"\u5de6\u53f3\u7ffb\u8f6c", None))
        self.checkBox_flip_top_down.setText(QCoreApplication.translate("DialogPngDirectionFix", u"\u4e0a\u4e0b\u7ffb\u8f6c", None))
        self.checkBox_rotate_90.setText(QCoreApplication.translate("DialogPngDirectionFix", u"90\u5ea6", None))
        self.checkBox_rotate_180.setText(QCoreApplication.translate("DialogPngDirectionFix", u"180\u5ea6", None))
        self.pushButton_start.setText(QCoreApplication.translate("DialogPngDirectionFix", u"\u5f00\u59cb\u5904\u7406", None))
        self.pushButton_save_settings.setText(QCoreApplication.translate("DialogPngDirectionFix", u"\u4fdd\u5b58\u8bbe\u7f6e", None))
    # retranslateUi

