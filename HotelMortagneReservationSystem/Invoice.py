from datetime import datetime

class Invoice:
    def __init__(self, invoice_id, invoice_description, payment_date, balance=0):
        self.invoice_id = invoice_id
        self.invoice_description = invoice_description
        self.payment_date = payment_date
        self.balance = balance
    
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
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
        invoice_id = f"{timestamp}-{self.invoice_id}"
        self.invoice_id = invoice_id
        self.invoice_description = invoice_description
        self.balance += amount

        print(f"Invoice {self.invoice_id} has been created with a balance of {self.balance}.")

    
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
invoice = Invoice(1, "Room rental fee", "2022-04-01")


print("NOTE:")
invoice.createInvoice("test desc", 200.0)

#Printing a test for the first invoice
print("\t\tINVOICE")
print("-------------------------------------------")
print(f"Invoice ID: {invoice.invoice_id}")
print(f"Description: {invoice.invoice_description}")
print(f"Payment Date: {invoice.payment_date}")
print(f"Balance: {invoice.balance}") # Should print 200.0
print("-------------------------------------------")


print("NOTE:")
invoice.createInvoice("test desc 2", -100.0)


#Printing a test for a second invoice
print("\n\t\tINVOICE")
print("-------------------------------------------")
print(f"Invoice ID: {invoice.invoice_id}")
print(f"Description: {invoice.invoice_description}")
print(f"Payment Date: {invoice.payment_date}")
print(f"Balance: {invoice.balance}") # Should print 100.0
print("-------------------------------------------")


#Testing for selectInvoice
invoice1 = Invoice(1, "Room rental fee", "2022-04-01", 200.0)
invoice2 = Invoice(2, "Cleaning fee", "2022-05-01", 100.0)
invoice3 = Invoice(3, "Late payment fee", "2022-06-01", 50.0)

invoice_list = [invoice1, invoice2, invoice3]

selected_invoice = invoice1.selectInvoice(invoice_list)
