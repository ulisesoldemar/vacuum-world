from logging.config import valid_ident
from tkinter import Tk, Label, Button, Entry, Frame, ttk, StringVar, END
from agent import Agent
from environtment import Environment
from evaluator import Evaluator
from random import randint
from time import sleep



window = Tk()
window.config(bg='black')
window.geometry('640x360')
window.resizable(False, False)
window.title('Vacuum World')


def number_validation(input: str) -> bool:
    if input in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        return True
    return False

env = None
def agregar_datos():
    global env
    r = int(rows_input.get())
    c = int(cols_input.get())
    try:
        env = Environment(r, c)
    except ValueError:
        return
        

def random_layout(rows_input: Entry, cols_input: Entry):
    rows_input.insert(0, str(randint(0, 10)))
    cols_input.insert(0, str(randint(0, 10)))

rows_label = Label(window, text='Filas', width=10).grid(
    column=0, row=0, pady=20, padx=10)

rows_input = Entry(window,  width=20, font=('Arial', 12))
rows_input.grid(column=1, row=0)

cols = Label(window, text='Columnas', width=10).grid(
    column=0, row=1, pady=20, padx=10)
cols_input = Entry(window, width=20, font=('Arial', 12))
cols_input.grid(column=1, row=1)

random_layout = Button(window, width=20, font=(
    'Arial', 12, 'bold'), text='Aleatorio', bg='orange', bd=5, command=random_layout(rows_input, cols_input))
random_layout.grid(columnspan=2, row=2, pady=20, padx=10)

run = Button(window, width=20, font=('Arial', 12, 'bold'),
             text='Ejecutar', bg='green2', bd=5)
run.grid(columnspan=2, row=5, pady=20, padx=10)
window.mainloop()
