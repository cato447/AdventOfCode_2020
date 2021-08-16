import numpy as np

def first():
    with open("/Users/cato447/Code/Cato447/AdventOfCode_2020/Scripts/res/day3.txt") as f:
        lines = [line.replace("\n", "").split() for line in f.readlines()]
        column = 0
        trees = 0
        for line in lines:
            if line[0][column] == '#':
                trees += 1
            if column < len(line[0])-3:
                column += 3
            else:
                column += 3
                column -= len(line[0])
        return trees


def second():
    with open("/Users/cato447/Code/Cato447/AdventOfCode_2020/Scripts/res/day3.txt") as f:
        lines = [line.replace("\n", "").split() for line in f.readlines()]
        stepsX = [1, 3, 5, 7, 1]
        stepsY = [1, 1, 1, 1, 2]
        countTrees = []
        for stepX, stepY in zip(stepsX, stepsY):
            column = 0
            trees = 0
            for index in range(0,len(lines),stepY):
                if lines[index][0][column] == '#':
                    trees += 1
                column += stepX
                if column > len(lines[index][0])-3:
                    column -= len(lines[index][0])
            countTrees.append(trees)
        return np.prod(countTrees)
        

print(f"First solution: {first()}")
print(f"Second solution: {second()}")