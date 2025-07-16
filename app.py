def calculator():

    print("Simple Calculator (type 'exit' to quit)\n")

    while True:
        user_input = input("Enter calculation (e.g. 5 + 3): ")

        if user_input.lower() == 'exit':
            print("👋 Exiting calculator.")
            break

        try:
            num1, op, num2 = user_input.split()
            num1 = float(num1)
            num2 = float(num2)

            if op == '+':
                print(f"= {num1 + num2}")
            elif op == '-':
                print(f"= {num1 - num2}")
            elif op == '*':
                print(f"= {num1 * num2}")
            elif op == '/':
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(f"= {num1 / num2}")
            else:
                print("Invalid operator")

        except ValueError:
            print(" Invalid input format. Use: number operator number")


if __name__ == "__main__":
    calculator()    
