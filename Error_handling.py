# Get user input 
name = input("Enter your name: ")
# Keep asking for age until a valid number is entered
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input! Please Enter a number. ")
        