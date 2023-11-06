from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter.messagebox import showinfo, showerror, showwarning


colors = [
	"red", "blue", "yellow", "green", "pink", "black", "purple"
]

def generate_color(mylabel):	
    global selected_color
    selected_color = random.randint(0, len(colors) - 1)
    mylabel["bg"] = colors[selected_color]

def MH_COLORS():
    def check_answer():
        user_answer = answer.get().lower()
        if user_answer == colors[selected_color]:
            showinfo(title="EXACTLY", message="WOW! GOOD JOB!")
        else:
            showerror(title="WRONG", message="Oops! It's wrong! Try again")

    color_gui = Toplevel()
    color_gui.geometry("500x200")
    color_gui.title('COLORs')

    label_mau = Label(color_gui, text="                 ", bg='#FFE4B5')
    generate_color(label_mau)
    label_mau.grid(row=0, column=0,ipadx=50, ipady=20,padx=50, pady=20)

    answer = Entry(color_gui)
    answer.place(x=250, y=50)

    btnAnswer = Button(color_gui, text="Result", command=check_answer)
    btnAnswer.place(x=400, y=50)

    def next_color():
        generate_color(label_mau)
        answer.delete(0, END)  # Clear the answer entry
        answer.focus()

    next_color_button = Button(color_gui, text="Next Color", command=next_color)
    next_color_button.place(x=200, y=100)

    color_gui.mainloop()


 
    
    

