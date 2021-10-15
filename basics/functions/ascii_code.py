#Find ascii code fo a letter
print("Program Started!")
print("Please enter a standard character")
letter = input()

if len(letter) == 1:
    print(f"The ASCII code for {letter} is {ord(letter)}")
else:
    print("Error try again, with a single character")
print("Program ended!")


