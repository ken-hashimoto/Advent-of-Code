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
    rope = [[0, 0] for _ in range(10)]
    visited = set()
    visited.add(0)
    for t in text:
        d, cnt = t.split(" ")
        for _ in range(int(cnt)):
            if d == "R":
                rope[0][0] += 1
            if d == "L":
                rope[0][0] -= 1
            if d == "U":
                rope[0][1] += 1
            if d == "D":
                rope[0][1] -= 1
            for i in range(1, 10):
                if rinsetsu(rope[i - 1], rope[i]) or naname(rope[i - 1], rope[i]):
                    break
                # 方向ベクトル
                vec = (rope[i - 1][0] - rope[i][0], rope[i - 1][1] - rope[i][1])
                rope[i][0] += sign(vec[0])
                rope[i][1] += sign(vec[1])
            visited.add(rope[9][0] * 10000 + rope[9][1])
    print(len(visited))
