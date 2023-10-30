import random
import string


def process_string(input_string):
    i = 0
    while i + 14 <= len(input_string):
        slice = input_string[i:i + 14]
        state = set()

        for letter in reversed(slice):
            if letter in state:
                i += 1
                break
            else:
                state.add(letter)
        else:
            return i

    return state


# Generate a string of 'a' to 'z' characters
s = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

# Ensure there is at least one occurrence where 14 of them are different
s = s[:50] + string.ascii_lowercase[:14] + s[64:]

position = process_string(s)
if position is not None:
    print("The unique seqence starts at position:", position,
          "\nAnd that sequence is:", s[position:position+14])
else:
    print("The sequence doesn't contain 14 unique characters in a row.")
