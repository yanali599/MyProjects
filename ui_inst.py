from PyQt5 import QtCore, QtWidgets
import PyQt5.QtWidgets as qtw
class Ui_Inst(object):
    def setupUi(self, Ui_Inst):
        Ui_Inst.setObjectName("Ui_Inst")
        Ui_Inst.resize(310, 229)

        self.gridLayout = QtWidgets.QGridLayout(Ui_Inst)
        self.gridLayout.setObjectName("gridLayout")
        self.table = qtw.QTableWidget(Ui_Inst)
        self.table.setObjectName("textEdit")
        self.gridLayout.addWidget(self.table, 0, 0)


        self.table.setColumnCount(2)     
        self.table.setRowCount(1)       
 

        self.table.setHorizontalHeaderLabels(["Equation", "Time"])
 

        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")

        i=-1
        f = open('FullMath.txt', 'r')
        for line in f:
         i+=1
         row = self.table.rowCount()
         self.table.setRowCount(row + 1)
         self.table.setItem(i, 0, qtw.QTableWidgetItem(''.join(line.split())))
        f.close
        f = open('FullTime.txt', 'r')
        i=-1
        for line in f:
         i+=1
         self.table.setItem(i, 1, qtw.QTableWidgetItem(''.join(line.split())))
        f.close 

        self.table.resizeColumnsToContents()
 
        self.gridLayout.addWidget(self.table, 0, 0)  
        self.retranslateUi(Ui_Inst)
        QtCore.QMetaObject.connectSlotsByName(Ui_Inst)




    def retranslateUi(self, Ui_Inst):
        _translate = QtCore.QCoreApplication.translate
        Ui_Inst.setWindowTitle(_translate("Ui_Inst", "History"))


