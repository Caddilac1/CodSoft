def calculator():
    print("Welcome to my calculator app!")
    print("Operations: Add(+) ,  Subtract(-) ,  Multiply(*) ,  Divide(/) ")
    print("Type 'exit' to exit")

    while True:
        operation = input("what operation do you want to perform on your numbers (+ , - , / , *): ")


        if operation == 'exit':
            print("Thank you for using this calculator! See you next time")
            break


        if operation not in ['+' , '-' , '/' , '*']:
            print("Invalid entery... Try again")
            continue

        try:    
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Enter numeric values")
            continue

        results = 0

        if operation == '+':
            results = num1 + num2
            print(f"{num1} + {num2} = {results}")

        elif operation == '-':
            results = num1 - num2
            print(f"{num1} - {num2} = {results}")

        elif operation == '*':
            print(f"{num1} * {num2} = {results}")
            results = num1 * num2
        elif operation == '/':
            
            if num2 == 0:
                print("Error: Division by 0 not possible!")

            else:
                results = num1 / num2
                print(f"{num1} / {num2} = {results}")
                
                



calculator()            

