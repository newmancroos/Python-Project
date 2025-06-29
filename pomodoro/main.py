import math
from idlelib.configdialog import font_sample_text
from lib2to3.pytree import convert
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #timer_text
    canvas.itemconfig(timer_text, text="00:00")
    #title_reset
    title_text.config(text="Timer", fg=GREEN)
    # reset check mark
    tik_label.config(text="")

    global  reps
    reps =0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60

    if reps % 8 ==0:
        title_text.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps %2 ==0:
        title_text.config(text="Break", fg=PINK)
        # If it's the 2dn/4th/6th/7th rep:
        count_down(short_break_sec)
    else:
        title_text.config(text="Work", fg=GREEN)
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_minutes =math.floor(count/60)
    count_second = count%60

    if int(count_second) <10:
         count_second =  f"0{count_second}"

    count_time = f"{count_minutes}:{count_second}"

    canvas.itemconfig(timer_text,text=count_time)
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +="✔"
        tik_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_text = Label()
title_text.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
# title_text.pack(side="top")
title_text.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img )
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

tik_label = Label(fg=GREEN)
tik_label.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()