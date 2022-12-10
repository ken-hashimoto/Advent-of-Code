PATH = "Day6/input.txt"

with open(PATH, encoding="UTF-8") as input_file:
    text = input_file.read()
    s = []
    marker = 14
    for i in range(len(text)):
        if i < marker - 1:
            s.append(text[i])
            continue
        s.append(text[i])
        if len(s) == len(set(s)):
            print(i + 1)
            exit()
        else:
            s.pop(0)
