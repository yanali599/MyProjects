from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Start(object):
    def setupUi(self, Ui_Start):
        Ui_Start.setObjectName("Ui_Start")
        Ui_Start.resize(306, 212)
        self.gridLayout = QtWidgets.QGridLayout(Ui_Start)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Ui_Start)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 1, 1, 1)

        self.retranslateUi(Ui_Start)
        QtCore.QMetaObject.connectSlotsByName(Ui_Start)

    def retranslateUi(self, Ui_Start):
        _translate = QtCore.QCoreApplication.translate
        Ui_Start.setWindowTitle(_translate("Ui_Start", "Form"))
        self.label.setText(_translate("Ui_Start", "Calculator by Яна Пулинович"))
