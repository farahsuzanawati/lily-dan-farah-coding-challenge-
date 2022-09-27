print("Welcome To Coding Challenge Python")

import random

print("Let's review one of the atomic number")
Element = input("What is atomic number of oxygen")
print ("_______________________________________________")

print("It's just a review for our khowledge. Let's guess the other atomic numbers!")
number = random.randint (1,10)
if number == 1:
  print("This element category is known as natural gas")
elif number == 2:
  print("this element is boiling and melting point are the lowest")
elif number == 3:
  print("This element is least dense metal and least dense solid")
elif number == 4:
  print("this elementis used is widely used to make X-Ray tubes")
elif number == 5:
  print("this element is three valence electrons for forming covalent bonds")
elif number == 6:
  print("this element is nonmetallic and tetravalent")
elif number == 7:
  print("thiselement is common element in the universe")
elif number == 8:
  print("this element is a member of the chalcogen group in the periodic table")
elif number == 9:
  print("this element is lightest halogen and exists at standard conditions as a highly toxic")
else:
  print("this element is the second of these three rare gases to be discovered")
  
print("Guess the atomic number!")

guess = None

while number!= guess:

    guess = int(input("Pick a number between 1 to 10: "))

    if number == guess:
        print("You absolutely correct!")
    elif number > guess:
        print("Try a bigger number.")
    else :
        print("Try a smaller number.")

restart = "Yes"
restart = input("Another game? Answer Yes or No").lower()

while restart == "Yes":
    playgame()


