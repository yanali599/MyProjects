import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget ,QGridLayout,QPushButton,QLineEdit
from msilib import Table
from operator import contains
from fileinput import close
from sympy import * 
import datetime
from ui_start import Ui_Start
from ui_inst  import Ui_Inst


class StartWindow(QtWidgets.QWidget, Ui_Start):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)   
        self.setWindowTitle('Calculator')
        self.setLayout(QVBoxLayout())
        self.keypad()
        self.temp_nums=[]
        self.fin_nums=[]

        self.show()
        
    def keypad(self):
        container=QWidget()
        container.setLayout(QGridLayout())

        #Кнопочки
        self.result_field = QLineEdit()
        btn_result=QPushButton('Enter',clicked = self.func_result)
        btn_clear = QPushButton('Clear',clicked = self.clear_calc)
        btn_history = QPushButton('History',clicked = self.history_calc)
        btn_9 = QPushButton('9',clicked = lambda:self.num_press('9'))
        btn_8 = QPushButton('8',clicked = lambda:self.num_press('8'))
        btn_7 = QPushButton('7',clicked = lambda:self.num_press('7'))
        btn_6 = QPushButton('6',clicked = lambda:self.num_press('6'))
        btn_5 = QPushButton('5',clicked = lambda:self.num_press('5'))
        btn_4 = QPushButton('4',clicked = lambda:self.num_press('4'))
        btn_3 = QPushButton('3',clicked = lambda:self.num_press('3'))
        btn_2 = QPushButton('2',clicked = lambda:self.num_press('2'))
        btn_1 = QPushButton('1',clicked = lambda:self.num_press('1'))
        btn_0 = QPushButton('0',clicked = lambda:self.num_press('0'))
        btn_pow = QPushButton('^',clicked = lambda:self.num_press('^'))
        btn_plus = QPushButton('+',clicked = lambda:self.num_press('+'))
        btn_mins = QPushButton('-',clicked = lambda:self.num_press('-'))
        btn_mult = QPushButton('*',clicked = lambda:self.num_press('*'))
        btn_divd = QPushButton('/',clicked = lambda:self.num_press('/'))
        btn_x = QPushButton('x',clicked = lambda:self.num_press('x'))
        btn_y = QPushButton('y',clicked = lambda:self.num_press('y'))

        #Размещение кнопочек на сетке

        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(btn_result,1,0)
        container.layout().addWidget(btn_clear,1,1)
        container.layout().addWidget(btn_history,1,2)
        container.layout().addWidget(btn_pow,1,3)
        container.layout().addWidget(btn_9,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_7,2,2)
        container.layout().addWidget(btn_plus,2,3)
        container.layout().addWidget(btn_6,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_4,3,2)
        container.layout().addWidget(btn_mins,3,3)
        container.layout().addWidget(btn_3,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_1,4,2)
        container.layout().addWidget(btn_mult,4,3)
        container.layout().addWidget(btn_0,5,0)
        container.layout().addWidget(btn_divd,5,3)
        container.layout().addWidget(btn_x,5,1)
        container.layout().addWidget(btn_y,5,2)
        self.layout().addWidget(container)

    def num_press(self,key_number):
        self.temp_nums.append(key_number)
        temp_string=''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums)+temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self,operator):
         temp_string = ''.join(self.temp_nums)
         self.fin_nums.append(temp_string)
         self.fin_nums.append(operator)
         self.temp_nums=[]
         self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
         
         fin_string=''.join(self.fin_nums)+''.join(self.temp_nums)
         NormalOrNot=false
         for i in fin_string:
             if(i=='x' or i=='y'):
                 NormalOrNot=true
                 break
         if(NormalOrNot==false):
             result_string=eval(fin_string)
         else:
             result_string = solve(fin_string).__str__()#математика
             result_string= result_string.replace('[','')
             result_string= result_string.replace(']','')
             result_string= result_string.replace('{','')
             result_string= result_string.replace('}','')
             result_string= result_string.replace(':','')
             result_string= result_string.replace(' ','')
         fin_string+='='
         fin_string+=str(result_string)
         f = open('FullMath.txt', 'a')
         f.write(fin_string+'\n')
         f.close
         f = open('FullTime.txt', 'a')
         now = datetime.datetime.now()
         f.write(str(now.time())+'\n')
         f.close
         self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums=[]
        self.fin_nums=[]
    def history_calc(self):
        self.inst = QtWidgets.QWidget()
        ui_ins = Ui_Inst()
        ui_ins.setupUi(self.inst)
        self.inst.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = StartWindow()
    w.show()
    sys.exit(app.exec_())