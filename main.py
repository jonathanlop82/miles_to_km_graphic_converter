from tkinter import *

def convert_miles_to_km():
    miles = float(input.get())
    km = miles * 1.60934
    label_result["text"] = str(km)

#Window
window = Tk()
window.title("Mile to Km Comverter")
window.minsize(width=400,height=200)
window.config(padx=100, pady=50)

#labels
label_equal = Label(text="is equal to", font=("Arial",18,"normal"))
label_equal.grid(column=0, row=1)

label_miles = Label(text="Miles", font=("Arial",16,"normal"))
label_miles.grid(column=2, row=0)

label_km = Label(text="Km", font=("Arial",16,"normal"))
label_km.grid(column=2, row=1)

label_result = Label(text="0", font=("Arial",24,"bold"))
label_result.grid(column=1, row=1)

#inputs
input = Entry(width=10)
input.grid(column=1, row=0)

#Button
calc = Button(text="Calculate", command=convert_miles_to_km)
calc.grid(column=1, row=2)










window.mainloop()