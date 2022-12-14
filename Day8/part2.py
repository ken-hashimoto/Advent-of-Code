PATH = "Day8/input.txt"


def search_right(G, i, j, H, W):
    h = G[i][j]
    ret = 0
    while j + 1 < W:
        j += 1
        if h >= G[i][j]:
            ret += 1
        if h <= G[i][j]:
            break
    return ret


def search_left(G, i, j, H, W):
    h = G[i][j]
    ret = 0
    while 0 <= j - 1:
        j -= 1
        if h >= G[i][j]:
            ret += 1
        if h <= G[i][j]:
            break
    return ret


def search_up(G, i, j, H, W):
    h = G[i][j]
    ret = 0
    while 0 <= i - 1:
        i -= 1
        if h >= G[i][j]:
            ret += 1
        if h <= G[i][j]:
            break
    return ret


def search_down(G, i, j, H, W):
    h = G[i][j]
    ret = 0
    while i + 1 < H:
        i += 1
        if h >= G[i][j]:
            ret += 1
        if h <= G[i][j]:
            break
    return ret


with open(PATH, encoding="UTF-8") as input_file:
    text = list(input_file.read().split("\n"))
    G = []
    for t in text:
        G.append(list(map(int, list(t))))
    H = len(text)
    W = len(text[0])
    Grid = [[0 for _ in range(W)] for _ in range(H)]
    ans = 1
    for i in range(H):
        for j in range(W):
            g = 1
            if i != 0:  # 上端ではないとき
                g *= search_up(G, i, j, H, W)
            if i != H - 1:  # 下端ではないとき
                g *= search_down(G, i, j, H, W)
            if j != 0:  # 左端でないとき
                g *= search_left(G, i, j, H, W)
            if j != W - 1:  # 右端でないとき
                g *= search_right(G, i, j, H, W)
            Grid[i][j] = g
            ans = max(ans, g)
    print(ans)
