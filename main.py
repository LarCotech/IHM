import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("MyDinnerParty")
        self.geometry("320x500")

        # Initialisation header app
        self.header()
        # Initialisation corps 1 de l'application avec les infos du dinner
        self.core1_init()

        self.mainloop()

    def header(self):
        self.frame1 = tk.Frame(self, width=300, height=50)
        self.frame1.pack_propagate(False)
        self.frame1.pack()

        self.lbF1 = tk.Label(self.frame1, text="MyDinnerParty", fg='black')
        self.lbF1.pack(side='left')

        self.btnF1 = tk.Button(self.frame1, text="BTN1")
        self.btnF2 = tk.Button(self.frame1, text="BTN2")

        self.btnF1.pack(side='right')
        self.btnF2.pack(side='right')

    def core1_init(self):
        self.frameCore1 = tk.Frame(self)
        self.frameCore1.pack()

        self.titleDinner = tk.Label(self.frameCore1, text="Anniversaire de Papy", fg='black')
        self.titleDinner.pack()

        self.place = tk.Radiobutton(self.frameCore1, value="Tours")
        self.date = tk.Radiobutton(self.frameCore1, value="09/12/2023 : 12h30")
        self.paiement = tk.Radiobutton(self.frameCore1, value="Chacun paie sa part", text="Chacun paie sa part")
        self.confirm = tk.Radiobutton(self.frameCore1, value="Nombre de confirmation : 10", text="Nombre de confirmation : 10")

        self.place.pack()
        self.date.pack()
        self.paiement.pack()
        self.confirm.pack()


# Initialisation Application
app = Application()
