
import random
import string

print("===== PASSWORD GENERATOR =====")

# user input
length = int(input("Enter password length: "))

# character set
characters = string.ascii_letters + string.digits + string.punctuation

# generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# display result
print("\n🔐 Generated Password:", password)