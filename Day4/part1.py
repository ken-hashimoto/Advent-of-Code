PATH = "Day4/input.txt"

with open(PATH, encoding="UTF-8") as input_file:
    text = input_file.read().split("\n")
    ans = 0
    for line in text:
        elf1, elf2 = line.split(",")
        elf1_head, elf1_tail = map(int, elf1.split("-"))
        elf2_head, elf2_tail = map(int, elf2.split("-"))
        if elf1_head <= elf2_head and elf2_tail <= elf1_tail:
            ans += 1
        elif elf2_head <= elf1_head and elf1_tail <= elf2_tail:
            ans += 1
    print(ans)
