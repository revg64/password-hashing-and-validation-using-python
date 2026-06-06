from tkinter import *
import bcrypt
# no actual password is visible here
def validate_func(password):
    hased=b'$2b$12$KLlqNMTn.Dy8EYshhatxS.9MbwDkC1Qj82ET/VCmTq9.vjJ9MoRse'
    password=bytes(password,encoding='utf-8')
    if bcrypt.checkpw(password,hased):   # return True or False
        print("Login succesfull")
    else:
        print("wrong password")


root=Tk()
root.geometry("300x300")

pass_entry=Entry(root)
pass_entry.pack()


button1=Button(text="validate",command=lambda: validate_func(pass_entry.get()))
button1.pack()

root.mainloop()