from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")


window.mainloop()

miles_input = Entry()
miles_label = Label(text="Miles")

is_equal_label = Label(text="is equal to")

kilometer_results_label = Label(text="0")

kilometer_label = Label(text="Km")

calculate_button = Button(text="Calculate")