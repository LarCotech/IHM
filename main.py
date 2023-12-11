import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("MyDinnerParty")
        self.geometry("380x500")

        # Initialisation header app
        self.header()
        # Initialisation corps 1 de l'application avec les infos du dinner
        self.core1_init()

        self.mainloop()

    def header(self):
        self.frame1 = tk.Frame(self, width=380, height=50, bg="#D9D9D9")
        self.frame1.pack_propagate(False)
        self.frame1.pack()

        self.lbF1 = tk.Label(self.frame1, text="MyDinnerParty", fg='black', bg="#D9D9D9")
        self.lbF1.pack(side='left', padx=10)

        self.btnF1 = tk.Button(self.frame1, text="BTN1", bg="#D9D9D9")
        self.btnF2 = tk.Button(self.frame1, text="BTN2")

        self.btnF1.pack(side='right', padx=20)
        self.btnF2.pack(side='right', padx=10)

    def core1_init(self):
        self.frameCore1 = tk.Frame(self, width=380, height=175, bg='#EAECEE')
        self.frameCore1.pack_propagate(False)
        self.frameCore1.pack()

        self.titleDinner = tk.Label(self.frameCore1, text="Anniversaire de Papy", fg='black', bg='#EAECEE')
        self.titleDinner.pack(pady=(15, 0))

        self.place = tk.Radiobutton(self.frameCore1, value="Tours", text="Tours", state="disabled", bg='#EAECEE')
        self.date = tk.Radiobutton(self.frameCore1, value="09/12/2023 : 12h30", text="09/12/2023 : 12h30", bg='#EAECEE')
        self.paiement = tk.Radiobutton(self.frameCore1, value="Chacun paie sa part", text="Chacun paie sa part", bg='#EAECEE')
        self.confirm = tk.Radiobutton(self.frameCore1, value="Nombre de confirmation : 10", text="Nombre de confirmation : 10", bg='#EAECEE')

        self.place.pack(anchor='w', padx=(20, 0), pady=(10, 0))
        self.date.pack(anchor='w', padx=(20, 0))
        self.paiement.pack(anchor='w', padx=(20, 0))
        self.confirm.pack(anchor='w', padx=(20, 0))

        self.update = tk.Button(self.frameCore1, text="Modifier")
        self.update.pack(anchor='e')


# Initialisation Application
app = Application()
