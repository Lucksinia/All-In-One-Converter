import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window("Converter", "darkly")

# Functionality TODO


def temp_text(events):
    # This is the question
    input_c.delete(0, END)
    print(events)


def convert(events):
    try:
        c = numbers_c.get()
        f = numbers_f.get()
        k = numbers_k.get()
        print(events)
        print(c, k, f)
    except:
        assert TypeError


# Variables
numbers_c = ttk.IntVar()
numbers_f = ttk.IntVar()
numbers_k = ttk.IntVar()

# Main layout
frame = ttk.Frame(master=root)
input_c = ttk.Entry(master=frame, bootstyle=PRIMARY, textvariable=numbers_c)
input_f = ttk.Entry(master=frame, bootstyle=PRIMARY, textvariable=numbers_f)
input_k = ttk.Entry(master=frame, bootstyle=PRIMARY, textvariable=numbers_k)
input_c.pack(padx=5, pady=5)
input_f.pack(after=input_c, padx=5, pady=5)
input_k.pack(after=input_f, padx=5, pady=5)
frame.pack(pady=10)

# Bindings

input_c.bind("<FocusIn>", temp_text)
input_f.bind("<FocusIn>", temp_text)
input_k.bind("<FocusIn>", temp_text)
input_c.bind_all("<Return>", convert)

root.mainloop()
