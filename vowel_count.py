# ----FUAD KOLAWOLE'S PRACTICE PROGRAMS----

# To count the number of vowels in a given word

vowels = ["a", "e", "i", "o", "u"]
word = input("Enter a single word: ")
# What if the user inputs nothing and tries to proceed?
while len(word) == 0:
    print("You can't proceed!!")
    word = input("Enter a single word: ")
count = 0
for character in word.lower():
    if character in vowels:
        count += 1
print("There are {} vowels in {}".format(count, word))
