class Invoice:

   def _init_(self, invoice_id, invoice_description, payment_date, balance):
       
       self.invoice_id = invoice_id
       self.invoice_description = invoice_description
       self.payment_date = payment_date
       self.balance = balance

    
    #getter and setter for invoice id
    def _set_invoice_id(self, id)
        self.invoice_id = id
    
    def _get_invoice_id(self)
        return self.invoice_id

    #getter and setter for invoice description
    def _set_invoice_description(self, input)
        self.invoice_description = input
    
    def _get_invoice_description(self)
        return self.invoice_description

    #getter and setter for invoice description
    def _set_payment_date(self, date)
        self.payment_date = date
    
    def _get_payment_date(self)
        self.payment_date
    

    #getter and setter for balance
    def _set_balance(self, amount)
        self.balance = amount
    
    def _get_balance(self)
        return self.balance

        