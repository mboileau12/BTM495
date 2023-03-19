class Reservation:
    def __init__(self, reservation_id, reservation_date, no_of_occupants, rooms, booked_customer, check_in):
        self.reservation_id = reservation_id
        self.reservation_date = reservation_date
        self.no_of_occupants = no_of_occupants
        self.rooms = rooms
        self.booked_customer = booked_customer
        self.check_in = check_in

    def search_Reservation(self, reservation):
        return self if reservation.booked_customer == self.booked_customer and reservation.rooms == self.rooms else None

    def select_Reservation(self, room):
        return self if self.rooms == room else None

    def update_Reservation(self, check_in):
        if self.booked_customer == check_in.booked_customer and self.rooms == check_in.rooms:
            self.check_in = check_in.check_in


class Room:
    def __init__(self, room_id, room_status):
        self.room_id = room_id
        self.room_status = room_status

    def retrieve_Room_Status(self):
        return self.room_status

    def update_Room_Availability(self, reservation, room):
        if self.room_status == "available" and self.room_id == room:
            self.room_status = "occupied"
            reservation.rooms = room
