import random

image = """                                                                                                                                                                                                                                                                                                 
█████▄  ▄▄▄   ▄▄▄▄  ▄▄▄▄ ▄▄   ▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄       ▄████  ▄▄▄▄▄ ▄▄  ▄▄ ▄▄▄▄▄ ▄▄▄▄   ▄▄▄ ▄▄▄▄▄▄ ▄▄▄  ▄▄▄▄  
██▄▄█▀ ██▀██ ███▄▄ ███▄▄ ██ ▄ ██ ██▀██ ██▄█▄ ██▀██     ██  ▄▄▄ ██▄▄  ███▄██ ██▄▄  ██▄█▄ ██▀██  ██  ██▀██ ██▄█▄ 
██     ██▀██ ▄▄██▀ ▄▄██▀  ▀█▀█▀  ▀███▀ ██ ██ ████▀      ▀███▀  ██▄▄▄ ██ ▀██ ██▄▄▄ ██ ██ ██▀██  ██  ▀███▀ ██ ██ 

"""
print(image)
alphabet = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o' , 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
sign = ['!','@','#','$','*']


while True:
    while True:
        try:
            print("Choose the combinations for you password.")
            alpha = int(input("1. How many alphabets you want in your password? "))
            num = int(input("2. How many numbers you want in your password? "))
            symbols = int(input("3. How many symbols you want in your password? "))
            if alpha > 0 and num > 0 and symbols > 0:
                break
            else:
                print("Please provide positive numbers")
        except ValueError:
                print("Invalid choice")

    result = []
    for i in range(alpha):
        result.append(random.choice(alphabet))
    for i in range(num):
        result.append(random.choice(numbers))
    for i in range(symbols):
        result.append(random.choice(sign))

    random.shuffle(result)
    password = ""

    for i in result:
        password += i
    print(f"Password = {password}\nYou can use this password or you can try again for a new password.")
    again = input("Type 'y' to try again and 'n' if you want to exit. " ).lower()
    if again == "n":
        break
    else:
        print("\n" * 5)



