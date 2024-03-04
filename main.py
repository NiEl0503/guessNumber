#Import the random module to generate random numbers.
import random

secret_number = random.randint(1, 100)
print("generated random number:", secret_number)

#input function to get the player input
while True:
        #player's turn
        attempt_player = int(input("Your turn. Make your guess: "))
      
        if attempt_player < secret_number:
            print("Your assumption has been low 🙁")
        elif attempt_player > secret_number:
            print("Your assumption has been high 🤯")
        else:
            print("🚀 Congratulations! you guessed the secret number 🚀")
            break

          #computer turn
        attempt_computador = random.randint(1, 100)
        print("Computer turn, assumption:", attempt_computador)
       
        
        if attempt_computador < secret_number:
            print("The computer's assumption is low 🤯")
        elif attempt_computador > secret_number:
            print("The computer's assumption is high 🙁")
        else:
            print("The computer guessed the secret number 💻")
            break