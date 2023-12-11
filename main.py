import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("MyDinnerParty")
        self.geometry("300x500")

        # Initialisation header app
        self.header()
        # Initialisation corps 1 de l'application avec les infos du dinner
        self.core1_init()
        # Message Part
        self.coreMessage_init()
        # Footer
        self.footer()
        # Show APP
        self.mainloop()

    def header(self):
        self.frame1 = tk.Frame(self, width=300, height=50, bg="#D9D9D9")
        self.frame1.pack_propagate(False)
        self.frame1.pack()

        self.lbF1 = tk.Label(self.frame1, text="MyDinnerParty", fg='black', bg="#D9D9D9")
        self.lbF1.pack(side='left', padx=10)

        self.btnF1 = tk.Button(self.frame1, text="BTN1", bg="#D9D9D9")
        self.btnF2 = tk.Button(self.frame1, text="BTN2")

        self.btnF1.pack(side='right', padx=20)
        self.btnF2.pack(side='right', padx=10)

    def footer(self):
        self.frameFooter = tk.Frame(self, width=300, height=50, bg="#D9D9D9")
        self.frameFooter.pack_propagate(False)
        self.frameFooter.pack(side='bottom')

    def core1_init(self):
        self.frameCore1 = tk.Frame(self, width=300, height=175, bg='#EAECEE')
        self.frameCore1.pack_propagate(False)
        self.frameCore1.pack()

        self.titleDinner = tk.Label(self.frameCore1, text="Anniversaire de Papy", fg='black', bg='#EAECEE')
        self.titleDinner.pack(pady=(15, 0))

        # String Var
        self.placeVar = tk.StringVar(self.frameCore1, "Tours")
        self.dateVar = tk.StringVar(self.frameCore1, "09/12/2023 : 12h30")
        self.paiementVar = tk.StringVar(self.frameCore1, "Chacun paie sa part")
        self.confirmVar = tk.StringVar(self.frameCore1, "Nombre de confirmation : 10")

        self.placeLabel = tk.Label(self.frameCore1, textvariable=self.placeVar, fg='black', bg='#EAECEE')
        self.dateLabel = tk.Label(self.frameCore1, textvariable=self.dateVar, fg='black', bg='#EAECEE')
        self.paiementLabel = tk.Label(self.frameCore1, textvariable=self.paiementVar, fg='black', bg='#EAECEE')
        self.confirmLabel = tk.Label(self.frameCore1, textvariable=self.confirmVar, fg='black', bg='#EAECEE')

        self.placeLabel.pack(anchor='w', padx=(20, 0), pady=(10, 0))
        self.dateLabel.pack(anchor='w', padx=(20, 0))
        self.paiementLabel.pack(anchor='w', padx=(20, 0))
        self.confirmLabel.pack(anchor='w', padx=(20, 0))

        self.update = tk.Button(self.frameCore1, text="Modifier", width=10, height=20, command=self.update_value)
        self.update.pack(anchor='se', padx=(0, 15), pady=(0, 5))

    def coreMessage_init(self):
        self.frameCore2 = tk.Frame(self, width=300, height=225)
        self.frameCore2.pack_propagate(False)
        self.frameCore2.pack(pady=20)

        self.frameCoreInvite = tk.Frame(self.frameCore2, width=100, height=225, bg='#2C3E50')
        self.frameCoreInvite.pack_propagate(False)
        self.frameCoreInvite.pack(side='left')

        self.frameCoreMessage = tk.Frame(self.frameCore2, width=200, height=225, bg='#EAECEE')
        self.frameCoreMessage.pack_propagate(False)
        self.frameCoreMessage.pack(side='top')

        # Invité
        self.inv1 = tk.Label(self.frameCoreInvite, text="Inv1\nInv2\nInv3", fg='black', bg="#D9D9D9")

        self.inv1.pack(anchor='n', padx=5, pady=5)

        self.btnAdd = tk.Button(self.frameCoreInvite, text="Ajouter", bg="#D9D9D9")
        self.btnAdd.pack(side='bottom', pady=5)

        # Message
        self.messagEntry = tk.Entry(self.frameCoreMessage)
        self.messagEntry.insert(0, "Envoyer un message")
        self.messagEntry.pack(side='bottom', pady=5)

    def update_value(self):
        newWindow = UpdateValue(self)


class UpdateValue:

    def __init__(self, app):
        self.app = app
        self.updateValueWindow = tk.Toplevel(app)

        self.lieuLabel = tk.Label(self.updateValueWindow, text="Lieu : ")
        self.lieuEntry = tk.Entry(self.updateValueWindow)

        self.dateLabel = tk.Label(self.updateValueWindow, text="Date : ")
        self.dateEntry = tk.Entry(self.updateValueWindow)

        self.paiementLabel = tk.Label(self.updateValueWindow, text="Comment payer ?")
        self.paiementEntry = tk.Entry(self.updateValueWindow)

        self.lieuLabel.pack(padx=10, pady=(20, 0))
        self.lieuEntry.pack(padx=10)
        self.dateLabel.pack(padx=10)
        self.dateEntry.pack(padx=10)
        self.paiementLabel.pack(padx=10)
        self.paiementEntry.pack(padx=10)

        self.submitBtn = tk.Button(self.updateValueWindow, text="Submit", command=self.submit)
        self.submitBtn.pack(side='left', padx=10, pady=(10, 20))

        self.cancel = tk.Button(self.updateValueWindow, text="Cancel", command=self.updateValueWindow.destroy)
        self.cancel.pack(side='right', padx=10, pady=(10, 20))

    def submit(self):
        # Set les nouvelles valeurs
        if self.lieuEntry.get() != '':
            self.app.placeVar.set(self.lieuEntry.get())

        if self.dateEntry.get() != '':
            self.app.dateVar.set(self.dateEntry.get())

        if self.paiementEntry.get() != '':
            self.app.paiementVar.set(self.paiementEntry.get())

        # Supp top level page
        self.updateValueWindow.destroy()


# Initialisation Application
if __name__ == '__main__':
    app = Application()
