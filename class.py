name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(card_num):
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False

def verify_vaccination(Vaccinated):
  print(f"is {animal_category} vaccinated? Type 1 for yes and 2 for no")
  to_vaccinate = int(input('Please Enter your choice:'))
  if to_vaccinate == 1:
    print("Vaccinated Already")
    if to_vaccinate == 2:
      print("Vaccination Required")


if verify_credit_card("1234 4334 1001 0000") == True:
  print('Valid Credit Card')
  print("Deducted $39", ",New Balcane:",  account_balance - 39.00) 
else:
  print("Invalid Credit Card")


help()
increase_age()
print(age)
