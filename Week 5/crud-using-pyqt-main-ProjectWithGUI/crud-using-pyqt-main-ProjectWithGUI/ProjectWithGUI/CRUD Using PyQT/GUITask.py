# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUITask.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1198, 957)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #F6F6F6;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -869, 1153, 1812))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(600, 1790))
        self.scrollArea_2.setMouseTracking(True)
        self.scrollArea_2.setTabletTracking(True)
        self.scrollArea_2.setAcceptDrops(True)
        self.scrollArea_2.setStyleSheet("background-color:#F6F6F6;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1129, 1788))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 1121, 141))
        self.label_4.setStyleSheet("background-image: url(:/logos/estamping.png);\n"
"border-radius : 8px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setGeometry(QtCore.QRect(180, 150, 701, 131))
        self.label_23.setStyleSheet("background-image: url(:/challan/Screenshot 2022-10-07 011803ss.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.prove = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.prove.setGeometry(QtCore.QRect(170, 1100, 721, 173))
        self.prove.setStyleSheet("background-color:white;\n"
"")
        self.prove.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.prove.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prove.setObjectName("prove")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.prove)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label3 = QtWidgets.QFrame(self.prove)
        self.label3.setStyleSheet("background-color:#EEEEEE;")
        self.label3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label3.setObjectName("label3")
        self.frame_5 = QtWidgets.QFrame(self.label3)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 291, 58))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 71, 51))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/think/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.label3)
        self.instruction3 = QtWidgets.QFrame(self.prove)
        self.instruction3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.instruction3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.instruction3.setObjectName("instruction3")
        self.label_3 = QtWidgets.QLabel(self.instruction3)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.instruction3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_4.setGeometry(QtCore.QRect(170, 300, 721, 261))
        self.groupBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.cmbDistrict_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.cmbDistrict_4.setEnabled(True)
        self.cmbDistrict_4.setGeometry(QtCore.QRect(30, 100, 271, 31))
        self.cmbDistrict_4.setStyleSheet("#cmbDistrict{\n"
"border: 1px solid #white;\n"
"border-raduis : 4px;\n"
"padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.cmbDistrict_4.setObjectName("cmbDistrict_4")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.cmbDistrict_4.addItem("")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(370, 220, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(370, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStrikeOut(False)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(370, 160, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(30, 160, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(660, 120, 41, 31))
        self.label_28.setStyleSheet("background-image: url(:/newPrefix/book.png);")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.cmbTehsil_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.cmbTehsil_4.setGeometry(QtCore.QRect(370, 100, 271, 31))
        self.cmbTehsil_4.setStyleSheet("#cmbTehsil{\n"
"border: 1px solid #white  ;\n"
"border-raduis : 4px;\n"
"padding-left : 10px\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.cmbTehsil_4.setObjectName("cmbTehsil_4")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbTehsil_4.addItem("")
        self.cmbStampPaperType_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.cmbStampPaperType_4.setGeometry(QtCore.QRect(30, 180, 271, 31))
        self.cmbStampPaperType_4.setStyleSheet("#cmbStampPaperType{\n"
"border: 1px solid #black  ;\n"
"border-raduis : 4px;\n"
"padding-left : 10px\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.cmbStampPaperType_4.setObjectName("cmbStampPaperType_4")
        self.cmbStampPaperType_4.addItem("")
        self.cmbStampPaperType_4.addItem("")
        self.cmbDeed_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.cmbDeed_4.setGeometry(QtCore.QRect(370, 180, 271, 31))
        self.cmbDeed_4.setStyleSheet("#cmbDeed{\n"
"border: 1px solid #white  ;\n"
"border-raduis : 4px;\n"
"padding-left : 10px\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.cmbDeed_4.setObjectName("cmbDeed_4")
        self.cmbDeed_4.addItem("")
        self.cmbDeed_4.addItem("")
        self.gvAgentInfo_4 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.gvAgentInfo_4.setGeometry(QtCore.QRect(0, 0, 731, 51))
        self.gvAgentInfo_4.setStyleSheet("background-image: url(:/challan/challan.png);")
        self.gvAgentInfo_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gvAgentInfo_4.setObjectName("gvAgentInfo_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setGeometry(QtCore.QRect(170, 580, 721, 191))
        self.groupBox_3.setAcceptDrops(False)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 140, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lblAgentCNIC_3 = QtWidgets.QLabel(self.groupBox_3)
        self.lblAgentCNIC_3.setGeometry(QtCore.QRect(330, 119, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAgentCNIC_3.setFont(font)
        self.lblAgentCNIC_3.setObjectName("lblAgentCNIC_3")
        self.lblAgentName_3 = QtWidgets.QLabel(self.groupBox_3)
        self.lblAgentName_3.setGeometry(QtCore.QRect(48, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAgentName_3.setFont(font)
        self.lblAgentName_3.setObjectName("lblAgentName_3")
        self.lblAgentName_4 = QtWidgets.QLabel(self.groupBox_3)
        self.lblAgentName_4.setGeometry(QtCore.QRect(47, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAgentName_4.setFont(font)
        self.lblAgentName_4.setObjectName("lblAgentName_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 90, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lblAgentCNIC_4 = QtWidgets.QLabel(self.groupBox_3)
        self.lblAgentCNIC_4.setGeometry(QtCore.QRect(330, 73, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAgentCNIC_4.setFont(font)
        self.lblAgentCNIC_4.setAutoFillBackground(False)
        self.lblAgentCNIC_4.setObjectName("lblAgentCNIC_4")
        self.LEAgentName_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.LEAgentName_3.setGeometry(QtCore.QRect(47, 90, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LEAgentName_3.setFont(font)
        self.LEAgentName_3.setClearButtonEnabled(True)
        self.LEAgentName_3.setObjectName("LEAgentName_3")
        self.LEAgentName_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.LEAgentName_4.setGeometry(QtCore.QRect(50, 140, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LEAgentName_4.setFont(font)
        self.LEAgentName_4.setClearButtonEnabled(True)
        self.LEAgentName_4.setObjectName("LEAgentName_4")
        self.gvAgentInfo_3 = QtWidgets.QGraphicsView(self.groupBox_3)
        self.gvAgentInfo_3.setGeometry(QtCore.QRect(0, 0, 731, 51))
        self.gvAgentInfo_3.setStyleSheet("background-image: url(:/logos/agent.png);")
        self.gvAgentInfo_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gvAgentInfo_3.setObjectName("gvAgentInfo_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_5.setGeometry(QtCore.QRect(170, 790, 721, 141))
        self.groupBox_5.setAcceptDrops(False)
        self.groupBox_5.setAutoFillBackground(False)
        self.groupBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gvAgentInfo_6 = QtWidgets.QGraphicsView(self.groupBox_5)
        self.gvAgentInfo_6.setGeometry(QtCore.QRect(0, 0, 721, 51))
        self.gvAgentInfo_6.setStyleSheet("background-image: url(:/logos/Screenshot 2022-10-07 150139.png);")
        self.gvAgentInfo_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gvAgentInfo_6.setObjectName("gvAgentInfo_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(500, 10, 191, 38))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("color:green;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plus/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(40, 80, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_6.setGeometry(QtCore.QRect(170, 950, 721, 131))
        self.groupBox_6.setAcceptDrops(False)
        self.groupBox_6.setAutoFillBackground(False)
        self.groupBox_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gvAgentInfo_7 = QtWidgets.QGraphicsView(self.groupBox_6)
        self.gvAgentInfo_7.setGeometry(QtCore.QRect(0, 0, 721, 51))
        self.gvAgentInfo_7.setStyleSheet("background-image: url(:/logos/secondParty.png);")
        self.gvAgentInfo_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gvAgentInfo_7.setObjectName("gvAgentInfo_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setGeometry(QtCore.QRect(500, 10, 191, 38))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color:green;")
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnReset = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btnReset.setGeometry(QtCore.QRect(690, 1330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnReset.setFont(font)
        self.btnReset.setStyleSheet("#btnReset{\n"
"background-color:rgb(71, 181, 148)\n"
"}")
        self.btnReset.setObjectName("btnReset")
        self.btnNext = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btnNext.setGeometry(QtCore.QRect(800, 1330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnNext.setFont(font)
        self.btnNext.setStyleSheet("#btnNext{\n"
"    color: white;\n"
"background-color: rgb(80, 212, 129);\n"
"}")
        self.btnNext.setObjectName("btnNext")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setGeometry(QtCore.QRect(-10, 1370, 1141, 451))
        self.label_5.setStyleSheet("background-image: url(:/footer/footer.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_23.raise_()
        self.prove.raise_()
        self.label_4.raise_()
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox_5.raise_()
        self.groupBox_6.raise_()
        self.btnReset.raise_()
        self.btnNext.raise_()
        self.label_5.raise_()
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.addWidget(self.scrollArea_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Retype the code from the picture:"))
        self.cmbDistrict_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.cmbDistrict_4.setItemText(0, _translate("MainWindow", "Select District"))
        self.cmbDistrict_4.setItemText(1, _translate("MainWindow", "Attock"))
        self.cmbDistrict_4.setItemText(2, _translate("MainWindow", "Bawalnagar"))
        self.cmbDistrict_4.setItemText(3, _translate("MainWindow", "Bahawalpur"))
        self.cmbDistrict_4.setItemText(4, _translate("MainWindow", "Bakhar"))
        self.cmbDistrict_4.setItemText(5, _translate("MainWindow", "Chakwal"))
        self.cmbDistrict_4.setItemText(6, _translate("MainWindow", "Cheniot"))
        self.cmbDistrict_4.setItemText(7, _translate("MainWindow", "Faisalabad"))
        self.cmbDistrict_4.setItemText(8, _translate("MainWindow", "Lahore"))
        self.cmbDistrict_4.setItemText(9, _translate("MainWindow", "Lodhran"))
        self.cmbDistrict_4.setItemText(10, _translate("MainWindow", "Mianwali"))
        self.cmbDistrict_4.setItemText(11, _translate("MainWindow", "Multan"))
        self.cmbDistrict_4.setItemText(12, _translate("MainWindow", "Sargodha"))
        self.label_13.setText(_translate("MainWindow", "For Sale Deed please use Conveyance"))
        self.label_25.setText(_translate("MainWindow", "Tehsil"))
        self.label_10.setText(_translate("MainWindow", "District"))
        self.label_26.setText(_translate("MainWindow", "Deed Name"))
        self.label_27.setText(_translate("MainWindow", "Stamp Paper Type"))
        self.cmbTehsil_4.setItemText(0, _translate("MainWindow", "Select Tehsil"))
        self.cmbTehsil_4.setItemText(1, _translate("MainWindow", "Bahawalnagar Tehsil"))
        self.cmbTehsil_4.setItemText(2, _translate("MainWindow", "Chishtian Tehsil"))
        self.cmbTehsil_4.setItemText(3, _translate("MainWindow", "Ahmadpur East Tehsil"))
        self.cmbTehsil_4.setItemText(4, _translate("MainWindow", "Khairpur Tamewali Tehsil"))
        self.cmbTehsil_4.setItemText(5, _translate("MainWindow", "Khanpur Tehsil"))
        self.cmbTehsil_4.setItemText(6, _translate("MainWindow", "Alipur Tehsil"))
        self.cmbTehsil_4.setItemText(7, _translate("MainWindow", "Jampur Tehsil"))
        self.cmbTehsil_4.setItemText(8, _translate("MainWindow", "Faisalabad City Tehsil"))
        self.cmbTehsil_4.setItemText(9, _translate("MainWindow", "Kamalia Tehsil"))
        self.cmbTehsil_4.setItemText(10, _translate("MainWindow", "Rawalpindi Tehsil"))
        self.cmbTehsil_4.setItemText(11, _translate("MainWindow", "Sillanwali Tehsil"))
        self.cmbTehsil_4.setItemText(12, _translate("MainWindow", "Isakhel Tehsil"))
        self.cmbTehsil_4.setItemText(13, _translate("MainWindow", "Mianwali Tehsil"))
        self.cmbStampPaperType_4.setItemText(0, _translate("MainWindow", "Judicial"))
        self.cmbStampPaperType_4.setItemText(1, _translate("MainWindow", "Non-Judicial"))
        self.cmbDeed_4.setItemText(0, _translate("MainWindow", "Court Fee"))
        self.cmbDeed_4.setItemText(1, _translate("MainWindow", "Contract Fee"))
        self.lblAgentCNIC_3.setText(_translate("MainWindow", "Agent Email"))
        self.lblAgentName_3.setText(_translate("MainWindow", "Agent Contact"))
        self.lblAgentName_4.setText(_translate("MainWindow", "Agent Name"))
        self.lblAgentCNIC_4.setText(_translate("MainWindow", "Agent CNIC"))
        self.pushButton_10.setText(_translate("MainWindow", "Add First Party"))
        self.label.setText(_translate("MainWindow", "Please add at least one First Party"))
        self.pushButton_11.setText(_translate("MainWindow", "Add Second Party"))
        self.label_2.setText(_translate("MainWindow", "Please add at least one Second Party"))
        self.btnReset.setText(_translate("MainWindow", "RESET"))
        self.btnNext.setText(_translate("MainWindow", "NEXT"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())