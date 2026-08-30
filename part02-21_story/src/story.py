# Write your solution here

narrate = ""
previous = ""

while True:
    words = input("Please type in a word: ")

    if words == "end":
        break
    if previous == words:
        break

    narrate += " " + words

    previous = words

print(f"{narrate}")
