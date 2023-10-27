# Лабораторная работа 8 ИСТбд-12 Горашко А.С. реализация 6 лабораторной работы с помощью использования библиотеки
# tkinter для написания GUI
# Текст 6 лабы:
# Задание состоит из двух частей.
# 1 часть – написать программу в соответствии со своим вариантом задания.
# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на
# характеристики объектов и целевую функцию для оптимизации решения. Цветочный магазин подает розы К видов.
# Сформировать все возможные варианты букетов. В букете должно быть не больше N цветов.
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Radiobutton


def cwr(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


# #Функция генерирует все букеты длинной не больше N
def generate_bouquets(K, N):
    flowers = list(range(1, K+1))
    bouquets = []

    for num_flowers in range(1, N+1):
        for bouquet in cwr(flowers, num_flowers):
            bouquets.append(bouquet)
    return bouquets


#Функция генерирует все букеты длинной не больше N, в которых один вид роз не встречается больше 2 раз
def generate_hardboquets(K,N):
    flowers = list(range(1, K+1))
    bouquets = []

    for num_flowers in range(1, N+1):
        for bouquet in cwr(flowers, num_flowers):
            if len(set(bouquet)) >= len(bouquet) - 1:
                bouquets.append(bouquet)
                most_expensive_bouquet(bouquet)
    return bouquets


max = 0
maxbouquet = tuple()
s = 0
pricelist = {1:100,2:58,3:44,4:87,5:154,6:118,7:65,8:29,9:95,10:299,11:43,12:59,13:999,14:32,15:29,16:51,17:240,18:178,19:44,20:74}

#Целевая функция ищет самый дорогой букет и его стоймость


def most_expensive_bouquet(list):
    global s
    global max
    global maxbouquet
    for i in list:
        s += pricelist.get(i)
    if s > max:
        max = s
        maxbouquet = tuple(list)
        s = 0


def default():
    max = 0
    labelPrice.grid_forget()
    labelMax.grid_forget()
    scrollRez.grid_forget()
    labelRez.grid_forget()
    label2.configure(text='Введите кол-во видов:')
    label2.grid(column=0, row=2)
    label3.configure(text="Введите максимальный размер букета:")
    label3.grid(column=0,row=4)
    textBox1.grid(column=0, row=3)
    textBox2.grid(column=0,row=5)
    textBox1.focus()
    button1.grid(column=1,row=5)

def click():
    if selected.get() == 1:
        k = textBox1.get()
        n = textBox2.get()
        try:
            rez = str(generate_bouquets(int(k),int(n)))
        except ValueError:
            labelRez.configure(text="Некорректные значения")
            labelRez.grid(column=0, row=6)
        scrollRez.insert(INSERT,rez)
        labelRez.configure(text="Сгенерированные букеты:")
        labelRez.grid(column=0,row=6)
        scrollRez.grid(column=0,row=7)
    if selected.get() == 2:
        labelMax.configure(text="")
        labelPrice.configure(text="")
        global max
        max = 0
        scrollRez.delete(1.0,END)
        k = textBox1.get()
        n = textBox2.get()
        try:
            rez = str(generate_hardboquets(int(k),int(n)))
        except ValueError:
            labelRez.configure(text="Некорректные значения")
            labelRez.grid(column=0,row=6)
        except TypeError:
            labelRez.configure(text="Не больше 20!")
            labelRez.grid(column=0,row=6)
        scrollRez.insert(INSERT,rez)
        labelRez.configure(text="Сегенерированные букеты:")
        labelMax.configure(text="Самый дорогой букет: {}".format(maxbouquet))
        labelPrice.configure(text="Цена: {}".format(max))
        labelRez.grid(column=0,row=6)
        scrollRez.grid(column=0,row=7)
        labelMax.grid(column=0,row=8)
        labelPrice.grid(column=0,row=9)

def advanced():
    global max
    max = 0
    scrollRez.grid_forget()
    labelRez.grid_forget()
    label2.configure(text='Введите кол-во видов(не больше 20):')
    label2.grid(column=0, row=2)
    label3.configure(text="Введите максимальный размер букета:")
    label3.grid(column=0, row=4)
    textBox1.grid(column=0, row=3)
    textBox2.grid(column=0, row=5)
    textBox1.focus()
    button1.grid(column=1, row=5)


mainWindow = Tk()
mainWindow.title("lab8")
mainWindow.geometry('600x400')
label1 = Label(mainWindow, text="Выберете реализацию.", font=('Arial Bold', 11))
label1.grid(column=0,row=0)
selected = IntVar()
rad1 = Radiobutton(mainWindow,text='Простая', value=1, variable=selected,command=default)
rad1.grid(column=0,row=1)
rad2 = Radiobutton(mainWindow,text='Сложная', value=2, variable=selected,command=advanced)
rad2.grid(column=1,row=1)
label2 = Label(mainWindow, text=" ", font=('Arial Bold', 11))
label3 = Label(mainWindow,text=" ",font=('Arial Bold', 11))
labelMax = Label(mainWindow, text=" ", font=('Arial Bold', 11))
labelPrice = Label(mainWindow, text=" ", font=('Arial Bold', 11))
labelRez = Label(mainWindow,text=" ",font=('Arial Bold', 11))
scrollRez = scrolledtext.ScrolledText(mainWindow,width=40,height=10,font=('Arial Bold', 11))
textBox1 = Entry(mainWindow,width=10)
k = ""
n = ""
textBox2 = Entry(mainWindow,width=10)
button1 = Button(mainWindow,text="Ввод",command=lambda : click())
mainWindow.mainloop()



