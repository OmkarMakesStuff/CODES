import random
import time
a = 'Snake'
b = 'Water'
c = 'Gun'
user_var = 0
userscore = 0
compscore = 0
choices = ['snake','water','gun']
print('Welcome to Snake Water Gun!')
print('The rules are simple')
print('Snake drinks Water, Water disables Gun, Gun kills Snake!')
print('If you win, you get 1 point, if you lose, I get 1 point!')
while True:
    print('Are you ready?')
    ready_input = input('Enter yes or no: ').strip().lower()
    
    if ready_input == 'yes':
        print("Great! Let's begin!")
        break
    elif ready_input == 'no':
        print('Type yes when you are ready to play!')
    else:
        print('Invalid input: Please type yes or no!')
print("We will count to 3, \nAt the same time you show your choice \nI'll show mine \nLet's see who wins, \nBest of luck!")
def main():
   global userscore, compscore
   print("Enter 'snake', 'water', or 'gun' in... ")
   time.sleep(1)
   print('1...')
   time.sleep(1)
   print('2...')
   time.sleep(2)
   print('3!')
   gameinp = input("Enter now! :")
   compchoice = random.choice([a, b, c])
    
   print(f'You choose : {gameinp} \nI choose {compchoice}!')
   gameinp = gameinp.strip().lower()
   compchoice = compchoice.lower()
   
   if gameinp == compchoice:
         print("It's a draw!")
         print("We both get no points!")
       
      
   elif gameinp == 'snake' and compchoice  == 'water':
         print("Snake drinks Water! You win! \nYou Get 1 point!")
         userscore += 1
        
       
   elif gameinp == 'snake' and compchoice == 'gun':
         print('Gun kills Snake! I win! /nI get 1 point!')
    
         compscore += 1
        
   elif gameinp == 'water' and compchoice == 'snake':
         print("Snake drinks Water! I win! \nI Get 1 point!")
        
         compscore  += 1
       
   elif gameinp == 'water' and compchoice == 'gun':
         print('Water disables Gun! You win! /nYou get 1 point!')
         userscore += 1
       
              
   elif gameinp == 'gun' and compchoice == 'snake':
         print("Gun kills snake! you win! \nyou Get 1 point!")
         userscore += 1
         
         
   elif gameinp == 'gun' and compchoice == 'water':
         print('Water disables Gun! I win! /nI get 1 point!')
       
         compscore += 1
   else:
        print('Invalid input Enter again!')   
        return
   playagain()


def playagain():
   againinp = ''
   print('Want to play again? Enter yes or no :')
   againinp = input()
   againinp = againinp.strip().lower()
   while True:
      if againinp == 'yes':
             main()
      elif againinp == 'no':
             print('Goobye!')
             exit()
      else:
             print("Invalid input, please enter Yes or No!")
main()