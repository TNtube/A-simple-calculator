from tkinter import *

screen = Tk()

calc = StringVar(screen)
calc.set("")

show = Frame(screen)

entry = Entry(show, textvariable=calc, width="19")
entry.grid(column=0, row=0)

ac = Button(show, text='AC', width=4, height=2, command=lambda: calc.set(""))
ac.grid(column=1, row=0)

show.pack()

buttons = Frame(screen)

tab = ["789/",
       "456*",
       "123+",
       "0.=-"]

for i, line in enumerate(tab):
    for j, case in enumerate(line):
        if case == "=":
            a = lambda x=case: calc.set(eval(calc.get()))
        else:
            a = lambda x=case: calc.set(calc.get() + x)
        Button(buttons, text=case, width=4, height=2, command=a).grid(column=j, row=i)

buttons.pack()

screen.mainloop()
