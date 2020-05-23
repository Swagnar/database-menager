# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shop.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

#when delete -> do not show again in fill_widgetTable

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.Qt import *
import mysql.connector
import re,sys

cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "cisco1",
    database = "clothes"
)

def main():
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())

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
        MainWindow.resize(989, 721)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(-20, 10, 781, 671))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.comboBox_select = QtGui.QComboBox(self.centralwidget)
        self.comboBox_select.setGeometry(QtCore.QRect(830, 40, 141, 27))
        self.comboBox_select.setObjectName(_fromUtf8("comboBox_select"))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))
        self.comboBox_select.addItem(_fromUtf8(""))



        self.comboBox_add = QtGui.QComboBox(self.centralwidget)
        self.comboBox_add.setGeometry(QtCore.QRect(830, 110, 141, 27))
        self.comboBox_add.setObjectName(_fromUtf8("comboBox_add"))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.comboBox_add.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 20, 211, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(770, 70, 211, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(770, 90, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(770, 140, 211, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(770, 160, 141, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(770, 210, 211, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(770, 230, 111, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))



        self.pushButton_select = QtGui.QPushButton(self.centralwidget)
        self.pushButton_select.setGeometry(QtCore.QRect(770, 40, 61, 27))
        self.pushButton_select.setObjectName(_fromUtf8("pushButton_select"))
        self.pushButton_select.clicked.connect(self.select_from_table)

        self.pushButton_add = QtGui.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(770, 110, 61, 27))
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.pushButton_add.clicked.connect(self.add_record_to_table)

        self.pushButton_delete = QtGui.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(770, 180, 61, 27))
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.pushButton_delete.clicked.connect(self.delete_from_table)

        self.pushButton_edit = QtGui.QPushButton(self.centralwidget)
        self.pushButton_edit.setGeometry(QtCore.QRect(770, 250, 61, 27))
        self.pushButton_edit.setObjectName(_fromUtf8("pushButton_edit"))
        self.pushButton_edit.clicked.connect(self.edit_record)



        self.spinBox_delete = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_delete.setGeometry(QtCore.QRect(830, 180, 60, 27))
        self.spinBox_delete.setObjectName(_fromUtf8("spinBox_delete"))

        self.spinBox_edit = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_edit.setGeometry(QtCore.QRect(830, 250, 60, 27))
        self.spinBox_edit.setObjectName(_fromUtf8("spinBox_edit"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.le = QLineEdit()
        self.le2 = QLineEdit()



    def retranslateUi(self, MainWindow):



        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.comboBox_select.setItemText(0, _translate("MainWindow", "ceny", None))
        self.comboBox_select.setItemText(1, _translate("MainWindow", "designer", None))
        self.comboBox_select.setItemText(2, _translate("MainWindow", "dostawa", None))
        self.comboBox_select.setItemText(3, _translate("MainWindow", "dostawca", None))
        self.comboBox_select.setItemText(4, _translate("MainWindow", "kategorie", None))
        self.comboBox_select.setItemText(5, _translate("MainWindow", "kraje", None))
        self.comboBox_select.setItemText(6, _translate("MainWindow", "marka", None))
        self.comboBox_select.setItemText(7, _translate("MainWindow", "poddostawa", None))
        self.comboBox_select.setItemText(8, _translate("MainWindow", "pracownik", None))
        self.comboBox_select.setItemText(9, _translate("MainWindow", "produkt", None))
        self.comboBox_select.setItemText(10, _translate("MainWindow", "sklep", None))
        self.comboBox_select.setItemText(11, _translate("MainWindow", "stanowisko", None))
        self.pushButton_select.setText(_translate("MainWindow", "OK", None))
        self.label.setText(_translate("MainWindow", "Wyświetlanie zawartości tabeli", None))
        self.label_2.setText(_translate("MainWindow", "Dodaj do tabeli", None))
        self.comboBox_add.setItemText(0, _translate("MainWindow", "ceny", None))
        self.comboBox_add.setItemText(1, _translate("MainWindow", "designer", None))
        self.comboBox_add.setItemText(2, _translate("MainWindow", "dostawa", None))
        self.comboBox_add.setItemText(3, _translate("MainWindow", "dostawca", None))
        self.comboBox_add.setItemText(4, _translate("MainWindow", "kategorie", None))
        self.comboBox_add.setItemText(5, _translate("MainWindow", "kraje", None))
        self.comboBox_add.setItemText(6, _translate("MainWindow", "marka", None))
        self.comboBox_add.setItemText(7, _translate("MainWindow", "poddostawa", None))
        self.comboBox_add.setItemText(8, _translate("MainWindow", "pracownik", None))
        self.comboBox_add.setItemText(9, _translate("MainWindow", "produkt", None))
        self.comboBox_add.setItemText(10, _translate("MainWindow", "sklep", None))
        self.comboBox_add.setItemText(11, _translate("MainWindow", "stanowisko", None))
        self.pushButton_add.setText(_translate("MainWindow", "OK", None))
        self.label_3.setText(_translate("MainWindow", "Usuń rekord z tabeli", None))
        self.pushButton_delete.setText(_translate("MainWindow", "OK", None))
        self.pushButton_edit.setText(_translate("MainWindow", "OK", None))
        self.label_4.setText(_translate("MainWindow", "Edytuj rekord", None))



    def fill_WidgetTable(self,MainWindow,tableName):



        rows = self.tableWidget.rowCount()
        tmp = 0
        tbColumns = self.return_columns(self,tableName)
        tbValues = self.return_values_in_table(self,tableName)

        self.tableWidget.setColumnCount(len(tbColumns))
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)

        while tmp != len(tbColumns):
            item = QtGui.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(tmp, item)

            item2 = self.tableWidget.horizontalHeaderItem(tmp)                                                      
            item2.setText(_translate("MainWindow", tbColumns[tmp][0], None))

            tmp += 1

        for x in range(len(tbValues)):
            self.tableWidget.insertRow(rows)
            for y in range(len(tbColumns)):
                self.tableWidget.setItem(rows, y, QtGui.QTableWidgetItem(str(tbValues[x][y])))
                #print tbValues[x][y]
            rows += 1
        


    def select_from_table(self, MainWindow):   


        self.tableWidget.setRowCount(0)
        tbName = str(self.comboBox_select.currentText())
        self.fill_WidgetTable(self,tbName)



    def edit_record(self,MainWindow):
        cursor = cnx.cursor()

        tbName = str(self.comboBox_select.currentText())
        tbColumns = self.return_columns(self, tbName)
        tbColumnsStringList = []
        rowId2edit = self.spinBox_edit.value()
        sqlTbColumns = []


        for x in tbColumns: 
            tbColumnsStringList.append(str(x))

        item, ok = QInputDialog.getItem(self.le, "Edytuj "+tbName, "Kolumna do edycji:", tbColumnsStringList, 0, False)
        if ok and item:
            self.le.setText(item)

        x = re.findall(r"([a-z]+.+[a-z])",str(self.le.text()))
        y = ""
        for i in x:
            y += i
        print y
        text, ok = QInputDialog.getText(self.le2, "Edytuj "+tbName, "Nowa wartosc: ")
        userInput = str(text)

        sql = "UPDATE "+tbName+" SET "+y+" = '"+userInput+"' WHERE "+tbColumns[0][0]+" = "+str(rowId2edit)
        cursor.execute(sql)

        #text, ok = QInputDialog.getText(self.le )

    def add_record_to_table(self,MainWindow):
        cursor = cnx.cursor()


        tbName = str(self.comboBox_add.currentText())
        tbColumns = self.return_columns(self,tbName)
        rows = self.tableWidget.rowCount()
        userInputValueList = []
        columnDataTypesString = ""

        for x in tbColumns:
        
            text, ok = QInputDialog.getText(self.le2, "Dodaj do "+tbName, str(x))

            if ok:
                columnDataTypesString += "%s,"
                if str(text) == "":
                    userInputValueList.append(None)
                else:
                    userInputValueList.append(str(text))

        print userInputValueList
        columnDataTypesString = columnDataTypesString[:-1]
        sql = "INSERT INTO "+tbName+" VALUES ("+columnDataTypesString+")"

        cursor.execute(sql, userInputValueList)
        cursor.close()


        

    def delete_from_table(self, MainWindow):   



        rowId2delete = self.spinBox_delete.value()
        tbName = str(self.comboBox_select.currentText())
        tbColumns = self.return_columns(self,tbName)
        cursor = cnx.cursor()
        sql = "DELETE FROM "+tbName+" WHERE "+tbColumns[0][0]+" = "+str(n)
        cursor.execute(sql)

        self.tableWidget.removeRow(n-1)



    def return_values_in_table(self,MainWindow,tableName):



        cursor = cnx.cursor()
        if tableName == "designer":
            sql = "SELECT designer.id_designera, marka.nazwa_marki, designer.imie, designer.nazwisko FROM designer INNER JOIN marka ON designer.id_marki = marka.id_marki"
        elif tableName == "sklep":
            sql = "SELECT sklep.id_sklepu, sklep.nazwa_sklepu, pracownik.imie, kraje.nazwa_kraju FROM (sklep INNER JOIN pracownik ON sklep.id_managera = pracownik.id_pracownika) INNER JOIN kraje ON sklep.id_kraju = kraje.id_kraju;"
        elif tableName == "pracownik":
            sql = "SELECT pracownik.id_pracownika, sklep.nazwa_sklepu, pracownik.imie, stanowisko.tytul, 'pracownik.etat_h/t' FROM (pracownik INNER JOIN sklep ON pracownik.id_sklepu = sklep.id_sklepu) INNER JOIN stanowisko ON pracownik.id_stanowiska = stanowisko.id_stanowiska;"
        elif tableName == "stanowisko":
            sql = "SELECT stanowisko.id_stanowiska, stanowisko.tytul, stanowisko.stawka_h FROM stanowisko;"
        elif tableName == "marka":
            sql = "SELECT marka.id_marki, marka.nazwa_marki, kraje.nazwa_kraju FROM marka INNER JOIN kraje ON marka.id_kraju = kraje.id_kraju;"
        elif tableName == "dostawca":
            sql = "SELECT dostawca.id_dostawcy, dostawca.nazwa_firmy, dostawca.telefon, dostawca.adres FROM dostawca"
        elif tableName == "kraje":
            sql = "SELECT kraje.id_kraju, kraje.nazwa_kraju FROM kraje;"
        elif tableName == "ceny":
            sql = "SELECT ceny.id_ceny, ceny.detail_price, ceny.primary_price FROM ceny;"
        elif tableName == "kategorie":
            sql = "SELECT kategorie.id_kategorii, kategorie.nazwa_kategorii FROM kategorie;"
        elif tableName == "dostawa":
            sql = "SELECT dostawca.id_dostawy, dostawca.nazwa_firmy, sklep.nazwa_sklepu FROM (dostawa INNER JOIN dostawca ON dostawa.id_dostawcy = dostawca.id_dostawcy) INNER JOIN sklep ON dostawa.id_sklepu = sklep.id_sklepu"
        elif tableName == "poddostawa":
            sql = "SELECT poddostawa.id_poddostawy, dostawca.nazwa_firmy, poddostawa.ilosc_produktu, produkt.nazwa_produktu FROM ((poddostawa INNER JOIN dostawa ON poddostawa.id_dostawy = dostawa.id_dostawy) INNER JOIN dostawca ON dostawa.id_dostawcy = dostawca.id_dostawcy) INNER JOIN produkt ON produkt.id_poddostawy = poddostawa.id_poddostawy;"
        elif tableName == "produkt":
            sql = "SELECT produkt.id_produktu, produkt.nazwa_produktu, ceny.detail_price,  sklep.nazwa_sklepu, marka.nazwa_marki, 'produkt.waga[g]', kategorie.nazwa_kategorii FROM (((produkt INNER JOIN ceny ON produkt.id_ceny = ceny.id_ceny) INNER JOIN marka ON produkt.id_marki = marka.id_marki) INNER JOIN kategorie ON produkt.id_kategorii = kategorie.id_kategorii) INNER JOIN sklep ON produkt.id_sklepu = sklep.id_sklepu;"    
        else:
            sql = "SELECT * FROM "+tableName
        cursor.execute(sql)
        row = cursor.fetchall()
        cursor.close()

        valuesINtableTuple = list(row)
        valuesINtableList = []
        tmp_val = []

        for x in valuesINtableTuple:
            tmp_val = list(x)
            valuesINtableList.append(tmp_val)
        return valuesINtableList



    def return_columns(self, MainWindow, tableName):


        
        sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='clothes' AND `TABLE_NAME`='"+tableName+"'"

        cursor = cnx.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        cursor.close()

        columns_List = []

        col_t2l = list(row)

        for x in col_t2l:
            y = re.findall("'([^']*)'", str(x))
            columns_List.append(y)

        return columns_List



        '''
        columnList -> wiadomo
        n -> len(columnList)
        userValueList = []
        id2delete = spinBox obok guzika
        for n:
            okienko ->  columnList[n], 
                        editLine ->  userValueList.append()
            Albo
                        editLine -> odrazu wysyłam sql, 
            UPDATE + tableName + SET + columnList[n] = userInput WHERE id = id2delete
        '''
main()
