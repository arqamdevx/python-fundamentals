# Problem 12 — Greater of Three Numbers

a = int(input("Enter first digit:"))
b = int(input("Enter second digit:"))
c = int(input("Enter third digit:"))

if a > b and a > c:
    print(a,"is greatest")
elif b > a and b > c:
    print(b,"is greatest")
elif c > a and c > b:
    print(c,"is greatest")
elif a == b and a > c:
    print(a,"and",b,"are equal and greatest")
elif b == c and b > a :
    print(b,"and",c,"are equal and greatest")
elif a == c and a > b :
    print(a,"and",c,"are equal and greatest")
else:
    print("All three numbers are equal")