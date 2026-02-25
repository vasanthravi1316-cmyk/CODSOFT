image = """                                                         
▄█████  ▄▄▄  ▄▄     ▄▄▄▄ ▄▄ ▄▄ ▄▄     ▄▄▄ ▄▄▄▄▄▄ ▄▄▄  ▄▄▄▄  
██     ██▀██ ██    ██▀▀▀ ██ ██ ██    ██▀██  ██  ██▀██ ██▄█▄ 
▀█████ ██▀██ ██▄▄▄ ▀████ ▀███▀ ██▄▄▄ ██▀██  ██  ▀███▀ ██ ██                                                        
"""

def addition(n1,n2):
    return n1 + n2

def subtract(n1,n2):
     return n1 - n2

def multiply(n1,n2):
     return n1 * n2

def divide(n1,n2):
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return n1 / n2

def calculator():
    print(image)
    operations = { "+": addition, "-" : subtract, "*" : multiply,"/": divide }
    while True:
        try:
            # To handle exception if input 1 is not a number
            num1 = float(input("Enter 1st number: "))
            break
        except ValueError:
            print("Give a proper input.")
    while True: # main calculator loop

        while True: # loop to get 2nd input
            try:
                # To handle exception if input 1 is not a number
                num2 = float(input("Enter 2nd number: "))
                break
            except ValueError:
                print("Give a proper input.")

        for i in operations:
            print(i, end = " ")
        print()
        while True: #loop to get operation which are available
            symbol = input("Which operation do you want to perform: ")
            if symbol not in operations:
                print("Enter operations from shown above")
            else:
                break
        try:
            result = operations[symbol](num1, num2)
            print("Result = ",result)
        except ZeroDivisionError as e:
            print(e)
            continue

        continue_result = input("Type 'y' to continue or 'n' to exit.").lower()
        if continue_result == "y":
            num1 = result
        else:
            break

calculator()





  

