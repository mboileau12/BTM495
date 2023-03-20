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

    def searchReservation(self, reservation_id):
        if self.reservation_id == reservation_id:
            return self
        else:
            return None
        
    def selectReservation(self, available_reservations):
        if not available_reservations:
            print("No available reservations.")
            return None

        print("Available Reservations:")
        for i, res in enumerate(available_reservations):
            print(f"{i + 1}. Reservation ID: {res.reservation_id} - Date: {res.reservation_date} - Number of Occupants: {res.number_of_occupants}")

        while True:
            choice = input("Enter the number of the reservation you would like to select: ")
            try:
                choice = int(choice)
                if choice < 1 or choice > len(available_reservations):
                    raise ValueError()
            except ValueError:
                print("Invalid input. Please enter a number between 1 and ", len(available_reservations))
            else:
                break

        return available_reservations[choice - 1]


#Testing for method: createReservation
room = Room(1, "101", "Single", "A cozy room with a view")


reservation = Reservation(1, "2023-03-01", room)


room.set_reservation(reservation)

print("\nCreate Reservation Method:\n----------------------------------------------")
#calling the createReservation() method.
print("Create Reservation Method:")
reservation.createReservation("2023-03-01", 2) 
reservation.createReservation("2023-03-02", 2)



print("\nSearch Reservation Method:\n----------------------------------------------")
#calling the searchReservation()
reservation2 = Reservation(2, "2023-03-02", room)

result = reservation.searchReservation(1)
if result is not None:
    print(f"Found reservation {result.reservation_id} with date {result.reservation_date}")
else:
    print("Reservation not found")

result = reservation2.searchReservation(3)
if result is not None:
    print(f"Found reservation {result.reservation_id} with date {result.reservation_date}")
else:
    print("Reservation not found")



print("\nSelect Reservation Method:\n----------------------------------------------")
#Testing for selectReservation()
room1 = Room(1, "101", "Single", "A cozy room with a view")
room2 = Room(2, "102", "Double", "A spacious room with a balcony")
room3 = Room(3, "103", "Suite", "A luxurious suite with a jacuzzi")

reservation1 = Reservation(1, "2023-03-01", room1)
reservation2 = Reservation(2, "2023-03-02", room2)
reservation3 = Reservation(3, "2023-03-03", room3)

available_reservations = [reservation1, reservation2, reservation3]

my_reservation = Reservation(4)

selected_reservation = my_reservation.selectReservation(available_reservations)

if selected_reservation is not None:
    print(f"Selected reservation ID: {selected_reservation.reservation_id}")
else:
    print("No reservation was selected.")