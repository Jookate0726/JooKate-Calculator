from tkinter import *
import pyttsx3

calc = Tk()
calc.title("JooKate Calculator")
calc.configure(bg="red")

e = Entry(calc, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=50, pady=10)

tell = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
tell.setProperty('voice', voice_id)
tell.setProperty('rate', 150)
tell.setProperty('volume', 1)


def add(n):
    first = e.get()
    e.delete(0, END)
    e.insert(0, first + n)


def clear():
    e.delete(0, END)


def equal():

    global ans

    ans = eval(e.get())
    e.delete(0, END)
    e.insert(0, ans)

    tell.say(ans)
    tell.runAndWait()


b1 = Button(calc, text="1", bg="black", fg="white", padx=40, pady=20, command=lambda: add("1")).grid(row=3, column=0)
b2 = Button(calc, text="2", bg="black", fg="white", padx=40, pady=20, command=lambda: add("2")).grid(row=3, column=1)
b3 = Button(calc, text="3", bg="black", fg="white", padx=40, pady=20, command=lambda: add("3")).grid(row=3, column=2)
b4 = Button(calc, text="4", bg="black", fg="white", padx=40, pady=20, command=lambda: add("4")).grid(row=2, column=0)
b5 = Button(calc, text="5", bg="black", fg="white", padx=40, pady=20, command=lambda: add("5")).grid(row=2, column=1)
b6 = Button(calc, text="6", bg="black", fg="white", padx=40, pady=20, command=lambda: add("6")).grid(row=2, column=2)
b7 = Button(calc, text="7", bg="black", fg="white", padx=40, pady=20, command=lambda: add("7")).grid(row=1, column=0)
b8 = Button(calc, text="8", bg="black", fg="white", padx=40, pady=20, command=lambda: add("8")).grid(row=1, column=1)
b9 = Button(calc, text="9", bg="black", fg="white", padx=40, pady=20, command=lambda: add("9")).grid(row=1, column=2)
b0 = Button(calc, text="0", bg="black", fg="white", padx=40, pady=20, command=lambda: add("0")).grid(row=4, column=0)
bdot = Button(calc, text=".", bg="black", fg="white", padx=40, pady=20, command=lambda: add(".")).grid(row=4, column=1)
badd = Button(calc, text="+", bg="grey", fg="black", padx=40, pady=20, command=lambda: add("+")).grid(row=4, column=3)
bsub = Button(calc, text="-", bg="grey", fg="black", padx=40, pady=20, command=lambda: add("-")).grid(row=3, column=3)
bmul = Button(calc, text="*", bg="grey", fg="black", padx=40, pady=20, command=lambda: add("*")).grid(row=2, column=3)
bdiv = Button(calc, text="/", bg="grey", fg="black", padx=40, pady=20, command=lambda: add("/")).grid(row=1, column=3)
bmod = Button(calc, text="%", bg="black", fg="white", padx=40, pady=20, command=lambda: add("%")).grid(row=4, column=2)
bclear = Button(calc, text="Clear", bg="grey", fg="black", padx=79, pady=20, command=clear).grid(row=5, column=0, columnspan=2)
beq = Button(calc, text="=", bg="grey", fg="black", padx=92, pady=20, command=equal).grid(row=5, column=2, columnspan=2)



calc.mainloop()
