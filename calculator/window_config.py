from tkinter import PhotoImage

def configure_window(window):
	window.geometry("500x600") 
	window.title("Scientific Calculator.")
	window.config(background = "#63666A")
	icon = PhotoImage(file = "misc/logo.png")
	window.iconphoto(True, icon)