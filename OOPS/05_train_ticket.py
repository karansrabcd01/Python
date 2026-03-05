"""
Problem Statement:-
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.

"""

""" 
Understood: 
    Class Train
    1. Book Ticket
    2. Get Status (number of seats available)
    3. Get Fare information

 """

class Train:
    
    def __init__(self, train_name, total_seats, fare_per_ticket):
        """
        Constructor Method.
        Initializes train details.

        tarin_name -> Name Of the train
        total_seats -> Total available seats
        fare_per_ticket-> Ticket price

        """
        self.train_name=train_name
        self.total_seats=total_seats
        self.available_seats=total_seats #Initially all seats are available
        self.fare_per_ticket=fare_per_ticket
    
    # Method to book ticket
    def book_ticket(self, seats_requested):
        """
        Books Seats if available.
        Reduces available seats after Booking.

        """

        if seats_requested<=0:
            print("Please enter a valid number of seats.")

        elif seats_requested>self.available_seats:
            print("Sorry! Not Enough seats available")
        
        else:
            self.available_seats -= seats_requested
            total_cost = seats_requested * self.fare_per_ticket
            print(f"{seats_requested} seats booked successfully!")
            print(f"Total Fare:₹{total_cost}")
    

    #Method to check seat status
    def get_status(self):

        """
        Display available seats.

        """

        print(f"Train: {self.train_name}")
        print(f"Available seats: {self.available_seats}/{self.total_seats}")

    # Method to get fare information
    def get_fare_info(self):
        """
        Displays fare per ticket.

        """

        print(f"Train: {self.train_name}")
        print(f"Fare per ticket: ₹{self.fare_per_ticket}")


#creating object of Train Class

train1=Train("Rajdhani Express",100,1500)

#check status
train1.get_status()

#get Fare info

train1.get_fare_info()

#Book ticket
train1.book_ticket(3)

#Check status again

train1.get_status()