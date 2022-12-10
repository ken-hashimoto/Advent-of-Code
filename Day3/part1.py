PATH = "Day3\input.txt"


def score(x):
    if x in [chr(i) for i in range(65, 91)]:
        return ord(x) - 38
    else:
        return ord(x) - 96


with open(PATH, encoding="UTF-8") as input_file:
    text = input_file.read().split("\n")
    ans = 0
    for line in text:
        n = len(line)
        head, tail = set(line[: n // 2]), set(line[n // 2 :])
        s = head & tail
        ans += score(s.pop())
    print(ans)
