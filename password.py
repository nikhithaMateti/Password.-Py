import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Please enter valid numeric values.")
        exit()

    if password_length <= 0 or num_passwords <= 0:
        print("Please enter positive values for password length and number of passwords.")
        exit()

    passwords = generate_multiple_passwords(num_passwords, password_length)

    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx}: {password}")
