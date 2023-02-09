class Room:

    def _init_(self, room_id, room_number, room_type, room_description, room_rates, room_status):
        self.room_id = room_id
        self.room_number = room_number
        self.room_type = room_type
        self.room_description = room_description
        self.room_rates = room_rates
        self.room_status = room_status

    #getter and setter for room id
    
    def _set_room_id(self, id)
        self.room_id = id
    
    def _get_room_id(self)
        return room_id

    #getter and setter for room number
    #input is considered a string because we're assuming there could be rooms named "Room 10 A" AKA 
    #what is displayed on the website or in company's database
    def _set_room_number(self, input)
        self.room_number = input
        
    def _get_room_number(self)
        return room_number

    #getter and setter for room type
    def _set_room_type(self, input)
        self.room_type = input
    
    def _get_room_type(self)
        return self.room_type

    #getter and setter for room description
    def _set_room_description(self, input)
        self.room_description = input
    
    def _get_room_description(self)
        return self.room_description

    #getter and setter for room_rates
    def _set_room_rates(self, price)
        self.room_rates = price
    
    def _get_room_rates(self)
        return self.room_rates

    #getter and setter for room status
    def _set_room_status(self, status)
        self.room_status = status
    
    def _get_room_status(self)
        return self.room_status
        
