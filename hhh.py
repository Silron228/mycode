# ШАХМАТЫ
import copy

white_frame = ["♙", "♞", "♝", "♜", "♛", "♚"]
black_frame = ["♙", '♘', "♗", "♖", "♕", "♔"]
algebrs = ["pawn", "knight", "bishop", "rook", "queen", "king"]
amount = [8, 2, 2, 2, 1, 1]

desk = []
block = [("■", "white"), ("□", "black")]
alf = [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]
alf0 = ["a", "b", "c", "d", "e", "f", "g", "h"]
numder = [str(i) for i in range(1, 9)][::-1]

pawns_figur = []
knights_figur, bishops_figur, rooks_figur = [], [], []
king_figur, queen_figur = [], []

all_figur = [pawns_figur, knights_figur, bishops_figur, rooks_figur, queen_figur, king_figur]

def create_figur():
    def flag(col):
        if col == "white": return white_frame
        else: return black_frame

    def create(listas: list, colors, name, amount1):
        for i in range(amount1):
            listas.append([i+1, name, colors, flag(colors)[algebrs.index(name)], True, False, []])

    def create_two(coler):
        for i in range(len(algebrs)):
            create(all_figur[i], coler, algebrs[i], amount[i])    
    create_two("white"), create_two("black")
  
def create_desk():
    global desk, desk_archive
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
    
    desk_archive = copy.deepcopy(desk)
    
def disposal():
    
    # растановка пешек
    def pawn_mid():

        def reverse_figur(booling):
            global pawns_figur
            if booling != " ": pawns_figur = pawns_figur[::-1]
        
        def pawn_plant(row, color_frame):
            for i in range(len(alf0)):
                cord = handler(alf0[i] + str(row))
                desk[cord[0]][cord[1]] = color_frame[0]
                pawns_figur[i][-1] = cord
            reverse_figur(True)

        pawn_plant(2, white_frame)
        pawn_plant(7, black_frame)

    def rook_bishop_knight_mid(): 
        def rook_bishop_knight_plant(row, color_frame, number_frame, figur, a, b, c):
            for i in range(a, b, c):
                cord = handler(alf0[i] + str(row))
                desk[cord[0]][cord[1]] = color_frame[number_frame]

                if row == 1:
                    figur[0][-1] = cord
                    figur[1][-1] = cord
                else:
                    figur[2][-1] = cord
                    figur[3][-1] = cord
            
        rook_bishop_knight_plant(1, white_frame, 3, rooks_figur, 0, 8, 7)
        rook_bishop_knight_plant(8, black_frame, 3, rooks_figur, 0, 8, 7)  
        rook_bishop_knight_plant(1, white_frame, 2, bishops_figur, 2, 7, 3)
        rook_bishop_knight_plant(8, black_frame, 2, bishops_figur, 2, 7, 3)   
        rook_bishop_knight_plant(1, white_frame, 1, knights_figur, 1, 8, 5)
        rook_bishop_knight_plant(8, black_frame, 1, knights_figur, 1, 8, 5)       

    def queen_king_mid(): 
        def queen_king_plant(row, color_frame, number_frame, figur):
            cord = handler(alf0[number_frame-1] + str(row))
            desk[cord[0]][cord[1]] = color_frame[number_frame]
            if row == 1:
                figur[0][-1] = cord
            else:
                figur[-1][-1] = cord

        queen_king_plant(1, white_frame, 4, queen_figur)
        queen_king_plant(8, black_frame, 4, queen_figur)
        queen_king_plant(1, white_frame, 5, king_figur)
        queen_king_plant(8, black_frame, 5, king_figur)
                  
    pawn_mid() 
    rook_bishop_knight_mid()
    queen_king_mid()


def handler(move):
    
    if len(move) == 5 or len(move) == 2:
        for i in move:
            if (i in alf0 or i.lower() in alf0) or (i == "-") or (i in numder):
                move_hand = [i.lower() for i in move if "-" not in i]

                # откуда
                try:
                    x1 = alf0.index(move_hand[0])+1
                    y1 = numder.index(move_hand[1])+1
                except ValueError:
                    moves()

                
                if len(move) == 5:
                    # куда
                    try:
                        x2 = alf0.index(move_hand[2])+1
                        y2 = numder.index(move_hand[3])+1
                    except ValueError:
                        moves()

                    if desk[y1][x1] == block[0][0] or \
                        desk[y1][x1]== block[1][0]:

                            print("not move"), moves()
                    else:
                        print(desk[y1][x1], "->", desk[y2][x2])

                        return [y1, x1, y2, x2]
                else:
                    return [y1, x1]
            else:
                print("not move"), moves()
    
def moves():
    # e4-e5 or E4-E5
    move = str(input("-"))

    mov = handler(move)

    # пешка
    
    if desk[mov[0]][mov[1]] == white_frame[0]:
        for i in pawns_figur:
            # двойной ход
            if str([mov[0]]+[mov[1]]) == str(i[-1]):
                if mov[1] == mov[-1] and mov[0] == mov[-2]+2:
                    if i[-2] == False:
                        desk[mov[2]][mov[3]] = white_frame[0]
                        i[-1] = [mov[2], mov[3]]
                        desk[mov[0]][mov[1]] = desk_archive[mov[0]][mov[1]]
                        i[-2] = True
                    else:
                        print("not move"), moves()
                # одиночный ход
                elif mov[1] == mov[-1] and mov[0] == mov[-2]+1:
                    desk[mov[2]][mov[3]] = white_frame[0]
                    i[-1] = [mov[2], mov[3]]
                    desk[mov[0]][mov[1]] = desk_archive[mov[0]][mov[1]]
                    i[-2] = True
                else:
                    print("not move"), moves()





def print_desk():
    for i in desk:
        print(" ".join(i))
    

if __name__ == "__main__":
    create_figur()
    create_desk() 
    disposal()
    
    for i in all_figur: print(i)  
    
    print_desk()

    while True:
        moves()
        for i in all_figur: print(i) 
        print_desk()