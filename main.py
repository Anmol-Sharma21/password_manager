from tkinter import *
from tkinter import messagebox
from random import *
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)
    password_ent.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_ent.get()
    email = user_ent.get()
    password = password_ent.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="error", message="you can't leave any field empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            website_ent.delete(0, END)
            password_ent.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_ent.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="error", message="no data file found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="website",
                                message=f" website: {website} \n email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="error", message=" no data saved ")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = Label(text="Username/Email:")
user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries

website_ent = Entry(width=21)
website_ent.grid(row=1, column=1)
website_ent.focus()

user_ent = Entry(width=35)
user_ent.grid(row=2, column=1, columnspan=2)
user_ent.insert(0, "xyz@gmail.com")

password_ent = Entry(width=21)
password_ent.grid(row=3, column=1)

# buttons
search_btn = Button(text="SEARCH", width=13, command=find_password)
search_btn.grid(row=1, column=2)
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
