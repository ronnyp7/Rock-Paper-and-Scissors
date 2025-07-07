import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))

if user_choice == 0:
    print("You chose: " + rock)
elif user_choice == 1:
    print("You chose: " + paper)
elif user_choice == 2:
    print("You chose: " + scissors)

computer_choice = random.randint(a=0, b=2)
print(f"Computer chose {computer_choice}")

if computer_choice == 0:
    print("Computer chose: " + rock)
elif computer_choice == 1:
    print("Computer chose: " + paper)
elif computer_choice == 2:
    print("Computer chose: " + scissors)

if user_choice == 0 and computer_choice == 0:
    print("Pair!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You won!")

if user_choice == 1 and computer_choice == 0:
    print("You won!")
elif user_choice == 1 and computer_choice == 1:
    print("Pair!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")

if user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You won!")
elif user_choice == 2 and computer_choice == 2:
    print("Pair!")



