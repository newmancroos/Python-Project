
# from tkinter import Tk, Entry, Button, Label, Text, END, Spinbox, Scale, IntVar, Checkbutton, Radiobutton, Listbox
from tkinter import *
#Components
#----------
def button_click():
    miles_input = input.get()
    km_answer = round(float(miles_input) * 1.60934, 2)
    my_label_km["text"]=str(km_answer)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=120)
window.config(padx=20, pady=20)

input =Entry(width=8)
input.grid(column=1, row=0)

#Label
my_label_mile = Label(text="Miles", font=("Arial",18))
my_label_mile.grid(column=2, row=0)
# my_label_mile.config(padx=50, pady=50)

#Label
my_label_equal = Label(text="is equal to", font=("Arial",18))
my_label_equal.grid(column=0, row=1)
# my_label_equal.config(padx=5, pady=5)

#Label
my_label_km = Label(text="0", font=("Arial",18))
my_label_km.grid(column=1, row=1)
# my_label_km.config(padx=5, pady=5)

#Label
my_label_k = Label(text="Km", font=("Arial",18))
my_label_k.grid(column=2, row=1)
# my_label_km.config(padx=5, pady=5)


my_button = Button(text="Calculate",command=button_click)
my_button.grid(column=1, row=2)
# my_button.pack(side="left")


window.mainloop()