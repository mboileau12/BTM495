class Reservations:

    def _init_(self, reservation_id, reservation_date, number_of_occupants = 0):
        self.reservation_id = reservation_id
        self.reservation_date = reservation_date
        self.number_of_occupants = number_of_occupants

    #getter and setter for reservation id
    def _set_reservation_id(self, id)
        self.reservation_id = id
    
    def _get_reservation_id(self)
        return self.reservation_id
    
    #getter and setter for reservation date
    def _set_reservation_date(self, date)
        self.reservation_date = date
    
    def _get_reservation_date(self)
        return self.reservation_date
    
    #getter and setter for number of occupants within a reservation
    def _set_number_of_occupants(self, numOfOccupants)
        self.number_of_occupants = numOfOccupants
    
    def _get_number_of_occupants(self)
        return self.number_of_occupants