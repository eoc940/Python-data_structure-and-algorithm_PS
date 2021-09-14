# 영어 끝말잇기

def convert(idx, n):
    mok, nam = divmod(idx, n)
    return [nam+1, mok+1]

def solution(n, words):
    answer = []
    last = words[0][0]
    used = set()
    for idx, val in enumerate(words):
        if val[0] != last:
            return convert(idx, n)
        prior = len(used)
        used.add(val)
        after = len(used)
        if prior == after:
            return convert(idx, n)
        last = val[-1]
    return [0,0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n,words))