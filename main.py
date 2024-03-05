#Import the random module to generate random numbers.
import random

def guess_number():
    secret_number = random.randint(1, 100)
    #print("generated random number:", secret_number)
    attempts_player = []
    attempts_computer = []
   
    print("Welcome! I challenge you to guess the number I'm thinking of between 1 and 100 😎")

    player_name = input("Please, write your name: ")
    while True:
        #player's turn
        
        attempt_player = int(input(f"Your turn {player_name}: Make your guess: "))
       
        attempts_player.append(attempt_player)
        
        if attempt_player < secret_number:
            print("Your assumption has been low 🙁")
        elif attempt_player > secret_number:
            print("Your assumption has been high 🤯")
        else:
            print(f"🚀 Congratulations! you guessed the secret number in {len(attempts_player)} attempts🚀")
            break

        #computer turn
        attempt_computer = random.randint(1, 100)
        print("Computer turn, assumption:", attempt_computer)
        
        attempts_computer.append(attempt_computer)
        
        if attempt_computer < secret_number:
            print("The computer's assumption is low 🤯")
        elif attempt_computer > secret_number:
            print("The computer's assumption is high 🙁")
        else:
            print(f"The computer 💻 guessed the secret number in {len(attempts_computer)} attempts")
            break

guess_number()