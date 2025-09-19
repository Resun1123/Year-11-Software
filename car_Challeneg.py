#Instantiate another car object
#Add another attribute (for_sale)
#Add sale status for sale or not for sale to the __str__ method
#Create two more cars and print all car statuses with a loop


class Car:
    def __init__(self,make,model,year,price=None,for_sale = None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = for_sale

    def __str__(self):
        return f'Make:{self.make}, Model:{self.model}, (Made in: {self.year}) - Price: ${self.price}' # Added for sale to the __str__ method 
# Different cars with different attributes    
car1 = Car('Toyota', 'Supra', 2004, 20000, True)
car2 = Car('Nissan', 'GTR', 2010, 50000, False)
car3 = Car('Honda','Civic',2015, 15000, False)

Cars = [car1, car2, car3]

for car in Cars:
    print("========================")
    print(car)
    print("========================")
x = input('Which car do you want to buy')
if x == car1:
        print(f'You have selected {car1.make} {car1.model} for ${car1.price}')
if x == car2:
        print(f'You have selected {car2.make} {car2.model} for ${car2.price}')
if x == car3:
        print(f'You have selected {car3.make} {car3.model} for ${car3.price}')
    # Added a check for the for_sale attribute 

if car.for_sale == True:
        print(f'Make:{car.make}, Model:{car.model} is for Sale')
else:
        print(f'Make:{car.make}, Model:{car.model} is not for Sale')

# to ask the user which car they want to buy and if it is available for sale 


        