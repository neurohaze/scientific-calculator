from tkinter import *
from window import window

equation_text = ""
equation_label = StringVar()

display_label = Label(window, textvariable = equation_label, font = 'consolas', bg = "white", width = 24, height = 10)
display_label.pack()