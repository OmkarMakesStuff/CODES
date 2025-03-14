def check_password():
    user_input = input("Enter your password: ")  # Get input from user
    correct_password = "password123"  # Predefined correct password
    
    if not user_input:  
        return "Password cannot be empty!"  
    
    if user_input == correct_password:
        return "Password accepted!"
    else:
        return "Incorrect password!"

# Run the function and print the result
print(check_password())
