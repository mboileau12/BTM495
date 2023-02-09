class Service:

    def _init_(self, service_name, service_type, service_description, service_rates = 0, service_status):
        self.service_name = service_name
        self.service_type = service_type
        self.service_description = service_description
        self.service_rates = service_rates
        self.service_status = service_status

    #getter and setter for service name
    def _set_service_name(self, input)
        self.service_name = input

    def _get_service_name(self)
        return self.service_name

    #getter and setter for service type
    def _set_service_type(self, input)
        self.service_type = input

    def _get_service_type(self)
        return self.service_type
    
    #getter and setter for service description
    def _set_service_description(self, input)
        self.service_description = input

    def _get_service_description(self)
        return self.service_description
    
    #getter and setter for service rates

    def _set_service_rates(self, price)
        self.service_rates = price

    def _get_service_rates(self)
        return self.service_rates

    #getter and setter for service status

    def _set_service_status(self, input)
        self.service_status = input

    def _get_service_status(self)
        return self.service_status
         