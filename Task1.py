class Car:
    def __init__(self, registration, max_speed:int):
        self.registration = registration
        self.max_speed = max_speed
        self.distance = 0
        self.current_speed = 0

    def display(self):
        print(f"Registration: {self.registration}")
        print(f"Max speed: {self.max_speed}km/h")
        print(f"Distance: {self.distance}km")
        print(f"Current speed: {self.current_speed}")

car = Car("ABC-123",142)
car.display()