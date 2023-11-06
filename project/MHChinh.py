from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MHDangNhap import man_hinh_dang_nhap
from MHColors import MH_COLORS
from tkinter.messagebox import showinfo, showerror, showwarning

root = Tk()
root.title('VOCABULARY STUDY')
root.geometry("500x500")
root.config(bg='#F2B33D')
frame = Frame(root,bg='#F2B33D')

Label(root, text="VOCABULARY STUDY", fg="black", font="Arial 16").place(x=150, y = 50)

#Button
Button(frame, text="COLORs", command= MH_COLORS).grid(row=0, column=0,ipadx=50, ipady=20,padx=50, pady=20)
Button(frame, text="ANIMALs").grid(row=0, column=1, ipadx=50, ipady=20,padx=20, pady=20)
Button(frame, text="FRUITs").grid(row=1, column=0, ipadx=50, ipady=20,padx=20, pady=20)
Button(frame, text="TRAVEL").grid(row=1, column=1, ipadx=50, ipady=20,padx=20, pady=20)

frame.pack(expand=True)


#menu bar
menu_bar = Menu(root)

root.config(menu=menu_bar)
menu_file = Menu(menu_bar, tearoff=False)

def open_game_window():
    from BallGame import MHGame
    game_window = Toplevel()
    MHGame(game_window)



menu_file.add_command(label="LOG IN", command=lambda: man_hinh_dang_nhap(root))
menu_file.add_command(label="GAME", command = open_game_window) 
menu_file.add_separator()
menu_file.add_command(label="Exit")
menu_bar.add_cascade(label="Menu", menu=menu_file)

#mnu_export = Menu(menu_bar, tearoff=False)
#mnu_export.add_command(label="Export vocabulary list")
#menu_bar.add_cascade(label="Export", menu=mnu_export)



root.mainloop()