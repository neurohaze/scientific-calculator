from tkinter import PhotoImage

def configure_window(root_window):
	# Making universal dimension. Ignore for now.
	# screen_width = root_window.winfo_screenwidth()
	# screen_height = root_window.winfo_screenheight()
	# width = int(round(screen_width*0.26, -1))
	# height = int(round(screen_height*0.50, -1))
	# root_window.geometry(f"{width}x{height}")

	root_window.geometry("500x730")
	root_window.resizable(False, False)
	
	root_window.title("Scientific Calculator")
	root_window.config(background = "black")
	icon = PhotoImage(file = "misc/logo.png")
	root_window.iconphoto(True, icon)