from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    websit_value = website_entry.get()
    email_value = username_entry.get()
    password_value = password_entry.get()
    messagebox.askokcancel(title=websit_value,
                           message=f"These are the details entered: \nEmail: {email_value}\nPassword: {password_value}\nIs it ok to save?")
    # messagebox.showinfo("Success", "Your data is saved.")

    with open("data.txt", 'a') as file:
        file.write(f"{websit_value} | {email_value} | {password_value}\n")
    website_entry.delete(0, END)
    # username_entry.delete(0, "end")
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=55)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END, "ivan78990@gmail.com")

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

# Buttons
genetate_button = Button(text="Generate Password")
genetate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()