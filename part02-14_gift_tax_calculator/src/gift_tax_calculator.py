# Write your solution here
gift = int(input("Value of gift: "))

if gift < 5000:
    tax = "no tax"

elif gift <= 25000:
    tax = 100 + ((gift - 5000) * (8 / 100))

elif gift <= 55000:
    tax = 1700 + ((gift - 25000) * (10 / 100))

elif gift <= 200000:
    tax = 4700 + ((gift - 55000) * (12 / 100))

elif gift <= 1000000:
    tax = 22100 + ((gift - 200000) * (15 / 100))

else:
    tax = 142100 + ((gift - 1000000) * (17 / 100))


print(f"Amount of tax: {tax} euros")
