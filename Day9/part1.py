PATH = "Day9/input.txt"
from copy import deepcopy


def rinsetsu(H, T):
    return abs(H[0] - T[0]) + abs(H[1] - T[1]) <= 1


def naname(H, T):
    for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if T[0] == H[0] + i and T[1] == H[1] + j:
            return True
    return False


def sign(n):
    if n == 0:
        return 0
    return abs(n) // n


with open(PATH, encoding="UTF-8") as input_file:
    text = input_file.read().split("\n")
    T = [0, 0]
    H = [0, 0]
    visited = set()
    visited.add(0)
    for t in text:
        d, cnt = t.split(" ")
        for c in range(int(cnt)):
            prev_H = deepcopy(H)
            if d == "R":
                H[0] += 1
            if d == "L":
                H[0] -= 1
            if d == "U":
                H[1] += 1
            if d == "D":
                H[1] -= 1
            if rinsetsu(H, T) or naname(H, T):
                continue
            vec = (H[0] - T[0], H[1] - T[1])
            T[0] += sign(vec[0])
            T[1] += sign(vec[1])
            visited.add(T[0] * 10000 + T[1])
    print(len(visited))
