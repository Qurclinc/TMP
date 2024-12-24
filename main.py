from tkinter import *  
from sympy import *
from sympy.abc import*
import random
from math import *
from tkinter.ttk import Checkbutton  
from tkinter import scrolledtext  


def is_prime(p):
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5 + 1)):
        if p % i == 0:
            return False
    else:
        return True

def vyvodT(T):
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, 'Матрица T:\n')
    txt.insert(INSERT, str(T[0,0])+' '*18)
    txt.insert(INSERT, str(T[0,1])+' '*18)
    txt.insert(INSERT, str(T[0,2])+' '*18)
    txt.insert(INSERT, str(T[0,3])+'\n')
    txt.insert(INSERT, str(T[1,0])+'  ')
    txt.insert(INSERT, str(T[1,1])+'  ')
    txt.insert(INSERT, str(T[1,2])+'  ')
    txt.insert(INSERT, str(T[1,3])+'\n')
    txt.insert(INSERT, str(T[2,0])+'  ')
    txt.insert(INSERT, str(T[2,1])+'  ')
    txt.insert(INSERT, str(T[2,2])+'  ')
    txt.insert(INSERT, str(T[2,3])+'\n')    
    txt.insert(INSERT, str(T[3,0])+'  ')
    txt.insert(INSERT, str(T[3,1])+'  ')
    txt.insert(INSERT, str(T[3,2])+'  ')
    txt.insert(INSERT, str(T[3,3])+'\n')

def vyvodA(A):
    txt.insert(INSERT, str(A[0])+'  ')
    txt.insert(INSERT, str(A[1])+'  ')
    txt.insert(INSERT, str(A[2])+'  ')
    txt.insert(INSERT, str(A[3])+'  ')
    
  
def clicked1():
     p = int(txt1.get())
     q = int(txt2.get())
     a1=p**(1/2)+q**(1/2) 
     a2=p**(1/2)-q**(1/2)
     a3=-p**(1/2)+q**(1/2)
     a4=-p**(1/2)-q**(1/2)
     T = Matrix([[1,1,1,1],[a1, a2, a3, a4],[a1*a1, a2*a2, a3*a3, a4*a4],[a1*a1*a1, a2*a2*a2, a3*a3*a3, a4*a4*a4]])
     if chk1_state.get() == True:
        vyvodT(T)
     m = Matrix([[0,0,0,0]])
     w = int(spin3.get())
     alfd = float(txt3.get())
     alfm = float(txt4.get())
     alf = -1*complex(alfd,alfm)
     if chk2_state.get() == True:
        txt.insert(INSERT, '\n')
        txt.insert(INSERT, 'Точки алгебраической решётки для матрицы T:\n')
     s = 0
     cc =''
     rn = int(spin1.get())
     rv = int(spin2.get())
     if selected.get() == 1:
        for l in range(w):
           for i in range(4):
               m[i]=random.randint(rn, rv)
           A = m*T
           if chk2_state.get() == True:
               txt.insert(INSERT, '\n')
               vyvodA(A)
           modul = max(1,abs(A[0]))*max(1,abs(A[1]))*max(1,abs(A[2]))*max(1,abs(A[3]))
           c = complex(modul**(alf))
           cc=cc+'+'+str(c)+'+\n'
           s = s + c
     if selected.get() == 2:
        for l in range(w):
           for i in range(4):
               m[i]=i+l
           A = m*T
           if chk2_state.get() == True:
               txt.insert(INSERT, '\n')
               vyvodA(A)
           modul = max(1,abs(A[0]))*max(1,abs(A[1]))*max(1,abs(A[2]))*max(1,abs(A[3]))
           c = complex(modul**(alf))
           cc=cc+'+'+str(c)+'+\n'
           s = s + c
     if chk3_state.get() == True:
        txt.insert(INSERT, '\n')
        txt.insert(INSERT, '\n')
        txt.insert(INSERT, 'Сумма в выбранных точках решётки:\n')
        txt.insert(INSERT, '\n')
        txt.insert(INSERT, cc[1:-1])
     if chk4_state.get() == True:
        txt.insert(INSERT, '\n')
        txt.insert(INSERT, '\n')
        txt.insert(INSERT, '� езультат вычисления суммы:\n')
        txt.insert(INSERT, '\n')
        txt.insert(INSERT, s)




  
window = Tk()  
window.title("Алгебраические решётки и гиперболическая дзета-функция алгебраических решёток")  
window.geometry('1200x500')  
lbl1 = Label(window, text="Введите простое p")  
lbl1.grid(column=0, row=0) 
lbl2 = Label(window, text="Введите простое q")  
lbl2.grid(column=0, row=1) 
lbl3 = Label(window, text="Выберите нижнюю границу диапазона")  
lbl3.grid(column=0, row=2) 
lbl4 = Label(window, text="Выберите верхнюю границу диапазона")  
lbl4.grid(column=0, row=3) 
lbl5 = Label(window, text="Выберите количество точек решётки")
lbl5.grid(column=0, row=4) 
lbl6 = Label(window, text="Введите действительную часть комплексного числа")
lbl6.grid(column=0, row=5) 
lbl7 = Label(window, text="Введите мнимую часть комплексного числа")
lbl7.grid(column=0, row=6) 
txt1 = Entry(window,width=10)  
txt1.grid(column=1, row=0, sticky=w) 
txt2 = Entry(window,width=10)  
txt2.grid(column=1, row=1, sticky=w) 
spin1 = Spinbox(window, from_=-10000, to=10000, width=10)  
spin1.grid(column=1, row=2, sticky=w)  
spin2 = Spinbox(window, from_=-10000, to=10000, width=10)  
spin2.grid(column=1, row=3, sticky=w) 
spin3 = Spinbox(window, from_=1, to=10000, width=10)  
spin3.grid(column=1, row=4, sticky=w) 
txt3 = Entry(window,width=10)  
txt3.grid(column=1, row=5, sticky=w) 
txt4 = Entry(window,width=10)  
txt4.grid(column=1, row=6, sticky=w) 


selected = IntVar()  
rad1 = Radiobutton(window,text='Случайный выбор точек алгебраической решётки', value=1, variable=selected)  
rad2 = Radiobutton(window,text='Перебор точек алгебраической решётки в заданном диапазоне', value=2, variable=selected)  
rad1.grid(column=3, row=5, sticky=w)   
rad2.grid(column=3, row=6, sticky=w)   

  

chk1_state = BooleanVar()  
chk1_state.set(False)  # проверка состояния чекбокса  
chk1 = Checkbutton(window, text='Показать матрицу T степеней алгебраически сопряженных алгебраических чисел', var=chk1_state)  
chk1.grid(column=3, row=0, sticky=w) 
chk2_state = BooleanVar()
chk2_state.set(False)  # проверка состояния чекбокса  
chk2 = Checkbutton(window, text='Показать выбранные точки алгебраической решетки для матрицы T', var=chk2_state)  
chk2.grid(column=3, row=1, sticky=w) 
chk3_state = BooleanVar() 
chk3_state.set(False)  # проверка состояния чекбокса  
chk3 = Checkbutton(window, text='Показать сумму для выбранных точек, построенную по формуле гиперболической дзета-функции алгебраической решётки', var=chk3_state)  
chk3.grid(column=3, row=2, sticky=w) 
chk4_state = BooleanVar() 
chk4_state.set(False)  # проверка состояния чекбокса   
chk4 = Checkbutton(window, text='Показать результат вычисления суммы, построенной для гиперболической дзета-функции алгебраической решётки', var=chk4_state)  
chk4.grid(column=3, row=3, sticky=w)

 
btn1 = Button(window, text="Вычислить и показать выбранные объекты", command=clicked1)  
btn1.grid(column=0, row=7)  


txt = scrolledtext.ScrolledText(window, width=100, height=20)  
txt.grid(column=3, row=7, sticky=w)  
  
window.mainloop()