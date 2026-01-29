from tkinter import *
import computation as comp
import functions as funcs


#Window Configurations
window = Tk()
window.geometry("500x600")
window.title("Scientific Calculator")
icon = PhotoImage(file = "../misc/logo.png")
window.config(background = "#63666A")
window.iconphoto(True, icon)

#Run the Window
window.mainloop()