#Create a new python file called car.py (or something similar)
 #Create a class for a car. 
 #What key properties will you include for a generic car? 
 #To see the output of your code, print the key properties of your class.
 #Remember that you can create sub-classes for specific vehicles that can inherit these general properties.Comment your code appropriately and add your final code here.


class Car:
    def __init__(self,make,model,year,colour,price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.price = price
        self.mileage = mileage
        self.owner = 'unknown'
        self.registration_number = 'unknown'

class Supra(Car):
    def __init_subclass__(cls):
        return super().__init_subclass__()
    
class Nissan(Car):
    def __init__subclass__(cls):
        return super().__init_subclass__()
    
Car1 = Supra("Toyota", "Supra", 2004, "Grey", 20000, 120000)
Car2 = Nissan("Nissan", "GTR", 2010, "Black", 50000, 80000)


print("Car 1 Details:", Car1.make, Car1.year, '$',Car1.price)



        