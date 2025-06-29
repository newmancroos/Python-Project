import tkinter
from os.path import commonpath
from tkinter import Tk, Entry, Button, Label, Text, END, Spinbox, Scale, IntVar, Checkbutton, Radiobutton, Listbox

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

#Components
#----------
#Label

my_label = Label(text="This is my First Label", font=("Arial",24, "bold"))
my_label.pack()


def button_click():
    # my_label["text"]=input.get()
    my_label.config(text=input.get())
    print("I got click")

my_button = Button(text="test",fg="red", bg="green")
my_button.pack()
my_button["text"]="Updated Text"
my_button.config(text="Another updated text",fg="blue", command=button_click)


#Entry (Input

input =Entry(width=20)
input.insert(END, string="Email")
input.pack()

textbox = Text(height=5, width=30)
textbox.focus()
textbox.insert(END, "Newman")
print(textbox.get("1.0", END))
textbox.pack()

def spinboc_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinboc_used)
spinbox.pack()

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=10, command=scale_used)
scale.pack()


def check_used():
    print(check_state.get())

check_state = IntVar()
check_button = Checkbutton(text="Is ON", variable=check_state, command=check_used)
check_button.pack()

def radio_use():
    print(radio_state.get())

radio_state = IntVar()
radio_button = Radiobutton(text="Option1",value=1,  variable=radio_state, command=radio_use)
radio_button1 = Radiobutton(text="Option2", value=2,  variable=radio_state, command=radio_use)
radio_button.pack()
radio_button1.pack()

def list_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for fruit in fruits:
    listbox.insert(fruit.index(fruit),fruit)
listbox.bind("<<ListboxSelect>>",  list_used)

listbox.pack()


window.mainloop()


#----------------------
import tkinter
from os.path import commonpath
from tkinter import Tk, Entry, Button, Label, Text, END, Spinbox, Scale, IntVar, Checkbutton, Radiobutton, Listbox

#Components
#----------
def button_click():
    # my_label["text"]=input.get()
    # my_label.config(text=input.get())
    print("I got click")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=100, pady=120)
#Label
my_label = Label(text="I am a Label", font=("Arial",18))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=30)

my_button = Button(text="Click Me",command=button_click)
# my_button["text"]="Updated Text"
my_button.grid(column=1, row=1)
# my_button.pack(side="left")

my_button = Button(text="New Button")
# my_button["text"]="New Button"
my_button.grid(column=2, row=0)
# my_button.pack(side="left")

#Entry (Input
input =Entry(width=20)
# input.insert(END, string="Email")
# input.pack(side="left")
input.grid(column=3, row=2)

window.mainloop()