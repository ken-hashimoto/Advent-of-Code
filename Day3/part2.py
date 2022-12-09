PATH = "Day3\input.txt"

def score(x):
  if x in [chr(i) for i in range(65,91)]:
    return ord(x)-38
  else:
    return ord(x)-96
with open(PATH,encoding="UTF-8") as input_file:
  text = input_file.read().split("\n")
  ans = 0
  lines = []
  for line in text:
    if len(lines) < 3:
      lines.append(line)
      if len(lines) == 3:
        s0,s1,s2 = set(lines[0]),set(lines[1]),set(lines[2])
        s = s0 & s1 & s2
        ans += score(s.pop())
        lines = []
  print(ans)



