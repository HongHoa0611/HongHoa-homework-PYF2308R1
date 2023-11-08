from tkinter import *
from tkinter import ttk

def man_hinh_dang_nhap(main_ui):
    login_ui = Toplevel(main_ui)
    login_ui.title("LOGIN")
    login_ui.geometry("320x160")

    Label(login_ui, text= "HELLO BABY", fg="#528B8B", font="Arial 16").place(x=100, y=10)
    Label(login_ui, text="YOUR NAME:").place(x=20, y=50)
    Entry(login_ui).place(x=115, y=50)

    #Label(login_ui, text="Email:").place(x=30, y=90)
    #Entry(login_ui).place(x=100, y=90)

    Label(login_ui, text="OUR HOUSE NO.:").place(x=20, y=90)
    Entry(login_ui).place(x=115, y=90)

    Button(login_ui, text="Login", command=lambda: login_ui.withdraw()).place(x=130, y=120)
    
    login_ui.mainloop()