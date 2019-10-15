from tkinter import *
from Switch import encrypt_input, decrypt_input
window = Tk()

def encrypt():
    text = encrypt_input(txt1.get())
    txt2.delete(0, "end")
    txt2.insert(0, str(text))

def decrypt():
    text = decrypt_input(txt2.get())
    txt1.delete(0, "end")
    txt1.insert(0, str(text))
v = ""
window.title("SwapEncryptor")
lbl1 = Label(window, text="Plain text")
lbl2 = Label(window, text="Encrypted text")
txt1 = Entry(window, width=10, textvariable=v)
txt2 = Entry(window, width=10, textvariable=v)
btn1 = Button(window, text="Encrypt", command=encrypt)
btn2 = Button(window, text="decrypt", command=decrypt)
lbl1.grid(column=0, row=0)
txt1.grid(column=0, row=1)
btn1.grid(column=0, row=2)
lbl2.grid(column=1, row=0)
txt2.grid(column=1, row=1)
btn2.grid(column=1, row=2)
window.geometry('350x200')
window.mainloop()

