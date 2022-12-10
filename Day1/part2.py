PATH = "Day1\input.txt"

with open(PATH, encoding="UTF-8") as input_file:
    text = input_file.read().split("\n\n")
    calories_per_elf = [list(map(int, line.splitlines())) for line in text]
    total = [sum(calorie) for calorie in calories_per_elf]
    total.sort(reverse=True)
    print(sum(total[:3]))
