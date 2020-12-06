xPosition = 0
treesEncounterd = 0

def makeStep():
    global xPosition
    if xPosition+3 >= map[0].__len__():
        xPosition = (xPosition+3) - map[0].__len__()
    else :
        xPosition += 3

f = open("Ressources/InputDay3.txt", 'r')

map = [f.strip() for f in f.readlines()]
deepestLevel = map.__len__()


for i in range(1,deepestLevel):
    makeStep()
    if map[i][xPosition] == '#':
        treesEncounterd += 1

print(treesEncounterd)

