from Room import Room
class Reservation:

    def __init__(self, reservation_id, reservation_date ="", room = "", number_of_occupants=0):
        self.reservation_id = reservation_id
        self.reservation_date = reservation_date
        self.number_of_occupants = number_of_occupants
        self.room = room

    # getter and setter for reservation id
    def _set_reservation_id(self, id):
        self.reservation_id = id

    def _get_reservation_id(self):
        return self.reservation_id

    # getter and setter for reservation date
    def _set_reservation_date(self, date):
        self.reservation_date = date

    def _get_reservation_date(self):
        return self.reservation_date

    # getter and setter for number of occupants within a reservation
    def _set_number_of_occupants(self, numOfOccupants):
        self.number_of_occupants = numOfOccupants

    def _get_number_of_occupants(self):
        return self.number_of_occupants

    def createReservation(self, reservation_date, number_of_occupants):
        if self.room.get_reservation() is not None:
            existing_reservation = self.room.get_reservation()
            if existing_reservation.reservation_date == reservation_date:
                print("Sorry, this room is already reserved for the selected date.")
                return

        self.reservation_date = reservation_date
        self.number_of_occupants = number_of_occupants
        self.room.set_reservation(self)
        print(f"Reservation for {number_of_occupants} occupants in room {self.room.room_number} has been created for {reservation_date}.")


room = Room(room_id=1, room_number="101", room_type="Single", room_description="A cozy room with a view")


reservation = Reservation(reservation_id=1, reservation_date="2022-01-01", room=room)


room.set_reservation(reservation)

#calling the createReservation() method.
reservation.createReservation("2022-01-01", 2) 
reservation.createReservation("2022-01-02", 2)
