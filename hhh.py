# ШАХМАТЫ
white_frame = ["♙", "♞", "♝", "♜", "♛", "♚"]
black_frame = ["♙", '♘', "♗", "♖", "♕", "♔"]
algebrs = ["pawn", "knight", "bishop", "rook", "queen", "king"]
amount = [8, 2, 2, 2, 1, 1]

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
            listas.append((i+1, name, colors, flag(colors)[algebrs.index(name)], True, "x", "y"))

    def create_two(coler):
        for i in range(len(algebrs)):
            create(all_figur[i], coler, algebrs[i], amount[i])
       
    create_two("white"), create_two("black")
  
def create_desk():
    desk = []
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
    
    for i in desk:
        print(i)
        
def disposal():
    pass

def handler():
    pass

def moves():
    pass


if __name__ == "__main__":
    create_figur()
    
    for i in all_figur:
        print(i)
    
    create_desk()

    
    