import tkinter as tk
import math

root = tk.Tk()
root.geometry("220x200")
root.title("Hi Github!")

numbers = tk.Label(root, text="", bg = "White", relief = "sunken")
numbers.pack(ipadx = 100, pady = 10)
current_input = ""
operator = ""
prev_input = ""

def number_press(n):
    
    global current_input
    current_input = current_input + str(n)
    numbers.configure(text = current_input)
    numbers.pack()


frame1 = tk.Frame()

button_7 = tk.Button(frame1, text = "7", command = lambda: number_press(7))
button_7.grid(row=0, column=0, ipadx = 5)
button_8 = tk.Button(frame1, text = "8", command = lambda: number_press(8))
button_8.grid(row=0, column=1, ipadx = 5)
button_9 = tk.Button(frame1, text = "9", command = lambda: number_press(9))
button_9.grid(row=0, column=2, ipadx = 5)
button_div = tk.Button(frame1, text = "/", command = lambda: operator_press("/"))
button_div.grid(row=0, column=3, ipadx = 5)
button_mod = tk.Button(frame1, text = "%", command = lambda: operator_press("%"))
button_mod.grid(row=0, column=4, ipadx = 4)

frame1.pack()

frame2 = tk.Frame()

button_4 = tk.Button(frame2, text = "4", command = lambda: number_press(4))
button_4.grid(row=0, column=0, ipadx = 5)
button_5 = tk.Button(frame2, text = "5", command = lambda: number_press(5))
button_5.grid(row=0, column=1, ipadx = 5)
button_6 = tk.Button(frame2, text = "6", command = lambda: number_press(6))
button_6.grid(row=0, column=2, ipadx = 5)
button_mul = tk.Button(frame2, text = "*", command = lambda: operator_press("*"))
button_mul.grid(row=0, column=3, ipadx = 5)
button_pow = tk.Button(frame2, text = "^", command = lambda: operator_press("^"))
button_pow.grid(row=0, column=4, ipadx = 5)

frame2.pack()

frame3 = tk.Frame()

button_1 = tk.Button(frame3, text = "1", command = lambda: number_press(1))
button_1.grid(row=0, column=0, ipadx = 5)
button_2 = tk.Button(frame3, text = "2", command = lambda: number_press(2))
button_2.grid(row=0, column=1, ipadx = 5)
button_3 = tk.Button(frame3, text = "3", command = lambda: number_press(3))
button_3.grid(row=0, column=2, ipadx = 5)
button_add = tk.Button(frame3, text = "+", command = lambda: operator_press("+"))
button_add.grid(row=0, column=3, ipadx = 3)
button_log = tk.Button(frame3, text = "log", command = lambda: operator_press("log"))
button_log.grid(row=0, column=4, ipadx = 1)

frame3.pack()

frame4 = tk.Frame()

button_dot = tk.Button(frame4, text = ".", command = lambda: number_press("."))
button_dot.grid(row=0, column=0, ipadx = 5)
button_0 = tk.Button(frame4, text = "0", command = lambda: number_press(0))
button_0.grid(row=0, column=1, ipadx = 5)
button_back = tk.Button(frame4, text = "<--", command = lambda: backspace())
button_back.grid(row=0, column=2, ipadx = 1)
button_sub = tk.Button(frame4, text = "-", command = lambda: operator_press("-"))
button_sub.grid(row=0, column=3, ipadx = 5)
button_clear = tk.Button(frame4, text = "C", command = lambda: clear())
button_clear.grid(row=0, column=4, ipadx=5)

frame4.pack()

frame5 = tk.Frame()

button_execute = tk.Button(frame5, text = "EXE", command = lambda: execute())
button_execute.grid(row=0, column=1, ipadx = 5)
button_quit = tk.Button(frame5, text = "Quit", bg = "Red", fg = "White", command = root.destroy)
button_quit.grid(row=0, column=2, ipadx = 5)

frame5.pack()
    
def operator_press(o):
    
    global current_input
    global operator
    global prev_input
    
    if "." in current_input:
        prev_input = float(current_input)
        current_input = ""
        numbers.configure(text = o)
        numbers.pack()
    else:
        prev_input = int(current_input)
        current_input = ""
        numbers.configure(text = o)
        numbers.pack()
    
    operator = o
    
def execute():
    
    global current_input
    global operator
    global prev_input
    
    if "." in current_input:
        current_input = float(current_input)
        prev_input = float(prev_input)
    elif type(prev_input) == type(0.01):
        current_input = float(current_input)
    else:
        current_input = int(current_input)
    
    if operator == "+":
        result = prev_input + current_input
        numbers.configure(text = result)
        numbers.pack()
        
    elif operator == "-":
        result = prev_input - current_input
        numbers.configure(text = result)
        numbers.pack()
        
    elif operator == "/":
        result = prev_input / current_input
        numbers.configure(text = result)
        numbers.pack()
        
    elif operator == "*":
        result = prev_input * current_input
        numbers.configure(text = result)
        numbers.pack()
        
    elif operator == "^":
        result = prev_input ** current_input
        numbers.configure(text = result)
        numbers.pack()
        
    elif operator == "%":
        result = prev_input % current_input
        numbers.configure(text = result)
        numbers.pack()
        
    elif operator == "log":
        result = math.log(prev_input, current_input)
        numbers.configure(text = result)
        numbers.pack()
        
    else:
        numbers.configure(text = current_input)
        numbers.pack()

def clear():
    
    global current_input
    global operator
    global prev_input
    
    current_input = ""
    operator = ""
    prev_input = ""
    numbers.configure(text = current_input)
    numbers.pack()

def backspace():
    
    global current_input
    current_input = current_input[:-1]
    numbers.configure(text = current_input)
    numbers.pack()


root.mainloop()

