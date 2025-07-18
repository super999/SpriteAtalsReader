# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 911)
        self.actionname_fix = QAction(MainWindow)
        self.actionname_fix.setObjectName(u"actionname_fix")
        self.action_about_editor = QAction(MainWindow)
        self.action_about_editor.setObjectName(u"action_about_editor")
        self.action_product_info = QAction(MainWindow)
        self.action_product_info.setObjectName(u"action_product_info")
        self.action_rotate_fix = QAction(MainWindow)
        self.action_rotate_fix.setObjectName(u"action_rotate_fix")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_select_json_dir = QPushButton(self.centralwidget)
        self.pushButton_select_json_dir.setObjectName(u"pushButton_select_json_dir")
        self.pushButton_select_json_dir.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_select_json_dir)

        self.lineEdit_json_dir = QLineEdit(self.centralwidget)
        self.lineEdit_json_dir.setObjectName(u"lineEdit_json_dir")
        self.lineEdit_json_dir.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.lineEdit_json_dir)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_select_dds_file = QPushButton(self.centralwidget)
        self.pushButton_select_dds_file.setObjectName(u"pushButton_select_dds_file")
        self.pushButton_select_dds_file.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.pushButton_select_dds_file)

        self.lineEdit_dds_file = QLineEdit(self.centralwidget)
        self.lineEdit_dds_file.setObjectName(u"lineEdit_dds_file")
        self.lineEdit_dds_file.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_dds_file)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.widget_json_dds = QWidget(self.centralwidget)
        self.widget_json_dds.setObjectName(u"widget_json_dds")
        self.widget_json_dds.setMinimumSize(QSize(0, 200))
        self.verticalLayout_3 = QVBoxLayout(self.widget_json_dds)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.checkBoxUseDDsJson = QCheckBox(self.widget_json_dds)
        self.checkBoxUseDDsJson.setObjectName(u"checkBoxUseDDsJson")

        self.verticalLayout_3.addWidget(self.checkBoxUseDDsJson)

        self.textEdit = QTextEdit(self.widget_json_dds)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.widget_json_dds)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBoxCenterAndResize256 = QCheckBox(self.centralwidget)
        self.checkBoxCenterAndResize256.setObjectName(u"checkBoxCenterAndResize256")
        self.checkBoxCenterAndResize256.setMinimumSize(QSize(0, 30))
        self.checkBoxCenterAndResize256.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBoxCenterAndResize256)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBoxDrawAxis = QCheckBox(self.centralwidget)
        self.checkBoxDrawAxis.setObjectName(u"checkBoxDrawAxis")
        self.checkBoxDrawAxis.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.checkBoxDrawAxis)

        self.checkBoxDrawBorderAndOrigin = QCheckBox(self.centralwidget)
        self.checkBoxDrawBorderAndOrigin.setObjectName(u"checkBoxDrawBorderAndOrigin")
        self.checkBoxDrawBorderAndOrigin.setEnabled(True)
        self.checkBoxDrawBorderAndOrigin.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.checkBoxDrawBorderAndOrigin)

        self.checkBoxDrawShape = QCheckBox(self.centralwidget)
        self.checkBoxDrawShape.setObjectName(u"checkBoxDrawShape")
        self.checkBoxDrawShape.setEnabled(True)
        self.checkBoxDrawShape.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.checkBoxDrawShape)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit_shape_width = QLineEdit(self.centralwidget)
        self.lineEdit_shape_width.setObjectName(u"lineEdit_shape_width")
        self.lineEdit_shape_width.setMinimumSize(QSize(0, 30))
        self.lineEdit_shape_width.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_shape_width.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout_5.addWidget(self.lineEdit_shape_width)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit_shape_height = QLineEdit(self.centralwidget)
        self.lineEdit_shape_height.setObjectName(u"lineEdit_shape_height")
        self.lineEdit_shape_height.setMinimumSize(QSize(0, 30))
        self.lineEdit_shape_height.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_shape_height)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 30))
        self.label_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_7.addWidget(self.label_3)

        self.lineEdit_canvas_width = QLineEdit(self.centralwidget)
        self.lineEdit_canvas_width.setObjectName(u"lineEdit_canvas_width")
        self.lineEdit_canvas_width.setMinimumSize(QSize(0, 30))
        self.lineEdit_canvas_width.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_canvas_width)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 30))
        self.label_4.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_7.addWidget(self.label_4)

        self.lineEdit_canvas_height = QLineEdit(self.centralwidget)
        self.lineEdit_canvas_height.setObjectName(u"lineEdit_canvas_height")
        self.lineEdit_canvas_height.setMinimumSize(QSize(0, 30))
        self.lineEdit_canvas_height.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_canvas_height)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(0, 30))
        self.pushButton_start.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_start)

        self.pushButton_open_output_dir = QPushButton(self.centralwidget)
        self.pushButton_open_output_dir.setObjectName(u"pushButton_open_output_dir")
        self.pushButton_open_output_dir.setMinimumSize(QSize(0, 30))
        self.pushButton_open_output_dir.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_open_output_dir)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 400))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setSpacing(60)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.listWidget_file_list = QListWidget(self.widget_2)
        self.listWidget_file_list.setObjectName(u"listWidget_file_list")

        self.horizontalLayout_8.addWidget(self.listWidget_file_list)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.addFileButton = QPushButton(self.widget_3)
        self.addFileButton.setObjectName(u"addFileButton")
        self.addFileButton.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.addFileButton)

        self.clearFileButton = QPushButton(self.widget_3)
        self.clearFileButton.setObjectName(u"clearFileButton")
        self.clearFileButton.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.clearFileButton)

        self.removeFileButton = QPushButton(self.widget_3)
        self.removeFileButton.setObjectName(u"removeFileButton")
        self.removeFileButton.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.removeFileButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 809, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionname_fix)
        self.menu.addAction(self.action_rotate_fix)
        self.menu_2.addAction(self.action_about_editor)
        self.menu_2.addAction(self.action_product_info)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sprite\u5904\u7406\u7a0b\u5e8f - PySide6\u793a\u4f8b", None))
        self.actionname_fix.setText(QCoreApplication.translate("MainWindow", u"PNG\u6279\u91cf\u91cd\u547d\u540d", None))
        self.action_about_editor.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005\u4fe1\u606f", None))
        self.action_product_info.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\u8bf4\u660e", None))
        self.action_rotate_fix.setText(QCoreApplication.translate("MainWindow", u"PNG\u56fe\u50cf\u65cb\u8f6c\u4fee\u590d", None))
        self.pushButton_select_json_dir.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9Json\u76ee\u5f55", None))
        self.lineEdit_json_dir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165\u6216\u70b9\u51fb\u53f3\u4fa7\u6309\u94ae\u9009\u62e9 Json \u76ee\u5f55", None))
        self.pushButton_select_dds_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9dds\u6587\u4ef6", None))
        self.lineEdit_dds_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165\u6216\u70b9\u51fb\u53f3\u4fa7\u6309\u94ae\u9009\u62e9 dds \u6587\u4ef6", None))
        self.checkBoxUseDDsJson.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528JsonDDS", None))
        self.checkBoxCenterAndResize256.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u5fc3\u5bf9\u9f50\u6269\u5c55", None))
        self.checkBoxDrawAxis.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u5bf9\u9f50\u5750\u6807\u8f74", None))
        self.checkBoxDrawBorderAndOrigin.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u5916\u6846\u548c\u8d77\u59cb\u70b9", None))
        self.checkBoxDrawShape.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u88c1\u526a\u6846(Shape)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"shape\u7684\u5bbd\u5ea6", None))
        self.lineEdit_shape_width.setText(QCoreApplication.translate("MainWindow", u"96", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"shape\u7684\u9ad8\u5ea6", None))
        self.lineEdit_shape_height.setText(QCoreApplication.translate("MainWindow", u"96", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u753b\u677f\u7684\u5bbd\u5ea6\uff1a", None))
        self.lineEdit_canvas_width.setText(QCoreApplication.translate("MainWindow", u"512", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u753b\u677f\u7684\u9ad8\u5ea6\uff1a", None))
        self.lineEdit_canvas_height.setText(QCoreApplication.translate("MainWindow", u"512", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5904\u7406", None))
        self.pushButton_open_output_dir.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u8f93\u51fa\u76ee\u5f55", None))
        self.addFileButton.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
        self.clearFileButton.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.removeFileButton.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

