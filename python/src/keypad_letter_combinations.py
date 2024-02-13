if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


''' Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
    Mapping from digits to letters is given below. Note that 1 does not map to any letters.
    Their order in the return does not matter.'''

keypad = ["", "", "abc", "def",
          "ghi",  "jkl", "mno", "pqrs", "tuv", "wxyz"]


@time_execution()
def sol(digits: str) -> list[str]:
    if not digits:
        return []

    def helper(i: int) -> None:
        if i == len(digits):
            combinations.append(''.join(combination))
            return

        for letter in keypad[int(digits[i])]:
            combination.append(letter)
            helper(i+1)
            combination.pop()

    combination = []
    combinations = []
    helper(0)
    return combinations


@time_execution()
def sol_v2(digits: str) -> list[str]:
    if not digits:
        return []

    def helper(i: int, comb: str = "") -> None:
        if i == len(digits):
            combinations.append(comb)
            return

        for letter in keypad[int(digits[i])]:
            helper(i+1, comb+letter)

    combinations = []
    helper(0)
    return combinations


@time_execution()
def sol_v3(digits: str) -> list[str]:
    if not digits:
        return []

    def helper(i: int) -> None:
        if i == len(digits):
            return [""]

        combinations = []
        for letter in keypad[int(digits[i])]:
            for comb in helper(i+1):
                combinations.append(letter+comb)

        return combinations

    return helper(0)


@time_execution()
def sol_v4(digits: str) -> list[str]:
    if not digits:
        return []

    def helper(i: int, j: int, comb: str = "") -> None:
        if i == len(digits):
            combinations.append(comb)
            return

        letters = keypad[int(digits[i])]
        if j == len(letters):  # Letter doesn't exist
            return

        # Take j-th letter from the letters on the numpad
        helper(i+1, 0, comb+letters[j])
        helper(i, j+1, comb)  # Don't take the j-th letter

    combinations = []
    helper(0, 0)
    return combinations
