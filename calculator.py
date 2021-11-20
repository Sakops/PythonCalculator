print("Choose operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

while True: 
    option = input("Choose your operation from above: ")

    if option in ("1", "2", "3", "4", "5"):
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        if option == "1": 
            print(num1 + num2)
        elif option == "2": 
            print(num1 - num2)
        elif option == "3": 
            print(num1 * num2)
        elif option == "4":
            try: 
                print(num1/num2)
                pass
            except ZeroDivisionError: 
                print("Undefined")
        elif option == "5": 
            print(num1 ** num2)
        continue
    else: 
        print("error")
    break
    