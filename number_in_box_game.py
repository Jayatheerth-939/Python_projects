import random

def boxes(numbers):
    # top border
    for _ in numbers:
        print("+-----+", end=" ")
    print()

    # number row
    for n in numbers:
        print(f"|  {n}  |", end=" ")
    print()


    # bottom border
    for _ in numbers:
        print("+-----+", end=" ")
    print()

def evaluater(guess_list,correct_list):
    correct = 0
    for g, c in zip(guess_list, correct_list):
        if g == c:
            correct += 1
    correct_choices = [g if g == c else "x" for g, c in zip(guess_list, correct_list)]
    return correct, correct_choices

#main block from here 

print("Welcome to the Number in Box Game!")
num_boxes = int(input("Enter the number of boxes u want to play with "))
options = list(range(1, num_boxes + 1))
correct_numbers = random.sample(options, num_boxes)  # Randomly select numbers for the boxes
boxes(num_boxes*["x"])  # Display empty boxes
display_list = num_boxes*["x"]

while True:
    guess = input(f"Enter your guess for the {num_boxes} boxes (space-separated numbers): ")
    guess_list = [int(x) for x in guess.split()]
    
    if len(guess_list) != num_boxes:
        print(f"Please enter exactly {num_boxes} numbers.")
        continue
    
    correct, display_list = evaluater(guess_list, correct_numbers)
    boxes(display_list)
    
    if correct == num_boxes:
        print("Congratulations! You've guessed all the numbers correctly!")
        break
    else:
        print(f"You got {correct} correct. Try again!")
