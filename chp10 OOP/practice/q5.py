'''
1 2 3 4 5 6 7 8 9 10
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seats, seatNo):
       ''' if seatNo in range(self.seats):
            print(f"Your seat no {seatNo} is cancelled")
            self.seats = self.seats + 1
        else :
            print(f"Your seat no {seatNo} is not present in the booking list")
      '''
       pass

intercity = Train("Intercity Express: 14015", 90, 10) # can change the seat
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
# intercity.cancelTicket(7,8) 