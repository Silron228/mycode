# ШАХМАТЫ
import copy

white_frame = ["♟", "♞", "♝", "♜", "♛", "♚"]
black_frame = ["♙", '♘', "♗", "♖", "♕", "♔"]
names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
amount = [8, 2, 2, 2, 1, 1]

desk, block = [], ["■", "□"]
alf = ["a", "b", "c", "d", "e", "f", "g", "h"]
numder = [str(i) for i in range(1, 9)][::-1]

knights_figur, bishops_figur, rooks_figur = [], [], []
pawns_figur, king_figur, queen_figur = [], [], []

all_figur = [pawns_figur, knights_figur, bishops_figur, rooks_figur, queen_figur, king_figur]

def create_figur():
    def flag(col):
        if col == "white": return white_frame
        else: return black_frame

    def create(listas: list, colors, name, amount1):
        for i in range(amount1):
            listas.append([i+1, name, colors, flag(colors)[names.index(name)], True, False, []])

    def create_two(coler):
        for i in range(len(names)):
            create(all_figur[i], coler, names[i], amount[i])    
    create_two("white"), create_two("black")
  
def create_desk():
    global desk, desk_archive
    # создаем список чередуемых квадратиков
    def plant():
        form = []
        for i in range(1, 9):
            if (i % 2 == 0): 
                form.append(block[1])
            else:
                form.append(block[0]) 
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
        desk.append([" "]+alf+[" "])
        desk = desk[::-1]
    
    desk_archive = copy.deepcopy(desk)
    
def setting():
    # растановка пешек
    def pawn_setting():

        def reverse_figur(booling):
            global pawns_figur
            if booling != " ": pawns_figur = pawns_figur[::-1]
        
        def pawn_plant(row, color_frame):
            for i in range(len(alf)):
                cord = handler(alf[i] + str(row))
                desk[cord[0]][cord[1]] = color_frame[0]
                pawns_figur[i][-1] = cord
            reverse_figur(True)

        pawn_plant(2, white_frame)
        pawn_plant(7, black_frame)

    def rbk_setting(): 
        def rbk_plant(row, color_frame, number_frame, figur, a, b):
            nm = 0
            for i in range(a, 8, b):
                cord = handler(alf[i] + str(row))
                desk[cord[0]][cord[1]] = color_frame[number_frame]
                
                
                if row == 1:
                    if nm == 0:
                        duble = copy.deepcopy(cord)
                        figur[0][-1] = cord
                        nm +=1
                    if duble != cord: figur[1][-1] = cord
                    
                else:
                    if nm == 0:
                        duble = copy.deepcopy(cord)
                        figur[2][-1] = cord
                        nm +=1
                    if duble != cord: figur[3][-1] = cord
                    
        def joil(color, k):
            rbk_plant(k, color, 1, knights_figur, 1, 5)
            rbk_plant(k, color, 2, bishops_figur, 2, 3)
            rbk_plant(k, color, 3, rooks_figur,   0, 7)
        joil(white_frame, 1), joil(black_frame, 8)

    def queen_king_mid(): 
        def queen_king_plant(row, color_frame, number_frame, figur):
            cord = handler(alf[number_frame-1] + str(row))
            desk[cord[0]][cord[1]] = color_frame[number_frame]

            if row == 1: figur[0][-1] = cord
            else: figur[-1][-1] = cord

        def joil(color, k):
            queen_king_plant(k, color, 4, queen_figur)
            queen_king_plant(k, color, 5, king_figur)
        joil(white_frame, 1), joil(black_frame, 8)
                  
    pawn_setting(), rbk_setting(), queen_king_mid()

def handler(move):
    
    if len(move) == 5 or len(move) == 2:
        for i in move:
            if (i in alf or i.lower() in alf) or (i == "-") or (i in numder):
                move_hand = [i.lower() for i in move if "-" not in i]
                # откуда
                try:
                    x1 = alf.index(move_hand[0])+1
                    y1 = numder.index(move_hand[1])+1           
                except ValueError: not_move()
        
                if len(move) == 5:
                    # куда
                    try:
                        x2 = alf.index(move_hand[2])+1
                        y2 = numder.index(move_hand[3])+1
                    except ValueError: not_move()

                    if desk[y1][x1] == block[0] or \
                        desk[y1][x1]== block[1]:
                            not_move()
                    else:
                        print(desk[y1][x1], "->", desk[y2][x2])

                        return [y1, x1, y2, x2]
                else:
                    return [y1, x1]
            else: not_move()
    else: not_move()
    
def moves():
    global mov, y1, x1, y2, x2
    try:
        mov = handler(str(input("-")))
    except KeyboardInterrupt: print(" game off"), exit()
    
    y1, x1 = mov[0], mov[1] 
    y2, x2 = mov[2], mov[3]

    def true_move(pawn, k):
        desk[y2][x2] = white_frame[k]
        pawn[-1] = [y2, x2]
        desk[y1][x1] = desk_archive[y1][x1]
        pawn[-2] = True
        print("успешный ход")

    def move_pawn():
        for pawn in pawns_figur: 
            if (desk[y2][x2] in block):
                if str([y1]+[x1]) == str(pawn[-1]):
                    if x1 == x2 and (y1 == y2 + 2):
                        if pawn[-2] == False:
                            if (desk[y2 + 1][x2] in block):
                                true_move(pawn, 0)
                                break
                        else: not_move()
                    elif x1 == x2 and y1 == y2 + 1:
                        true_move(pawn,0)
                        break
                    else: not_move()
            else: not_move()

    def move_kbr(frame):

        def move_knight():
            if (((x1 == x2 + 1) or (x1 == x2 - 1)) and ((y1 == y2 + 2) or (y1 == y2 - 2))) or \
                (((x1 == x2 + 2) or (x1 == x2 - 2)) and ((y1 == y2 + 1) or (y1 == y2 - 1))):
                    if desk[y2][x2] not in white_frame:
                        return True
                    else: not_move()

        def move_bishop():
            global resultat, k, result
            resultat = "X"    
            for i in range(9):
                k = 0        
                def instakl(yk, xk):
                    global k, result, resultat
                    result = []          
                    y0 = (eval(str(y2)+yk+str(k)))
                    x0 = (eval(str(x2)+xk+str(k)))                  
                    while (y0 != y1 and x0 != x1):                    
                        y0 = (eval(str(y2)+yk+str(k)))
                        x0 = (eval(str(x2)+xk+str(k)))                
                        if desk[y2][x2] == desk[y0][x0] and desk[y2][x2] in black_frame:  
                            result.append(True) 
                        if desk[y0][x0] not in block:
                            result.append(False)                       
                        k+=1 
                 
                    if result.count(False) == 2 and result.count(True) == 1: resultat = True
                    elif result.count(False) > 2: resultat = False               
                    else: resultat = True
                
                if (y1 == y2 + i and x1 == x2 + i): instakl("+", "+")
                if (y1 == y2 - i and x1 == x2 + i): instakl("-", "+")
                if (y1 == y2 + i and x1 == x2 - i): instakl("+", "-")
                if (y1 == y2 - i and x1 == x2 - i): instakl("-", "-")               
            return resultat   
        
        def move_rook(): 
            for i in range(9):
                k = 0
                result = []
                resultat = "X" 
                if (y1 == y2 + i) and (x1 == x2): 
                    while (y2 + k != y1):
                        if desk[y2][x2] == desk[y2 + k][x2] and desk[y2][x2] in black_frame:  
                            result.append(True) 
                        if desk[y2 + k][x2] not in block:
                            result.append(False) 
                        k+=1
                        
                if (y1 == y2 - i) and (x1 == x2):
                    while (y2 - k != y1):
                        if desk[y2][x2] == desk[y2 - k][x2] and desk[y2][x2] in black_frame:  
                            result.append(True) 
                        if desk[y2 - k][x2] not in block:
                            result.append(False) 
                        k+=1
                        
                if (x1 == x2 + i) and (y1 == y2):
                    while (x2 + k != y1):
                        if desk[y2][x2] == desk[y2][x2 + k] and desk[y2][x2] in black_frame:  
                            result.append(True) 
                        if desk[y2][x2 + k] not in block:
                            result.append(False) 
                        k+=1
                        
                if (x1 == x2 - i) and (y1 == y2):
                    while (x2 - k != y1):
                        if desk[y2][x2] == desk[y2][x2 - k] and desk[y2][x2] in black_frame:  
                            result.append(True) 
                        if desk[y2][x2 - k] not in block:
                            result.append(False) 
                        k+=1
                if result.count(False) == 2 and result.count(True) == 1: resultat = True
                elif result.count(False) > 2: resultat = False               
                else: resultat = True
                return resultat 
                  
        
        def move_dauble_figur(clas_figur, type_figur):
            for cl in clas_figur:
                if (desk[y2][x2] in (block+black_frame)):
                    if str([y1]+[x1]) == str(cl[-1]):
                        if type_figur == True:
                            true_move(cl, frame)
                            break
                        else: not_move()    
                    else: print("нет такой фигуры")            
                else: not_move()
        
        if frame == 1: move_dauble_figur(all_figur[frame], move_knight())
        if frame == 2: move_dauble_figur(all_figur[frame], move_bishop())
        if frame == 3: move_dauble_figur(all_figur[frame], move_rook())


    # если выбранная фигура
    if desk[y1][x1] == white_frame[0]: move_pawn()
    for i in range(1, 5):
        if desk[y1][x1] == white_frame[i]: move_kbr(i)
    
def print_desk(): [print(" ".join(i)) for i in desk]

def not_move(): play()

def print_all_figur():
    [print(i) for i in pawns_figur], [print("\n")]
    [print(i) for i in knights_figur], [print("\n")]
    [print(i) for i in bishops_figur]
    
def play():
    while True:
        print_desk()
        moves()

if __name__ == "__main__":
    create_figur(), create_desk(), setting()
    print_desk()
    play()      