# Importing everything from tkinter module. Import tkinter.fot as font in order to change font later.

from tkinter import *
import tkinter.font as font

# Declaring calculator_root as a root name windows [Tk()]. Declaring the title of the program (displayed on windows)
calculator_root = Tk()
calculator_root.title("Alan's Calculator")

# Overall font formatting. use myFont for later uses.
myFont = font.Font(family='Times New Roman', size = 15, weight = "bold")
myFont1 = font.Font(family = 'Consolas', size = 10, weight = "bold")

# Create entry (calculator main input/output panel) with dimensions. Locate the entry at the top, and below with 
# 5 other columns.
entrybar = Entry(calculator_root, width = 50, borderwidth = 2)
entrybar.grid(row = 0, column = 0, columnspan = 5, padx = 20, pady = 20)


# Define a function for when a button on the calculator is clicked. When a button is clicked, the entry bar will get 
# the item (number) from that button and saved in the current_item variable. The entry bar will then delete the current 
# number that it has stored and then insert (show) the previously clicked number (str(current_item)) and the next number
# (str(number))
def button_click(number):
    current_item = entrybar.get()
    entrybar.delete(0, END)
    entrybar.insert(0, str(current_item) + str(number))

# define a function for when the clear button is pressed. When the clear button is pressed, the entrybar will lose all of
# its content.
def button_clear():
    entrybar.delete(0, END)

# Define a function for addititon. This function is applied when the "+" button is pressed. The firstnumber variable will 
# store the value of the entry bar(which is inputted by pressing the number(s) before pressing "+".) "fnum" and "math" 
# are universal variables. fnum is used to convert the "firstnumber" variable string into an integer and "math" is used 
# to check for the operation later in the "equal_button" function. The same principle applies to other operators.
def addition():
    firstnumber = entrybar.get()
    global fnum
    global math
    math = "addition"
    fnum = int(firstnumber)
    entrybar.delete(0, END)

def subtraction():
    firstnumber = entrybar.get()
    global fnum
    global math
    math = "substraction"
    fnum = int(firstnumber)
    entrybar.delete(0, END)

def multiplication():
    firstnumber = entrybar.get()
    global fnum
    global math
    math = "multiplication"
    fnum = int(firstnumber)
    entrybar.delete(0, END)

def division():
    firstnumber = entrybar.get()
    global fnum
    global math
    math = "division"
    fnum = int(firstnumber)
    entrybar.delete(0, END)

# This function is execute when the equal button is pressed (when we need to execute the program to do the calculations)
# The function will first have to check for the operation that was chosen, and that's why "math" variable is bring into 
# use earlier. If "math" equals to certain values, then the program will perform a certain thing.
def equal_button():
    secondnumber = entrybar.get()
    entrybar.delete(0, END)
    
    # Once the operation buttons have been clicked, the entrybar will be empty and ready for another number to be inputed.
    # Here, the "secondnumber" varaible is used to store that second number and thus used within the program. We can then 
    # proceed to do calculation with each of these and the output the answer onto the entrybar. The "previousanswer" label
    # will show the full calculation. 
    if math == "addition":
        entrybar.insert(0, fnum + int(secondnumber))
        previousanswer = Label(calculator_root, text = (" " + str(fnum) + " + " + str(secondnumber) + " equals to "  + str(fnum + int(secondnumber))))
        previousanswer['font'] = myFont1
        previousanswer.grid(row = 4, column = 2, columnspan = 3)

    if math == "substraction":
        entrybar.insert(0, fnum - int(secondnumber))
        previousanswer = Label(calculator_root, text = (" " + str(fnum) + " - " + str(secondnumber) + " equals to " + str(fnum - int(secondnumber))))
        previousanswer['font'] = myFont1
        previousanswer.grid(row = 4, column = 2, columnspan = 3)
        
    if math == "multiplication":
        entrybar.insert(0, fnum * int(secondnumber))
        previousanswer = Label(calculator_root, text = (" " + str(fnum) + " x " + str(secondnumber) + " equals to " + str(fnum * int(secondnumber))))
        previousanswer['font'] = myFont1
        previousanswer.grid(row = 4, column = 2, columnspan = 3)

    if math == "division":
        entrybar.insert(0, fnum / int(secondnumber))
        previousanswer = Label(calculator_root, text = ("" + str(fnum) + " / " + str(secondnumber) + " equals to " + str(fnum / int(secondnumber))))
        previousanswer['font'] = myFont1
        previousanswer.grid(row = 4, column = 2, columnspan = 3)


# Button Configuration for each of the 9 number_buttons. Each of them will perform a lambda function (one line function) when click
# and it's redirected to the function button_click(number). The button['font'] = myFont states that the font used on each button must
# comply with the declared myFont.
button_1 = Button(calculator_root, text = "1", padx = 20, pady = 20, command = lambda: button_click(1)); button_1['font'] = myFont
button_2 = Button(calculator_root, text = "2", padx = 20, pady = 20, command = lambda: button_click(2)); button_2['font'] = myFont
button_3 = Button(calculator_root, text = "3", padx = 20, pady = 20, command = lambda: button_click(3)); button_3['font'] = myFont
button_4 = Button(calculator_root, text = "4", padx = 20, pady = 20, command = lambda: button_click(4)); button_4['font'] = myFont
button_5 = Button(calculator_root, text = "5", padx = 20, pady = 20, command = lambda: button_click(5)); button_5['font'] = myFont
button_6 = Button(calculator_root, text = "6", padx = 20, pady = 20, command = lambda: button_click(6)); button_6['font'] = myFont
button_7 = Button(calculator_root, text = "7", padx = 20, pady = 20, command = lambda: button_click(7)); button_7['font'] = myFont
button_8 = Button(calculator_root, text = "8", padx = 20, pady = 20, command = lambda: button_click(8)); button_8['font'] = myFont
button_9 = Button(calculator_root, text = "9", padx = 20, pady = 20, command = lambda: button_click(9)); button_9['font'] = myFont
button_0 = Button(calculator_root, text = "0", padx = 20, pady = 20, command = lambda: button_click(0)); button_0['font'] = myFont

# Clear and equal buttons are declared.
button_clear = Button(calculator_root, text = "Clear", padx = 36, pady = 20, command = button_clear); button_clear['font'] = myFont
button_equal = Button(calculator_root, text = "=", padx = 20, pady = 20, command = equal_button); button_equal['font'] = myFont

button_add = Button(calculator_root, text = "+", padx = 20, pady = 20, command = addition); button_add['font'] = myFont
button_minus = Button(calculator_root, text = "-", padx = 20, pady = 20, command = subtraction); button_minus['font'] = myFont
button_times = Button(calculator_root, text = "x", padx = 20, pady = 20, command = multiplication); button_times['font'] = myFont
button_divide = Button(calculator_root, text = "/", padx = 20, pady = 20, command = division); button_divide['font'] = myFont

# Button placement on the GUI. 
button_1.grid(row = 1, column = 0, columnspan = 1)
button_2.grid(row = 1, column = 1, columnspan = 1)
button_3.grid(row = 1, column = 2, columnspan = 1)

button_4.grid(row = 2, column = 0, columnspan = 1)
button_5.grid(row = 2, column = 1, columnspan = 1)
button_6.grid(row = 2, column = 2, columnspan = 1)

button_7.grid(row = 3, column = 0, columnspan = 1)
button_8.grid(row = 3, column = 1, columnspan = 1)
button_9.grid(row = 3, column = 2, columnspan = 1)

button_0.grid(row = 4, column = 0, columnspan = 1)
button_clear.grid(row = 3, column = 3, columnspan = 2)
button_equal.grid(row = 4, column = 1, columnspan = 1)

button_add.grid(row = 1, column = 3, columnspan = 1)
button_minus.grid(row = 1, column = 4, columnspan = 1)
button_times.grid(row = 2, column = 3, columnspan = 1)
button_divide.grid(row = 2, column = 4, columnspan = 1)

# Executing the whole program
calculator_root.mainloop()



