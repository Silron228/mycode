# ШАХМАТЫ
white_frame = ["♙", "♞", "♝", "♜", "♛", "♚"]
black_frame = ["♙", '♘', "♗", "♖", "♕", "♔"]
algebrs = ["pawn", "knight", "bishop", "rook", "queen", "king"]
amount = [8, 2, 2, 2, 1, 1]

block = [("■", "white"), ("□", "black")]
alf = ["a", "b", "c", "d", "e", "f", "g", "h"]
numder = [str(i) for i in range(1, 9)]

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
            listas.append((name, colors, flag(colors)[algebrs.index(name)]))

    def create_two(coler):
        for i in range(len(algebrs)):
            create(all_figur[i], coler, algebrs[i], amount[i])
       
    create_two("white"), create_two("black")
  
def create_desk():
    desk = []
    def plant():
        form = []
        for i in range(1, 9):
            if (i % 2 == 0): n = block[1][0]
            else: n = block[0][0]
            form.append(n)
        return form
    
    mode = plant()[::-1]
    for i in range(8):
        desk.append(mode[::-1])
        mode = mode[::-1]    
        
    for i in desk:
        print(i)
        
    # def graphics():
    #     pass

def handler():
    pass

def moves():
    pass


if __name__ == "__main__":
    create_figur()
    
    for i in all_figur:
        print(i)
    
    create_desk()

    
    