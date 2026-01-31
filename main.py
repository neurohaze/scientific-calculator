from tkinter import Tk
from calculator.window_config import configure_window
from calculator.display import create_display
from calculator.buttons import create_buttons

def main():
	window = Tk()
	configure_window(window)
	equation_var = create_display(window)
	create_buttons(window, equation_var)

	window.mainloop()

if __name__ == "__main__":
	main()