PATH = "Day2\input.txt"
score_per_result = {"win": 6, "draw": 3, "lose": 0}
score_per_hand = {"X": 1, "Y": 2, "Z": 3}


def result(x, y):
    if (x, y) in [("A", "X"), ("B", "Y"), ("C", "Z")]:
        return "draw"
    if (x, y) in [("A", "Y"), ("B", "Z"), ("C", "X")]:
        return "win"
    else:
        return "lose"


def jyanken_score(x, y):
    return score_per_hand[y] + score_per_result[result(x, y)]


with open(PATH, encoding="UTF-8") as input_file:
    text = input_file.read().split("\n")
    ans = 0
    for line in text:
        opponent, mine = line.split()
        ans += jyanken_score(opponent, mine)
    print(ans)
