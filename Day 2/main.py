with open('Data') as raw_data:
    matches = raw_data.readlines()


# Rock        A & X
# Paper       B & Y
# Scissors    C & Z


def part_1():
    rps_score = {"X": 1, "Y": 2, "Z": 3}  # Score from rock, paper or scissors
    tot_score = 0
    for match in matches:
        if match == "A Y\n" or match == "B Z\n" or match == "C X\n":  # If I win
            tot_score += 6
        if match == "A X\n" or match == "B Y\n" or match == "C Z\n":  # If draw
            tot_score += 3
        tot_score += rps_score[match[2]]  # Score from selection

    print(tot_score)


# I have __ if:
# Rock        AY, BX, CZ
# Paper       AZ, BY, CX
# Scissors    AX, BZ, CY

def part_2():
    results_score = {"X": 0, "Y": 3, "Z": 6}  # Score from win, lose or draw
    tot_score = 0
    for match in matches:
        if match == "A Y\n" or match == "B X\n" or match == "C Z\n":  # If I have Rock
            tot_score += 1
        if match == "A Z\n" or match == "B Y\n" or match == "C X\n":  # If I have Paper
            tot_score += 2
        if match == "A X\n" or match == "B Z\n" or match == "C Y\n":  # If I have Scissors
            tot_score += 3
        tot_score += results_score[match[2]]  # Score from results

    print(tot_score)


part_1()
part_2()