from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

      



app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')






btn_OK = QPushButton('Ответить')


lb_Question = QLabel('Какой национальности не существует?')


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_card = QVBoxLayout()


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(btn_OK)


window.setLayout(layout_card)

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)




layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)



RadioGroupBox.setLayout(layout_ans1)
layout_line2.addWidget(RadioGroupBox)
#Прячем радиогрупбокс
RadioGroupBox.hide()


#Панель результата

AnsGroupBox = QGroupBox('Результат:')
lb_Result = QLabel('Правильно/неправильно')
lb_Correct = QLabel('Правильный ответ!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)

AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)


#Добавление лэйаутов
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
#Функции
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if btn_OK.text() == 'Ответить':
       show_result()
    else:
        show_question()


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):   
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Correct.setText(q.right_answer)
    lb_Question.setText(q.question)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()
    



def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
    elif answers[1].isChecked():
        show_correct("Неправильно!")
    elif answers[2].isChecked():
        show_correct("Неправильно!")      
    elif answers[3].isChecked():
        show_correct("Неправильно!")


window.cur_question = -1
def next_question():    
    window.cur_question = +1
    if window.cur_question >= len(questions_list):
        window.cur_question = -1
    q = questions_list[window.cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == "Ответить":
        next_question()
    elif btn_OK.text() == "Результат":
        check_answer()




#Вопросы
questions_list = []
q = Question("Какой национальности не существует?", "Смурфы", "Энцы", "Алуеты", "Чулымцы")
q1 = Question("Государственный язык Бразилии", "Португальский", "Испанский", "Итальянский", "Бразильский")
questions_list.append(q)
questions_list.append(q1)



btn_OK.clicked.connect(click_ok)
        
window.setLayout(layout_card)



window.show()
app.exec_()





