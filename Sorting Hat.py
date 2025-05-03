# Simple sorting hat made by qrvnix

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# number 1
print("Q1. Do you like Dawn or Dusk?")
choice1 = int(input("  1. Dawn\n  2. Dusk\n"))
if choice1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif choice1 == 2:
    hufflepuff +=1
    slytherin += 1
else:
  print("Wrong input")

print('') # number 2
print("Q2. When I'm dead, I want people to remember me as:")
choice2 = int(input("  1. The Good\n  2. The Great\n  3. The Wise\n  4. The Bold\n"))
if choice2 == 1:
    hufflepuff += 2
elif choice2 == 2:
    slytherin += 2
elif choice2 == 3:
    ravenclaw += 2
elif choice2 == 4:
    gryffindor += 2
else:
  print("Wrong input.")

print('') # number 3
print("Q3. Which kind of instrument most pleases your ear?")
choice3 = int(input("  1. The violin\n  2. The trumpet\n  3. The piano\n  4. The drum\n"))
if choice3 == 1:
    slytherin += 4
elif choice3 == 2:
    hufflepuff += 4
elif choice3 == 3:
    ravenclaw += 4
elif choice3 == 4:
    gryffindor += 4
else:
  print("Wrong input.")

print('') # result
print("Here is the result:")
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("\nYou have been sorted. Your house is Gryffindor!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("\nYou have been sorted. Your house is Ravenclaw!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("\nYou have been sorted. Your house is Hufflepuff!")
else:
    print("\nYou have been sorted. Your house is Slytherin!")