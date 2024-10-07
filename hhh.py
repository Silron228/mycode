# ШАХМАТЫ
white_frame = ["♙", "♞", "♝", "♜", "♛", "♚"]
black_frame = ["♙", '♘', "♗", "♖", "♕", "♔"]
algebrs = ["pawn", "knight", "bishop", "rook", "queen", "king"]

pawns_figur = []
knights_figur, bishops_figur, rooks_figur = [], [], []
king_figur, queen_figur = [], []

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
    for i in range(1, amount + 1):
        listas.append(Figur(name, colors, flag(colors)[index_frame(name)]).constructor())

def create_two(coler):
    create_figur(pawns_figur, coler, "pawn", 8)
    create_figur(knights_figur, coler, "knight", 2)
    create_figur(bishops_figur, coler, "bishop", 2)
    create_figur(rooks_figur, coler, "rook", 2)
    create_figur(queen_figur, coler, "queen", 1)
    create_figur(king_figur, coler, "king", 1)
    
def create():
    create_two("white"), create_two("black")

if __name__ == "__main__":
    create()
    
    print(pawns_figur + knights_figur + bishops_figur + rooks_figur + king_figur + queen_figur)
    