# Problem 18 — Bonus Calculator

salary = float(input("Enter salary please :"))

if salary >= 50000:
    bonus = (salary * 10) / 100
else:
    bonus = (salary * 5) / 100
print("Your bonus is:", bonus)
