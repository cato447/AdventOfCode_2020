def first():
    with open("/Users/cato447/Code/Cato447/AdventOfCode_2020/Scripts/res/day1.txt") as f:
        numbers = [int(line.replace("\n", "")) for line in f.readlines()]
        for num in numbers:
            for index in range(len(numbers)):
                if num + numbers[index] == 2020:
                    return num * numbers[index]

def second():
    with open("/Users/cato447/Code/Cato447/AdventOfCode_2020/Scripts/res/day1.txt") as f:
        numbers = [int(line.replace("\n", "")) for line in f.readlines()]
        for num in numbers:
            for index1 in range(len(numbers)):
                for index2 in range(len(numbers)):
                    if num + numbers[index1] + numbers[index2] == 2020:
                        return num * numbers[index1] * numbers[index2]

print(f"First solution: {first()}")
print(f"Second solution: {second()}")