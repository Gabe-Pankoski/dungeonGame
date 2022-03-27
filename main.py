def dungeonSolver(dungeon: list[list[int]]) -> int:
    height = len(dungeon)-1
    width = len(dungeon[0])-1
    #If input is 1x1
    if width == 0 and height == 0:
        if dungeon[0][0] > 0:
            return 1
        else:
            return abs(dungeon[0][0])+1
    #If input is a row vector
    elif width == 0 and height != 0:
        minValue = 0
        for i in range(height, -1, -1):
            minValue += dungeon[i][0]
            if minValue > 0:
                minValue = 0
        return abs(minValue)+1
    #If input is a column vector
    elif height == 0 and width != 0:
        minValue = 0
        for i in range(width, -1, -1):
            minValue += dungeon[0][i]
            if minValue > 0:
                minValue = 0
        return abs(minValue)+1
    #Standard input
    else:
        #Bottom Row
        for i in range(width-1, -1, -1):
            dungeon[height][i] += dungeon[height][i+1]
            if dungeon[height][i] > 0:
                dungeon[height][i] = 0
        #Far Right Column
        for i in range(height-1, -1, -1):
            dungeon[i][width] += dungeon[i+1][width]
            if dungeon[i][width] > 0:
                dungeon[i][width] = 0
        #Begin traversing rest of matrix
        #Right to left
        for i in range(height-1, -1, -1):
            for j in range(width-1, -1, -1):
                val = max(dungeon[i+1][j], dungeon[i][j+1])
                dungeon[i][j] += val
                if dungeon[i][j] > 0:
                    dungeon[i][j] = 0
        return abs(dungeon[0][0])+1


layout1 = [ [-2,-3,3], [-5,-10,1], [10,30,-5] ]

health = dungeonSolver(layout1)
print(health)