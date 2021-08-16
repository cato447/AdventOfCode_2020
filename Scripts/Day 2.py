import regex

def first():
    with open("/Users/cato447/Code/Cato447/AdventOfCode_2020/Scripts/res/day2.txt") as f:
        lines = [line.replace("\n", "").split() for line in f.readlines()]
        validPasswords = 0
        for line in lines:
            occurences = len(regex.findall(line[1].replace(":", ""), line[2]))
            borders = [int(elem) for elem in line[0].split('-')]
            if borders[0] <= occurences <= borders[1]:
                validPasswords += 1
        return validPasswords


def second():
    with open("/Users/cato447/Code/Cato447/AdventOfCode_2020/Scripts/res/day2.txt") as f:
        lines = [line.replace("\n", "").split() for line in f.readlines()]
        validPasswords = 0
        for line in lines:
            borders = [int(elem) for elem in line[0].split('-')]
            if (line[2][int(borders[0])-1] == line[1].replace(":","")) != (line[2][int(borders[1])-1] == line[1].replace(":","")):
                validPasswords += 1
        return validPasswords

print(f"First solution: {first()}")
print(f"Second solution: {second()}")