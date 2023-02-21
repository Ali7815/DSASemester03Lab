# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Part01.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 1078)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 560, 681, 191))
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(313, 140, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lblAgentCNIC_2 = QtWidgets.QLabel(self.groupBox)
        self.lblAgentCNIC_2.setGeometry(QtCore.QRect(313, 119, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAgentCNIC_2.setFont(font)
        self.lblAgentCNIC_2.setObjectName("lblAgentCNIC_2")
        self.lblAgentName_2 = QtWidgets.QLabel(self.groupBox)
        self.lblAgentName_2.setGeometry(QtCore.QRect(31, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAgentName_2.setFont(font)
        self.lblAgentName_2.setObjectName("lblAgentName_2")
        self.lblAgentName = QtWidgets.QLabel(self.groupBox)
        self.lblAgentName.setGeometry(QtCore.QRect(30, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAgentName.setFont(font)
        self.lblAgentName.setObjectName("lblAgentName")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(313, 90, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lblAgentCNIC = QtWidgets.QLabel(self.groupBox)
        self.lblAgentCNIC.setGeometry(QtCore.QRect(313, 73, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblAgentCNIC.setFont(font)
        self.lblAgentCNIC.setAutoFillBackground(False)
        self.lblAgentCNIC.setObjectName("lblAgentCNIC")
        self.LEAgentName = QtWidgets.QLineEdit(self.groupBox)
        self.LEAgentName.setGeometry(QtCore.QRect(30, 90, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LEAgentName.setFont(font)
        self.LEAgentName.setClearButtonEnabled(True)
        self.LEAgentName.setObjectName("LEAgentName")
        self.LEAgentName_2 = QtWidgets.QLineEdit(self.groupBox)
        self.LEAgentName_2.setGeometry(QtCore.QRect(33, 140, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LEAgentName_2.setFont(font)
        self.LEAgentName_2.setClearButtonEnabled(True)
        self.LEAgentName_2.setObjectName("LEAgentName_2")
        self.gvAgentInfo = QtWidgets.QGraphicsView(self.groupBox)
        self.gvAgentInfo.setGeometry(QtCore.QRect(10, 10, 661, 51))
        self.gvAgentInfo.setStyleSheet("background-image: url(:/logos/agent.png);")
        self.gvAgentInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gvAgentInfo.setObjectName("gvAgentInfo")
        self.party1 = QtWidgets.QFrame(self.centralwidget)
        self.party1.setGeometry(QtCore.QRect(43, 761, 681, 173))
        self.party1.setStyleSheet("background-color:white;")
        self.party1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.party1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.party1.setObjectName("party1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.party1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label1 = QtWidgets.QFrame(self.party1)
        self.label1.setStyleSheet("background-color:#EEEEEE;")
        self.label1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label1.setObjectName("label1")
        self.frame = QtWidgets.QFrame(self.label1)
        self.frame.setGeometry(QtCore.QRect(10, 10, 291, 58))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color:black;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/users.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.label1)
        self.frame_2.setGeometry(QtCore.QRect(385, 10, 261, 58))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 180, 38))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:green;\n"
"image: url(:/plus/images.png);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plus/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.label1)
        self.instruction1 = QtWidgets.QFrame(self.party1)
        self.instruction1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.instruction1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.instruction1.setObjectName("instruction1")
        self.label = QtWidgets.QLabel(self.instruction1)
        self.label.setGeometry(QtCore.QRect(10, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.instruction1)
        self.prove = QtWidgets.QFrame(self.centralwidget)
        self.prove.setGeometry(QtCore.QRect(41, 1118, 681, 173))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/think/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
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
        self.party2 = QtWidgets.QFrame(self.centralwidget)
        self.party2.setGeometry(QtCore.QRect(42, 940, 681, 172))
        self.party2.setStyleSheet("background-color:white;\n"
"")
        self.party2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.party2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.party2.setObjectName("party2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.party2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label2 = QtWidgets.QFrame(self.party2)
        self.label2.setStyleSheet("\n"
"background-color:#EEEEEE;")
        self.label2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label2.setObjectName("label2")
        self.frame_3 = QtWidgets.QFrame(self.label2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 291, 58))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.SecondParty = QtWidgets.QPushButton(self.frame_3)
        self.SecondParty.setEnabled(False)
        self.SecondParty.setGeometry(QtCore.QRect(-10, 0, 221, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SecondParty.setFont(font)
        self.SecondParty.setAutoFillBackground(False)
        self.SecondParty.setStyleSheet("color:black;")
        self.SecondParty.setIcon(icon)
        self.SecondParty.setIconSize(QtCore.QSize(50, 50))
        self.SecondParty.setFlat(True)
        self.SecondParty.setObjectName("SecondParty")
        self.frame_4 = QtWidgets.QFrame(self.label2)
        self.frame_4.setGeometry(QtCore.QRect(250, 10, 391, 58))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(176, 10, 191, 38))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color:green;")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.label2)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(730, 290, 20, 1001))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setInvertedControls(True)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(39, 1310, 681, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 290, 680, 261))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.cmbDistrict_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbDistrict_3.setEnabled(True)
        self.cmbDistrict_3.setGeometry(QtCore.QRect(30, 100, 271, 31))
        self.cmbDistrict_3.setStyleSheet("#cmbDistrict{\n"
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
        self.cmbDistrict_3.setObjectName("cmbDistrict_3")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.cmbDistrict_3.addItem("")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(370, 220, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(370, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStrikeOut(False)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(370, 160, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(30, 160, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(660, 120, 41, 31))
        self.label_22.setStyleSheet("background-image: url(:/newPrefix/book.png);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.cmbTehsil_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbTehsil_3.setGeometry(QtCore.QRect(370, 100, 271, 31))
        self.cmbTehsil_3.setStyleSheet("#cmbTehsil{\n"
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
        self.cmbTehsil_3.setObjectName("cmbTehsil_3")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbTehsil_3.addItem("")
        self.cmbStampPaperType_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbStampPaperType_3.setGeometry(QtCore.QRect(30, 180, 271, 31))
        self.cmbStampPaperType_3.setStyleSheet("#cmbStampPaperType{\n"
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
        self.cmbStampPaperType_3.setObjectName("cmbStampPaperType_3")
        self.cmbStampPaperType_3.addItem("")
        self.cmbStampPaperType_3.addItem("")
        self.cmbDeed_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbDeed_3.setGeometry(QtCore.QRect(370, 180, 271, 31))
        self.cmbDeed_3.setStyleSheet("#cmbDeed{\n"
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
        self.cmbDeed_3.setObjectName("cmbDeed_3")
        self.cmbDeed_3.addItem("")
        self.cmbDeed_3.addItem("")
        self.gvAgentInfo_2 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.gvAgentInfo_2.setGeometry(QtCore.QRect(10, 10, 661, 51))
        self.gvAgentInfo_2.setStyleSheet("background-image: url(:/challan/challan.png);")
        self.gvAgentInfo_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gvAgentInfo_2.setObjectName("gvAgentInfo_2")
        self.instruction2 = QtWidgets.QFrame(self.centralwidget)
        self.instruction2.setGeometry(QtCore.QRect(40, 1040, 661, 73))
        self.instruction2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.instruction2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.instruction2.setObjectName("instruction2")
        self.label_2 = QtWidgets.QLabel(self.instruction2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 0, 711, 141))
        self.label_4.setStyleSheet("background-image: url(:/logos/estamping.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(40, 150, 701, 131))
        self.label_23.setStyleSheet("background-image: url(:/challan/Screenshot 2022-10-07 011803ss.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblAgentCNIC_2.setText(_translate("MainWindow", "Agent Email"))
        self.lblAgentName_2.setText(_translate("MainWindow", "Agent Contact"))
        self.lblAgentName.setText(_translate("MainWindow", "Agent Name"))
        self.lblAgentCNIC.setText(_translate("MainWindow", "Agent CNIC"))
        self.pushButton.setText(_translate("MainWindow", "First Party"))
        self.pushButton_2.setText(_translate("MainWindow", "Add First Party"))
        self.label.setText(_translate("MainWindow", "Please add at least one First Party"))
        self.label_3.setText(_translate("MainWindow", "Retype the code from the picture:"))
        self.SecondParty.setText(_translate("MainWindow", "Second Party"))
        self.pushButton_4.setText(_translate("MainWindow", "Add Second Party"))
        self.cmbDistrict_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.cmbDistrict_3.setItemText(0, _translate("MainWindow", "Select District"))
        self.cmbDistrict_3.setItemText(1, _translate("MainWindow", "Attock"))
        self.cmbDistrict_3.setItemText(2, _translate("MainWindow", "Bawalnagar"))
        self.cmbDistrict_3.setItemText(3, _translate("MainWindow", "Bahawalpur"))
        self.cmbDistrict_3.setItemText(4, _translate("MainWindow", "Bakhar"))
        self.cmbDistrict_3.setItemText(5, _translate("MainWindow", "Chakwal"))
        self.cmbDistrict_3.setItemText(6, _translate("MainWindow", "Cheniot"))
        self.cmbDistrict_3.setItemText(7, _translate("MainWindow", "Faisalabad"))
        self.cmbDistrict_3.setItemText(8, _translate("MainWindow", "Lahore"))
        self.cmbDistrict_3.setItemText(9, _translate("MainWindow", "Lodhran"))
        self.cmbDistrict_3.setItemText(10, _translate("MainWindow", "Mianwali"))
        self.cmbDistrict_3.setItemText(11, _translate("MainWindow", "Multan"))
        self.cmbDistrict_3.setItemText(12, _translate("MainWindow", "Sargodha"))
        self.label_12.setText(_translate("MainWindow", "For Sale Deed please use Conveyance"))
        self.label_19.setText(_translate("MainWindow", "Tehsil"))
        self.label_5.setText(_translate("MainWindow", "District"))
        self.label_20.setText(_translate("MainWindow", "Deed Name"))
        self.label_21.setText(_translate("MainWindow", "Stamp Paper Type"))
        self.cmbTehsil_3.setItemText(0, _translate("MainWindow", "Select Tehsil"))
        self.cmbTehsil_3.setItemText(1, _translate("MainWindow", "Bahawalnagar Tehsil"))
        self.cmbTehsil_3.setItemText(2, _translate("MainWindow", "Chishtian Tehsil"))
        self.cmbTehsil_3.setItemText(3, _translate("MainWindow", "Ahmadpur East Tehsil"))
        self.cmbTehsil_3.setItemText(4, _translate("MainWindow", "Khairpur Tamewali Tehsil"))
        self.cmbTehsil_3.setItemText(5, _translate("MainWindow", "Khanpur Tehsil"))
        self.cmbTehsil_3.setItemText(6, _translate("MainWindow", "Alipur Tehsil"))
        self.cmbTehsil_3.setItemText(7, _translate("MainWindow", "Jampur Tehsil"))
        self.cmbTehsil_3.setItemText(8, _translate("MainWindow", "Faisalabad City Tehsil"))
        self.cmbTehsil_3.setItemText(9, _translate("MainWindow", "Kamalia Tehsil"))
        self.cmbTehsil_3.setItemText(10, _translate("MainWindow", "Rawalpindi Tehsil"))
        self.cmbTehsil_3.setItemText(11, _translate("MainWindow", "Sillanwali Tehsil"))
        self.cmbTehsil_3.setItemText(12, _translate("MainWindow", "Isakhel Tehsil"))
        self.cmbTehsil_3.setItemText(13, _translate("MainWindow", "Mianwali Tehsil"))
        self.cmbStampPaperType_3.setItemText(0, _translate("MainWindow", "Judicial"))
        self.cmbStampPaperType_3.setItemText(1, _translate("MainWindow", "Non-Judicial"))
        self.cmbDeed_3.setItemText(0, _translate("MainWindow", "Court Fee"))
        self.cmbDeed_3.setItemText(1, _translate("MainWindow", "Contract Fee"))
        self.label_2.setText(_translate("MainWindow", "Please add at least one Second Party"))
# import fff_rc        
# import llooggoo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
