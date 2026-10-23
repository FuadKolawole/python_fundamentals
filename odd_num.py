# ----FUAD KOLAWOLE'S PRACTICE PROGRAMS----

# To print the odd numbers in a list

numbers = [63, 192, 15, 8, 33, 109, 89, 21, 6]

def odd_num():
    print("The odd numbers in this list are:")
    for number in numbers:
        if number%2 == 1:
            print(number, end=", ")
        # What if the list is empty?
        elif len(numbers) == 0:
            print("Task Impossible, list is empty!")
odd_num()



