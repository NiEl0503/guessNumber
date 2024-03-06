import random

def get_secret_number():
    return random.randint(1, 100)

def get_player_name():
    return input("Please, write your name: ")

def player_guess(player_name):
    while True:
        try:
            guess = int(input(f"Your turn {player_name}: Make your guess: "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def evaluate_guess(guess, secret_number, attempts):
    attempts.append(guess)
    
    if guess < secret_number:
        print("Your assumption has been low 🙁")
    elif guess > secret_number:
        print("Your assumption has been high 🤯")
    else:
        print(f"🚀 Congratulations! you guessed the secret number in {len(attempts)} attempts🚀")
        return True
    return False

def player_turn(player_name, secret_number, attempts):
    guess = player_guess(player_name)
    return evaluate_guess(guess, secret_number, attempts)

def computer_turn_smart(secret_number, attempts):
    min_num = 1
    max_num = 100

    guess = computer_smart_guess(min_num, max_num)
    attempts.append(guess)
    
    print("Computer turn, assumption:", guess)
    
    if guess < secret_number:
        print("The computer's assumption is low 🤯")
        min_num = guess + 1
    elif guess > secret_number:
        print("The computer's assumption is high 🙁")
        max_num = guess - 1
    else:
        print(f"The computer 💻 guessed the secret number in {len(attempts)} attempts")
        return True

    return False

def computer_smart_guess(min_num, max_num):
    return random.randint(min_num, max_num)

def print_separator():
    print("\n" + "-"*20)

def guess_number():
    play_again = 'yes'
    while play_again != 'no':
        secret_number = get_secret_number()
        attempts_player = []
        attempts_computer = []
        print("Welcome! I challenge you to guess the number I'm thinking of between 1 and 100 😎")
        
        print_separator()
        player_name = get_player_name()
        while True:
            if player_turn(player_name, secret_number, attempts_player):
                break
            
            print_separator()
            if computer_turn_smart(secret_number, attempts_computer):
                break
            print_separator()

            
        play_again = input("Do you want to play again? (yes/no): ").lower()

guess_number()

