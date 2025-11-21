# Title: Joe's Automotive
# Author: Arianna Endres
# Date: 11/21/2025

# Program that allows the user to select certain maintenance services and click a button to calculate the total cost.

import tkinter

class JoeAutomotive:
    def __init__(self):
        # Create and name the window.
        self.window = tkinter.Tk()
        self.window.title('Automotive')

        # Create the frames.
        self.list_frame = tkinter.Frame(self.window)
        self.total_frame = tkinter.Frame(self.window)
        self.buttons_frame = tkinter.Frame(self.window)

        # Fill the list frame:
        # Create a dictionary with maintenance services as the key and their corresponding prices as the value.
        self.maintenance_services = {'Oil Change':30.00, 'Lube Job':20.00, 'Radiator Flush':40.00,
                                'Transmission Fluid':100.00, 'Inspection':35.00, 'Muffler replacement':200.00,
                                'Tire rotation':20.00}

        # Create the listbox.
        self.maintenance_services_list = tkinter.Listbox(self.list_frame, selectmode=tkinter.MULTIPLE,
                                                         height=7, width=30)

        # Fill the listbox by iterating through the maintenance_services dictionary.
        for key in self.maintenance_services:
            value = self.maintenance_services[key]
            self.maintenance_services_list.insert(tkinter.END, key + ' - $' + str(f'{value:.2f}'))

        # Pack the list.
        self.maintenance_services_list.pack()


        # Fill the total frame:
        # Create StringVar object to associate with output label.
        self.total = tkinter.StringVar()

        # Create a label for the text before the total.
        self.text_total = tkinter.Label(self.total_frame, text=f'Total:')

        # Create a label for the total.
        self.total_label = tkinter.Label(self.total_frame, textvariable=self.total)

        # Pack the labels.
        self.text_total.pack(side='left')
        self.total_label.pack(side='left')


        # Fill the buttons frame:
        # Create the total button.
        self.calculate_total = tkinter.Button(self.buttons_frame, text='Calculate Total', relief='raised',
                                              command=self.calculate_total)

        # Create the quit button.
        self.quit = tkinter.Button(self.buttons_frame, text='Quit', command=self.window.quit)

        # Pack the buttons.
        self.calculate_total.pack(side='left')
        self.quit.pack(side='left')


        # Pack the windows
        self.list_frame.pack(padx=10, pady=(5, 0))
        self.total_frame.pack()
        self.buttons_frame.pack()


        # Tkinter main loop
        tkinter.mainloop()


    # Define the function that calculates the total
    def calculate_total(self):
        # Set the total equal to zero
        total = 0

        # For each index number in the list of selected services, get the corresponding price
        # and add it to a running total.
        for index in self.maintenance_services_list.curselection():
            # Turn the maintenance_services dictionary into a tuple in order to use the index
            # number to get the corresponding key. Then pass this key to the dictionary to get
            # the corresponding value number and add it to the running total.
            total += (self.maintenance_services[(tuple(self.maintenance_services))[index]])

        # Set self.total to the total added above. Add an extra zero after the decimal point,
        # convert it to a string, and add a dollar sign to get the correct formatting.
        self.total.set(str(f'${total:.2f}'))



if __name__ == '__main__':
    joe_automotive = JoeAutomotive()

