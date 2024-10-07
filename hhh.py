# ШАХМАТЫ
white_frame = ["♙", "♞", "♝", "♜", "♛", "♚"]
black_frame = ["♙", '♘', "♗", "♖", "♕", "♔"]
algebrs = ["pawn", "knight", "bishop", "rook", "queen", "king"]
number = [8, 2, 2, 2, 1, 1]

pawns_figur = []
knights_figur, bishops_figur, rooks_figur = [], [], []
king_figur, queen_figur = [], []

all_figur = [pawns_figur, knights_figur, bishops_figur, rooks_figur, king_figur, queen_figur]

class Figur():
    def __init__(self, name, color, frame) -> None:
        self.name = name
        self.color = color
        self.frame = frame
    
    def constructor(self):
        return (self.name, self.color, self.frame)

def flag(col):
    if col == "white": return white_frame
    else: return black_frame
    
def index_frame(n):
    return algebrs.index(n)

def create_figur(listas: list, colors, name, amount):
    for i in range(amount):
        listas.append(Figur(name, colors, flag(colors)[index_frame(name)]).constructor())

def create_two(coler):
    for i in range(len(algebrs)):
        create_figur(all_figur[i], coler, algebrs[i], number[0])
 
def create():
    create_two("white"), create_two("black")

if __name__ == "__main__":
    create()
    
    print(all_figur)
    