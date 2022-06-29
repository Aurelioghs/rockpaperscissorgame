#computer will choose random number
import random
#welcome message
print("\nHi! Let's play Rock Paper Scissor")

def play():
    #take input from user
    user_input = input("Select your option [rock, paper, scissor]: ")
    #computer to randomly chose an option
    # computer_option = ["rock", "paper", "scissors"]
    computer_option = random.choice(["rock", "paper", "scissor"])
    #output selections to the user
    print("********  You selected: ", user_input)
    print("********  Compubot: ", computer_option)

    if user_input == computer_option:
        return "********  It's a tie!"
    #will return the winner
    if winner(user_input, computer_option):
        return "********  You won!"
    #will return the loser
    return "********  You lost!"
    #function for the winner will return true
def winner(user, compubot):
    #paper>rock
    #rock>scissor
    #scissor>paper
    if(user == 'rock' and compubot == 'scissor') \
    or (user == 'scissor' and compubot == 'paper') \
    or (user == 'paper' and compubot == 'rock'):
        return True

print(play())
