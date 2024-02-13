from tkinter import *
from tkinter import messagebox
from random import randint , choice , shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def add_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list +symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    Entry3.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    try:
        with open("data.json", "r") as file:
            file_data = json.load(file)
    except :
        messagebox.showinfo(title = "Error",message = "No file exista in current format")
    else:
        website_name = Entry1.get()
        if website_name in file_data:
            messagebox.showinfo(title = "Confidential",message = f"Email:{file_data[website_name]['email']} \n Password:{file_data[website_name]['password']}")
        else:
            messagebox.showinfo(title = "WebsiteNotFoundError",message = "Website has not been added yet")
def save():
    website = Entry1.get()
    email = Entry2.get()
    password = Entry3.get()
    new_data = {
        website:{
            'email': email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Error",message = "Need valid Inputs")

    else:
        is_okay = messagebox.askokcancel(title = "Confirmation" , message = f"These are your inputs ;\n Email : {email}\n"
                                                                            f"Website : {website}\nPassword  : {password}\n"
                                                                            f"Are you Sure")


        if is_okay:
            try:
                with open("data.json","r") as file:
                    f_data = json.load(file)

            except :
                with open("data.json","w")as file:
                    json.dump(new_data,file,indent=4)
            else:
                f_data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(f_data, file, indent=4)

            finally:
                Entry1.delete(0, "end")
                Entry3.delete(0,"end")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window .title("Password Manager")
window.config(padx=50,pady = 50)

canva = Canvas(height = 200 , width = 200)
lock = PhotoImage(file = "logo.png")
canva.create_image(100,100,image = lock)
canva.grid(row =0,column = 1)

Label1 = Label(text = "Website")
Label1.grid(row = 1,column = 0 )

Label2 = Label(text = "Email/Username")
Label2.grid(row = 2,column = 0 )

Label3 = Label(text = "Password")
Label3.grid(row = 3,column = 0 )



Entry1 = Entry(width = 38)
Entry1.grid(row = 1 , column = 1 , columnspan = 2)
Entry1.focus()

Entry2 = Entry(width = 38)
Entry2.grid(row = 2 , column = 1 , columnspan = 2)
Entry2.insert(0,"sushantsudan3075@gmail.com")

Entry3 = Entry(width = 19)
Entry3.grid(row = 3 , column = 1 )


Button1 = Button(text = "Generate Password", command = add_password,width = 15)
Button1.grid(row = 3 , column = 2)

Button2 = Button(text = "Add" , width = 30 , command = save)
Button2.grid(row = 4 , column = 1 , columnspan = 2)

Button3 = Button(text = "Search" , width =15,command = search)
Button3.grid(row = 1 , column = 2)

window.mainloop()

