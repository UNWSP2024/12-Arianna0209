# Title: Long-Distance Calls
# Author: Arianna Endres
# Date: 11/21/2025

# Program that allows the user to select a rate category (from a set of radio buttons), and enter the number
# of minutes of the call into an Entry widget.  An info dialog box displays the charge for the call.

import tkinter

class CallRate:
    def __init__(self):
        # Create and title the window.
        self.window = tkinter.Tk()
        self.window.title("Call Rate Calculator")


        # Create the frames.
        self.prompt_frame = tkinter.Frame(self.window)
        self.rate_category_frame = tkinter.Frame(self.window)
        self.minutes_frame = tkinter.Frame(self.window)
        self.call_price_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)


        # Fill the prompt frame:
        # Create the text label.
        self.prompt = tkinter.Label(self.prompt_frame,
                                    text='Select the rate that corresponds with the time of your call:')

        # Pack the label.
        self.prompt.pack()


        # Fill the rate category frame:
        # Create two tuples with the rate information.
        self.rate_category = ('Daytime (6:00 A.M. through 5:59 P.M.)', 'Evening (6:00 P.M.  through 11:59 P.M.)',
                              'Off-Peak (midnight through 5:59 A.M.)')

        self.rate_per_min = (0.02, 0.12, 0.05)

        # Create an IntVar object.
        self.category_selection = tkinter.IntVar()

        # Create the radiobuttons.
        self.daytime_text = tkinter.Radiobutton(self.rate_category_frame,
                                                text=f'{self.rate_category[0]}: ${self.rate_per_min[0]} per minute',
                                                variable=self.category_selection, value=0)

        self.evening_text = tkinter.Radiobutton(self.rate_category_frame,
                                                 text=f'{self.rate_category[1]}: ${self.rate_per_min[1]} per minute',
                                                variable=self.category_selection, value=1)

        self.off_peak_text = tkinter.Radiobutton(self.rate_category_frame,
                                                 text=f'{self.rate_category[2]}: ${self.rate_per_min[2]} per minute',
                                                variable=self.category_selection, value=2)

        # Pack the radiobuttons.
        self.daytime_text.pack(anchor='w')
        self.evening_text.pack(anchor='w')
        self.off_peak_text.pack(anchor='w')


        # Fill the minutes frame:
        # Create the text before the entry widget.
        self.minute_entry_text = tkinter.Label(self.minutes_frame,
                                               text='Enter the length of your call in minutes: ')

        # Create the entry widget.
        self.minute_entry = tkinter.Entry(self.minutes_frame, width=10)

        # Pack the widgets.
        self.minute_entry_text.pack(side='left')
        self.minute_entry.pack(side='left')


        # Fill the call price frame:
        # Create the text before the price.
        self.price_text = tkinter.Label(self.call_price_frame, text='The cost of your call is:')

        # Create the StringVar object.
        self.price = tkinter.StringVar()

        # Create the price label.
        self.price_label = tkinter.Label(self.call_price_frame, textvariable=self.price)

        # Pack the labels.
        self.price_text.pack(side='left')
        self.price_label.pack(side='left')


        # Fill the button frame:
        # Create the calculate price button.
        self.calculate_price = tkinter.Button(self.button_frame, text='Calculate Price',
                                              relief='raised', command=self.calculate)

        # Create the quit button.
        self.quit = tkinter.Button(self.button_frame, text='Quit', command=self.window.quit)

        # Pack the buttons.
        self.calculate_price.pack(side='left')
        self.quit.pack(side='left')


        # Pack the frames.
        self.prompt_frame.pack()
        self.rate_category_frame.pack()
        self.minutes_frame.pack(pady=5)
        self.call_price_frame.pack(pady=5)
        self.button_frame.pack()


        # Tkinter main loop.
        self.window.mainloop()

    # Define the function that calculates the call price.
    def calculate(self):
        # Get the user entry for the length of the call.
        minutes = float(self.minute_entry.get())

        # Get the user's rate selection.
        rate = self.rate_per_min[self.category_selection.get()]

        # Calculate the price by multiplying the rate per minute
        # by the number of minutes.
        price = rate * minutes

        # Set the product as the price.
        self.price.set(f'${price:.2f}')


if __name__ == '__main__':
    call_rate = CallRate()



