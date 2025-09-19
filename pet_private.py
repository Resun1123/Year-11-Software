#Complete these activities:
#Make category a private attribute than test to make sure it can't be changed once created
#Add another private attribute for breed
#Comment your code appropriately.






class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False

    def have_birthday(self):
        self.age += 1

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Dog', age = 10)
p1._name = 'Bonnifer'
print(p1._name)
p1.__category = "Cat"
# This will raise an error because __category is private
# Sir I am not able to change the value of __category
# I am a bit confused about the private attribute
print(p1.__category)
print(p1)
