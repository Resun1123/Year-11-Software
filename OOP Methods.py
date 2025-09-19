print("Welcome to the Pet Data Management System")
print("Every vet's best friend")

class Pet:
    def __init__(self, name, category, age=0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0
    # add a method to vaccianate the pet
    def vaccinate(self):
        self.vaccinated = True
        print(f'{self.name} has been vaccinated.')
    # add a method to vaccinate the pet with an alternative method
    def vaccinate_alternative(self):
        if not self.vaccinated:
            self.vaccinated = True
            print(f'{self.name} has received an alternative vaccination.')
        else:
            print(f'{self.name} is already vaccinated.')
    #A method to clear out the balance 
    def clear_balance(self):
        self.account_balance = 0
        print(f'{self.name} account balance has been cleared.')
    # Adding a method get the pet age in Human years if Dog multiply by 7 and if Cat multiply by 6
    def get_human_years(self):
        human_years = self.age * 7 if self.category.lower() == 'dog' else self.age * 6
        print(f'{self.name} is {human_years} human years old.')
        return human_years
    # Adding a method to check the payment details of the pet
    def __str__(self):
        payment_details = 'registered' if len(self.ccard) == 19 else 'unregistered'
        return f'Name: {self.name}\nCategory: {self.category}\nPet Age: {self.age}\nVaccination Status: {self.vaccinated}\nPayment Details: {payment_details}'

# Creating instances
p1 = Pet('Bonnie', 'cat', 3)
p2 = Pet('Foxy', 'dog', 7)
p3 = Pet('Ashil', 'cat', 15)
p4 = Pet('Hootie', 'cat', 34)

Pets = [p1, p2, p3, p4]

for pet in Pets:
    print(pet)
    print(" ")