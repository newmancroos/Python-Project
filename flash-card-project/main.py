from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

to_learn={}
current_card={}
try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  #if continusly clikc the next button we need to cancel previousl;y started window.after

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400, 263,image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title=canvas.create_text(400, 150,text="Title", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(400,263, text="word",font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
unknown_button = Button(image=check_image, highlightthickness=0, command=is_known)
unknown_button.grid(row=1, column=1)

next_card()
window.mainloop()

