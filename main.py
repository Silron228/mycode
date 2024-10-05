map = [[0]*8]*8

def Beauty(hop):
    if hop == 0:
        return 0
    if hop == 1:
            return "P"

def DisplayMap(map):
    for i in range(8):
        for j in range(8):
            print(Beauty(map[i][j]), end=' ')
        print(end = "\n")

def MakeMove(id, map):
DisplayMap(map)



