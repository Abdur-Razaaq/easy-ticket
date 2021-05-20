# Importing all tools for use from tkinter
from tkinter import *
# Importing messagebox from tkinter
from tkinter import messagebox


class ClsTicketSales(object):
    def __init__(self, window):
        # Initialise window
        self.window = window
        # setting title
        self.window.title("TicketSales")
        # setting size
        self.window.geometry("500x600")
        # setting color
        self.window.config(bg="light green")

        # Heading
        self.heading = Label(self.window, text="Easy Ticket", bg="light blue")
        self.heading["font"] = "Roboto", 18
        self.heading.pack()

        # Mobile number label and entry
        self.cn_entry_label = Label(self.window, text="Enter Mobile Number:", bg="light blue")
        self.cell_number = Entry(self.window)
        # positioning label and entry using place
        self.cn_entry_label.place(x=40, y=40)
        self.cell_number.place(x=300, y=40)

        # Ticket category label and option menu
        self.category_label = Label(self.window, text="Select Ticket Category:", bg="light blue")  # adding bg color
        self.options = ["Soccer", "Movie", "Theater"]
        self.variable = StringVar(self.window)
        self.variable.set("Select Ticket")  # Default Value Shown on OptionMenu
        self.ticket_op = OptionMenu(window, self.variable, *self.options)
        # positioning label and OptionMenu using place
        self.category_label.place(x=40, y=120)
        self.ticket_op.place(x=300, y=120)

        # Label and Ticket numbering using Spinbox
        self.nr_tickets_label = Label(self.window, text="Number of Tickets Bought:", bg="light blue")  # adding bg color
        self.nr_tickets = Spinbox(self.window, width=10, from_=0, to=100)
        # positioning label and spinbox using place
        self.nr_tickets_label.place(x=40, y=200)
        self.nr_tickets.place(x=300, y=200)

        # Calculation button
        self.calc_button = Button(self.window, text='Calculate Ticket', bg="yellow", borderwidth="5",
                                  command=self.calc_prepayment)
        self.clear_button = Button(self.window, text='Clear Entries', bg="yellow", borderwidth="5", command=self.clear)
        # positioning button using place
        self.calc_button.place(x=60, y=280)
        self.clear_button.place(x=300, y=280)

        # Creating the Border
        self.border_top = Label(self.window, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                                bg="yellow")
        self.border_bottom = Label(self.window, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                                   bg="yellow")
        # positioning border using place
        self.border_top.place(y=360)
        self.border_bottom.place(y=560)

        # Results labels
        self.amount_pay = Label(self.window, text="", bg="light green")
        self.reserve = Label(self.window, text="", bg="light green")
        self.cell_label = Label(self.window, text="", bg="light green")
        # Positioning with place
        self.amount_pay.place(x=100, y=405)
        self.reserve.place(x=100, y=465)
        self.cell_label.place(x=100, y=525)

    # Calculations
    def calc_prepayment(self):
        ticket_no = int(self.nr_tickets.get())
        vat = 0.14  # VAT
        try:  # Error Capturing Using try
            int(self.cell_number.get())
            if len(self.cell_number.get()) < 10 or len(self.cell_number.get()) > 10:
                raise ValueError  # Error Capturing

            elif self.variable.get() == "Select Ticket":
                raise ValueError  # Error Capturing

            elif int(self.nr_tickets.get()) == 0:
                raise ValueError  # Error Capturing

            # Calculations for soccer ticket price
            elif self.variable.get() == "Soccer":
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # calculations for movie ticket price
            elif self.variable.get() == "Movie":
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # Calculations for Theater
            elif self.variable.get() == "Theater":
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # Reservation
            reserve_text = "Reservation for {} for : {} ".format(self.variable.get(), ticket_no)
            cell_text = "Reservation Made By: {}".format(self.cell_number.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:  # Error Message. Display Error with messagebox
            messagebox.showerror(message="INVALID - Please Try Again")

    def clear(self):  # Clears all user changed values
        self.cell_number.delete(0, END)
        self.cell_number.focus()
        self.variable.set("Select Ticket")
        self.nr_tickets.delete(0, END)
        self.nr_tickets.insert(0, 0)
        self.amount_pay.config(text="")
        self.reserve.config(text="")
        self.cell_label.config(text="")


# Creates window and ensures that the app stays running until terminated by the user
root = Tk()
ClsTicketSales(root)
root.mainloop()
