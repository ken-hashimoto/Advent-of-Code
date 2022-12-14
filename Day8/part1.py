PATH = "Day8/input.txt"
with open(PATH, encoding="UTF-8") as input_file:
    text = list(input_file.read().split("\n"))
    H = len(text)
    W = len(text[0])
    Grid = [[0 for _ in range(W)] for _ in range(H)]
    # ひとつずつ見ないようにして計算量を減らす
    for j in range(1, W - 1):  # 上から
        tmp_max = int(text[0][j])
        for i in range(1, H - 1):
            if tmp_max < int(text[i][j]):
                Grid[i][j] += 1
                tmp_max = int(text[i][j])
    for j in range(1, W - 1):  # 下から
        tmp_max = int(text[-1][j])
        for i in range(H - 2, 0, -1):
            if tmp_max < int(text[i][j]):
                Grid[i][j] += 1
                tmp_max = int(text[i][j])
    for i in range(1, H - 1):  # 左から
        tmp_max = int(text[i][0])
        for j in range(1, W - 1):
            if tmp_max < int(text[i][j]):
                Grid[i][j] += 1
                tmp_max = int(text[i][j])
    for i in range(1, H - 1):  # 右から
        tmp_max = int(text[i][-1])
        for j in range(W - 2, 0, -1):
            if tmp_max < int(text[i][j]):
                Grid[i][j] += 1
                tmp_max = int(text[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            if i == 0 or i == H - 1 or j == 0 or j == W - 1:
                ans += 1
                continue
            if Grid[i][j] >= 1:
                ans += 1
    print(ans)
