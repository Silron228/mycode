map = [[0]*8]*8

def Beauty(hop):
    match hop.split():
            case[0]:
                return 0
            case[1]:
                return "P"
            case[2]:
                return "C"
            case[3]:
                return "F"  
            case[4]:
                  return "K"
            case[5]:
                return "R"
            case[6]:
                return "B"
          


def DisplayMap(map):
    for i in range(8):
        for j in range(8):
            print(Beauty(map[i][j]), end=' ')
        print(end = "\n")

def MakeMove(id, map):
      DisplayMap(map)
