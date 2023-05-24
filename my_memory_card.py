from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,
QLabel,QVBoxLayout,QRadioButton,QHBoxLayout,QMessageBox,QGroupBox,QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q = Question('Кем должен был стать Сиддхартха по пророчеству','императором','художникам','бойцом','футболистом')
q1 = Question('Что увидел Сиддхартха когда ему было 20 лет?','труп','праздник','туалет','монаха')
q2 = Question('Как с арабского переводится Кааба','куб','стрела','корова','треугольник')
q3 = Question('Как звали маму Мухаммада','Амина','Сарвиноз','Саида','Кашей')

question_list.append(q)
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)

app = QApplication([])
win = QWidget()
win.setWindowTitle('Memory Card')
win.resize(400,200)
text = QLabel('Что увидел Сиддхартха когда ему было 20 лет?')
button1=QRadioButton('труп')
button2=QRadioButton('праздник')
button3=QRadioButton('туалет')
button4=QRadioButton('монаха')
button5=QPushButton('Ответить')

RadioGroupBox=QGroupBox('Варианты ответов')

H_line1 = QHBoxLayout()
V_line2 = QVBoxLayout()
V_line3 = QVBoxLayout()
V_line2.addWidget(button1)
V_line2.addWidget(button2)
V_line3.addWidget(button3)
V_line3.addWidget(button4)

H_line1.addLayout(V_line2)
H_line1.addLayout(V_line3)
RadioGroupBox.setLayout(H_line1)
AnsGroupBox=QGroupBox('Правильный ответ')
result = QLabel('Прав ты или нет?')
correct = QLabel('Ответ будет здесь!')
ans_v_line = QVBoxLayout()
ans_v_line.addWidget(result, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
ans_v_line.addWidget(correct, alignment= Qt.AlignCenter)
AnsGroupBox.setLayout(ans_v_line)

ButtonGroup = QButtonGroup()
ButtonGroup.addButton(button1)
ButtonGroup.addButton(button2)
ButtonGroup.addButton(button3)
ButtonGroup.addButton(button4)


H_line4 = QHBoxLayout()
H_line5 = QHBoxLayout()
H_line6 = QHBoxLayout()
main_v_line = QVBoxLayout()
