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
game_image = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors \n"))
print(game_image[user_choice])
computer_choice = random.randint(0,2)
print("Computer choice:")
print(game_image[user_choice])
if user_choice == 0 and computer_choice == 0:
    print("It's a tie!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You lose!")
elif user_choice == 1 and computer_choice == 1:
    print("It's a tie!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 2:
    print("It's a tie!")
else:
    print("Invalid number!")
