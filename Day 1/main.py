with open('Data') as raw_data:
    lines = raw_data.readlines()


def part_one(): # Part 2 solves this as well but this is how I solved 1 before seeing 2
    biggest = 0
    current = 0
    for line in lines:
        if line == "\n":
            if current > biggest:
                biggest = current
            current = 0
            continue
        current += int(line)
    print(biggest)


def part_two():
    elves = []
    current = 0
    for line in lines:
        if line == "\n":
            elves.append(current)
            current = 0
            continue
        current += int(line)
    elves.sort(reverse=True)
    print(sum(elves[0:3]))


part_one()
part_two()
