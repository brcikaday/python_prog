import random
 
while True:
    
    player = input("choose: ")
    bot = ["rock","paper","scissors"]
    bot_choice = random.choice(bot)
    print(f"bot chose: {bot_choice}")

    if player == "rock" and bot_choice == "paper":
        print("you lost")
    elif player == "rock" and bot_choice == "scissors":
        print("you have won")
    elif player == "scissors" and bot_choice == "rock":
        print("you lost")
    elif player == "scissors" and bot_choice == "paper":
        print("you have won")
    elif player == "paper" and bot_choice == "rock":
        print("you have won")
    elif player == "player" and bot_choice == "scissors":
        print("you lost")
    else:
        print("tie")
    
    play_again=input("if you want to stop playing enter stop else enter play: ")
    if play_again == "stop":
        break
