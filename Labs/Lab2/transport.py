from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, distance, speed, ticket_price):
        self.distance = distance
        self.speed = speed
        self.ticket_price = ticket_price

    @abstractmethod
    def calculate_time(self):
        pass

    @abstractmethod
    def calculate_cost(self, passengers):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} with distance {self.distance} km"

    def __repr__(self):
        return f"<Transport: {self.__class__.__name__}, Distance: {self.distance}, Speed: {self.speed}, Ticket Price: {self.ticket_price}>"

class Bus(Transport):
    def calculate_time(self):
        return self.distance / self.speed

    def calculate_cost(self, passengers):
        return passengers * self.ticket_price

class Train(Transport):
    def calculate_time(self):
        return self.distance / self.speed

    def calculate_cost(self, passengers):
        return passengers * self.ticket_price

class Airplane(Transport):
    def calculate_time(self):
        return self.distance / self.speed

    def calculate_cost(self, passengers):
        return passengers * self.ticket_price