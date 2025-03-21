while True:
    try:
        a = float(input('Please enter a number: '))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    print("\nWhat do you want to do with this number?")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")

    try:
        operation = int(input("Enter a number (1-4): "))
        if operation not in [1, 2, 3, 4]:
            print("Invalid choice! Please enter a number between 1 and 4.")
            continue
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    try:
        c = float(input('Please enter the second number: '))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    if operation == 1:
        print(f'Result: {a + c}')
    elif operation == 2:
        print(f'Result: {a - c}')
    elif operation == 3:
        print(f'Result: {a * c}')
    elif operation == 4:
        if c == 0:
            print('Error: Division by zero is not possible!')
            continue
        print(f'Result: {a / c}')

    while True:
        more_calc = input("\nDo you want to do more calculations? (Yes/No): ").strip().lower()
        if more_calc == "yes":
            break
        elif more_calc == "no":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")
