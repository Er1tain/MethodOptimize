from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('600x400')
root.title('Методы оптимизации(минимизации)')

Label(root, text='x1: ', font=("Arial", 14)).place(x=230, y=0)
x1 = Entry(root)
x1.place(x=265, y = 3)

Label(root, text='x2: ', font=("Arial", 14)).place(x=230, y=30)
x2 = Entry(root)
x2.place(x=265, y = 33)

Label(root, text='change: ', font=("Arial", 14)).place(x=188, y=60)
change = Entry(root)
change.place(x=265, y = 63)

Label(root, text='ex: ', font=("Arial", 14)).place(x=230, y=90)
ex = Entry(root)
ex.place(x=265, y = 93)

Label(root, text='ey: ', font=("Arial", 14)).place(x=230, y=120)
ey = Entry(root)
ey.place(x=265, y = 123)

Label(root, text='M: ', font=("Arial", 14)).place(x=230, y=150)
m = Entry(root)
m.place(x=265, y = 153)

instruction = Button(root, text="Инструкция",
                      command=lambda: messagebox.showinfo(title="Инструкция" ,message='x1, x2 - начальные координаты точки, change - градиентый спуск,ex, ey - допустимые погрешности для x1, x2, соответственно, M - количество итераций алгоритма'))
instruction.place(x=245, y=193)

calculation = Button(root, text="Вычислить")
calculation.place(x=335, y=193)

root = mainloop()