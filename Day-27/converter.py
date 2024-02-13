from tkinter import *

window = Tk()
window.minsize(200,200)
window.config(padx = 20,pady = 20)

Miles_entry = Entry(width = 10)
Miles_entry.grid(row = 0,column = 1)

label1 = Label(text = 'in km is')
label1.grid(row = 1 , column = 0)

label2 = Label(text = "km")
label2.grid(row = 1,column = 2)

label3 = Label(text = "Miles")
label3.grid(row = 0 , column = 2)

label4 = Label (text = 0)
label4.grid(row = 1 , column =1)

def convert():
    km_entry = round(int(Miles_entry.get()) * 1.6092,2)
    label4.config(text = km_entry)

converter = Button(text = "Convert", command = convert)
converter.grid(row =2 ,column = 1)

window.mainloop()