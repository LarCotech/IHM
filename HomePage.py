import tkinter as tk

rootWindow = tk.Tk()
rootWindow.geometry("300x500")
rootWindow.title("MyDinnerParty")
rootWindow.resizable(False, False)

header = tk.Frame(rootWindow, bg="#D9D9D9", width="300", height="50")
header.pack_propagate(False)
header.pack()

label1 = tk.Label(header, text="MyDinnerParty")
label1.pack(side='left', fill='both', expand=True, padx=(14, 20))

button1 = tk.Button(header, text="setting", bg="#2C3E50", fg="white")
button1.pack(side='right', fill='both', expand=True, padx=(0, 14))

button2 = tk.Button(header, text="profile", bg="#2C3E50", fg="white")
button2.pack(side='right', fill='both', expand=True,   padx=(0, 14))

rootWindow.mainloop()

print("loop finished!")
