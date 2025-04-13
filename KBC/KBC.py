import time

def KBC():
    questions = [
        "Which planet is known as the 'Morning Star'?",
        "What is the largest mammal in the world?",
        "What is the chemical symbol for water?",
        "Which country is famous for inventing pizza?",
        "What is the national flower of Japan?",
        "How many colors are in a rainbow?",
        "Which animal is known as the 'King of the Jungle'?",
        "What is the fastest land animal?",
        "Which ocean is the largest on Earth?",
        "How many continents are there in the world?"
    ]
    correct_answers = ["a", "b", "a", "a", "b", "c", "d", "b", "d", "c"]
    options = [
        ["A: Venus", "B: Mars", "C: Jupiter", "D: Saturn"],
        ["A: Elephant", "B: Blue Whale", "C: Giraffe", "D: Hippopotamus"],
        ["A: H2O", "B: CO2", "C: O2", "D: N2"],
        ["A: Italy", "B: France", "C: Spain", "D: Germany"],
        ["A: Rose", "B: Cherry Blossom", "C: Lily", "D: Lotus"],
        ["A: 5", "B: 6", "C: 7", "D: 8"],
        ["A: Elephant", "B: Leopard", "C: Tiger", "D: Lion"],
        ["A: Lion", "B: Cheetah", "C: Leopard", "D: Hyena"],
        ["A: Atlantic", "B: Arctic", "C: Indian", "D: Pacific"],
        ["A: 5", "B: 6", "C: 7", "D: 8"]
    ]
    winnings = [10000, 20000, 40000, 150000, 300000, 600000, 1000000, 2000000, 5000000]
    
    print("Hello and welcome to the new episode of who wants to be a millionaire!")
    time.sleep(1)
    print('*KBC theme music*')
    time.sleep(1)
    print("I am your host, Amitabh Baccchan!")
    time.sleep(1)
    print('Are you ready?')
    
    while True:
        ready = input('Enter Yes or No: ').strip().lower()
        if ready == 'yes':
            print('Great! Let us begin!')
            break
        elif ready == 'no':
            print('Let me know when you are ready!')
        else:
            print('Invalid input. Please enter Yes or No.')
    
    for i in range(len(questions)):
        if i == 0:
            print(f'Here is your first question for {winnings[i]} dollars:')
        else:
            print(f'Here is your next question for {winnings[i]} dollars:')
        
        time.sleep(1)
        print(questions[i])
        time.sleep(1)
        print('Your options are:')
        time.sleep(1)
        for option in options[i]:
            print(option)
        
        while True:
            answer = input('Enter your answer (A, B, C, or D): ').strip().lower()
            if answer in ['a', 'b', 'c', 'd']:
                if confirm_answer():
                    if answer == correct_answers[i]:
                        print(f'Congratulations! You have won {winnings[i]} dollars!')
                        if takehome(winnings[i]):
                            return
                        break
                    else:
                        print(f'Sorry! You have lost. The correct answer was {correct_answers[i]}.')
                        tryagain()
                        return
                else:
                    print("Re-enter your answer carefully!")
            else:
                print('Invalid input. Please enter A, B, C, or D.')
    
    print("Congratulations! You've answered all questions correctly! You have won Ten Million!")

def confirm_answer():
    while True:
        confirmation = input("Are you sure about your answer? (Yes or No): ").strip().lower()
        if confirmation == 'yes':
            return True
        elif confirmation == 'no':
            return False
        else:
            print("Invalid input. Please enter Yes or No.")

def tryagain():
    while True:
        try_again = input('Would you like to try again? (Yes or No): ').strip().lower()
        if try_again == 'yes':
            KBC()
            return
        elif try_again == 'no':
            print('Goodbye!')
            exit()
        else:
            print('Invalid input. Please enter Yes or No.')

def takehome(amount):
    while True:
        take_home = input("Would you like to take your money home? (Yes or No): ").strip().lower()
        if take_home == 'yes':
            print(f"Congratulations! You are walking away with {amount} dollars!")
            print("Goodbye!")
            exit()
        elif take_home == 'no':
            return False
        else:
            print("Invalid input. Please enter Yes or No.")

KBC()