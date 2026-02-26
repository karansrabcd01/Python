"""
OOP Inheritance Demo in Python
Shows:
- Inheritance
- Constructor chaining with super()
- Method overriding
- Polymorphism
- Encapsulation via a protected attribute convention
"""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._is_running = False  # protected-style attribute by convention

    def start(self):
        self._is_running = True
        return f"{self.brand} {self.model} started."

    def stop(self):
        self._is_running = False
        return f"{self.brand} {self.model} stopped."

    def info(self):
        return f"Vehicle: {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def info(self):  # method overriding
        return f"Car: {self.brand} {self.model}, Seats: {self.seats}"


class Bike(Vehicle):
    def __init__(self, brand, model, has_gears):
        super().__init__(brand, model)
        self.has_gears = has_gears

    def info(self):  # method overriding
        gears_text = "Yes" if self.has_gears else "No"
        return f"Bike: {self.brand} {self.model}, Gears: {gears_text}"


# Multilevel inheritance example
class ElectricCar(Car):
    def __init__(self, brand, model, seats, battery_kwh):
        super().__init__(brand, model, seats)
        self.battery_kwh = battery_kwh

    def info(self):  # overriding again
        return (
            f"Electric Car: {self.brand} {self.model}, "
            f"Seats: {self.seats}, Battery: {self.battery_kwh} kWh"
        )


def print_vehicle_details(vehicle):
    """Polymorphism: accepts any Vehicle subclass."""
    print(vehicle.info())
    print(vehicle.start())
    print(vehicle.stop())
    print("-" * 45)


if __name__ == "__main__":
    c1 = Car("Toyota", "Corolla", 5)
    b1 = Bike("Yamaha", "MT-15", True)
    e1 = ElectricCar("Tesla", "Model 3", 5, 60)

    # Same function, different subclass behaviors (polymorphism)
    for item in [c1, b1, e1]:
        print_vehicle_details(item)


"""
Sample Output:
Car: Toyota Corolla, Seats: 5
Toyota Corolla started.
Toyota Corolla stopped.
---------------------------------------------
Bike: Yamaha MT-15, Gears: Yes
Yamaha MT-15 started.
Yamaha MT-15 stopped.
---------------------------------------------
Electric Car: Tesla Model 3, Seats: 5, Battery: 60 kWh
Tesla Model 3 started.
Tesla Model 3 stopped.
---------------------------------------------
"""
