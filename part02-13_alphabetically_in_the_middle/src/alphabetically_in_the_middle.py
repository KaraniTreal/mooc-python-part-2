# Write your solution here

l1 = input("1st letter: ")
l2 = input("2nd letter: ")
l3 = input("3rd letter: ")

if l2 < l1 < l3 or l3 < l1 < l2:
    middle = l1
elif l1 < l2 < l3 or l3 < l2 < l1:
    middle = l2
else:
    middle = l3

print(f"The letter in the middle is {middle}")
