
# infinite while loop
while True:
    # try block for error handling
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        result = num1 / num2

# Exceptin one
    except ValueError:
        print("Error!: Invalid input! Please enter numeric values.\n")
# Exception two
    except ZeroDivisionError:
        print("Error!: Cannot divide by zero. Try again.\n")

    else:
        # If no exception occurs, print result and break the loop
        print(f" Result: {num1} ÷ {num2} = {result}")
        break

    finally:
        print(" successful division.\n")
