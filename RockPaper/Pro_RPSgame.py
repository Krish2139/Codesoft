'''
WORKFLOW OF PROJECT:
1 - Input from user(Rock, paper, scissor)
2 - Computer choice(computer will choose randomly not conditionally)
3 - Result print

CASES:
A - Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B - Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor
Scissor - Scissor = tie
Scissor - Paper = Scissor win
Scissor - Rock = Rock win
'''

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your Move = Rock, Paper, Scissor : ")
comp_choice = random.choice(item_list)

print("User choice = {}, Computer choice = {}".format(user_choice, comp_choice))

if user_choice == comp_choice:
    print("Both Chooses Same : tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper covers Rock = You win")
    else:
        print("Scissor cuts Paper = Computer win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor = Computer win")
    else:
        print("Scissor cuts Paper = You win")

else:
    print("Invalid choice")
    
