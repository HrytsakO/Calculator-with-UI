import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


window = tk.Tk()

window.title("Calculator")
window.geometry("216x300+50+50")  # width x height + x + y

text_result = tk.Text(window, height=2, width=28)
text_result.grid(columnspan=5)

button_ac = tk.Button(window, text="AC", width=2, command=lambda: clear_field())
button_ac.grid(row=2, column=1)
button_pm = tk.Button(window, text="+/-", width=2, command=lambda: add_to_calculation(''))
button_pm.grid(row=2, column=2)
button_per = tk.Button(window, text='%', width=2, command=lambda: add_to_calculation("/100*"))
button_per.grid(row=2, column=3)
button_div = tk.Button(window, text='/', width=2, command=lambda: add_to_calculation('/'))
button_div.grid(row=2, column=4)
button_7 = tk.Button(window, text='7', width=2, command=lambda: add_to_calculation(7))
button_7.grid(row=3, column=1)
button_8 = tk.Button(window, text='8', width=2, command=lambda: add_to_calculation(8))
button_8.grid(row=3, column=2)
button_9 = tk.Button(window, text='9', width=2, command=lambda: add_to_calculation(9))
button_9.grid(row=3, column=3)
button_mult = tk.Button(window, text='*', width=2, command=lambda: add_to_calculation('*'))
button_mult.grid(row=3, column=4)
button_4 = tk.Button(window, text='4', width=2, command=lambda: add_to_calculation(4))
button_4.grid(row=4, column=1)
button_5 = tk.Button(window, text='5', width=2, command=lambda: add_to_calculation(5))
button_5.grid(row=4, column=2)
button_6 = tk.Button(window, text='6', width=2, command=lambda: add_to_calculation(6))
button_6.grid(row=4, column=3)
button_minus = tk.Button(window, text='-', width=2, command=lambda: add_to_calculation('-'))
button_minus.grid(row=4, column=4)
button_1 = tk.Button(window, text='1', width=2, command=lambda: add_to_calculation(1))
button_1.grid(row=5, column=1)
button_2 = tk.Button(window, text='2', width=2, command=lambda: add_to_calculation(2))
button_2.grid(row=5, column=2)
button_3 = tk.Button(window, text='3', width=2, command=lambda: add_to_calculation(3))
button_3.grid(row=5, column=3)
button_plus = tk.Button(window, text='+', width=2, command=lambda: add_to_calculation('+'))
button_plus.grid(row=5, column=4)
button_0 = tk.Button(window, text='0', width=8, command=lambda: add_to_calculation(0))
button_0.grid(row=6, column=1, columnspan=2)
button_coma = tk.Button(window, text=',', width=2, command=lambda: add_to_calculation(','))
button_coma.grid(row=6, column=3)
button_equal = tk.Button(window, text='=', width=2, command=lambda: evaluate_calculation())
button_equal.grid(row=6, column=4)

window.mainloop()
