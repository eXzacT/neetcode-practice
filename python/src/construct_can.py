if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given a string 's' and an array of strings, return true if 's' can be made out of those words.
    Note that the same word in the dictionary may be reused multiple times in the segmentation.'''


@time_execution(executions=100)
def sol_dp(s: str, words: list[str]) -> bool:
    dp = [False]*(len(s)+1)
    dp[0] = True  # Can make up an empty string by not taking anything
    for i in range(len(s)+1):
        if dp[i]:
            for word in words:
                if word == s[i:i+len(word)]:
                    dp[i+len(word)] = True

    return dp[-1]


@time_execution(executions=100)
def sol_dp_v2(s: str, words: list[str]) -> bool:
    dp = [None]*(len(s)+1)
    dp[0] = ""
    for i in range(len(s)+1):
        if dp[i] is not None:
            for word in words:
                new_word = dp[i]+word
                if new_word == s:
                    return True
                # No point adding new words that don't match target
                if not s.startswith(new_word):
                    continue

                dp[len(new_word)] = new_word

    return False


@time_execution(executions=100)
def sol_dp_v3(s: str, words: list[str]) -> bool:
    dp = [False]*(len(s)+1)
    dp[0] = True  # Can make up an empty string by not taking anything
    for i in range(1, len(s)+1):
        for word in words:
            if i-len(word) >= 0 and dp[i-len(word)] and s[:i].endswith(word):
                dp[i] = True
                break

    return dp[-1]


@time_execution()
def sol(s: str, words: list[str]) -> bool:
    def helper(s: str) -> bool:
        if s == "":
            return True
        for word in words:
            if s.startswith(word):
                if helper(s[len(word):]):
                    return True

        return False

    return helper(s)


@time_execution()
def sol_memo(s: str, words: list[str]) -> bool:
    memo = {"": True}

    def helper(s: str) -> bool:
        if s in memo:
            return memo[s]
        for word in words:
            if s.startswith(word):
                if helper(s[len(word):]):
                    return True

        memo[s] = False
        return False

    return helper(s)


@time_execution()
def sol_v2(s: str, words: list[str]) -> bool:
    def helper(i: int, s: str) -> bool:
        if i == len(words):
            return False
        if s == "":
            return True

        if s.startswith(words[i]):
            return helper(0, s[len(words[i]):]) or helper(i+1, s)
        else:
            return helper(i+1, s)

    return helper(0, s)


@time_execution()
def sol_v2_memo(s: str, words: list[str]) -> bool:
    memo = {"": True}
    memo_hits = 0

    def helper(i: int, s: str) -> bool:
        nonlocal memo_hits
        if i == len(words):
            return False
        if s in memo:
            memo_hits += 1
            return memo[s]

        if s.startswith(words[i]):
            memo[s] = helper(0, s[len(words[i]):]) or helper(i+1, s)
        else:
            memo[s] = helper(i+1, s)
        return memo[s]

    return helper(0, s)
