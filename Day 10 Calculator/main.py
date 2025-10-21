
print("----------Calculator----------\n")


while True:
    result = 0
    firstNumber = int(input("First number: "))
    print("Choose operator:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    operator = int(input("Operator: "))
    secondNumber = int(input("Second number: \n"))
    
    if operator == 1:
        result = firstNumber + secondNumber
        print(f"{firstNumber} + {secondNumber} = {result}")
    elif operator == 2:
        result = firstNumber - secondNumber
        print(f"{firstNumber} - {secondNumber} = {result}")
    elif operator == 3:
        result = firstNumber * secondNumber
        print(f"{firstNumber} * {secondNumber} = {result}")
    elif operator == 4:
        result = firstNumber / secondNumber
        print(f"{firstNumber} / {secondNumber} = {result}")
    else:
        print("Invalid operator")

    print("\nDo you want to continue?")
    print("1. Yes")
    print("2. No")
    choice = int(input("Choice: "))
    if choice == 2:
        break
