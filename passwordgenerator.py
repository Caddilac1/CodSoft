import random
import string

def password_generator():
    print("Welcome to the Password Generator!")

   
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Password length must be at least 4 to include all character types.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    
    random.shuffle(password)

    
    final_password = ''.join(password)
    print(f"Your generated password is: {final_password}")

password_generator()
