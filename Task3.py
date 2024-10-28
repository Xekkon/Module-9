class Car:
    def __init__(self, registration, max_speed:int):
        self.registration = registration
        self.max_speed = max_speed
        self.distance = 0
        self.current_speed = 0

    def accelerate(self, speed_change: int):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours:int):
        self.distance += self.current_speed * hours


    def display(self):
        print(f"Registration: {self.registration}")
        print(f"Max speed: {self.max_speed}km/h")
        print(f"Distance: {self.distance}km")
        print(f"Current speed: {self.current_speed}")

car = Car("ABC-123",142)

car.accelerate(100)
print(f"Current speed after accelerating 100km/h: {car.current_speed} km/h")

car.drive(1.5)
print(f"Distance travelled after 1.5h: {car.distance} km")

car.drive(2)
print(f"Distance travelled after an additional 2hours: {car.distance} km")

