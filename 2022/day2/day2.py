with open("day2.txt", "r") as f:
    data = f.read().splitlines()

# A for Rock, B for Paper, and C for Scissors. 
# X for Rock, Y for Paper, and Z for Scissors

# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

shape_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

first_round_logic = {
    "X": { "C":"Win", "B":"Loss","A":"Draw"}, 
    "Y": { "A":"Win", "C":"Loss","B":"Draw"},
    "Z": { "B":"Win", "A":"Loss","C":"Draw"} 
}

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. 
second_round_result_logic = {
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win"
}

second_round_logic = {
    "A": { "Win":"Y", "Loss":"Z","Draw":"X"}, 
    "B": { "Win":"Z", "Loss":"X","Draw":"Y"},
    "C": { "Win":"X", "Loss":"Y","Draw":"Z"} 
}

match_type_score = {
    "Win": 6,
    "Loss": 0,
    "Draw": 3
}

# first round
first_round_score = 0
first_round_results = []
for d in data:
    you = d.split(" ")[1]
    them = d.split(" ")[0]
    result = first_round_logic[you][them]
    first_round_results.append(match_type_score[result] + shape_scores[you])

print(sum(first_round_results))

# second round
second_round_score = 0
second_round_results = []
for d in data:
    their_play = d.split(" ")[0]
    result_you_want = second_round_result_logic[d.split(" ")[1]]
    shape_you_want = second_round_logic[their_play][result_you_want]
    second_round_results.append(match_type_score[result_you_want] + shape_scores[shape_you_want])
    
print(sum(second_round_results))