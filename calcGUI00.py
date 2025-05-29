#290525 This is a simple calculator GUI using Tkinter in Python.
# calcGUI00.py
#import tkinter as tk
import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol) 
    text_result.delete(1.0, "end") #clear text area
    text_result.insert(1.0, calculation)  # Display the current calculation in the text area
# Placeholder for adding symbol to calculator display

def evaluate_calculation():
    global calculation 
    try:
        calculation = str(eval(calculation))  # Evaluate using python library "eval" the expression and convert to string

        text_result.delete(1.0, "end")  # Clear the text area
        text_result.insert(1.0, calculation)  # Display the result in the text area
    except:
        clear_field()  # If there's an error, clear the field
        text_result.insert(1.0, "#404 ERROR !!!")  # Display an error message
        pass
        # Evaluate the expression in the calculator
    pass
     
    
      # Placeholder for evaluating the calculator expression

def clear_field():
    global calculation
    calculation = ""  # Reset the calculation
    text_result.delete(1.0, "end")  # Clear the text area
    pass  # Placeholder for clearing the calculator display

#root = window name
root = tk.Tk()
#set the title of the window
root.title("abakus")
#set the size of the window
root.geometry("300x380")

# Set the background color of the window
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="silver", fg="black", bd=5, insertbackground='black')
text_result.grid(columnspan=5)

# Create buttons for the calculator
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1) , width=5, height=2, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, height=2, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, height=2, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, height=2, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, height=2, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, height=2, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, height=2, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, height=2, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, height=2, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, height=2, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation('+'), width=5, height=2, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation('-'), width=5, height=2, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation('*'), width=5, height=2, font=("Arial", 14))
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation('/'), width=5, height=2, font=("Arial", 14))
btn_divide.grid(row=5, column=4)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, height=2, font=("Arial", 14))
btn_close.grid(row=5, column=3)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, height=2, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=5, height=2, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, height=2, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
# Instance of the window
root.mainloop()