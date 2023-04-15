from datetime import datetime

from Customer import Customer
from Reservation import Reservation
from Room import Room
class Invoice:
    def __init__(self, invoice_id, customer, reservation_id, invoice_description, payment_date="", balance=0):
        self.invoice_id = invoice_id
        self.invoice_description = invoice_description
        self.payment_date = payment_date
        self.balance = balance
        self.customer = customer
        self.reservation_id = reservation_id
    

    # getter and setter for invoice id
    def _set_invoice_id(self, id):
        self.invoice_id = id
    
    def _get_invoice_id(self):
        return self.invoice_id

    # getter and setter for invoice description
    def _set_invoice_description(self, input):
        self.invoice_description = input
    
    def _get_invoice_description(self):
        return self.invoice_description

    # getter and setter for payment date
    def _set_payment_date(self, date):
        self.payment_date = date
    
    def _get_payment_date(self):
        return self.payment_date
    
    # getter and setter for balance
    def _set_balance(self, amount):
        self.balance = amount
    
    def _get_balance(self):
        return self.balance
    
    def createInvoice(self, invoice_description, amount):
        
        invoice_id = self.invoice_id
        self.invoice_id = invoice_id
        self.invoice_description = invoice_description
        self.balance = amount

        print(f"Invoice {self.invoice_id} has been created for {self.get_customer_name()} with a balance of {self.balance}.")

    
    def get_customer_name(self):
        return f"{self.customer.get_first_name()} {self.customer.get_last_name()}"
    
    def selectInvoice(self, invoice_list):
        if not invoice_list:
            print("No invoices available.")
            return None

        print("Available Invoices:")
        for i, invoice in enumerate(invoice_list):
            print(f"{i + 1}. {invoice.invoice_id} - {invoice.invoice_description} ({invoice.payment_date}) - {invoice.balance}")

        while True:
            choice = input("Enter the number of the invoice you would like to select: ")
            try:
                choice = int(choice)
                if choice < 1 or choice > len(invoice_list):
                    raise ValueError()
            except ValueError:
                print("Invalid input. Please enter a number between 1 and ", len(invoice_list))
            else:
                break

        selected_invoice = invoice_list[choice - 1]
        print(f"You have selected Invoice {selected_invoice.invoice_id} - {selected_invoice.invoice_description}.")
        return selected_invoice



#TESTING FOR METHOD: createInvoice()
#invoice = Invoice(1, "Room rental fee", "2022-04-01")

print("\nCreate Invoice Method:\n----------------------------------------------")
print("NOTE:")
room = Room(1, "101", "Single", "A cozy room with a view")
reservation = Reservation(1, "2023-03-01", room)
customer = Customer(123, "John", "Green", "123 Maroon St", "514-123-1234", "johngreen@none.com")
invoice = Invoice("001", customer,"", "Consulting services", "04-12-23")
invoice.createInvoice("Hotel Services", 500)

#Printing a test for the first invoice
print("\t\tINVOICE")
print("-------------------------------------------")
print(f"Invoice ID: {invoice.invoice_id}")
print(f"Customer Name: {customer.get_first_name()} {customer.get_last_name()}")
print(f"Reservation ID: {reservation._get_reservation_id()}")
print(f"Description: {invoice.invoice_description}")
print(f"Payment Date: {invoice.payment_date}")
print(f"Balance: {invoice.balance}") 
print("-------------------------------------------")



print("NOTE:")
room6 = Room(1, "101", "Single", "A cozy room with a view")
reservation6 = Reservation(3, "2023-03-01", room)
customer6 = Customer(123, "Greg", "Simons", "123 Red St", "514-543-5634", "gregsimons@none.com")
invoice6 = Invoice("023", customer,"", "Hotel and Addtional Services", "03-23-23")

invoice6.createInvoice("Hotel and Additional Services", 1000)

#Printing a test for a second invoice
print("\n\t\tINVOICE")
print("-------------------------------------------")
print(f"Invoice ID: {invoice6.invoice_id}")
print(f"Customer Name: {customer6.get_first_name()} {customer6.get_last_name()}")
print(f"Reservation ID: {reservation6._get_reservation_id()}")
print(f"Description: {invoice6.invoice_description}")
print(f"Payment Date: {invoice6.payment_date}")
print(f"Balance: {invoice6.balance}") 
print("-------------------------------------------")


print("\nSelect Invoice Method:\n----------------------------------------------")
#Testing for selectInvoice
invoice1 = Invoice(1, "Room rental fee", "2022-04-01", 200.0)
invoice2 = Invoice(2, "Cleaning fee", "2022-05-01", 100.0)
invoice3 = Invoice(3, "Late payment fee", "2022-06-01", 50.0)

invoice_list = [invoice1, invoice2, invoice3]

selected_invoice = invoice1.selectInvoice(invoice_list)
