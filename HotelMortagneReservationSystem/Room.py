class Room:
    def __init__(self, room_id, room_number, room_type, room_description, room_rates=0, room_status="", reservation=None):
        self.room_id = room_id
        self.room_number = room_number
        self.room_type = room_type
        self.room_description = room_description
        self.room_rates = room_rates
        self.room_status = room_status
        self.reservation = reservation


    def set_reservation(self, reservation):
        self.reservation = reservation

    def get_reservation(self):
        if self.reservation:
            return self.reservation
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

    def search_room(self, num_occupants, room_list):
        print("gets in the method")
        available_rooms = []
        for room in room_list:
            if room.room_status == "available" and room.room_rates > 0 and room.reservation is None:
                if room.room_rates >= num_occupants:
                    available_rooms.append(room)
        return available_rooms

    def select_room(self, available_rooms):
        if not available_rooms:
            print("No available rooms.")
            return None

        print("Available Rooms:")
        for i, room in enumerate(available_rooms):
            print(f"{i + 1}. {room.room_number} - {room.room_type} ({room.room_description}) - {room.room_rates}")

        while True:
            choice = input("Enter the number of the room you would like to select: ")
            try:
                choice = int(choice)
                if choice < 1 or choice > len(available_rooms):
                    raise ValueError()
            except ValueError:
                print("Invalid input. Please enter a number between 1 and ", len(available_rooms))
            else:
                break

        return available_rooms[choice - 1]


room1 = Room(1, "101", "Standard", "A standard room with a queen-sized bed", 100, "available")
room2 = Room(2, "102", "Standard", "A standard room with two double beds", 120, "available")
room3 = Room(3, "201", "Deluxe", "A deluxe room with a king-sized bed and a balcony", 150, "available")
room4 = Room(4, "202", "Deluxe", "A deluxe room with two queen-sized beds and a balcony", 180, "occupied")
room5 = Room(5, "301", "Suite", "A suite with a king-sized bed, a separate living room, and a kitchenette", 250, "available")

room_list = [room1, room2, room3, room4, room5]

reservation_date = "2023-03-20"
num_occupants = 2

print("Search Room Method:")
available_rooms = room1.search_room(num_occupants, room_list)

for room in available_rooms:
    print(room.room_number)


# Calling the select_room()
print("Select Room Method:")

available_rooms = room1.search_room(2, room_list)
selected_room = room1.select_room(available_rooms)

if selected_room:
    print(f"You have selected room {selected_room.room_number} - {selected_room.room_type} ({selected_room.room_description}) for {reservation_date}. The room rate is {selected_room.room_rates}.")


















