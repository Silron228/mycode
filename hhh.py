# ШАХМАТЫ
white_frame = ["♙", "♞", "♝", "♜", "♛", "♚"]
black_frame = ["♙", '♘', "♗", "♖", "♕", "♔"]
algebrs = ["pawn", "knight", "bishop", "rook", "queen", "king"]
amount = [8, 2, 2, 2, 1, 1]

desk = []
block = [("■", "white"), ("□", "black")]
alf = [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]
numder = [str(i) for i in range(1, 9)][::-1]

pawns_figur = []
knights_figur, bishops_figur, rooks_figur = [], [], []
king_figur, queen_figur = [], []

all_figur = [pawns_figur, knights_figur, bishops_figur, rooks_figur, king_figur, queen_figur]

def create_figur():
    def flag(col):
        if col == "white": return white_frame
        else: return black_frame

    def create(listas: list, colors, name, amount1):
        for i in range(amount1):
            listas.append([i+1, name, colors, flag(colors)[algebrs.index(name)], True, []])

    def create_two(coler):
        for i in range(len(algebrs)):
            create(all_figur[i], coler, algebrs[i], amount[i])
       
    create_two("white"), create_two("black")
  
def create_desk():
    global desk
    # создаем список чередуемых квадратиков
    def plant():
        form = []
        for i in range(1, 9):
            if (i % 2 == 0): 
                form.append(block[1][0])
            else:
                form.append(block[0][0]) 
        return form

    # создаем чередование реверсов
    mode = plant()[::-1]
    for _ in range(8):
        desk.append(mode[::-1])
        mode = mode[::-1]   
    
    # добавляем цифорки на доску
    for i in range(len(desk)):
        def rev():
            desk[i].append(numder[i])
            desk[i] = desk[i][::-1]
        rev(), rev()
    
    # добавляем буковки
    for _ in range(2):
        desk.append(alf)
        desk = desk[::-1]
    
    print(" ")
    for i in desk:
        print(i)
        
def disposal():
    def pawn_mid():
        global pawns_figur
        def pawns(color, amount):
            global pawns_figur
            if color == "black": 
                pawns_figur = pawns_figur[::-1]
            for i1 in range(1, 9):
                for pawn in pawns_figur:
                    if pawn[2] == color:
                        desk[amount][i1] = pawn[3]
                        pawns_figur[i1-1][-1].append(i1)
                        pawns_figur[i1-1][-1].append(amount)              
            if color == "black": 
                pawns_figur = pawns_figur[::-1]           
        pawns("white", 7)
        pawns("black", 2)
        
        def rev():
            global pawns_figur
            for i in range(8):
                pawns_figur[i][-1] = pawns_figur[i][-1][:2]  
            pawns_figur = pawns_figur[::-1]  
        rev(), rev()
        
    pawn_mid() 

def handler():
    pass

def moves():
    pass


if __name__ == "__main__":
    create_figur()
    
    create_desk()
    
    disposal()
    
    for i in all_figur:
        print(i)  
        
    for i in desk:
        print(i)