class Pet: # Define a class named Pet
    def __init__(self,name,species,age,vaccination_status): # Give it Attributes
        # This is the constructor method that initializes the attributes of the class
        self.name = name
        self.species = species
        self.age = age
        self.vaccination_status = vaccination_status

    def __str__(self): # Str method to return a string representation of the object
        return f"Name: {self.name} \nSpecies: {self.species} \nAge: {self.age} \nVaccination Status: {self.vaccination_status}"
            

# Create instances of the Pet class
p1 = Pet("Foxy", "Dog", 3 , "Vaccinated")
p2 = Pet("Ashil", "Cat", 15, "Not Vaccninated")
p3 = Pet("Miko", "Penguin", 2, "Vaccinated")
p4 = Pet("Hootie", "Goldfish", 34, "Not Vaccinated")
# Create a list of pets
pets = [p1,p2,p3,p4]

#Print each pet details in the list
for pet in pets: 
    print(pet)
    print(" ")
to_vaccinate = int(input("Which pet do you want to vaccinate? Type 1 for Foxy, 2 for Ashil, 3 for Miko, 4 for Hootie, 5 if you want to vaccinate all of them: "))
def vaccinate(pet): # Defina a function to vaccinate a pet
        
    if to_vaccinate == 1:
        pet = pets[0]
        pet.vaccination_status = 'Vaccinated'
        print(f'{pet.name} has been vaccinated')
    elif to_vaccinate == 2:
        pet = pets[1]
        pet.vaccination_status = 'Vaccinated'
        print(f'{pet.name} has been vaccinated')
    elif to_vaccinate == 3:
        pet = pets[2]
        pet.vaccination_status = 'Vaccinated'
        print(f'{pet.name} has been vaccinated')
    elif to_vaccinate == 4:
        pet = pets[3]
        pet.vaccination_status = 'Vaccinated'
        print(f'{pet.name} has been vaccinated')
    elif to_vaccinate == 5:
        for pet in pets:
            pet.vaccination_status = 'Vaccinated'
            print(f'{pet.name} has been vaccinated')

        else:
            print("Invalid Choice")






