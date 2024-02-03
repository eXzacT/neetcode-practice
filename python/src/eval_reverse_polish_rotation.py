if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an array of strings that represents an arithmetic expression in a Reverse Polish Notation, 
    evaluate the expression and return the results.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.'''


@time_execution()
def sol(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if len(token) != 1 or token.isdigit():
            stack.append(token)
        else:
            second = stack.pop()
            first = stack.pop()
            res = eval(first+token+second)
            stack.append(str(int(res)))

    return int(stack[0])


@time_execution()
def sol_v2(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(stack.pop()+stack.pop())
        elif token == '-':
            b, a = stack.pop(), stack.pop()
            stack.append(a-b)
        elif token == '*':
            stack.append(stack.pop()*stack.pop())
        elif token == '/':
            b, a = stack.pop(), stack.pop()
            stack.append(int(a/b))
        else:
            stack.append(int(token))

    return stack.pop()
