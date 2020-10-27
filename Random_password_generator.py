# Python program to generate random password using Tkinter module
import random
from tkinter import *

# Function for calculation of password
def generate():

    # Clear the previous results
    entry.delete(0, END)

    # Get the length of passowrd
    length = click.get()

    poor = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    medium = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    strong = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""

    # if strength selected is poor
    if stren.get() == 1:
        for i in range(0, length):
            password = password + random.choice(poor)
        entry.insert(10, password)

    # if strength selected is medium
    elif stren.get() == 0:
        for i in range(0, length):
            password = password + random.choice(medium)
        entry.insert(10, password)

    # if strength selected is strong
    elif stren.get() == 3:
        for i in range(0, length):
            password = password + random.choice(strong)
        entry.insert(10, password)
    else:
        print("Please choose an option")

# Main

# GUI window
root = Tk()
stren = IntVar()
click = IntVar()
click.set(8)
root.geometry("330x100")

# Title of GUI window
root.title("Random Password Generator")

# Label for length of password
len_label = Label(root, text="Length")
len_label.grid(row=0, column=0, padx=5, pady=5, sticky='W')

# OptionMenu for length options
drop = OptionMenu(root, click, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20)
drop.config(bg='white', activebackground='white', relief=GROOVE)
drop.grid(row=0, column=1)

# Label for Strength
strength_label = Label(root, text="Strength")
strength_label.grid(row=1, column=0, padx=5, pady=5, sticky='W')

# Radio Buttons for deciding the strength of password
# Default strength is Medium
poor_radio = Radiobutton(root, text="Poor", variable=stren, value=1)
poor_radio.grid(row=1, column=1, sticky='W')
medium_radio = Radiobutton(root, text="Medium", variable=stren, value=0)
medium_radio.grid(row=1, column=2, sticky='W')
strong_radio = Radiobutton(root, text="Strong", variable=stren, value=3)
strong_radio.grid(row=1, column=3, sticky='W')

# Label and Entry to show password generated
password_label = Label(root, text="Password")
password_label.grid(row=2, column=0, padx=5, pady=5, sticky='W')
entry = Entry(root)
entry.grid(row=2, column=1, columnspan=3, sticky='W')

# Button which will generate the password
generate_button = Button(root, text="Generate", bg="blue", fg="white", relief=GROOVE, command=generate)
generate_button.grid(row=2, column=3, padx=5, sticky='W')

# start the GUI
root.mainloop()
