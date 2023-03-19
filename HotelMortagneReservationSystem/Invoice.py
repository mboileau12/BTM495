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
