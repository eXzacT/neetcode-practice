if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.'''


@time_execution()
def sol(s: str) -> bool:
    closing_bracket = {"}": "{", "]": "[", ")": "("}
    current = []
    for c in s:
        # Found a closing bracket, does it match the last opening one we found?
        if c in closing_bracket:
            if current and current[-1] == closing_bracket[c]:
                current.pop()
            # Doesn't match or there was no opening one but trying to close
            else:
                return False
        else:
            current.append(c)

    return True if not current else False
