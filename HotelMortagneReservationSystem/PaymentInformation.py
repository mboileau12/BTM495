class PaymentInformation:
    def __init__(self, payment_id, payment_amount, payment_type, card_number, expiration_date, security_code,
                 billing_address):
        self.payment_id = payment_id
        self.payment_amount = payment_amount
        self.payment_type = payment_type
        self.card_number = card_number
        self. expiration_date = expiration_date
        self.security_code = security_code
        self.billing_address = billing_address


    #getter and setter for payment info id
    def _set_payment_id(self, id):
        self.payment_id = id

    def _get_payment_id(self):
        return self.payment_id

    # getters and setters for payment amount
    def _set_payment_amount(self, amount):
        self.payment_amount = amount

    def _get_payment_amount(self):
        return self.payment_amount

    # getters and setters for payment type
    def set_payment_type(self, type):
        self.payment_type = type

    def get_payment_type(self):
        return self.payment_type

    # getters and setters for payment card number
    def _set_card_number(self, cardNumber):
        self.card_number = cardNumber

    def _get_card_number(self):
        return self.card_number

    #getter and setter for expiration date
    def _set_exipiration_date(self, date):
        self.expiration_date = date

    def _get_expiration_date(self):
        return self.expiration_date

    #getter and setter for security code
    def _set_security_code(self, code):
        self.security_code = code

    def _get_security_code(self):
        return self.security_code

    #getter and setter for billing address
    def _set_billing_address(self, bill_address):
        self.billing_address = bill_address

    def _get_billing_address(self):
        return self.billing_address