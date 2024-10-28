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


    def display(self):
        print(f"Registration: {self.registration}")
        print(f"Max speed: {self.max_speed}km/h")
        print(f"Distance: {self.distance}km")
        print(f"Current speed: {self.current_speed}")

car = Car("ABC-123",142)
car.display()

car.accelerate(30)
print(f"Current speed after accelerating 30km/h: {car.current_speed} km/h")

car.accelerate(70)
print(f"Current speed after accelerating 70km/h: {car.current_speed} km/h")

car.accelerate(50)
print(f"Current speed after accelerating 50km/h: {car.current_speed}")

car.accelerate(-200)
print(f"Emergency brake applied as the has exceeded the max speed of the car: {car.current_speed}")
