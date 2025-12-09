# Problem 19 — Electricity Bill (Basic Slab)

unit = float(input("Enter unit :"))

n = unit-200
u = (100*5)+(100*7)+(n*10)
if unit > 0 and unit <= 100 :
    print("Your total light bill is :",unit*5)
elif unit > 100 and unit <= 200:
    m = unit-100
    print("Your total light bill is :",(100*5)+(m*7))
elif unit > 200 :
    print("Your total light bill is :",u)