from tkinter import *

root = Tk()
root.title('Calculator')

#Entry Text Box
e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Functioning of the Calulator
#taking the input and evaluating
def clicked(number):
    try:
        if(number == '='):
            current = e.get()
            e.delete(0, END)
            e.insert(0, eval(current))
            return 
        current = e.get()
        e.delete(0, END)
        e.insert(0,str(current) + str(number))
        current = e.get()
    except Exception:
        e.insert(0,'Error, Try Again!')

#For Backspace
def clicked_bs():
    x = len(e.get())
    e.delete(x-1, END)

#For Clear
def clicked_clear():
    e.delete(0,END)    

#initiating buttons
button_1 = Button(root, text="1", command=lambda: clicked(1), padx=30, pady=10)
button_2 = Button(root, text="2", command=lambda: clicked(2), padx=30, pady=10)
button_3 = Button(root, text="3", command=lambda: clicked(3), padx=30, pady=10)
button_4 = Button(root, text="4", command=lambda: clicked(4), padx=30, pady=10)
button_5 = Button(root, text="5", command=lambda: clicked(5), padx=30, pady=10)
button_6 = Button(root, text="6", command=lambda: clicked(6), padx=30, pady=10)
button_7 = Button(root, text="7", command=lambda: clicked(7), padx=30, pady=10)
button_8 = Button(root, text="8", command=lambda: clicked(8), padx=30, pady=10)
button_9 = Button(root, text="9", command=lambda: clicked(9), padx=30, pady=10)
button_0 = Button(root, text="0", command=lambda: clicked(0), padx=30, pady=10)
button_plus = Button(root, text="+", command=lambda: clicked('+'), padx=30, pady=10)
button_minus = Button(root, text="-", command=lambda: clicked('-'), padx=30, pady=10)
button_divide = Button(root, text="/", command=lambda: clicked('/'), padx=30, pady=10)
button_multiply = Button(root, text="x", command=lambda: clicked('*'), padx=30, pady=10)
button_dot = Button(root, text=".", command=lambda: clicked('.'), padx=31, pady=10)
button_bs = Button(root, text="<", command=clicked_bs, padx=29, pady=10)
button_clear = Button(root, text="C", command=clicked_clear, padx=30, pady=10)
button_equal = Button(root, text="=", command=lambda: clicked('='), padx=29, pady=10)
button_brac_st = Button(root, text="(", command=lambda: clicked('('), padx=30, pady=10)
button_brac_end = Button(root, text=")", command=lambda: clicked(')'), padx=30, pady=10)

#positioning the buttons
button_brac_st.grid(row=1, column=0, pady=2)
button_brac_end.grid(row=1, column=1, pady=2)
button_clear.grid(row=1, column=2, pady=2)
button_bs.grid(row=1, column=3, pady=2)

button_divide.grid(row=2, column=3, pady=2)
button_9.grid(row=2, column=2, pady=2)
button_8.grid(row=2, column=1, pady=2)
button_7.grid(row=2, column=0, pady=2)

button_multiply.grid(row=3, column=3, pady=2)
button_6.grid(row=3, column=2, pady=2)
button_5.grid(row=3, column=1, pady=2)
button_4.grid(row=3, column=0, pady=2)

button_minus.grid(row=4, column=3, pady=2)
button_3.grid(row=4, column=2, pady=2)
button_2.grid(row=4, column=1, pady=2)
button_1.grid(row=4, column=0, pady=2)

button_plus.grid(row=5, column=3, pady=2)
button_equal.grid(row=5, column=2, pady=2)
button_0.grid(row=5, column=1, pady=2)
button_dot.grid(row=5, column=0, pady=2)

root.mainloop()