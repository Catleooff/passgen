import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

password = generate_password(12)

with open("passgen.txt", "w") as f:
    f.write(password)

print("пароль в файле")
