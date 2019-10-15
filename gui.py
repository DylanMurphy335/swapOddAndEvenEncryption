from tkinter import *
from Switch import encrypt_input
window = Tk()

def encrypt():
    text = encrypt_input(txt1.get())
    txt1.delete(0, "end")
    txt1.insert(0, str(text))

v = ""
window.title("SwapEncryptor")
lbl1 = Label(window, text="Enter text")
txt1 = Entry(window, width=30, textvariable=v)
btn1 = Button(window, text="Encrypt/Decrypt", command=encrypt)
lbl1.grid(column=1, row=1)
txt1.grid(column=1, row=2)
btn1.grid(column=1, row=3)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(4, weight=1)
window.geometry('350x200')
window.mainloop()

