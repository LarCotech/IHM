import tkinter as tk
from tkinter import ttk

# defining main window
rootWindow = tk.Tk()
rootWindow.geometry("300x500")
rootWindow.title("MyDinnerParty")
rootWindow.resizable(False, False)

#define header
header = tk.Frame(rootWindow, bg="#D9D9D9", width="300", height="50")
header.pack_propagate(False)
header.pack(side="top", fill="both", expand=True)

#define body
body = tk.Frame(rootWindow, bg="#FFFFFF", width="300", height="450")
body.pack_propagate(False)
body.pack(fill="y", expand=True)

#define footer
footer = tk.Frame(rootWindow, bg="#D9D9D9", width="300", height="50")
footer.pack_propagate(False)
footer.pack(side="bottom", fill="both", expand=True)

# --------header--------
# title MyDinnerParty
title = tk.Label(header, text="MyDinnerParty", bg="white")
title.pack(side='left', fill='both', expand=False, padx=(14, 20), pady=(5, 5))

# button for profile page
buttonProfile = tk.Button(header, text="setting", bg="#2C3E50", fg="white")
buttonProfile.pack(side='right', fill='both', expand=True, padx=(0, 14), pady=(5, 5))

# button for settings page
buttonSettings = tk.Button(header, text="profile", bg="#2C3E50", fg="white")
buttonSettings.pack(side='right', fill='both', expand=True, padx=(0, 14), pady=(5, 5))

# --------body--------

# button to filter only repas you organized
buttonMyRepas = tk.Button(body, text="Mes repas", bg="#2C3E50", fg="white")
buttonMyRepas.pack(fill='both', expand=False, padx=(14, 14), pady=(5, 5))

# button to filter only repas you were invited
buttonMyRepas = tk.Button(body, text="Mes invitations", bg="#2C3E50", fg="white")
buttonMyRepas.pack(fill='both', expand=False, padx=(14, 14), pady=(5, 5))

# treeview for all repas
table = tk.ttk.Treeview(body, columns=['repas', 'hote', 'location', 'type'])
table.heading('repas', text='repas')
table.heading('hote', text='hote')
table.heading('location', text='location')
table.heading('type', text='type')
table.column('repas', width="72")
table.column('hote', width="72")
table.column('location', width="72")
table.column('type', width="72")
table.pack(fill='both', expand=True, padx=(5, 5))
table['show'] = 'headings'
table.insert('', 'end', values=('repas #1', 'moi', 'chez moi', 'Continental'))
table.insert('', 'end', values=('repas #2', 'Jane Smith', 'Salle à manger', 'Cuisine locale'))
table.insert('', 'end', values=('repas #3', 'moi', 'restaurant', 'Gastronomique'))


# button to add repas
buttonAddRepas = tk.Button(body, text="Add", bg="#2C3E50", fg="white")
buttonAddRepas.pack(fill='both', expand=False, padx=(14, 14), pady=(5, 5))

# button to delete repas
buttonDeleteRepas = tk.Button(body, text="Delete", bg="#2C3E50", fg="white")
buttonDeleteRepas.pack(fill='both', expand=False, padx=(14, 14), pady=(5, 5))

rootWindow.mainloop()

print("loop finished!")
