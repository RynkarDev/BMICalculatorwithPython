from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=400,height=400)

def weight_entry_click(event):
    if weight_entry.get() == "Enter your weight":
        weight_entry.delete(0,"end")
        weight_entry.insert(0,"")
        weight_entry.config(fg="black")

def focusout(event):
    if weight_entry.get() == "":
        weight_entry.insert(0, "Enter your weight")
        weight_entry.config(fg="grey")

def height_entry_click(event):
    if height_entry.get() == "Enter your height":
        height_entry.delete(0,"end")
        height_entry.insert(0,"")
        height_entry.config(fg="black")

def height_focusout(event):
    if height_entry.get() == "":
        height_entry.insert(0,"Enter your height")
        height_entry.config(fg="grey")

def calculate_button_bmi():
    try:
        weight = float(weight_entry.get()) 
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            result_label.config(text=" You are skeleton.")
        elif bmi < 25:
            result_label.config(text="You have normal weight.")
        elif bmi < 30:
            result_label.config(text="You are slightly overweight.")
        elif bmi < 35:
            result_label.config(text="You are obese.")
        else:
            result_label.config(text="Elephant!") 
    except ValueError:
         result_label.config(text="Please enter valid numbers")

weight_entry = Entry(window, font=("Arial",16), width=20, fg="grey")
weight_entry.pack(pady=10)
weight_entry.insert(0,"Enter your weight") #you must write 60.0 1.74 like this
weight_entry.bind("<FocusIn>", weight_entry_click)
weight_entry.bind("<FocusOut>",focusout)

height_entry = Entry(window,font=("Arial",16),width=20, fg="grey")
height_entry.pack(pady=10)
height_entry.insert(0,"Enter your height") #you must write 60.0 1.74 like this
height_entry.bind("<FocusIn>",height_entry_click)
height_entry.bind("<FocusOut>",height_focusout)

calculate_button = Button(window, text="Your BMI",command=calculate_button_bmi)
calculate_button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()