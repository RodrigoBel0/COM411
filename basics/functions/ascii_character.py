# find an ascii character
print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())
if code in range(32, 126):
    print(f"The character represented by the ASCII code {code} is {chr(code)} ")
else:
    print("Put a suitable number between 31 and 126")
print("Program Ended!")
