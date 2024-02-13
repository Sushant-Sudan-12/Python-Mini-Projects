from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
REPS = 0
MARK = ""
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(TIMER)
    label1.config(text = "Timer")
    label2.config(text = "")
    canva.itemconfig(timer_text , text = "00:00")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def add_mark():
    global MARK
    MARK += "✔"
    label2.config(text = MARK )


def start_timer():
    global REPS
    REPS+=1
    long_break = LONG_BREAK_MIN* 60
    short_break = SHORT_BREAK_MIN* 60
    work_min = WORK_MIN* 60


    if REPS %8 == 0:
        count_down(long_break)
        label1.config(text = "Break",fg = RED,bg = YELLOW)
        add_mark()
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)




    elif REPS % 2 == 0:
        count_down(short_break)
        label1.config(text="Break",fg = PINK,bg = YELLOW)
        add_mark()
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)


    else :
        count_down(work_min)
        label1.config(text="Work",fg = GREEN,bg = YELLOW)
        window.attributes("-topmost",1)
        window.attributes("-topmost", 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min_c = math.floor(count/60)
    sec_c = count%60
    if sec_c < 10 :
        sec_c = f"0{sec_c}"

    canva.itemconfig(timer_text , text=f"{min_c}:{sec_c}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000,count_down,count-1)
    elif REPS< 8:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.minsize(height = 500,width = 500)
window.config(padx = 100 , pady = 50 , bg = YELLOW)



canva = Canvas(width = 200 , height = 224 , bg = YELLOW ,  highlightthickness=0)
tomato = PhotoImage(file = "tomato.png")
canva.create_image(100,112,image = tomato)
timer_text = canva.create_text(100,130,text = "00:00",fill = "white",font = (FONT_NAME,30,"bold"))
canva.grid(row =1,column = 1)

start = Button(text = "Start", command = start_timer )
start.grid(row = 2,column = 0)

reset = Button(text = "Reset", command = reset_timer)
reset.grid(row = 2, column = 2)

label1 = Label(text = "Timer",fg = GREEN,bg = YELLOW, font = (FONT_NAME,50,"normal"))
label1.grid(row = 0 , column = 1)

label2 = Label(fg = GREEN , bg =  YELLOW)
label2.grid(row = 3 ,column = 1)

window.mainloop()

