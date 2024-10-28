import random

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

    def drive(self, hours: float):
        self.distance += self.current_speed * hours


    def display(self):
        print(f"{self.registration:<10}{self.max_speed:<15}{self.current_speed:<15}{self.distance:<15}")

cars = []
for i in range(1,11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(registration, max_speed))

race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.distance >= 10000:
            race_finished = True
            break


print(f"\n Race results:")
print(f"{'Registration':<10} {'Max Speed(km/h)':<15} {'Current Speed(km/h)':<15} {'Distance(km)':<15}")
print("-" * 55)
for car in cars:
    car.display()


