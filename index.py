"""
 O APP VAI SER UM BUSCA CEP COM Tkinter
"""
from enum import auto
from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from requests import delete
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
textLog
checkIfUpdate = True

def buscarCep():
    cep = CepEntry.get()
    endereco = Address(cep)
    resultsContents = StringVar()
    textLog['textvariable'] = resultsContents
    if(endereco):
        resultsContents.set(f"""
                            Logradouro -> {endereco.logradouro}
                            Bairro -> {endereco.bairro}
                            Cidade/UF -> {endereco.localidadeUF}
                            CEP -> {endereco.CEP}
                            """)
    del(endereco)
    del(resultsContents)


button = ttk.Button(window, text='Buscar', command=buscarCep)
button.place(x=255,y=90)

textLog.place(x=100,y=130)



window.mainloop()
