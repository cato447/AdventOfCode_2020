import numpy

f = open("Ressources/InputDay3.txt", 'r')

map = [f.replace('\n', '') for f in f.readlines()]

rightSteps = [1,3,5,7,1]
downSteps = [1,1,1,1,2]

treesEncounterd = []

x_pos = 0
counter = 0

for right, down in zip(rightSteps, downSteps):
    trees = 0 
    x_pos = 0
    for y_pos in range (0, len(map), down):
        if map[y_pos][x_pos] == '#':
            trees += 1
        x_pos = (x_pos + right) % len(map[0])
    treesEncounterd.append(trees)

print (numpy.prod(treesEncounterd))

