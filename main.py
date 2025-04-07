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

#Работа с меню
PhotoMenu = tkinter.PhotoImage(file="photo/Dinozaver.png")#Сохранили фото в переменную PhotoMenu
#Параметер screen(родитель виджета) и image(установленное изабражение)
picture2=tkinter.Label(screen,image=PhotoMenu)
picture2.place(x=0,y=0)#Разместили Виджет(этикетка) по кардинатам x=0,y=0

#Работа с кнопкой играть
questionsM1=["Сколько градусов в прямом угле?",
           "Какое число является наименьшим простым числом?",
           "Что равно 1/4 от 20?",
           "Какой результат будет, если сложить 1/2 и 1/4?",
           "Какое число является квадратом 5?",
           "Сколько сантиметров в метре?",
           "Какой периметр у квадрата со стороной 4 см?",
           "Какое число является наименьшим общим кратным для 3 и 4?",
           "Какой результат будет, если умножить 0.5 на 0.4?",
           "Какое число является наибольшим делителем для 18?"]
answers1=["0.6",
          "1.56",
          "6",
          "8.9",
          "0.9",
          "0.55",
          "2.4",
          "3.3",
          "5",
          "8.5"]
answers2=["45",
          "67",
          "91",
          "10",
          "75",
          "18",
          "89",
          "56",
          "22",
          "34"]
answers3=["5/5",
          "3/4",
          "8/10",
          "2/4",
          "6/9",
          "1/8",
          "4/6",
          "7/8",
          "18/8",
          "3/5"]
def button():
    global klass_photo
    klass_photo = tkinter.PhotoImage(file="photo/klass.png")
    klass=tkinter.Label(screen,image=klass_photo)
    klass.place(x=0,y=0,width=1042,height = 607)
    random_number= random.randrange(0,9)
    text = tkinter.Label(screen, text=questionsM1[random_number],wraplength=600,fg="#d9dad9",bg="#5a7250",font=("Impact", 18))
    text.place(x=60, y=35,width=600,height=60)
    if random_number == 0:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=90
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers3[random_numbers2[0]]
            b=answers3[random_numbers2[1]]
            d=answers3[random_numbers2[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 1:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=1
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=1
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=1
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=1
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            d=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 2:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=5
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=5
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=5
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=5
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            d=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 3:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=3/4
            random_numbers3 = random.sample(range(10), 3)
            b=answers3[random_numbers3[0]]
            d=answers3[random_numbers3[1]]
            k=answers3[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=3/4
            random_numbers3 = random.sample(range(10), 3)
            a=answers3[random_numbers3[0]]
            d=answers3[random_numbers3[1]]
            k=answers3[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=3/4
            random_numbers3 = random.sample(range(10), 3)
            a=answers3[random_numbers3[0]]
            b=answers3[random_numbers3[1]]
            k=answers3[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=3/4
            random_numbers3 = random.sample(range(10), 3)
            a=answers3[random_numbers3[0]]
            b=answers3[random_numbers3[1]]
            d=answers3[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 4:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=90
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            d=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 5:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=90
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            d=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 6:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=90
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            d=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 7:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=90
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            d=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 8:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=90
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            d=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
    elif random_number == 9:
        random_number2 = random.randrange(0, 3)
        if random_number2 == 0:
            a=90
            random_numbers3 = random.sample(range(10), 3)
            b=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 1:
            b=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            d=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 2:
            d=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            k=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
        elif random_number2 == 3:
            k=90
            random_numbers3 = random.sample(range(10), 3)
            a=answers2[random_numbers3[0]]
            b=answers2[random_numbers3[1]]
            d=answers2[random_numbers3[2]]
            AnswerM1_1 = tkinter.Button(screen, text=a, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_1.place(x=100, y=110, width=180, height=120)
            AnswerM1_2 = tkinter.Button(screen, text=b, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#5a7250", font=("Impact", 15))
            AnswerM1_2.place(x=100, y=260, width=180, height=120)
            AnswerM1_3 = tkinter.Button(screen, text=d, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_3.place(x=500, y=110, width=180, height=120)
            AnswerM1_4 = tkinter.Button(screen, text=k, borderwidth=0, command=button, wraplength=180, fg="#d9dad9",
                                        bg="#6c8661", font=("Impact", 15))
            AnswerM1_4.place(x=500, y=260, width=180, height=120)
konopka_button_photo= tkinter.PhotoImage(file="photo/konopka_button.png")
konopka_button=tkinter.Button(screen,image=konopka_button_photo,borderwidth=0,activebackground="#5a7250",command=button)
konopka_button.place(x=100,y=88,width = 274,height = 135)
#Размер- 271 на 134

#Работа с кнопкой выход
def exit():
    screen.destroy()
konopka_exit_photo= tkinter.PhotoImage(file="photo/konopra_exit.png")
konopka_exit=tkinter.Button(screen,image=konopka_exit_photo,borderwidth=0,activebackground="#5a7250",command=exit)
konopka_exit.place(x=475,y=88,width = 274,height = 135)

#


tkinter.mainloop()#Обрабатывает работу экрана

