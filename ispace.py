'''
github.com/razyar
'''


from PyQt4 import QtCore, QtGui
import sys
import os
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(281, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/root/phantom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 80, 261, 71))
        self.label.setAutoFillBackground(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 147, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 350, 171, 17))
        self.label_4.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(282, 157, 161, 31))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(280, 184, 161, 21))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(436, 157, 20, 51))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(280, 140, 171, 21))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.widget_4 = QtGui.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(266, 157, 21, 51))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuIVPN_options = QtGui.QMenu(self.menuSettings)
        self.menuIVPN_options.setObjectName(_fromUtf8("menuIVPN_options"))
        self.menuMigMig = QtGui.QMenu(self.menuSettings)
        self.menuMigMig.setObjectName(_fromUtf8("menuMigMig"))
        self.menuDomains = QtGui.QMenu(self.menuSettings)
        self.menuDomains.setAutoFillBackground(False)
        self.menuDomains.setObjectName(_fromUtf8("menuDomains"))
        MainWindow.setMenuBar(self.menubar)
        self.actionTurn_on = QtGui.QAction(MainWindow)
        self.actionTurn_on.setObjectName(_fromUtf8("actionTurn_on"))
        self.actionSupport = QtGui.QAction(MainWindow)
        self.actionSupport.setObjectName(_fromUtf8("actionSupport"))
        self.actionSubmit_request = QtGui.QAction(MainWindow)
        self.actionSubmit_request.setObjectName(_fromUtf8("actionSubmit_request"))
        self.actionSupport_2 = QtGui.QAction(MainWindow)
        self.actionSupport_2.setObjectName(_fromUtf8("actionSupport_2"))
        self.actionSubmit_new_domain = QtGui.QAction(MainWindow)
        self.actionSubmit_new_domain.setObjectName(_fromUtf8("actionSubmit_new_domain"))
        self.actionNew_iSpaceCode = QtGui.QAction(MainWindow)
        self.actionNew_iSpaceCode.setObjectName(_fromUtf8("actionNew_iSpaceCode"))
        self.menuIVPN_options.addAction(self.actionTurn_on)
        self.menuMigMig.addAction(self.actionSubmit_request)
        self.menuDomains.addAction(self.actionSubmit_new_domain)
        self.menuSettings.addAction(self.menuDomains.menuAction())
        self.menuSettings.addAction(self.menuMigMig.menuAction())
        self.menuSettings.addAction(self.menuIVPN_options.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        

        def QtCore_object4():
	    	UseriCode = self.lineEdit.text()
	    	if UseriCode == 'razyarrazy':
	    		QtCore_Stage2()
	    	if UseriCode == "":
	    		print 'Need iCode'
	    	else:
	    		print 'Failed'
	    
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSubmit_new_domain, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.update)
        QtCore.QObject.connect(self.actionSubmit_request, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.update)
        QtCore.QObject.connect(self.actionTurn_on, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.update)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), QtCore_object4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    global QtCore_Stage2
    def QtCore_Stage2():
		os.system('python platform.py')



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "iSpace", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">iSpace Network</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "Enter iCode: ", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>didnt have? <a href=\"https://ispace.mig/newcode\"><span style=\" text-decoration: underline; color:#0000ff;\">get one free</span></a></p></body></html>", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Requests", None))
        self.menuIVPN_options.setTitle(_translate("MainWindow", "iVPN", None))
        self.menuMigMig.setTitle(_translate("MainWindow", "MigMig", None))
        self.menuDomains.setTitle(_translate("MainWindow", "Domains", None))
        self.actionTurn_on.setText(_translate("MainWindow", "Submit request for anonymous servicces", None))
        self.actionSupport.setText(_translate("MainWindow", "Support", None))
        self.actionSubmit_request.setText(_translate("MainWindow", "Submit request for MigMig search engine", None))
        self.actionSupport_2.setText(_translate("MainWindow", "Support", None))
        self.actionSubmit_new_domain.setText(_translate("MainWindow", "Submit new domain", None))
        self.actionNew_iSpaceCode.setText(_translate("MainWindow", "New iSpaceCode", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

