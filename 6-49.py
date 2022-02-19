import random

firstNr = None
secondNr = None
thirdNr = None
fourthNr = None
fifthNr = None
sixthNr = None

choice1, choice2, choice3, choice4, choice5, choice6 = None, None, None, None, None, None

numbersGuessed = 0

def checkDuplicates():
  if firstNr == secondNr == thirdNr == fourthNr == fifthNr == sixthNr:
    generateNumbers()

def generateNumbers():
  global firstNr, secondNr, thirdNr, fourthNr, fifthNr, sixthNr
  firstNr = random.randint(1, 49)
  secondNr = random.randint(1, 49)
  thirdNr = random.randint(1, 49)
  fourthNr = random.randint(1, 49)
  fifthNr = random.randint(1, 49)
  sixthNr = random.randint(1, 49)
  checkDuplicates()

def checkUserInput():
  numbers = [choice1, choice2, choice3, choice4, choice5, choice6]
  if len(numbers) != len(set(numbers)):
    print("You have entered duplicate numbers. Please enter the numbers again")
    userInput()
  elif choice1 > 49 or choice2 > 49 or choice3 > 49 or choice4 > 49 or choice5 > 49 or choice6 > 49:
    print("Your numbers must be between 1 and 49. Please enter the numbers again")
    userInput()

def userInput():
  global choice1, choice2, choice3, choice4, choice5, choice6
  print("Enter the first number: ")
  choice1 = int(input())
  print("Enter the second number: ")
  choice2 = int(input())
  print("Enter the third number: ")
  choice3 = int(input())
  print("Enter the fourth number: ")
  choice4 = int(input())
  print("Enter the fifth number: ")
  choice5 = int(input())
  print("Enter the sixth number: ")
  choice6 = int(input())
  checkUserInput()

def checkNumbers():
  global numbersGuessed, firstNr, secondNr, thirdNr, fourthNr, fifthNr, sixthNr, choice1, choice2, choice3, choice4, choice5, choice6
  if choice1 == firstNr or choice1 == secondNr or choice1 == thirdNr or choice1 == fourthNr or choice1 == fifthNr or choice1 == sixthNr:
    numbersGuessed = numbersGuessed + 1
  if choice2 == firstNr or choice2 == secondNr or choice2 == thirdNr or choice2 == fourthNr or choice2 == fifthNr or choice2 == sixthNr:
    numbersGuessed = numbersGuessed + 1
  if choice3 == firstNr or choice3 == secondNr or choice3 == thirdNr or choice3 == fourthNr or choice3 == fifthNr or choice3 == sixthNr:
    numbersGuessed = numbersGuessed + 1
  if choice4 == firstNr or choice4 == secondNr or choice4 == thirdNr or choice4 == fourthNr or choice4 == fifthNr or choice4 == sixthNr:
    numbersGuessed = numbersGuessed + 1
  if choice5 == firstNr or choice5 == secondNr or choice5 == thirdNr or choice5 == fourthNr or choice5 == fifthNr or choice5 == sixthNr:
    numbersGuessed = numbersGuessed + 1
  if choice6 == firstNr or choice6 == secondNr or choice6 == thirdNr or choice6 == fourthNr or choice6 == fifthNr or choice6 == sixthNr:
    numbersGuessed = numbersGuessed + 1
  if numbersGuessed >= 3:
    print("You win! You guessed " + str(numbersGuessed) + " numbers out of 6 numbers!")
  else:
    print("You lost... You guessed " + str(numbersGuessed) + " numbers out of 6 numbers! Better luck next time!")
  print("The winning numbers are: " + str(firstNr) + ", " + str(secondNr) + ", " + str(thirdNr) + ", " + str(fourthNr) + ", " + str(fifthNr) + ", " + str(sixthNr))
  print("Your numbers are: " + str(choice1) + ", " + str(choice2) + ", " + str(choice3) + ", " + str(choice4) + ", " + str(choice5) + ", " + str(choice6))

generateNumbers()
checkDuplicates()
userInput()
checkUserInput()
checkNumbers()
