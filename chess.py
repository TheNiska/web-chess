from abc import ABC, abstractmethod


class Piece(ABC):
    image_part1 = "<img src='/static/chess/"
    image_part2 = " class='piece-img'>"

    def __init__(self, name, position, color):
        self.name = name
        self.position = position
        self.color = color
        self.sprite = f"{self.image_part1}{name}_{color}.png'" \
                      f"{self.image_part2}"

    @abstractmethod
    def move(self):
        pass


class Pawn(Piece):
    def move(self):
        print('sth')


class Queen(Piece):
    def move(self):
        print('sth')


class King(Piece):
    def move(self):
        print('sth')


class Bishop(Piece):
    def move(self):
        print('sth')


class Knight(Piece):
    def move(self):
        print('sth')


class Rook(Piece):
    def move(self):
        print('sth')


class Board:
    def __init__(self):
        board = {}
        letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd',
                   5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        first_letter = ord('a')
        last_letter = ord('h')

        for i in range(1, 9):
            for j in range(1, 9):
                cell_name = letters[i] + str(j)
                board[cell_name] = 0

        for i in range(first_letter, last_letter + 1):
            p_wh = chr(i) + '2'
            p_bl = chr(i) + '7'
            board[p_wh] = Pawn('pawn', p_wh, 'white')
            board[p_bl] = Pawn('pawn', p_bl, 'black')

        board['d1'] = Queen('queen', 'd1', 'white')
        board['d8'] = Queen('queen', 'd8', 'black')
        board['e1'] = King('king', 'e1', 'white')
        board['e8'] = King('king', 'e8', 'black')
        board['c1'] = Bishop('bishop', 'c1', 'white')
        board['c8'] = Bishop('bishop', 'c8', 'black')
        board['f1'] = Bishop('bishop', 'f1', 'white')
        board['f8'] = Bishop('bishop', 'f8', 'black')
        board['b1'] = Knight('knight', 'b1', 'white')
        board['b8'] = Knight('knight', 'b8', 'black')
        board['g1'] = Knight('knight', 'g1', 'white')
        board['g8'] = Knight('knight', 'g8', 'black')
        board['a1'] = Rook('rook', 'a1', 'white')
        board['a8'] = Rook('rook', 'a8', 'black')
        board['h1'] = Rook('rook', 'h1', 'white')
        board['h8'] = Rook('rook', 'h8', 'black')

        self.board = board

    def move(self, start_pos, end_pos):
        # isValidMove = self.board[start_pos].can_go_there()
        # but the method of piece can_go_there() must know board,
        # so how to interact between Piece objects and the Board object?
        self.board[end_pos] = self.board[start_pos]
        self.board[start_pos] = 0
        return True
