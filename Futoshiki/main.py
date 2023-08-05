from Futoshiki.Models.Board import Board
from Futoshiki.Models.EdgeType import EdgeType

if __name__ == '__main__':
    b = Board(4)

    b.set_value((1, 1), 1)
    b.set_value((2, 2), 2)
    b.set_value((3, 3), 3)
    b.set_edge((0, 2), EdgeType.LT, (0, 3))
    b.set_edge((2, 2), EdgeType.GT, (3, 2))
    print(b)
    print(b.is_valid_board())
    print(b.solve())
    print(b)
