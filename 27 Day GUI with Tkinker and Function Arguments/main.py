from tkinter import *

def button_clicked():
    miles = float(input.get())
    km = miles * 1.609
    answer.config(text=f'{km}')

# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Label
my_label = Label(text="is equal to", font=("Arial", 14))
my_label.grid(row=1, column=0)

miles = Label(text="Miles", font=("Arial", 14))
miles.grid(row=0, column=2)

km = Label(text="Km", font=("Arial", 14))
km.grid(row=1, column=2)

answer = Label(text="0", font=("Arial", 14))
answer.grid(row=1, column=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

# Entry
input = Entry(width=7)
input.grid(row=0, column=1)

window.mainloop()