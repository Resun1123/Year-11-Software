#Add attribute weight and write a getter method for weight
#Add setter method or weight and make sure it is a positive number (integer or float)
#Comment your code appropriately




class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0
    # defining a setter method for the name and making sure it is a string
    def set__name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print("Name must be a string")
    # defining a getter method for the name and returning the name
    def get_name(self):
        return self._name
    # defining a getter method for the weight and returning the weight
    def get_weight(self):
        return self.weight
    
    # defining the setter method the weight and making sure its positive
    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print("Weight must be a positive number")
        else:
            print("Weight must be a number")
p1 = Pet(name = 'Bonnie', category = 'Dog', age = 10)
p1.set_weight(10)
p1.set__name('Bonnifer')
print('Pet Name: ',p1.get_name())
print('Pet Weight: ',p1.get_weight()) 

