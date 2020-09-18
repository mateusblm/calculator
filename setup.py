import sys


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


class calculator:
    def __init__(self):
        self.calculator = tk.Tk()
        self.calculator.title = ("Calculator")
        self.calculator.geometry = (500, 500)
        self.calculator.config(bg="black")

        # font for the Entry
        large_font = ('Verdana', 15,)
        # font for self.ButtonCalcs

        self.Frame = tk.Frame(self.calculator, width=500, height=400)
        self.Frame.grid(row=1, column=0)
        self.top_Frame = tk.Frame(self.calculator, width=500, height=100)
        self.top_Frame.grid(row=0, column=0)

        self.result = tk.StringVar()
        self.entry = tk.Entry(self.top_Frame, textvariable=self.result, width=30, bg="black", fg="white",
                              font=large_font)
        self.entry.grid(row=0, column=0, ipady=15)

        large_font = ("Verdana", 15)
        small_font = ("Verdana", 10)
        self.ButtonCalc_clear = tk.Button(self.Frame, text="C", padx=40, pady=20, command=self.ButtonCalc_clear,
                                          font=small_font)
        self.ButtonCalc_clear.grid(row=1, column=0)
        self.ButtonCalc_add_sub = tk.Button(self.Frame, text="+/-", padx=39, pady=20)
        self.ButtonCalc_add_sub.grid(row=1, column=1)
        self.ButtonCalc_percentage = tk.Button(self.Frame, text="%", padx=40, pady=20)
        self.ButtonCalc_percentage.grid(row=1, column=2)
        self.ButtonCalc_division = tk.Button(self.Frame, text="/", padx=40, pady=20, command=self.division, bg="orange",
                                             font=small_font)
        self.ButtonCalc_division.grid(row=1, column=3)

        self.ButtonCalc_7 = tk.Button(self.Frame, text="7", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("7"))
        self.ButtonCalc_7.grid(row=2, column=0)
        self.ButtonCalc_8 = tk.Button(self.Frame, text="8", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("8"))
        self.ButtonCalc_8.grid(row=2, column=1)
        self.ButtonCalc_9 = tk.Button(self.Frame, text="9", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("9"))
        self.ButtonCalc_9.grid(row=2, column=2)
        self.ButtonCalc_mult = tk.Button(self.Frame, text="*", padx=40, pady=20, command=self.multiplication,
                                         bg="orange",
                                         font=small_font)
        self.ButtonCalc_mult.grid(row=2, column=3)

        self.ButtonCalc_4 = tk.Button(self.Frame, text="4", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("6"))
        self.ButtonCalc_4.grid(row=3, column=0)
        self.ButtonCalc_5 = tk.Button(self.Frame, text="5", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("5"))
        self.ButtonCalc_5.grid(row=3, column=1)
        self.ButtonCalc_6 = tk.Button(self.Frame, text="6", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("4"))
        self.ButtonCalc_6.grid(row=3, column=2)
        self.ButtonCalc_substraction = tk.Button(self.Frame, text="-", padx=40, pady=20, command=self.substraction,
                                                 bg="orange",
                                                 font=small_font)
        self.ButtonCalc_substraction.grid(row=3, column=3)

        self.ButtonCalc_1 = tk.Button(self.Frame, text="1", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("1"))
        self.ButtonCalc_1.grid(row=4, column=0)
        self.ButtonCalc_2 = tk.Button(self.Frame, text="2", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("2"))
        self.ButtonCalc_2.grid(row=4, column=1)
        self.ButtonCalc_3 = tk.Button(self.Frame, text="3", padx=40, pady=20,
                                      command=lambda: self.ButtonCalc_click("3"))
        self.ButtonCalc_3.grid(row=4, column=2)
        self.ButtonCalc_addition = tk.Button(self.Frame, text="+", padx=40, pady=20, command=self.addition, bg="orange",
                                             font=small_font)
        self.ButtonCalc_addition.grid(row=4, column=3)

        self.ButtonCalc_0 = tk.Button(self.Frame, text="0", command=lambda: self.ButtonCalc_click("0"), padx=40,
                                      pady=20)
        self.ButtonCalc_0.grid(row=5, column=0, columnspan=3)
        self.ButtonCalc_decimal = tk.Button(self.Frame, text=".", padx=40, pady=20)
        self.ButtonCalc_decimal.grid(row=5, column=2)
        self.ButtonCalc_equal = tk.Button(self.Frame, text="=", padx=40, pady=20, command=self.equal, bg="orange",
                                          font=small_font)
        self.ButtonCalc_equal.grid(row=5, column=3)
        self.calculator.mainloop()


    def ButtonCalc_click(self, number):
        current_number = self.result.get()
        self.entry.delete(0, "end")
        self.entry.insert(0, current_number + number)


    def ButtonCalc_clear(self):
        self.entry.delete(0, "end")


    def addition(self):
        global current_number
        current_number = int(self.result.get())
        self.entry.delete(0, "end")
        global selection
        selection = "add"


    def multiplication(self):
        global current_number
        current_number = int(self.result.get())
        self.entry.delete(0, "end")

        global selection
        selection = "multiplication"


    def substraction(self):
        global current_number
        current_number = int(self.result.get())
        self.entry.delete(0, "end")
        global selection
        selection = "substraction"


    def division(self):
        global current_number
        current_number = int(self.result.get())
        self.entry.delete(0, "end")
        global selection
        selection = "division"


    def equal(self):
        second_number = int(self.result.get())
        self.entry.delete(0, "end")

        global current_number
        global selection
        if selection == "add":
            self.entry.insert(0, int(second_number) + current_number)
        if selection == "multiplication":
            self.entry.insert(0, current_number * int(second_number))
        if selection == "substraction":
            self.entry.insert(0, current_number - int(second_number))
        if selection == "division":
            self.entry.insert(0, current_number / int(second_number))
          
calculator()
