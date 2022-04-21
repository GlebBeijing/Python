# phrase = "Let’s Replicate a Function"
# upper = 0
# lower = 0
# for letter in phrase:
#     if letter.isupper():
#         upper += 1
#     elif letter.islower():
#         lower += 1
# print(str(upper) + " and " + str(lower))

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters("beautiful", "fantastic"))