from tkinter import *
from tkinter import font as tkFont

root = Tk()
root.title("Simple Calculator")
#Sets the window's icon
img = PhotoImage(file="C:/Users/Harold/Desktop/Python/calc.ico")
root.tk.call('wm', 'iconphoto', root._w, img)

#Sets the display screen
text = Entry(root, width = 55, borderwidth = 5)
text.grid(row = 0, column = 0, columnspan = 3)

#Essential mathematical operations function definitions
def button_click(num):
    curr = text.get()
    text.delete(0, END) #Clears the entry box for new input
    text.insert(0, str(curr) + str(num))

def add():
    """Adds two given numbers"""
    first_number = text.get()
    global f_num
    global operation
    operation = "addition"
    f_num = int(first_number)
    text.delete(0, END)

def subtract():
    """Subtracts two given numbers"""
    first_number = text.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = int(first_number)
    text.delete(0, END)
    
def multiply():
    """Multiplies two given numbers"""
    first_number = text.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = int(first_number)
    text.delete(0, END)

def divide():
    """Divides two given numbers"""
    first_number = text.get()
    global f_num
    global operation
    operation = "division"
    f_num = int(first_number)
    text.delete(0, END)

def equal():
    """Displays the result of the given mathematical operation on the display screen"""
    second_number = text.get()
    text.delete(0, END)
    if operation == "addition":
        text.insert(0, f_num + int(second_number))
    if operation == "subtraction":
        text.insert(0, f_num - int(second_number))
    if operation == "multiplication":
        text.insert(0, f_num * int(second_number))
    if operation == "division":
        if int(second_number) != 0:
            result = f_num / int(second_number)
            if result * 10 != int(result):
                text.insert(0, round(result, 3))
            else:
                text.insert(0, result)
        else:  #Avoids division by zero / ZeroDivision error
            text.insert(0, "Cannot Divide by 0")

def clear():
    """Clears the display screen
       Must be performed before another calculation is correctly evaluated
    """
    text.delete(0, END)


#GUI Implementation

#Define buttons
helv12 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
button_1 = Button(root, text="1", padx = 45, pady = 20, font = helv12, command = lambda: button_click(1))
button_2 = Button(root, text="2", padx = 45, pady = 20, font = helv12, command = lambda: button_click(2))
button_3 = Button(root, text="3", padx = 45, pady = 20, font = helv12, command = lambda: button_click(3))
button_4 = Button(root, text="4", padx = 45, pady = 20, font = helv12, command = lambda: button_click(4))
button_5 = Button(root, text="5", padx = 45, pady = 20, font = helv12, command = lambda: button_click(5))
button_6 = Button(root, text="6", padx = 45, pady = 20, font = helv12, command = lambda: button_click(6))
button_7 = Button(root, text="7", padx = 45, pady = 20, font = helv12, command = lambda: button_click(7))
button_8 = Button(root, text="8", padx = 45, pady = 20, font = helv12, command = lambda: button_click(8))
button_9 = Button(root, text="9", padx = 45, pady = 20, font = helv12, command = lambda: button_click(9))
button_0 = Button(root, text="0", padx = 45, pady = 20, font = helv12, command = lambda: button_click(0))
button_clear = Button(root, text="Clear", padx = 90, pady = 20, font = helv12, command = clear)
button_add = Button(root, text="+", padx = 45, pady = 20, font = helv12, command = add)
button_subtract = Button(root, text="-", padx = 45, pady = 20, font = helv12, command = subtract)
button_multiply = Button(root, text="*", padx = 45, pady = 20, font = helv12, command = multiply)
button_divide = Button(root, text="/", padx = 45, pady = 20, font = helv12, command = divide)
button_equal = Button(root, text="=", padx = 106, pady = 20, font = helv12, command = equal)
button_subtract = Button(root, text="-", padx = 47, pady = 20, font = helv12, command = subtract)
button_multiply = Button(root, text="*", padx = 47, pady = 20, font = helv12, command = multiply)
button_divide = Button(root, text="/", padx = 48, pady = 20, font = helv12, command = divide)

#Display buttons on window
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)

button_add.grid(row = 5, column = 0)
button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 4, column = 1)
button_divide.grid(row = 4, column = 2)

button_clear.grid(row = 5, column = 1, columnspan = 2)
button_equal.grid(row = 6, column = 1, columnspan = 2)

#Run the GUI program
root.mainloop()
