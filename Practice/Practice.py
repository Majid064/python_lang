import random

class Train():
    def book(self , trainNo , fro , to):
        print(f"ticket is booked in train no: {trainNo} form {fro} to {to}")

    def getStatus(self , trainNo):
        pass

    def getFare(self , trainNo , fro , to):
        print(f"ticket fare in train no: {trainNo} form {fro} to {to} is {random.randint(222,5555)}")