# Write your solution here
counter = 0
sum = 0
positive = 0
negative = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))
    sum += num

    if num > 0:
        positive += 1
    if num < 0:
        negative += 1

    if num == 0:
        break
    counter += 1

    mean = sum / counter


print(f"Numbers typed in {counter}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
