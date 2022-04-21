phrase = "Let’s Replicate a Function"
upper = 0
lower = 0
for letter in phrase:
    if letter.isupper():
        upper += 1
    elif letter.islower():
        lower += 1
print(str(upper) + " and " + str(lower))
