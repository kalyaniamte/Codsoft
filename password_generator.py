import random
import string

def generate_password(length, complexity):
    if complexity == '1':
        # Lowercase letters
        characters = string.ascii_lowercase
    elif complexity == '2':
        # Lowercase and uppercase letters
        characters = string.ascii_letters
    elif complexity == '3':
        # Lowercase, uppercase, and digits
        characters = string.ascii_letters + string.digits
    elif complexity == '4':
        # Lowercase, uppercase, digits, and punctuation
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity option.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password: "))
    print("Select complexity level:")
    print("1. Lowercase letters only")
    print("2. Lowercase and uppercase letters")
    print("3. Lowercase, uppercase letters, and digits")
    print("4. Lowercase, uppercase letters, digits, and punctuation")
    
    complexity = input("Enter your choice (1-4): ")
    
    generated_password = generate_password(length, complexity)
     
    if generated_password:
        print(f"Generated password: {generated_password}")

if __name__ == "__main__":
    main()
