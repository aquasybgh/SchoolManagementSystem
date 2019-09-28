# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_pg.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_pg(object):
    def setupUi(self, admin_pg):
        admin_pg.setObjectName("admin_pg")
        admin_pg.resize(852, 570)
        admin_pg.setAutoFillBackground(False)
        admin_pg.setStyleSheet("QMainWindow \n"
"{ \n"
"  background-image: url(/home/aquasybgh/Desktop/SMS/Images/Ghana+Girl+Students1IMG_5804.jpg);\n"
"opacity: 0.5\n"
"\n"
" }\n"
"")
        self.centralwidget = QtWidgets.QWidget(admin_pg)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_sel = QtWidgets.QFrame(self.centralwidget)
        self.frame_sel.setGeometry(QtCore.QRect(9, 9, 181, 552))
        self.frame_sel.setAutoFillBackground(False)
        self.frame_sel.setStyleSheet("QWidget\n"
"{\n"
"   background-color:  rgba(85, 87, 83,0.5);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color:  rgb(238, 238, 236); ;\n"
"     border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"QLabel\n"
"{\n"
"background-color: rgba(238, 238, 236,0);\n"
"color:white;\n"
"\n"
"}")
        self.frame_sel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sel.setObjectName("frame_sel")
        self.label = QtWidgets.QLabel(self.frame_sel)
        self.label.setGeometry(QtCore.QRect(0, 10, 181, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_sel)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 151, 91))
        self.label_2.setObjectName("label_2")
        self.user_right_lbl = QtWidgets.QLabel(self.frame_sel)
        self.user_right_lbl.setGeometry(QtCore.QRect(10, 140, 41, 18))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        font.setItalic(True)
        self.user_right_lbl.setFont(font)
        self.user_right_lbl.setObjectName("user_right_lbl")
        self.username_lbl = QtWidgets.QLabel(self.frame_sel)
        self.username_lbl.setGeometry(QtCore.QRect(10, 160, 161, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.username_lbl.setFont(font)
        self.username_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.username_lbl.setObjectName("username_lbl")
        self.pushButton = QtWidgets.QPushButton(self.frame_sel)
        self.pushButton.setGeometry(QtCore.QRect(0, 210, 181, 26))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_sel)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 260, 181, 26))
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_sel)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 310, 181, 26))
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_sel)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 360, 181, 26))
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_sel)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 410, 181, 26))
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_sel)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 510, 81, 26))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_sel)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 460, 181, 26))
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_stbar = QtWidgets.QFrame(self.centralwidget)
        self.frame_stbar.setGeometry(QtCore.QRect(202, 541, 641, 20))
        self.frame_stbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_stbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_stbar.setObjectName("frame_stbar")
        self.label_5 = QtWidgets.QLabel(self.frame_stbar)
        self.label_5.setGeometry(QtCore.QRect(11, 3, 74, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_stbar)
        self.label_6.setGeometry(QtCore.QRect(460, 0, 74, 18))
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.frame_stbar)
        self.line.setGeometry(QtCore.QRect(250, 0, 51, 20))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 10, 341, 421))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, -23, 74, 61))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        admin_pg.setCentralWidget(self.centralwidget)

        self.retranslateUi(admin_pg)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(admin_pg)

    def retranslateUi(self, admin_pg):
        _translate = QtCore.QCoreApplication.translate
        admin_pg.setWindowTitle(_translate("admin_pg", "ADMIN "))
        self.label.setText(_translate("admin_pg", "SCHOOL NAME"))
        self.label_2.setText(_translate("admin_pg", "LOGO HERE"))
        self.user_right_lbl.setText(_translate("admin_pg", "ADMIN"))
        self.username_lbl.setText(_translate("admin_pg", "USERNAME"))
        self.pushButton.setText(_translate("admin_pg", "Student Registration"))
        self.pushButton_2.setText(_translate("admin_pg", "Staff Registration"))
        self.pushButton_3.setText(_translate("admin_pg", "Academics"))
        self.pushButton_4.setText(_translate("admin_pg", "Administrative"))
        self.pushButton_5.setText(_translate("admin_pg", "Data Overview"))
        self.pushButton_6.setText(_translate("admin_pg", "LOG OUT"))
        self.pushButton_7.setText(_translate("admin_pg", "Fees Management"))
        self.label_5.setText(_translate("admin_pg", "TextLabel"))
        self.label_6.setText(_translate("admin_pg", "TextLabel"))
        self.label_3.setText(_translate("admin_pg", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_pg = QtWidgets.QMainWindow()
    ui = Ui_admin_pg()
    ui.setupUi(admin_pg)
    admin_pg.show()
    sys.exit(app.exec_())
