#Интерфейс- способ взаимодействие программы и пользователя при помощи виджетов
#Виджет- элимент интерфейса(кнопка,текстовое поле,картинка)
import random
import tkinter#импортировали модуль для работы с интерфейсом
from os import write

#Работа с экраном приложения
screen= tkinter.Tk()#Создаем экран
screen.geometry("1042x607+200+100")#Меняем размер и кардинаты экрана
screen.resizable(False, False)#Запрещаем менять размер экрана
#screen.attributes("-alpha", 0.9)
screen.title("DinoSholl")#Меняем имя экрана на "DinoSholl"

#Сохраняю все картинки
PhotoMenu = tkinter.PhotoImage(file="photo/Dinozaver.png")#Сохранили фото в переменную PhotoMenu
klass_photo = tkinter.PhotoImage(file="photo/klass.png")
konopka_button_photo= tkinter.PhotoImage(file="photo/konopka_button.png")
konopka_exit_photo= tkinter.PhotoImage(file="photo/konopra_exit.png")

#Список с вопросами
#\/Двумерный массив\/(то есть,списки внутри главного списка)
questions_and_answers1 = [
    ("Сколько будет 2 + 3?", "5", ["23", "10", "6"]),
    ("Что больше: 5 или 7?", "7", ["они равны", "5", "их нельзы сравнить"]),
    ("Найдите разность: 10 - 4.", "6", ["8", "401", "14"]),
]
questions_and_answers2 = [
    ("Сколько будет 8 + 6?","14",["23","86","2"]),
    ("Найдите произведение: 3 × 4.","12",["34","8","16"]),
    ("Разделите 20 на 5.","4",["5","2","25"])
]
questions_and_answers3 = [
    ("Сколько будет 12 + 15?", "27", ["1215", "38", "16"]),
    ("Найдите частное: 21 ÷ 3.", "7", ["4", "213", "63"]),
    ("Вычтите 7 из 30.", "23", ["37", "4", "15"]),
]
questions_and_answers4 = [
    ("Сколько будет 45 + 23?", "68", ["4523", "86", "59"]),
    ("Найдите произведение: 7 × 8.", "56", ["87", "78", "65"]),
    ("Разделите 50 на 5.", "10", ["250", "505", "55"]),
]
questions_and_answers5 = [
    ("Сколько будет 64 ÷ 4?", "16", ["76", "32", "644"]),
    ("Найдите остаток от деления 29 на 3.", "1", ["3", "293", "12"]),
    ("Вычтите 17 из 50.", "33", ["25", "67", "28"]),
]
questions_and_answers6 = [
    ("Сколько будет 12 × 12?", "144", ["1212", "2121", "167"]),
    ("Найдите частное: 144 ÷ 12.", "12", ["114", "87", "14412"]),
    ("Сложите 35 и 28.", "63", ["76", "3528", "42"]),
]
questions_and_answers7 = [
    ("Найдите сумму: 1/2 + 1/4.", "3/4", ["2/6", "2/4", "3/4"]),
    ("Вычтите 1/3 из 1.", "2/3", ["5/10", "1/2", "4/6"]),
    ("Умножьте 3/4 на 2.", "6/8", ["6/4", "1", "9/16"]),
]
questions_and_answers8 = [
    ("Сколько будет 0.5 + 0.75?", "0.8", ["0.95", "1.90", "0.23"]),
    ("Вычтите 0.2 из 1.5.", "1.7", ["1.52", "1.51", "1.89"]),
    ("Умножьте 0.3 на 4.", "1.2", ["0.2", "1.8", "1.5"]),
]
questions_and_answers9 = [
    ("Решите уравнение: x + 5 = 10.", "5", ["6", "2", "9"]),
    ("Найдите x: 3x = 12.", "-", ["56", "42", "9"]),
    ("Решите уравнение: 2x + 3 = 9.", "3", ["8", "2", "5"]),
]
questions_and_answers10 = [
    ("Решите уравнение: 2x - 3 = 7.", "2", ["7", "45", "14"]),
    ("Найдите x: 4(x + 1) = 12.", "2", ["7", "21", "15"]),
    ("Решите уравнение: x/2 + 3 = 7.", "8", ["7", "32", "2"]),
]
list_questions=[
    questions_and_answers1,
    questions_and_answers2
]
questions=[]
for i in list_questions:
    random_figure = random.randrange(0, 2)
    question_answer = i[random_figure]
    questions.append(question_answer)

#Функции
def button_play():
    global klass_photo
    random_number = random.randrange(0, 9)
    Question= questions_and_answers[random_number]
    print(Question)
    klass=tkinter.Label(screen,image=klass_photo)
    klass.place(x=0,y=0,width=1042,height = 607)
    text = tkinter.Label(screen, text= Question[0],wraplength=600,fg="#d9dad9",bg="#5a7250",font=("Impact", 18))
    text.place(x=60, y=35,width=600,height=60)
    random_number2= random.randrange(0,3)
    if random_number2 == 0:
        a=Question[1]
        d=Question[2][0]
        b=Question[2][2]
        k=Question[2][1]
    elif random_number2 == 1:
        a=Question[2][2]
        d=Question[1]
        b=Question[2][1]
        k=Question[2][0]
    elif random_number2 == 2:
        a=Question[2][0]
        d=Question[2][1]
        b=Question[1]
        k=Question[2][2]
    elif random_number2 == 3:
        a=Question[2][1]
        d=Question[2][2]
        b=Question[2][0]
        k=Question[1]
    AnswerM1_1 = tkinter.Button(screen, text= a, borderwidth=0, command=button_play, wraplength=180, fg="#d9dad9",
                                bg="#5a7250", font=("Impact", 15))
    AnswerM1_1.place(x=100, y=110, width=180, height=120)
    AnswerM1_2 = tkinter.Button(screen, text= d, borderwidth=0, command=button_play, wraplength=180, fg="#d9dad9",
                                bg="#5a7250", font=("Impact", 15))
    AnswerM1_2.place(x=100, y=260, width=180, height=120)
    AnswerM1_3 = tkinter.Button(screen, text= b, borderwidth=0, command=button_play, wraplength=180, fg="#d9dad9",
                                bg="#6c8661", font=("Impact", 15))
    AnswerM1_3.place(x=500, y=110, width=180, height=120)
    AnswerM1_4 = tkinter.Button(screen, text= k, borderwidth=0, command=button_play, wraplength=180, fg="#d9dad9",
                                bg="#6c8661", font=("Impact", 15))
    AnswerM1_4.place(x=500, y=260, width=180, height=120)
def exit():
    screen.destroy()

#Виджеты первого экрана
       #Фон для экрана
picture2=tkinter.Label(screen,image=PhotoMenu)
#Параметер screen(родитель виджета) и image(установленное изабражение)
picture2.place(x=0,y=0)#Разместили Виджет(этикетка) по кардинатам x=0,y=0
       #Кнопка играть
konopka_button=tkinter.Button(screen,image=konopka_button_photo,borderwidth=0,activebackground="#5a7250",command= button_play)
konopka_button.place(x=100,y=88,width = 274,height = 135)
       #Кнопка выход
konopka_exit=tkinter.Button(screen,image=konopka_exit_photo,borderwidth=0,activebackground="#5a7250",command=exit)
konopka_exit.place(x=475,y=88,width = 274,height = 135)

tkinter.mainloop()#Обрабатывает работу экрана

