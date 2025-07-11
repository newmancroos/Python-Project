from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)


    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += str(char)

    # print(f"Your password is: {password}")
    password_text.insert(0, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_text.get()
    username = username_text.get()
    password = password_text.get()

    error_message=""
    if len(website) == 0:
        error_message += "Website should not be empty\n"

    if len(username) == 0:
        error_message += "Username/Email should not be empty\n"

    if len(password)==0:
        error_message += "Password should not be empty\n"

    # messagebox.showinfo(title="", message="")

    if  len(error_message) != 0:
        messagebox.showerror(title="ERROR", message=error_message)
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email: {username}\n Password: {password}\nIs is ok to save?")

        if is_ok:
            with  open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
                website_text.delete(0,END)
                password_text.delete(0, END)
                website_text.focus()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_text = Entry(width=35)
website_text.grid(row=1, column=1, columnspan=2, sticky="EW")
website_text.focus()

username_text = Entry(width=35)
username_text.grid(row=2, column=1, columnspan=2, sticky="EW")
username_text.insert(0, "newmancroos@email.com")
password_text = Entry(width=21)
password_text.grid(row=3, column=1, sticky="EW")

password_button= Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

add_button= Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()