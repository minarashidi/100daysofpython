from tkinter import *
from tkinter import messagebox
from password_generator_data import letters, numbers, symbols
from random import shuffle, randint, choice
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)
    password_list = []
    # for char in range(nr_letters):
    #     password_list += choice(letters)
    password_list += [choice(letters) for char in range(nr_letters)]
    password_list += [choice(numbers) for char in range(nr_numbers)]
    password_list += [choice(symbols) for char in range(nr_symbols)]

    shuffle(password_list)
    # for char in password_list:
    #     generated_password += char
    generated_password = "".join(password_list)
    pyperclip.copy(generated_password)
    password_entry.delete(0, END)
    password_entry.insert(END, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(message=f"Here are the details entered: \n "
                                               f"Website: {website}\n "
                                               f"Email: {email}\n "
                                               f"Password: {password}\n "
                                               f"Do you want to save the data?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website Label
website_label = Label(text="Website:", font=(FONT_NAME, 15, "bold"))
website_label.grid(row=1, column=0)

# Website Entry
website_entry = Entry(width=38)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email Label
email_label = Label(text="Email/Username:", font=(FONT_NAME, 15, "bold"))
email_label.grid(row=2, column=0)

# Email Entry
email_entry = Entry(width=38)
email_entry.insert(END, string="mina.rashidi.86@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password Label
password_label = Label(text="Password:", font=(FONT_NAME, 15, "bold"))
password_label.grid(row=3, column=0)

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
