# Import necessary libraries
from tkinter import *
import math

# Function to add to the calculator's current expression
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the calculator's current expression
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete the last character of the current expression
def button_delete():
    global calc_operator
    calc_operator = calc_operator[:-1]
    text_input.set(calc_operator)

# Function to calculate the factorial of a number
def factorial(n):
    try:
        return math.factorial(int(n))
    except (ValueError, OverflowError):
        return "ERROR"

def fact_func():
    global calc_operator
    try:
        result = str(factorial(int(calc_operator)))
        calc_operator = result
        text_input.set(result)
    except Exception as e:
        text_input.set("ERROR")

# Functions for trigonometric operations (assume input is in degrees)
def trig_sin():
    global calc_operator
    try:
        result = str(math.sin(math.radians(float(calc_operator))))
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("ERROR")

def trig_cos():
    global calc_operator
    try:
        result = str(math.cos(math.radians(float(calc_operator))))
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("ERROR")

def trig_tan():
    global calc_operator
    try:
        result = str(math.tan(math.radians(float(calc_operator))))
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("ERROR")

def trig_cot():
    global calc_operator
    try:
        result = str(1 / math.tan(math.radians(float(calc_operator))))
        calc_operator = result
        text_input.set(result)
    except (ValueError, ZeroDivisionError):
        text_input.set("ERROR")

# Function for square root calculation
def square_root():
    global calc_operator
    try:
        result = str(math.sqrt(float(calc_operator)))
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("ERROR")

# Function for cube root calculation
def third_root():
    global calc_operator
    try:
        result = str(float(calc_operator) ** (1 / 3))
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("ERROR")

# Function to change the sign of the current number
def sign_change():
    global calc_operator
    if calc_operator.startswith('-'):
        calc_operator = calc_operator[1:]
    else:
        calc_operator = '-' + calc_operator
    text_input.set(calc_operator)

# Function to calculate the percentage
def percent():
    global calc_operator
    try:
        result = str(float(calc_operator) / 100)
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("ERROR")

# Function to evaluate the expression entered
def button_equal():
    global calc_operator
    try:
        result = str(eval(calc_operator))
        text_input.set(result)
        calc_operator = result
    except (SyntaxError, ZeroDivisionError, NameError):
        text_input.set("ERROR")

# Initialize the calculator
tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Calculator")

calc_operator = ""
text_input = StringVar()

# Display panel for the calculator
text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth=5, bg='#BBB', justify='right')
text_display.grid(columnspan=5, padx=10, pady=15)

# Define button styles
button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}

# Layout Buttons
Button(tk_calc, button_params, text='7', command=lambda: button_click('7')).grid(row=1, column=0, sticky="nsew")
Button(tk_calc, button_params, text='8', command=lambda: button_click('8')).grid(row=1, column=1, sticky="nsew")
Button(tk_calc, button_params, text='9', command=lambda: button_click('9')).grid(row=1, column=2, sticky="nsew")
Button(tk_calc, button_params, text='/', command=lambda: button_click('/')).grid(row=1, column=3, sticky="nsew")
Button(tk_calc, button_params, text='AC', command=button_clear_all).grid(row=1, column=4, sticky="nsew")

Button(tk_calc, button_params, text='4', command=lambda: button_click('4')).grid(row=2, column=0, sticky="nsew")
Button(tk_calc, button_params, text='5', command=lambda: button_click('5')).grid(row=2, column=1, sticky="nsew")
Button(tk_calc, button_params, text='6', command=lambda: button_click('6')).grid(row=2, column=2, sticky="nsew")
Button(tk_calc, button_params, text='*', command=lambda: button_click('*')).grid(row=2, column=3, sticky="nsew")
Button(tk_calc, button_params, text='DEL', command=button_delete).grid(row=2, column=4, sticky="nsew")

Button(tk_calc, button_params, text='1', command=lambda: button_click('1')).grid(row=3, column=0, sticky="nsew")
Button(tk_calc, button_params, text='2', command=lambda: button_click('2')).grid(row=3, column=1, sticky="nsew")
Button(tk_calc, button_params, text='3', command=lambda: button_click('3')).grid(row=3, column=2, sticky="nsew")
Button(tk_calc, button_params, text='-', command=lambda: button_click('-')).grid(row=3, column=3, sticky="nsew")
Button(tk_calc, button_params, text='=', command=button_equal).grid(row=3, column=4, sticky="nsew")

Button(tk_calc, button_params, text='0', command=lambda: button_click('0')).grid(row=4, column=0, sticky="nsew")
Button(tk_calc, button_params, text='.', command=lambda: button_click('.')).grid(row=4, column=1, sticky="nsew")
Button(tk_calc, button_params, text='+', command=lambda: button_click('+')).grid(row=4, column=2, sticky="nsew")
Button(tk_calc, button_params, text='%', command=percent).grid(row=4, column=3, sticky="nsew")
Button(tk_calc, button_params, text='sqrt', command=square_root).grid(row=4, column=4, sticky="nsew")

# Start the main loop for the calculator
tk_calc.mainloop()
