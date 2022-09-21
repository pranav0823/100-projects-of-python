import random 

print("Welcome to rock paper scissors game")

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



images = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0 :
  print("You have entered an invalid number, You lose")
else:
  print(images[user_choice])

  cpu_choice = random.randint(0,2)
  print("Computer chosen :")
  print(images[cpu_choice])
  
  if user_choice == 0 and cpu_choice == 1 :
    print("You lose")
  elif user_choice == 0 and cpu_choice == 2 :
    print("You win")
  elif cpu_choice > user_choice:
    print("You lose")
  elif user_choice > cpu_choice:
    print("You win!")
  elif cpu_choice == user_choice:
    print("It's a draw")


