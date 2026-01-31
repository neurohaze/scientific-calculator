from tkinter import Label, StringVar

def create_display(window):
    equation_var = StringVar(master=window)
    equation_var.set("")

    display = Label(
        window,
        textvariable=equation_var,
        font=("Consolas", 20),
        bg="white",
        width=24,
        height=2,
        anchor="e"
    )
    display.pack(pady=10)

    return equation_var
