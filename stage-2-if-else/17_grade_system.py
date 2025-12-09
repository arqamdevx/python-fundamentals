# Problem 17 — Grade System

marks = float(input("Enter marks:"))

if marks >= 90 and marks <= 100:
    print("You got grade : A")
elif marks >= 75 and marks <= 89 :
    print("You got grade : B")
elif marks >= 50 and marks <= 74 :
    print("You got grade : C")
elif marks >= 0 and marks < 50:
    print("Fail!")
else:
    print("Invalid Marks!")