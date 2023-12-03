# Exercise no 3:
# Write a program to accept a string from the user and display characters 
# that are present at an even index number.

user_input = input("Enter a string: ")
result = user_input[::2]
print("Printing only even index characters: ", result)
