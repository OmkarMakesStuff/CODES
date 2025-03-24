import string
import random
import time

FILENAME = "encoded_messages.txt"

def generate_random_letters():
    """Generate 3 random lowercase letters"""
    return ''.join(random.choices(string.ascii_lowercase, k=3))

def encode_word(word):
    """Encode a single word"""
    random_start = generate_random_letters()
    random_end = generate_random_letters()
    
    if len(word) <= 3:
        return word[::-1]  # Reverse short words
    else:
        return random_start + word[1:] + word[0] + random_end

def encode_sentence():
    """Encode a whole sentence"""
    sentence = input("Enter a sentence to encode: ").strip().lower()
    words = sentence.split()
    
    encoded_words = [encode_word(word) for word in words]
    encoded_sentence = ' '.join(encoded_words)
    
    message_name = input("What would you like to name this message? ").strip()
    
    with open(FILENAME, "a") as file:
        file.write(f"{message_name}: {encoded_sentence}\n")
    
    print(f"Message '{message_name}' has been encoded and saved!")

def decode_word(word):
    """Decode a single word"""
    if len(word) <= 3:
        return word[::-1]  # Reverse short words
    else:
        core = word[3:-3]  # Remove random letters
        return core[-1] + core[:-1]

def decode_sentence():
    """Decode an encoded sentence"""
    encoded_sentence = input("Enter the encoded sentence: ").strip().lower()
    words = encoded_sentence.split()
    
    decoded_words = [decode_word(word) for word in words]
    decoded_sentence = ' '.join(decoded_words)
    
    print(f"Decoded message: {decoded_sentence}")

def open_encoded_messages():
    """Display stored encoded messages"""
    try:
        with open(FILENAME, "r") as file:
            messages = file.readlines()
            if not messages:
                print("No saved messages found.\n")
            else:
                print("Saved Encoded Messages:")
                for message in messages:
                    print(message.strip())
                print()
    except FileNotFoundError:
        print("No saved messages found.\n")

def main():
    """Main program loop"""
    while True:
        print("\nWelcome to the Secret Encoder-Decoder Program!")
        print("1. Encode a new message")
        print("2. Decode a message")
        print("3. Open saved encoded messages")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ").strip()

        if choice == '1':
            encode_sentence()
        elif choice == '2':
            decode_sentence()
        elif choice == '3':
            open_encoded_messages()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
