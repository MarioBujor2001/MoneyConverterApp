from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Money Converter")
global api
try:
    api_request = requests.get("http://data.fixer.io/api/latest?access_key=b069f29b50c3e732d552a5fe21948c1c&format=1")
    api = json.loads(api_request.content)
except Exception as e:
    api = "error"


lei = StringVar()
euro = StringVar()
dolar = StringVar()
clicked = StringVar()
clicked.set('LEI')
options = [
    "LEI",
    "EURO",
    "DOLARI"
]


def clear_screen():
    entry_sum.delete(0, END)
    # entry_type.delete(0, END)
    but_conv_euro = Button(root, text="In Euro", padx=20, pady=20, command=conv_euro, state=ACTIVE)
    but_conv_euro.grid(row=4, column=0)
    but_conv_lei = Button(root, text="In Lei", padx=20, pady=20, command=conv_lei, state=ACTIVE)
    but_conv_lei.grid(row=4, column=1)
    but_conv_dolar = Button(root, text="In Dolar", padx=20, pady=20, command=conv_dolar, state=ACTIVE)
    but_conv_dolar.grid(row=4, column=2)

def conv_euro():
    value = float(entry_sum.get())
    entry_sum.delete(0, END)
    # tip_valuta = entry_type.get()
    tip_valuta = clicked.get()
    tip_valuta = tip_valuta.upper()
    if tip_valuta == "LEI":
        value = value / api['rates']['RON']
        entry_sum.insert(0, value)
    elif tip_valuta == "DOLARI":
        value = value * 0.82
        entry_sum.insert(0, value)
    elif tip_valuta == "EURO":
        but_conv_euro = Button(root, text="In Euro", padx=20, pady=20, command=conv_euro, state=DISABLED)
        but_conv_euro.grid(row=4, column=0)
        but_conv_lei = Button(root, text="In Lei", padx=20, pady=20, command=conv_lei, state=DISABLED)
        but_conv_lei.grid(row=4, column=1)
        but_conv_dolar = Button(root, text="In Dolar", padx=20, pady=20, command=conv_dolar, state=DISABLED)
        but_conv_dolar.grid(row=4, column=2)
        entry_sum.insert(0, "Nu se poate!")
    # entry_type.delete(0, END)
    clicked.set("EURO")


def conv_lei():
    value = float(entry_sum.get())
    entry_sum.delete(0, END)
    # tip_valuta = entry_type.get()
    tip_valuta = clicked.get()
    tip_valuta = tip_valuta.upper()
    if tip_valuta == "EURO":
        value = value * api['rates']['RON']
        entry_sum.insert(0, value)
    elif tip_valuta == "DOLARI":
        value = value / 0.24
        entry_sum.insert(0, value)
    elif tip_valuta == "LEI":
        but_conv_euro = Button(root, text="In Euro", padx=20, pady=20, command=conv_euro, state=DISABLED)
        but_conv_euro.grid(row=4, column=0)
        but_conv_lei = Button(root, text="In Lei", padx=20, pady=20, command=conv_lei, state=DISABLED)
        but_conv_lei.grid(row=4, column=1)
        but_conv_dolar = Button(root, text="In Dolar", padx=20, pady=20, command=conv_dolar, state=DISABLED)
        but_conv_dolar.grid(row=4, column=2)
        entry_sum.insert(0, "Nu se poate!")
    # entry_type.delete(0, END)
    clicked.set("LEI")


def conv_dolar():
    value = float(entry_sum.get())
    entry_sum.delete(0, END)
    # tip_valuta = entry_type.get()
    tip_valuta = clicked.get()
    tip_valuta = tip_valuta.upper()
    if tip_valuta == "LEI":
        value = value * 0.24
        entry_sum.insert(0, value)
    elif tip_valuta == "EURO":
        value = value / 0.82
        entry_sum.insert(0, value)
    elif tip_valuta == "DOLARI":
        but_conv_euro = Button(root, text="In Euro", padx=20, pady=20, command=conv_euro, state=DISABLED)
        but_conv_euro.grid(row=4, column=0)
        but_conv_lei = Button(root, text="In Lei", padx=20, pady=20, command=conv_lei, state=DISABLED)
        but_conv_lei.grid(row=4, column=1)
        but_conv_dolar = Button(root, text="In Dolar", padx=20, pady=20, command=conv_dolar, state=DISABLED)
        but_conv_dolar.grid(row=4, column=2)
        entry_sum.insert(0, "Nu se poate!")
    # entry_type.delete(0, END)
    clicked.set("DOLARI")


# entry_type = Entry(root, width=35, borderwidth=5)
entry_sum = Entry(root, width=35, borderwidth=5)
but_conv_euro = Button(root, text="In Euro", padx=20, pady=20, command=conv_euro)
but_conv_lei = Button(root, text="In Lei", padx=20, pady=20, command=conv_lei)
but_conv_dolar = Button(root, text="In Dolari", padx=20, pady=20, command=conv_dolar)
but_clear_screen = Button(root, text="Reinitializare", padx=20, pady=10, command=clear_screen)
drop = OptionMenu(root, clicked, *options)

entry_sum.grid(row=0, column=0, columnspan=3)
# entry_type.grid(row=2, column=0, columnspan=3)
drop.grid(row=2, column=0, columnspan=3)
Label(root, text="Suma introdusa este in: ").grid(row=1, column=0)
but_conv_euro.grid(row=4, column=0)
but_conv_lei.grid(row=4, column=1)
but_conv_dolar.grid(row=4, column=2)
but_clear_screen.grid(row=5, column=1)
Label(root, text="Doresc sa schimb: ").grid(row=3, column=0)

root.mainloop()