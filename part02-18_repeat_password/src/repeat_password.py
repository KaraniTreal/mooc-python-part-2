# Write your solution here
pas1 = input("Password: ")
while True:
    pas2 = input("Repeat password: ")

    if pas1 != pas2:
        print("They do not match!")
    elif pas1 == pas2:
        break
print("User account created!")
