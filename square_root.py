# ----FUAD KOLAWOLE'S PRACTICE PROGRAMS----

# Program to find square root

def sqrt(n):
    # What if the user inputs a negative number?
    if n < 0:
        print("Enter a positive integer, please.")
    else:
        return n**(1/2)
num = int(input("Enter a number to find its square root: "))
result = sqrt(num)
print(f"The square root of {num} = {result}")