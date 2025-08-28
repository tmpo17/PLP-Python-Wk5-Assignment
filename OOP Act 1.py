class Car:
   def __init__(self, brand, model):
       self.brand = brand
       self.model = model

   def drive(self):
       print(f"The {self.brand} {self.model} is fast!")

my_car = Car("Mercedes", "Benz")
my_car.drive()

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def charge(self):
        print(f"Charging the {self.brand} {self.model} that has a {self.battery_size}-kWh battery.")

my_electric_car = ElectricCar("Tesla", "Model S", 100)
my_electric_car.drive()
my_electric_car.charge()
