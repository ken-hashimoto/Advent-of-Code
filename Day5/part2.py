PATH = "Day5/input.txt"
from collections import defaultdict, deque

with open(PATH, encoding="UTF-8") as input_file:
    init, move = input_file.read().split("\n\n")
    ans = 0
    piles = defaultdict(list)
    for boxes_text in init.split("\n")[::-1][1:]:
        for i, c in enumerate(boxes_text[1::4]):
            if c == " ":
                continue
            piles[i + 1].append(c)
    for m in move.split("\n"):
        _, cnt, _, frm, _, to = m.split()
        cnt, frm, to = int(cnt), int(frm), int(to)
        p = piles[frm][-cnt:]
        piles[to] = piles[to] + p
        piles[frm] = piles[frm][:-cnt]
    ans_li = []
    for key in piles.keys():
        ans_li.append(piles[key].pop())
    print("".join(ans_li))
