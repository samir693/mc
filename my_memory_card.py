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
H_line4.addWidget(text,alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
H_line5.addWidget(RadioGroupBox)
H_line5.addWidget(AnsGroupBox)
AnsGroupBox.hide()
H_line6.addWidget(button5)
main_v_line.addLayout(H_line4)
main_v_line.addLayout(H_line5)
main_v_line.addLayout(H_line6)
win.setLayout(main_v_line)

def show_answer():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button5.setText('Следующий вопрос')
def show_question():
    ButtonGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    ButtonGroup.setExclusive(True)
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button5.setText('Ответить')

def next_question():
    win.cur_question += 1
    if win.cur_question == len(question_list):
        win.cur_question = 0
    q = question_list[win.cur_question]
    ask(q)


def test():
   if button5.text()=='Ответить':
        check_answer()
   else:
        next_question()

answers = [button1, button2, button3, button4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    result.setText(res)
    show_answer()

def check_answer():
    if answers[0].isChecked():
        show_correct('Поздравляю ты просветлился!')
    else:
        show_correct('Не повезло ты не святой!')


button5.clicked.connect(test)
win.cur_question = -1
next_question()
win.show()
app.exec_()
