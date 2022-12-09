PATH = "Day2\input.txt"
score_per_result = {
  "win":6,
  "draw":3,
  "lose":0
}
score_per_hand = {
  "X":1,
  "Y":2,
  "Z":3
}
def result(x,y):
  if (x,y) in [("A","X"),("B","Y"),("C","Z")]:
    return "draw"
  if (x,y) in [("A","Y"),("B","Z"),("C","X")]:
    return "win"
  if (x,y) in [("A","Z"),("B","X"),("C","Y")]:
    return "lose" 


def hand_to_choose(x,y):
  if y == "X": # 負けの時
    hands_dict = {
      "A":"Z",
      "B":"X",
      "C":"Y"
    }
  if y == "Y": #引き分けの時
    hands_dict = {
      "A":"X",
      "B":"Y",
      "C":"Z"
    }
  if y == "Z": # 勝つとき
    hands_dict = {
      "A":"Y",
      "B":"Z",
      "C":"X"
    }
  return hands_dict[x]


def jyanken_score(x,y):
  return score_per_hand[y] + score_per_result[result(x,y)]

with open(PATH,encoding="UTF-8") as input_file:
  text = input_file.read().split("\n")
  ans = 0
  for line in text:
    opponent,mine = line.split()
    mine = hand_to_choose(opponent,mine)
    ans += jyanken_score(opponent,mine)
  print(ans)
