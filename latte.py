drinks = ['Latte', 'Cappuccino', 'Espresso', 'Mocha']
snacks = ['Cookies', 'Muffin', 'Croissant']
specials = ['Gasoline']

regDrinkPrice = 3.50
lrgDrinkPrice = 4.50

#print menu
print('Welcome to the Coffee Shop!')
print('\nHere is our drink menu: ')
print("(Regular: £3.50)  (Large: £4.50)")
for drink in drinks:
  print(drink)
  
print('\nHere is our snack menu: ')
print('(All snacks £2.00)')
for snack in snacks:
  print(snack)
  
print("Today's special menu item is: ")
for special in specials:
  print(special)
  print("Buy today at just £5.00!")

#create empty lists to store purchases
drinksPurchase = []
snacksPurchase = []
specialsPurchase = []

#ask user what they would like
askDrink = input('\nWhat type of drink would you like? ')
askSnack = input('What type of snack would you like? ')
askSpecial = input('What type of special would you like? ')

#add user choices to empty lists
drinksPurchase.append(askDrink)
snacksPurchase.append(askSnack)
specialsPurchase.append(askSpecial)

#ask if user would like to purchase more
morePurchase = input('\nWould you like to purchase anything else? (y/n) ')

#if statement that allows user to purchase multiple items
while morePurchase == 'y':
  askDrink2 = input('What type of drink would you like? ')
  askSnack2 = input('What type of snack would you like? ')
  askSpecial2 = input('What type of special would you like? ')
  
  drinksPurchase.append(askDrink2)
  snacksPurchase.append(askSnack2)
  specialsPurchase.append(askSpecial2)
  
  morePurchase = input('Would you like to purchase anything else? (y/n) ')
