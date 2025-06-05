from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.remove_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_it())
        self.remove_pushButton.setGeometry(QtCore.QRect(60, 90, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remove_pushButton.setFont(font)
        self.remove_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(15, 151, 561, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mylist_listWidget.setFont(font)
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.add_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_lineEdit.setGeometry(QtCore.QRect(10, 20, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_lineEdit.setFont(font)
        self.add_lineEdit.setObjectName("add_lineEdit")
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_it())
        self.clear_pushButton.setGeometry(QtCore.QRect(330, 90, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_pushButton.setFont(font)
        self.clear_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_it())
        self.add_pushButton.setGeometry(QtCore.QRect(430, 20, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.add_pushButton.setIconSize(QtCore.QSize(16, 16))
        self.add_pushButton.setObjectName("add_pushButton")
        self.close_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = MainWindow.close)
        self.close_pushButton.setGeometry(QtCore.QRect(20, 490, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.close_pushButton.setFont(font)
        self.close_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.close_pushButton.setObjectName("close_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_it(self):
        item_text = self.add_lineEdit.text()
        if item_text.strip():
            self.mylist_listWidget.addItem(item_text)
            self.add_lineEdit.setText("")

    def clear_it(self):
        self.mylist_listWidget.clear()

    def remove_it(self):
        selected_items = self.mylist_listWidget.selectedItems()
        for item in selected_items:
            self.mylist_listWidget.takeItem(self.mylist_listWidget.row(item))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "სტალინის სიმულატორი"))
        self.remove_pushButton.setText(_translate("MainWindow", "დახვრიტე სუბიექტი"))
        self.clear_pushButton.setText(_translate("MainWindow", "ყველა დახვრიტე"))
        self.add_pushButton.setText(_translate("MainWindow", "მიუსაჯე დახვრეტა"))
        self.close_pushButton.setText(_translate("MainWindow", "მოწამლე სტალინი"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
