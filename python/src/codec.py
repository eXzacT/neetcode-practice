def encode(strs: list[str]) -> str:
    return ''.join(map(lambda s: f"#{len(s)}{s}", strs))


def decode(s: str) -> list[str]:
    idx = 1
    res = []

    while idx < len(s):
        str_len = int(s[idx])
        word = s[idx+1:idx+1+str_len]
        res.append(word)
        idx += str_len+2

    return res


def sol(strs: list[str]) -> str:
    return decode(encode(strs))
