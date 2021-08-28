import tkinter as tk
from tkinter import messagebox

import coordinatesLocator


# Function for check if the input string is a number

def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


# Function for getting Input from text boxes

def get_input():

    input1 = input_txt.get(1.0, "end-1c")
    input2 = input_txt2.get(1.0, "end-1c")

    #   if the input is not numbers
    if not(is_number(input1)) or not(is_number(input2)):
        return messagebox.showinfo('Non Number Input! \nEnter coordinates numbers ........')

    else:
        label.config(text="Latitude Input: " + input1)
        label2.config(text="Longitude Input: " + input2)
        label3.config(text="\nexit the application and open the map file \n\n"
                           "(Map.html file will be created in the current folder)\n")

        coordinatesLocator.find_map_location(input1, input2)

        # destroy input labels and button

        find_location_Button.destroy()

        input_txt.destroy()
        input_txt2.destroy()

        latitude_text.destroy()
        longitude_text.destroy()

        constructions.destroy()

        # exit button

        exit_button = tk.Button(frame, text="Exit", command=frame.destroy, height=3, width=15, bg='White')
        exit_button.pack()

        # success message box

        return messagebox.showinfo('Location found', 'your map saved successfully!')


# Top level window

frame = tk.Tk()
frame.title("Coordinates Locator On Map")
frame.geometry('600x400')

constructions = tk.Label(frame, text="\nEnter coordinates\n")
constructions.pack()

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
find_location_Button = tk.Button(frame, text="Find Location", command=get_input,
                                 height=3, width=15, bg='White', fg='Red')
find_location_Button.pack()

# Label Creation

label = tk.Label(frame, text="")
label2 = tk.Label(frame, text="")
label3 = tk.Label(frame, text="")

label.pack()
label2.pack()
label3.pack()

frame.mainloop()

