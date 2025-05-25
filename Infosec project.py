# Write a program that asks the user for a number of days. The program then prints out the number of seconds in the number of days given.
# Ask the user for the number of days
days = int(input("Enter the number of days: "))
# Calculate the number of seconds in the given days
seconds = days * 24 * 60 * 60
# Print the result
print(f"There are {seconds} seconds in {days} day(s).")


