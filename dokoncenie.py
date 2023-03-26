import tkinter as tk

win = tk.Tk()

atext = tk.Label(win,text="koeficient a:")
atext.pack()
a = tk.Entry(win)
a.pack()

btext = tk.Label(win,text="koeficient b:")
btext.pack()
b = tk.Entry(win)
b.pack()

ctext = tk.Label(win,text="koeficient c:")
ctext.pack()
c = tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get())
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2 - 4*ka*kc
    if d<0:
        vysledok = tk.Label(win,text = "Nema riesenie v R")
        vysledok.pack()
    elif d == 0:
        vysledok = tk.Label(win,text = "Ma prave 1 riesenie v R: x:"+ str(-kb/(2*ka)))
        vysledok.pack()
    else:
        vysledok = tk.Label(win,text = "Ma 2 riesenia v R: x1 =" + str(-kb + d ** 0.5 / (2*ka))+"\n"+"x2 = "+ str(-kb - d ** 0.5 / (2*ka)))
        vysledok.pack()

button = tk.Button(win, text = "hotovko!",command=executor)
button.pack()

win.mainloop()
