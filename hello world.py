import math
#A program to make a simple calculator.

#This function adds two numbers
def add(x, y):
	return x + y

#This function subtracts two numbers.
def subtract(x, y):
	return x - y

#This function multiplies two numbers.
def multiply(x, y):
	return x * y

#This function divides two numbers.	
def divide(x, y):
	return x / y

def square(x):
    return x*x

def squareroott(x):
    return Squareroot(x)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Squareroot")

game_play = True

while game_play  == True:
	#Take input from the user
	choice = input("Enter choice(1/2/3/4): ")

	#Check if choice is one of the four options.
    if choice in ('1', '2', '3', '4', '5', '6'):
		num1 = float(input("Enter first number:"))
		num2 = float(input("Enter the second number:"))

		if choice == "1":
			print(num1, "+", num2, "=", add(num1, num2))

		if choice == "2":
			print(num1, "-", num2, "=", subtract(num1, num2))

		if choice == "3":
			print(num1, "*", num2, "=", multiply(num1, num2))

		if choice == "4":
			print(num1, "/", num2, "=", divide(num1, num2))	

		if choice == "5":
    		answer = square(num1)
    		print(answer)

		if choice == "6":
    		answer = squareroott(num1)
			print(answer)


    else:
        print("Invalid input!!!")

	   

