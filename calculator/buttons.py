from tkinter import Button, Frame
from calculator.utils import append, clear, compute, delete, apply_function
import math

BUTTONS = [
    ["sin", "cos", "tan", "√", "∛","()"],
    ["sin⁻¹", "cos⁻¹", "tan⁻¹", "π","DEL", "AC"],
    ["ln", "log", "7", "8", "9", "/"],
    ["eˣ", "1/x", "4", "5", "6", "*"],
    ["x²", "xʸ", "1", "2", "3", "-"],
    ["x³","e", "0", ".", "=", "+"]
    ]

def create_buttons(root_window, input_equation_var):
    frame = Frame(root_window)
    frame.pack()

    for row in BUTTONS:
        row_frame = Frame(frame)
        row_frame.pack()
        
        for label in row:
            if label == "AC":
                cmd = lambda ev = input_equation_var: clear(ev)
            elif label == "DEL":
                cmd = lambda ev = input_equation_var: delete(ev)
            elif label == "=":
                cmd = lambda ev = input_equation_var: compute(ev)
            else:
            	cmd = lambda val = label, ev= input_equation_var: append(val, ev)
                  
            Button(
                row_frame,
                text=label,
                width=5,
                height=2,
                command=cmd
                ).pack(side="left", padx=2, pady=2)