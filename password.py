import random
import string

def generate_password(length):
    #abcdefghijjklmnopqrstuvwxyz0123456789!@#$%^&*()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))

password = generate_password(length)
print("Generated Password:", password)