import tkinter as tk 
import tkinter.ttk as ttk
import matplotlib.pyplot as wykres
import numpy as lista

window = tk.Tk() 
window.title("BifDraw") 
window.geometry("480x340")
window.resizable(width=False, height=False)

cancelStat = False
stepRes = [31, 301, 3001, 30001]

#Obsługa paska postępu 

def cancelProcess():   
    global cancelStat 
    cancelStat = True
    progresBar['value'] = 0
    stopButton.place(x = 10, y = 635)
    label2['text'] = "0%"
    window.update()


def progresBarUpdate(a, div1, div2, res):
    if  round(a) % div1 == div2:
        statusBar = str(progresBar['value'])
        statusBar = statusBar+"%"
        label2['text'] = statusBar
        progresBar['value'] += res
        window.update()


def callback(eventObject):
    if combo.current() == 1:
        drawButton2.place(x = 330, y = 215)
        label8.place(x = 305, y = 130)
        label9.place(x = 305, y = 170)
        label10.place(x = 425, y = 170)
        label11.place(x = 305, y = 90)
        txt.delete(0, tk.END)
        txt2.delete(0, tk.END)
        txt3.delete(0, tk.END)
        txt.insert(tk.INSERT, "100")
        txt2.insert(tk.INSERT, "50")
        txt3.insert(tk.INSERT, "0.5")
        combo2.current(2)
        combo3.current(0)
        combo3.place(x = 390, y = 90)
        txt4.delete(0, tk.END)
        txt4.insert(tk.INSERT, "0.5")
        txt4.place(x = 390, y = 132)
        txt5.delete(0, tk.END)
        txt5.insert(tk.INSERT, "1")
        txt5.place(x = 405, y = 172)
    else:
        drawButton2.place(x = 330, y = 795)
        label8.place(x = 305, y = 700)
        label9.place(x = 305, y = 730)
        label10.place(x = 405, y = 730)
        label11.place(x = 305, y = 790)
        label12.place(x = 305, y = 730)
        label13.place(x = 305, y = 770)
        txt4.place(x = 385, y = 792)
        txt5.place(x = 385, y = 732)
        txt.delete(0, tk.END)
        txt2.delete(0, tk.END)
        txt3.delete(0, tk.END)
        txt.insert(tk.INSERT, "10000")
        txt2.insert(tk.INSERT, "9900")
        txt3.insert(tk.INSERT, "0.5")
        combo2.current(2)
        combo3.place(x = 390, y = 790)

def callback2(eventObject):
    if combo3.current()==1:
        label12.place(x = 305, y = 130)
        label13.place(x = 305, y = 170)
    else:
        label12.place(x = 305, y = 730)
        label13.place(x = 305, y = 770)


#Obsługa błędów

def checkErrors():

    try:
        int(txt.get())
    except ValueError:
        tk.messagebox.showerror("Error","The number of steps given is not an integer.")
        return False
    if int(txt.get()) <= 0:
        tk.messagebox.showerror("Error","The number of steps given is not a positive number.")
        return False
    if int(txt.get()) > 99999:
        tk.messagebox.showerror("Error","The number of steps specified should be less than 100,000.")
        return False
    
    try:
        int(txt2.get())
    except ValueError:
        tk.messagebox.showerror("Error","The given number of rejected steps is not an integer.")
        return False
    if int(txt2.get()) >= int(txt.get()):
        tk.messagebox.showerror("Error","The specified number of rejected steps should be less than the number of total steps.")
        return False
    if int(txt2.get()) <= 0:
        tk.messagebox.showerror("Error","The given number of rejected steps is not a positive number.")
        return False

    try:
        float(txt3.get())
    except ValueError:
        tk.messagebox.showerror("Error","The value given is not a number.")
        return False
    if float(txt3.get()) <= 0 or float(txt3.get()) >= 1:
        tk.messagebox.showerror("Error","The initial population value should be within the set (0, 1).")
        return False

    try:

        float(txt4.get())
    except ValueError:
        tk.messagebox.showerror("Error","The specified value of the parameter q is not a number.")
        return False

    try:
        int(txt5.get())
    except ValueError:
        tk.messagebox.showerror("Error","The specified range limit is not an integer.")
        return False
    if int(txt5.get()) <= 0:
        tk.messagebox.showerror("Error","The specified range limit is not a positive number.")
        return False

#Rysowanie diagramu

def mapa2(n, x0, w, q):
    x = x0
    wartosci = []
    for i in range(n):
        #x=x+w*(x**q)*((1-x)**((-q)+2))
        x=w*(x**q)*((1-x)**((-q)+2))
        wartosci.append(x)
    return wartosci

def mapa(n, x0, a):
    x = x0
    wartosci = []
    for i in range(n):
        x = a*x*(1-x)
        wartosci.append(x)
    return wartosci

def obsluga():
    if checkErrors() == False:
        return

    global cancelStat
    cancelStat = False
    progresBar['value'] = 0
    window.update()
    diagram_bifurkacyjny = set([])
    kroki = int(txt.get())
    minKroki = int(txt2.get())
    stepResIndex = combo2.current()
    x0 = float(txt3.get())
    przestrzen_a = lista.linspace(1, 4, stepRes[stepResIndex])
    stopButton.place(x = 10, y = 255)

    for a in przestrzen_a:
        
        if cancelStat == True:
            return
        if stepResIndex == 0:
            progresBarUpdate(a * 10**(stepResIndex+1), 3, 1, 10)
            #progresBarUpdate(a, 0.3, 0.1, 10)
        else:
            progresBarUpdate(a * 10**(stepResIndex+1), 3 * 10**(stepResIndex-1), 1 * 10**(stepResIndex-1), 1)
            #progresBarUpdate(a, 0.03, 0.01, 1)

        tablica_punktow = mapa(kroki, x0, a)
        tablica_punktow = tablica_punktow[minKroki:]
        
        for Xn in tablica_punktow:
            diagram_bifurkacyjny.add((a, Xn))
    
    stopButton.place(x = 10, y = 635)

    tablica_a = []
    tablica_Xi = []

    for punkt in diagram_bifurkacyjny:
        (a, Xn) = punkt
        tablica_a.append(a)
        tablica_Xi.append(Xn)

    wykres.axis([1, 4, 0, 1])
    wykres.plot(tablica_a, tablica_Xi, '.', markersize=1)
    wykres.title("Classic bifurcation chart")
    wykres.ylabel(r'$x$')
    wykres.xlabel(r'${\alpha}$')
    wykres.show()

def obsluga2():
    if checkErrors() == False:
        return

    global cancelStat
    cancelStat = False
    progresBar['value'] = 0
    window.update()
    diagram_bifurkacyjny = set([])
    kroki = int(txt.get())
    minKroki = int(txt2.get())
    stepResIndex = combo2.current()
    x0 = float(txt3.get())

    maxW = int(txt5.get())
    maxWIndex = combo2.current()
    maxWIndex = maxWIndex + 1
    maxWIndex = maxW * (10**maxWIndex) + 1
    przestrzen_w = lista.linspace(0, maxW, maxWIndex)
    stopButton.place(x = 10, y = 255)
    dependentType = combo3.current()
    q = float(txt4.get())

    for w in przestrzen_w:
        if cancelStat == True:
            return
        if stepResIndex == 0:
            progresBarUpdate(w * 10**(stepResIndex+1), maxW, 0, 10)
        else:
            progresBarUpdate(w * 10**(stepResIndex+1), maxW* 10**(stepResIndex-1), 0, 1)

        if dependentType==0:
            tablica_punktow = mapa2(kroki, x0, w, q)
        else:
            tablica_punktow = mapa2(kroki, x0, q, w)
        tablica_punktow = tablica_punktow[minKroki:]
        
        for Xn in tablica_punktow:
            diagram_bifurkacyjny.add((w, Xn))
    
    stopButton.place(x = 10, y = 635)

    tablica_w = []
    tablica_Xi = []

    for punkt in diagram_bifurkacyjny:
        (w, Xn) = punkt
        tablica_w.append(w)
        tablica_Xi.append(Xn)
    #title = title + r'$x_{i+1} = x_i + wx{_i^q}(1-x_i)^{-q+2}$'
    #wykres.axis([1, 4, 0, 1])
    wykres.plot(tablica_w, tablica_Xi, '.', markersize=1)
    wykres.title("Bifurcation diagram of the generalized q-logistic equation")
    wykres.ylabel(r'$x$')
    if dependentType == 0:
        wykres.xlabel(r'$w$')
    else:
        wykres.xlabel(r'$q$')
    wykres.show()

#Pasek postępu

progresBar = ttk.Progressbar(window, orient = tk.HORIZONTAL,length = 460, mode = 'determinate')
progresBar.place(x = 10, y = 310)

#Tekstboxy

txt = tk.Entry(window ,width=7, justify='right', font = ("Arial", 11))
txt.insert(tk.INSERT, "10000")
txt.place(x = 205, y = 92)
txt2 = tk.Entry(window ,width=7, justify='right', font = ("Arial", 11))
txt2.insert(tk.INSERT, "9900")
txt2.place(x = 205, y = 132)
txt3 = tk.Entry(window ,width=7, justify='right', font = ("Arial", 11))
txt3.insert(tk.INSERT, "0.5")
txt3.place(x = 205, y = 172)
txt4 = tk.Entry(window ,width=7, justify='right', font = ("Arial", 11))
txt4.insert(tk.INSERT, "0.5")
txt4.place(x = 385, y = 792)
txt5 = tk.Entry(window ,width=2, justify='right', font = ("Arial", 11))
txt5.insert(tk.INSERT, "1")
txt5.place(x = 385, y = 732)

#Teksty

label1 = tk.Label(window, text="Choose an eq.:",font = ("Arial", 12, "bold"))
label1.place(x = 10, y = 20)
label2 = tk.Label(window, text="0%", font = ("Arial", 11))
label2.place(x = 90, y = 285)
label3 = tk.Label(window, text="Number of total steps:", font = ("Arial", 11, "bold"))
label3.place(x = 10, y = 90)
label4 = tk.Label(window, text="Rejected number of steps:", font = ("Arial", 11, "bold"))
label4.place(x = 10, y = 130)
label5 = tk.Label(window, text="Progress:", font = ("Arial", 11, "bold"))
label5.place(x = 10, y = 285)
label6 = tk.Label(window, text="Resolution:", font = ("Arial", 11, "bold"))
label6.place(x = 10, y = 210)
label7 = tk.Label(window, text="Initial value: ", font = ("Arial", 11, "bold"))
label7.place(x = 10, y = 170)
label8 = tk.Label(window, text="Value of q: ", font = ("Arial", 11, "bold"))
label8.place(x = 305, y = 790)
label9 = tk.Label(window, text="Range of w: (0 - ", font = ("Arial", 11, "bold"))
label9.place(x = 305, y = 730)
label10 = tk.Label(window, text=")", font = ("Arial", 11, "bold"))
label10.place(x = 405, y = 730)
label11 = tk.Label(window, text="Dep.:", font = ("Arial", 11, "bold"))
label11.place(x = 305, y = 740)
label12 = tk.Label(window, text="Value of w: ", font = ("Arial", 11, "bold"))
label13 = tk.Label(window, text="Range of q: ", font = ("Arial", 11, "bold"))
label12.place(x = 305, y = 730)
label13.place(x = 305, y = 770)

#Lista

combo = ttk.Combobox(window,values=[
                                    "Classical logistic equation", 
                                    "Generalized q-logistic equation"],
                            font = ("Arial", 12),
                            state="readonly",
                            width=32)

combo.current(0)
combo.place(x = 160, y = 20)

combo2 = ttk.Combobox(window,values=[
                                    "0,1", 
                                    "0,01",
                                    "0,001",
                                    "0,0001"],
                            font = ("Arial", 11),
                            state="readonly",
                            width=7, justify='right')

combo2.current(2)
combo2.place(x = 130, y = 212)

combo3 = ttk.Combobox(window,values=[
                                    "x to w", 
                                    "x to q"],
                            font = ("Arial", 12),
                            state="readonly",
                            width=6)

combo3.current(0)
combo3.place(x = 160, y = 725)

#Przyciski 

style = ttk.Style()
style.configure('TButton', font = 
               ('calibri', 17, 'bold'), 
                    borderwidth = '4') 
style.configure('C.TButton', font = 
               ('calibri', 17, 'bold'), 
                    borderwidth = '4') 
style.configure('W.TButton', font = 
               ('calibri', 10, 'bold'), 
                    borderwidth = '4')

style.map('TButton', foreground = [('active', '!disabled', 'green')], 
                     background = [('active', 'black')]) 

style.map('C.TButton', foreground = [('active', '!disabled', 'red')], 
                     background = [('active', 'black')]) 

style.map('W.TButton', foreground = [('active', '!disabled', 'red')], 
                     background = [('active', 'black')]) 

drawButton = ttk.Button(window, text = 'Draw', command = obsluga) 
drawButton.place(x = 330, y = 215)

drawButton2 = ttk.Button(window, text = 'Draw', command = obsluga2) 
drawButton2.place(x = 330, y = 795)

combo.bind("<<ComboboxSelected>>", callback)
combo3.bind("<<ComboboxSelected>>", callback2)

exitButton = ttk.Button(window, text = 'Exit', style = 'C.TButton', command = window.destroy) 
exitButton.place(x = 330, y = 260)

stopButton = ttk.Button(window, text = 'Abort', style = 'W.TButton', command = cancelProcess) 

tk.mainloop()