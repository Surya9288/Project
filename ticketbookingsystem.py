# Ticket booking system

class Ticket:
    def __init__(self, name, age, depature, destination, date, price, num_seats):
        self.name = name
        self.age = age
        self.depature = depature
        self.destination = destination
        self.date = date
        self.price = price
        self.num_seats = num_seats

class TicketBookingSystem:
    def __init__(self):
        self.tickets = []

    def book_ticket(self, name, age, depature, destination, date, price,):
        ticket = Ticket(name, age, depature, destination, date, price)
        self.tickets.append(ticket)
        print("Ticket booked.")

    def display_tickets(self):
        if not self.tickets:
            print("No tickets booked yet")
        else:
            print("Booked Tickets:")
            for i, ticket in enumerate(self.tickets,1):
                print(f"Ticket {i}:")
                print(f"Name : {ticket.name}")
                print(f"Age : {ticket.age}")
                print(f"depature : {ticket.depature}")
                print(f"Destination : {ticket.destination}")
                print(f"Date : {ticket.date}")
                print(f"Price : {ticket.price}")
                print()

def main():
    ticketsystem = TicketBookingSystem()

    while True:
        print("1. Book Ticket")
        print("2. View Booked Tickets")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your Name: ")
            age = input("Enter your Age: ")
            depature = input("Enter your Depature: ")
            destination = input("Enter your Destination: ")
            date = input("Enter your Date: ")
            price = input("Enter your Price: ")
    
            ticket_system.book_ticket(name, age, depature, destination, date, price)
        elif choice == '2':
            ticket_system.display_tickets()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()  

