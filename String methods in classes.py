

#Add a default new credit card value  of unknown
 #In the __str__ method, let the user know if the pet has registered payment details  
 #Add the vaccinated status  and include it in the special __str__ function




class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False   
    # define a string to show the payment details of the pet
    
    def __str__(self):
        payment_Details = 'unregisterd'
        if len(self.ccard) == 19:
            payment_Details = 'registerd'

        my_status = 'Name: ' + self.name + '\nCategory:' + self.category + '\nAge:' + str(self.age) + '\nVaccination Status: ' + str(self.vaccinated)  + '\nPayment Details: ' + str(self.payment_Details)
        return my_status
    #returns the status of the pet giving the name category annd age etc

#Add another pet to the list (try different methods)
#Vaccinate each pet in the list using a FOR loop


p1 = Pet('Bonnie', 'Cat', 3)   
p2 = Pet('Jayden', 'lizard', 3) #added another pet for the list      
#start for loop to vaccinate each pet in the list
#first create a list for all the pets

pets = [p1, p2]
for pet in pets:
    print(pet)
    print(" ")