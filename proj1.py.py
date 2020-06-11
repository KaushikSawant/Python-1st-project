def intro():
	bot_name=input("Enter Bot name")
	year=input("Enter the BOT creation year")
	print("Hello My Name is", bot_name)
	print("I was created in ", year)

def user():
	print("Please remind me your name")
	user_name=input()
	print("what a great name you have ", user_name, "!!!")

def age():
	print("Let me Guess your Age")
	print("Tell me remainders of dividing your age by 3, 5 and 7")

	rem_3=int(input())
	rem_5=int(input())
	rem_7=int(input())
	age = (rem_3 * 70 + rem_5 * 21 + rem_7 * 15) % 105

	print("Your age is",age,"that's a good time to start programming!")

def count():
	print("I can count to any number you want")
	number = int(input())
	current = 0

	while current <= number:
		print(current,'!')
		current += 1
def question():
	print("Lets test your programming knowledge")
	print("when India got Independence")
	print("""
		1. 1974
		2. 1948
		3. 1793
		4. 1947
		""")
	x=int(input())
	if x==1:
		print("Please try again.")
	else:
		if x==2:
			print("Please try again.")
		if x == 3:
			print("Please try again.")
		else:
			print("Bingo corrrect answer!")
def end():
	print("congrats have a nice day!")								

	
intro()
user()
age()
count()
question()
