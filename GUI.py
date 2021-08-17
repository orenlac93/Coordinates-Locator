import tkinter as tk
from tkinter import messagebox

import coordinatesLocator

# Top level window

frame = tk.Tk()
frame.title("Coordinates Locator On Map")
frame.geometry('600x400')

constructions = tk.Label(frame, text="\nEnter coordinates\n")
constructions.pack()


# Function for getting Input from text boxes

def get_input():

    input1 = input_txt.get(1.0, "end-1c")
    input2 = input_txt2.get(1.0, "end-1c")

    label.config(text="Latitude Input: " + input1)
    label2.config(text="Longitude Input: " + input2)
    label3.config(text="\nclose the app and open the map file \n(Map.html)")

    coordinatesLocator.find_map_location(input1, input2)
    return messagebox.showinfo('Location found', 'your map saved successfully!')


latitude_text = tk.Label(frame, text="Latitude")
latitude_text.config(font=("Courier", 14))
latitude_text.pack()

# first TextBox Creation
input_txt = tk.Text(frame, height=2, width=30)
input_txt.pack()

longitude_text = tk.Label(frame, text="Longitude")
longitude_text.config(font=("Courier", 14))
longitude_text.pack()

# second TextBox Creation
input_txt2 = tk.Text(frame, height=2, width=30)
input_txt2.pack()

# extra text

extra_text = tk.Label(frame, text="\n")
extra_text.config(font=("Courier", 14))
extra_text.pack()

# Button Creation
find_location_Button = tk.Button(frame, text="Find Location", command=get_input)
find_location_Button.pack()

# Label Creation

label = tk.Label(frame, text="")
label2 = tk.Label(frame, text="")
label3 = tk.Label(frame, text="")

label.pack()
label2.pack()
label3.pack()

frame.mainloop()
