# Cafeteria App:

# Develop a Python program that simulates a restaurant reservation system, allowing users to reserve tables and manage their bookings.

# Requirements:

#     Create a Restaurant class to represent the restaurant establishment.

#     Define attributes for the Restaurant class, such as name, address, phone number, and menu.

#     Create a Table class to represent individual tables in the restaurant.

#     Define attributes for the Table class, such as table_number, capacity, and availability.

#     Create a Reservation class to represent individual customer reservations.

#     Define attributes for the Reservation class, such as customer_name, party_size, reservation_time, and table_id.

#     Implement methods for the Restaurant class to manage tables and reservations:

#     a. add_table() to add new tables to the restaurant's table list.

#     b. list_tables() to display a list of all available tables.

#     c. reserve_table() to accept a reservation request, checking availability and updating the Table and Reservation objects accordingly.

#     Implement methods for the Table class to manage its availability:

#     a. is_available() to check if the table is available for a particular reservation time.

#     b. mark_available() to set the table's availability to true.

#     c. mark_unavailable() to set the table's availability to false.

#     Implement methods for the Reservation class to manage customer bookings:

#     a. calculate_total() to calculate the total cost of the reservation based on the menu items ordered.

#     b. print_reservation() to display a detailed summary of the reservation details.

#     Create a user interface (UI) using the console module to facilitate user interaction with the reservation system.

#     Allow users to perform the following actions:

# a. View the restaurant's details and menu.

# b. Browse available tables and make reservations.

# c. View their existing reservations and cancel them if necessary.

# d. Manage their reservation details, such as adding or removing guests.

# Additional Challenges:

#     Implement a payment system to handle the processing of reservation payments.

#     Develop a web application using Django or Flask to provide a more user-friendly interface for managing reservations.


class Restaurant:
    def __init__(self, name, address, phone_number, menu):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.menu = menu
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def list_tables(self):
        for table in self.tables:
            print(
                f"Table {table.table_number} - Capacity: {table.capacity} - Availability: {table.availability}"
            )

    def reserve_table(self, customer_name, party_size, reservation_time):
        for table in self.tables:
            if table.table_number == table.is_available():
                table.mark_unavailable()
                reservation = Reservation(customer_name, party_size, reservation_time)
                return reservation
        return None


class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.availability = True

    def is_available(self):
        return self.availability

    def mark_available(self):
        self.availability = True

    def mark_unavailable(self):
        self.availability = False


class Reservation:
    pass
