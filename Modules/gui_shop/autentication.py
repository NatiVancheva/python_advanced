import tkinter as tk
import json
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from Modules.gui_shop.products import render_products_screen
from canvas import app
from helpers import clean_screen


def login(username, password):
    with open("db/user_credentials_db.txt") as f:
        for line in f:
            user, pwd = line.strip().split(", ")
            if user == username and pwd == password:
                with open("db/current_user.txt", "w") as file:
                    file.write(username)
                render_products_screen()
                return

    render_login_screen(error="Invalid username/password")


def render_login_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)

    password = tk.Entry(app)
    password.grid(row=1, column=0)

    tk.Button(app, text="Enter", fg="black", bg="green", command=lambda: login(username.get(), password.get())).grid(row=2, column=0)

    if error:
        tk.Label(app, text=error, fg="red").grid(row=3, column=0)


def register(**user):
    if user["username"] == "" or user["password"] == "" or user["last_name"] == "" or user["first_name"] == "":
        render_register_screen(error="All fields are required!")
        return
    if user["username"] == user["password"]:
        render_register_screen(error="Username and password cannot be the same!")
        return
    if len(user["password"]) < 6:
        render_register_screen(error="Password must be at least 6 characters long!")
        return
    if len(user["username"]) < 2:
        render_register_screen(error="Username must be at least 2 characters long!")
        return
    pass_validation_map = {"upper": False, "lower": False, "digit": False, "specials": False}
    for char in user["password"]:
        if char in ascii_lowercase:
            pass_validation_map["lower"] = True
        elif char in ascii_uppercase:
            pass_validation_map["upper"] = True
        elif char in digits:
            pass_validation_map["digit"] = True
        elif char in punctuation:
            pass_validation_map["specials"] = True
    if not all(pass_validation_map.values()):
        render_register_screen(error="Password must contain at least one uppercase letter, one lowercase letter, one digit and one special character!")
        return
    if len(user["first_name"]) < 2 or len(user["last_name"]) < 2:
        render_register_screen(error="Fisrt and last name must be at least 2 characters long!")
        return

    user.update({"products": []})
    with open("db/user_credentials_db.txt", "r+") as file:
        users = [line.strip().split(", ")[0] for line in file]
        if user["username"] in users:
            render_register_screen(error="Username already exists")
            return
        file.write(f'{user["username"]}, {user["password"]}\n')

    with open("db/users.txt", "a") as f:
        f.write(json.dumps(user) + "\n")
    render_login_screen()

def render_register_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)

    password = tk.Entry(app)
    password.grid(row=1, column=0)

    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)

    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)

    tk.Button(app, text="Register", bg="green", fg="black", command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(), last_name=last_name.get())).grid(row=4, column=0)

    if error:
        tk.Label(app, text=error, fg="red").grid(row=5, column=0)

def render_main_enter_screen():
    clean_screen()

    tk.Button(app, text="Login", fg="white", bg="green", command=render_login_screen).grid(row=0, column=0)
    tk.Button(app, text="Register", fg="black", bg="yellow").grid(row=0, column=1, command=render_register_screen)