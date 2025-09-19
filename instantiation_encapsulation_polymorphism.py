#---begin Python ---
class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    def report(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Colour: {self.colour}")
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")


# Instantiating objects from the Car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")
car3 = Car("Ford","Mustang", 2021,"Black")

car3.report()
car2.start()



