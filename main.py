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
           "Какое число является наибольшим делителем для 18?"
           ]
def button():
    global klass_photo
    klass_photo = tkinter.PhotoImage(file="photo/klass.png")
    klass=tkinter.Label(screen,image=klass_photo)
    klass.place(x=0,y=0,width=1042,height = 607)
    random_number= random.randrange(0,9)
    text = tkinter.Label(screen, text=questionsM1[random_number],wraplength=600,fg="#d9dad9",bg="#5a7250",font=("Impact", 18))
    text.place(x=60, y=35,width=600,height=60)
    AnswerM1_1 = tkinter.Button(screen, text="1",borderwidth=0,command=button,wraplength=180, fg="#d9dad9", bg="#5a7250",font=("Impact", 15))
    AnswerM1_1.place(x=100,y=110,width=180,height=120)
    AnswerM1_2 = tkinter.Button(screen, text="2",borderwidth=0,command=button,wraplength=180, fg="#d9dad9", bg="#5a7250",font=("Impact", 15))
    AnswerM1_2.place(x=100,y=260,width=180,height=120)
    AnswerM1_3 = tkinter.Button(screen, text="3",borderwidth=0,command=button,wraplength=180, fg="#d9dad9", bg="#6c8661",font=("Impact", 15))
    AnswerM1_3.place(x=500, y=110, width=180, height=120)
    AnswerM1_4 = tkinter.Button(screen, text="4",borderwidth=0,command=button,wraplength=180, fg="#d9dad9", bg="#6c8661",font=("Impact", 15))
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

