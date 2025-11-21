# Title: MPG Calculator
# Author: Arianna Endres
# Date: 11/21/2025

# GUI window allows user to enter the number of gallons a vehicle can hold and the number
# of miles it can go on a full tank.
# The program then calculates the MPG when the user clicks the "Calculate MPG" button.

import tkinter

class GUImpg:
    def __init__(self):

        # Create and title the window.
        self.window = tkinter.Tk()
        self.window.title('MPG Calculator')

        # Create a frame for each line of the window.
        self.gallon_frame = tkinter.Frame(self.window)
        self.miles_frame = tkinter.Frame(self.window)
        self.answer_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)

        # Fill the gallon frame:
        # Add the label before the input box.
        self.gallon_label = tkinter.Label(self.gallon_frame, text='Enter the number of gallons '
                                                                  'your vehicle holds: ')

        # Add the entry box.
        self.gallon_entry = tkinter.Entry(self.gallon_frame, width=5)

        # Pack the widgets.
        self.gallon_label.pack(side='left')
        self.gallon_entry.pack(side='left')


        # Fill the miles frame:
        # Add the label before the input box.
        self.miles_label = tkinter.Label(self.miles_frame, text='Enter the number of miles your '
                                                                'vehicle can go on one tank: ')

        # Add the entry box.
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)

        # Pack the widgets.
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')


        # Fill the answer frame:
        # Create StringVar object to associate with output label.
        self.mpg = tkinter.StringVar()

        # Create label for text before answer.
        self.answer_text = tkinter.Label(self.answer_frame, text=f'Your vehicle\'s MPG is: ')

        # Create label for answer.
        self.mpg_label = tkinter.Label(self.answer_frame, textvariable=self.mpg)

        # Pack the widgets.
        self.answer_text.pack(side='left')
        self.mpg_label.pack(side='left')


        # Fill the button frame:
        # Create the calculate button.
        self.calculate_button = tkinter.Button(self.button_frame, text='Calculate MPG', relief='raised',
                                               command = self.calculate)

        # Create the quit button.
        self.quit = tkinter.Button(self.button_frame, text='Quit', relief='raised', command=self.window.quit)

        # Pack the buttons.
        self.calculate_button.pack(side='left')
        self.quit.pack(side='left')


        # Pack the frames.
        self.gallon_frame.pack()
        self.miles_frame.pack(padx=5)
        self.answer_frame.pack()
        self.button_frame.pack()

        # Tkinter main loop
        tkinter.mainloop()

    def calculate(self):
        # Get the entry for the number of miles the vehicle can go and convert it to a float.
        # Do the same for the number of gallons the vehicle can hold, and then divide the miles by the gallons.
        mpg = (float(self.miles_entry.get()))/(float(self.gallon_entry.get()))

        # Convert the MPG number to a string and set it as self.mpg.
        self.mpg.set(str(f'{mpg:.2f}'))


if __name__ == '__main__':
    gui_mpg = GUImpg()