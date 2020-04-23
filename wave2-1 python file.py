# Read the integer from the user
num = int(input("Enter the integer: "))

# Determine whether it is even or odd by using remainder operator
if num % 2 == 1:
    print(num, "is odd.")
else:
    print(num, "is even.")