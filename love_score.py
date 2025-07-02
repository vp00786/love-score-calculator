# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")

def calculate_love_score(n1, n2):
    number_1 = 0
    number_2 = 0

    for letter in n1:
        if letter in "true":
            number_1 += 1
    for letter in n2:
        if letter in "true":
            number_1 += 1

    for lett in n2:
        if lett in "love":
            number_2 += 1
    for lett in n1:
        if lett in "love":
            number_2 += 1

    print(f"Love score: {number_1}{number_2}")

n_1 = input("What is your name? ")
n_2 = input("What is your partner's name? ")
n1 = n_1.lower()
n2 = n_2.lower()
calculate_love_score(n1, n2)
