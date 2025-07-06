# Python project to implement palindrome checker
# Author: Anuj Savant
# Date: 6/7/25

string = input("Enter a string:")

length = len(string)
i=0

for i in range(length -1):
    if string[i] != string[length - i - 1]:
        print("Not a palindrome")
        break
else:
    print("Palindrome")