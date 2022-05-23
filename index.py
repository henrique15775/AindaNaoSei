"""
 O APP VAI SER UM BUSCA CEP COM Tkinter
"""
from enum import auto
from logging import root
from tkinter import *
from tkinter import ttk
from src.model.address import Address



window = Tk()
window.title("Busca Cep")
window.geometry("600x400")
window.configure(background="white")
window.resizable(width=False,height=False)


digiteCEPLabel = Label(window, text="Digite o CEP", bg="WHITE")
digiteCEPLabel.place(x=255,y=35)
CepEntry = Entry(window)

CepEntry.place(x=230,y=65)
textLog = Label(window, bg="WHITE")

checkIfUpdate = True

def buscarCep():
    cep = CepEntry.get()
    #endereco = Address(cep)
    endereco = Address(cep)
    print(endereco.localidadeUF)
    
button = ttk.Button(window, text='Buscar', command=buscarCep)
button.place(x=265,y=90)


resultsContents = StringVar()
textLog['textvariable'] = resultsContents
resultsContents.set('New value to display')



window.mainloop()
