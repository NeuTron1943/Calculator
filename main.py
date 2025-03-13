from tkinter import *
from tkinter import ttk
from calculatorBusinessLogic import Add

root = Tk()
root.title("Calculator")
root.geometry("400x600+600+400")

mainFrame = ttk.Frame(root, padding=10, )
mainFrame.grid()

mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

a = StringVar(value="0")
aEntry = ttk.Entry(mainFrame, width=10, textvariable=a)
aEntry.grid(column=1, row=1, sticky=(S, E))

b = StringVar(value="0")
bEntry = ttk.Entry(mainFrame, width=10, textvariable=b)
bEntry.grid(column=3, row=1, sticky=(S, W))

result = StringVar()
ttk.Label(mainFrame, textvariable=result).grid(column=5, row=1, sticky=(S, E))

def calculate(*args, **kwargs):
    try:
        value = float(Add(a.get(), b.get()))
        result.set(value)
    except ValueError:
        pass
ttk.Button(mainFrame, text="Calculate", 
           command=calculate,
           ).grid(column=2, columnspan=3, row=2, sticky=(S))

ttk.Label(mainFrame, text="+").grid(column=2, row=1, sticky=(S))
ttk.Label(mainFrame, text="=").grid(column=4, row=1, sticky=(S))

for child in mainFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

aEntry.focus()
root.bind("<Return>", calculate)


l = ttk.Label(mainFrame, text="Testing")
l.grid(column=2, row=3)
l.bind('<Enter>', lambda e: l.configure(text="Moved mouse inside"))
l.bind('<Leave>', lambda e: l.configure(text="Moved mouse outside"))
l.bind('<ButtonPress-1>', lambda e: l.configure(text="Clicked left mouse"))
l.bind('<3>', lambda e: l.configure(text="Clicked right mouse"))
l.bind('<Double-1>', lambda e: l.configure(text="Double clicked"))
l.bind('<B3-Motion>', lambda e: l.configure(text=f'Right drag to ({e.x}, {e.y})'))

root.mainloop()