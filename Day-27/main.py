from tkinter import *

window = Tk()
window.minsize(300,300)
window.title("GUI")
window.config(padx=20,pady=20)
# LABEL

my_label = Label(text = "This is a label", font=('Times New Roman',24,"bold"))
# my_label.pack()
my_label.grid(row = 0,column = 0 )
def got_clicked():
    print("clicked")
    my_label.config(text = "Got Clicked")
    print(my_entry.get())

# BUTTON

my_button = Button(text = "Click Me",command = got_clicked)
# my_button.pack()
my_button.grid(row = 1,column = 1)

new_button = Button(text = "Don't click")
new_button.grid(row = 0,column = 2)

# ENTRY

my_entry = Entry(width = 10)
# my_entry.pack()
my_entry.grid(row=2,column = 3)
my_entry.get()  # gets the entry put it in event listener like our button


window.mainloop()