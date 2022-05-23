"""
 O APP VAI SER UM BUSCA CEP COM Tkinter
"""
from enum import auto
from logging import root
from tkinter import *
from tkinter import ttk
from src.model import address
window = Tk()

window.title("Busca Cep")
window.geometry("600x400")
window.configure(background="white")
window.resizable(width=False,height=False)
#window = Frame(window, bg="WHITE")
#window.grid(column=0, row=0)
digiteCEPLabel = Label(window, text="Digite o CEP", bg="WHITE")
digiteCEPLabel.place(x=255,y=35)
logradouroEntry = Entry(window)
#logradouroEntry.grid(column=2,row=2)
logradouroEntry.place(x=230,y=65)
textLog = Label(window, bg="WHITE")



resultsContents = StringVar()
textLog['textvariable'] = resultsContents
resultsContents.set('New value to display')
#textLog.insert('1.0', 'here is my\ntext to insert')
#textLog.grid(column=2,row=3)
window.mainloop()
