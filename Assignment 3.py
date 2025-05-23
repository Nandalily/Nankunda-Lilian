# factorial using lambda function

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
# Call the function
print("The factorial of 5 is", factorial(5))


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # Call the function
# print("The factorial of 5 is", factorial(5))