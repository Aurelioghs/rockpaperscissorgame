#computer will choose random number
import random
#welcome message
print("Hi!")

def play():
#take input from user
    user_input = input("Select your option [rock, paper, scissors]: ")
#computer to randomly chose an option
    computer_option = ["rock", "paper", "scissors"]
    choose_option = random.choice(computer_option)
#output selections to the user
    print("********  You selected: " , user_input)
    print("********  Compubot:", choose_option)

    if user_input == choose_option:
        return "It's a tie!"
