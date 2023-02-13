class Customer:
    def __init__(self, customer_id, first_name, last_name, address, phone_number,
                 email_address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address

    #get and set methods for customer_id
    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, id):
        self.customer_id = id

    #get and set methods for firstname
    def get_first_name(self):
        return self.first_name

    def set_first_name(self, fname):
        self.first_name = fname

    #get and set methods for lastname
    def get_last_name(self):
        return self.last_name

    def set_last_name(self, lname):
        self.last_name = lname

    #get and set methods for address
    def get_address(self):
        return self.address

    def set_address(self, cust_address):
        self.address = cust_address

    # get and set methods for phone number
    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, number):
        self.phone_number = number

    # get and set methods for email
    def get_email_address(self):
        return self.email_address

    def set_email_address(self, email):
        self.email_address = email







