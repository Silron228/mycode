map = [[0]*8]*8

def Beauty(hop):
    if hop == 0:
        return 0
    if hop == 1:
            return "P"
map[2][3] = 1

def DisplayMap(map):
    for i in range(8):
        print(Beauty(map[i][0]), " ", Beauty(map[i][1]), " ", Beauty(map[i][2]), " ", Beauty(map[i][3]), " ", Beauty(map[i][4]), " ", Beauty(map[i][5]), " ", Beauty(map[i][6]), " ", Beauty(map[i][7]))

DisplayMap(map)

