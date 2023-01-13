age = input("How old are you: ")
if age:
    age = int(age)
if age >= 18 and age < 21:
    print("YOU CAN ENTER WITH IDENTIFICATION")
elif int(age) >= 21:
    print("YOU CAN ENTER AND CAN DRINK")
else:
    print("YOU CAN'T COME IN, YOU'RE A CHILD!")
else:
    print("Please enter an age!")
