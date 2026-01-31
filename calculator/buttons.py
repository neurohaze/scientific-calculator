from tkinter import Button, Frame
from calculator.utils import append, clear, compute

BUTTONS = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

def create_buttons(window, equation_var):
    frame = Frame(window)
    frame.pack()

    for row in BUTTONS:
        row_frame = Frame(frame)
        row_frame.pack()
        

        for label in row:
            if label == "C":
                cmd = clear(equation_var)
            elif label == "=":
                cmd = compute(equation_var)
            else:
            	cmd = append(label, equation_var)

            Button(
                row_frame,
                text=label,
                width=5,
                height=2,
                command=cmd
            ).pack(side="left", padx=2, pady=2)

