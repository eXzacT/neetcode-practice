import random
import string

ascii = {char: ord(char) - 96 for char in string.ascii_lowercase}


def process_string_bitwise(input: string) -> int:
    """
    Finds the starting index of the first 14-character slice in a string where all characters are unique.

    This function iterates over the input string one character at a time, checking slices of 14 characters. 
    For each slice, it uses bitwise operations to track the ASCII values of the characters. If it encounters 
    a character that has already appeared in the current slice, it moves to the next slice. If it finds a slice 
    where all characters are unique, it returns the starting index of that slice.

    Parameters:
    input (str): The input string to check.

    Returns:
    int: The starting index of the first 14-character slice where all characters are unique. 
         If no such slice is found, it returns None.
    """

    i = 0
    while i + 14 <= len(input):
        slice = input[i:i + 14]
        state = 0

        for index, letter in enumerate(reversed(slice)):
            alphabet_pos = ascii[letter]
            # This means the character appeared twice because 1 and 1 will return a non 0 value (30/10/2023)
            if state & (1 << alphabet_pos) != 0:
                # Subtract from 14 because it's reversed (31/10/2023)
                i += 14 - index
                break
            state |= 1 << alphabet_pos
        # If we get to this else it means that the loop finished without encountering a duplicate (30/10/2023)
        else:
            return i

    return None


def process_string(input_string):
    """ Same as the above but not using bitwise operations, rather checking with a set (31/10/2023) """
    i = 0
    while i + 14 <= len(input_string):
        slice = input_string[i:i + 14]
        letters_set = set()

        for index, letter in enumerate(reversed(slice)):
            if letter in letters_set:
                i += 14 - index
                break
            else:
                letters_set.add(letter)
        else:
            return i

    return None


# Generate a string of 'a' to 'z' characters
s = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

# Ensure there is at least one occurrence where 14 of them are different
s = s[:50] + string.ascii_lowercase[:14] + s[64:]

position = process_string_bitwise(s)

if position is not None:
    print("The unique seqence starts at position:", position,
          "\nAnd that sequence is:", s[position:position+14])
else:
    print("The sequence doesn't contain 14 unique characters in a row.")
