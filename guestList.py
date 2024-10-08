# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\guestList.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_guestsList(object):
    def setupUi(self, guestsList):
        guestsList.setObjectName("guestsList")
        guestsList.resize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Images/guests.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        guestsList.setWindowIcon(icon)
        guestsList.setStyleSheet("background-color: rgb(237, 246, 249);")
        self.listWidget = QtWidgets.QListWidget(guestsList)
        self.listWidget.setGeometry(QtCore.QRect(15, 50, 470, 330))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(guestsList)
        self.label.setGeometry(QtCore.QRect(20, 6, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Fredoka")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(guestsList)
        QtCore.QMetaObject.connectSlotsByName(guestsList)
        # Populate the list widget with data from the database
        self.populateListWidget()

    def populateListWidget(self):
        # Connect to the SQLite database
        connection_obj = sqlite3.connect('guests.db')
        cursor_obj = connection_obj.cursor()

        # Execute the SELECT statement
        statement = '''SELECT * FROM guests'''
        cursor_obj.execute(statement)

        # Fetch all rows from the query
        rows = cursor_obj.fetchall()

        # Iterate over the rows and add each to the list widget
        for row in rows:
            item_text = " ".join(map(str, row))  # Convert each row to a string
            list_item = QtWidgets.QListWidgetItem(item_text)
            self.listWidget.addItem(list_item)

        # Close the database connection
        connection_obj.close()
    
    
    def retranslateUi(self, guestsList):
        _translate = QtCore.QCoreApplication.translate
        guestsList.setWindowTitle(_translate("guestsList", "List of the Guests"))
        self.label.setText(_translate("guestsList", "List of all the guests"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    guestsList = QtWidgets.QWidget()
    ui = Ui_guestsList()
    ui.setupUi(guestsList)
    guestsList.show()
    sys.exit(app.exec_())
