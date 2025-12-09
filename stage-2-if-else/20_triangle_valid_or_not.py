# Problem 20 — Triangle Valid or Not

a = float(input("Enter Side A :"))
b = float(input("Enter Side B :"))
c = float(input("Enter Side C :"))

if a + b > c and b + c > a and c + a > b :
    print("Valid Triangle")
else:
    print("Not a Triangle")
    