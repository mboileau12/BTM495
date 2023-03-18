from Reservation import Reservation
class Room:
    def __init__(self, room_id, room_number, room_type, room_description, room_rates=0, room_status=""):
        self.room_id = room_id
        self.room_number = room_number
        self.room_type = room_type
        self.room_description = room_description
        self.room_rates = room_rates
        self.room_status = room_status
        self.reservation_date = None


    def set_reservation(self, reservation):
        self.reservation = reservation

    def get_reservation(self):
        if self.reservation:
            return self.reservation.reservation_date
        else:
            return None

    # getter and setter for room id

    def _set_room_id(self, id):
        self.room_id = id

    def _get_room_id(self):
        return self.room_id

    # getter and setter for room number
    # input is considered a string because we're assuming there could be rooms named "Room 10 A" AKA
    # what is displayed on the website or in company's database
    def _set_room_number(self, input):
        self.room_number = input

    def _get_room_number(self):
        return self.room_number

    # getter and setter for room type
    def _set_room_type(self, input):
        self.room_type = input

    def _get_room_type(self):
        return self.room_type

    # getter and setter for room description
    def _set_room_description(self, input):
        self.room_description = input

    def _get_room_description(self):
        return self.room_description

    # getter and setter for room_rates
    def _set_room_rates(self, price):
        self.room_rates = price

    def _get_room_rates(self):
        return self.room_rates

    # getter and setter for room status
    def _set_room_status(self, status):
        self.room_status = status

    def _get_room_status(self):
        return self.room_status

    def searchRoom(self, reservation_date=None, number_of_occupants=None):
        """
        This method searches for rooms based on the given reservation date and/or number of occupants.

        Args:
            reservation_date (str): Date in the format of 'YYYY-MM-DD'
            number_of_occupants (int): Number of occupants required in the room

        Returns:
            List[Room]: List of rooms that match the given search criteria
        """
        matching_rooms = []

        # Check if the room is available on the given reservation date
        if reservation_date is not None:
            if self.get_reservation() == reservation_date:
                matching_rooms.append(self)

        # Check if the room can accommodate the given number of occupants
        if number_of_occupants is not None:
            if self.room_status == "" and number_of_occupants <= self.number_of_occupants:
                matching_rooms.append(self)

        return matching_rooms

# Create some Room objects
room1 = Room(1, "101", "Single", "Standard room", 100)
room2 = Room(2, "102", "Double", "Deluxe room", 150)
room3 = Room(3, "103", "Suite", "Luxury room", 200)

# Set reservations on some rooms
reservation1 = Reservation(1, "2022-03-20", 2)
reservation2 = Reservation(2, "2022-03-22", 1)
reservation3 = Reservation(3, "2022-03-23", 3)
room1.set_reservation(reservation1)
room2.set_reservation(reservation2)
room3.set_reservation(reservation3)

# Test searchRoom() method with different parameters on an instance of Room class
matching_rooms = room1.searchRoom(reservation_date="2022-03-20")
assert len(matching_rooms) == 1 and matching_rooms[0]._get_room_number() == "101"

matching_rooms = room1.searchRoom(number_of_occupants=2)
assert len(matching_rooms) == 2 and {room._get_room_number() for room in matching_rooms} == {"101", "102"}

matching_rooms = room2.searchRoom(room_number="102")
assert len(matching_rooms) == 1 and matching_rooms[0]._get_room_number() == "102"

matching_rooms = room3.searchRoom(room_type="Suite")
assert len(matching_rooms) == 1 and matching_rooms[0]._get_room_number() == "103"

