while True: 
   a = float(input('Please enter a number: '))
   print('What do you want to do with this number?\nType 1 for addition\nType 2 for subtraction\nType 3 for multiplication\nType 4 for division!')
   b = int(input('Enter a number: '))
   if b not in [1, 2, 3, 4]:
      print('Maybe you did not enter a number between 1 and 4. Let\'s try that again!')
      continue
   c = float(input('Please enter the second number: '))
   if b == 1:
      print(f'Result: {a + c}')
   elif b == 2:
      print(f'Result: {a - c}')
   elif b == 3:
      print(f'Result: {a * c}')
   elif b == 4:
      if c == 0:
         print('Division by 0 is not possible, please enter something else!')
         continue
      print(f'Result {a / c}')
while True:
   more_calc = input('Do you want to do more calculations? Type yes or no:').strip().lower()
   if more_calc == "yes":
      break
   elif more_calc == "no":
      print('Goodbye!')
      exit()
   else:
      print('Error: Invalid Input! Please enter yes or no!')
      continue