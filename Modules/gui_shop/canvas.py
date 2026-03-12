import tkinter as tk

def create_app():
    root = tk.Tk() #създава прозореца
    root.title("GUI Shop")
    root.geometry("700x600+150+150") # дължина, ширина, координати на х и у
    return root

app = create_app()