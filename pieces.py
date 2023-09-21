from chess_piece import Chess_Piece


class Pawn(Chess_Piece):

    def __init__(self, ID, position, color, direction, board_size=(8, 8)):
        super().__init__(ID, position, color, direction, board_size)
        self.direction = "UP" if color == "white" else "DOWN"

    def get_valid_moves(self):
        moves = []
        x, y = self.position

        if self.direction == "UP":
            if y < self.board_size[1] - 1:
                moves.append((x, y + 1))
            if y == 1 and y + 2 < self.board_size[1]:
                moves.append((x, y + 2))

        elif self.direction == "DOWN":
            if y > 0:
                moves.append((x, y - 1))
            if y == self.board_size[1] - 2 and self.board_size[1] > 1:
                moves.append((x, y - 2))

        return moves

    def take(self, target):
        if self.direction == "UP":
            if target.position in [(self.position[0] - 1, self.position[1] + 1),
                                   (self.position[0] + 1, self.position[1] + 1)]:
                self.position = target.position
                target.remove()

        elif self.direction == "DOWN":
            if target.position in [(self.position[0] - 1, self.position[1] - 1),
                                   (self.position[0] + 1, self.position[1] - 1)]:
                self.position = target.position
                target.remove()

    def replace(self, new_piece):
        if not new_piece.is_piece_on_board():
            previous_pos = self.position
            self.remove()
            new_piece.place(previous_pos)

    def remove(self):
        self.position = (None, None)

    def place(self, new_pos):
        if not self.is_valid_position(new_pos):
            return
        self.position = new_pos


class Knight(Chess_Piece):

    def get_valid_moves(self):
        moves = []
        x, y = self.position

        offsets = [(1, 2), (2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1), (1, -2), (-2, 1)]

        for dx, dy in offsets:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_position((new_x, new_y)):
                moves.append((new_x, new_y))

        return moves

    def place(self, new_pos):
        if not self.is_valid_position(new_pos):
            return
        self.position = new_pos

    def remove(self):
        self.position = (None, None)


class King(Chess_Piece):

    def get_valid_moves(self):
        moves = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for d in directions:
            new_x = self.position[0] + d[0]
            new_y = self.position[1] + d[1]

            if 0 <= new_x < self.board_size[0] and 0 <= new_y < self.board_size[1]:
                moves.append((new_x, new_y))

        return moves

    def place(self, new_pos):
        if self.is_valid_position(new_pos):
            self.position = new_pos

    def move(self, target_pos):
        if self.is_valid_position(target_pos):
            self.position = target_pos

    def take(self, target):
        target_position = target.get_position()
        if target_position in self.get_valid_moves():
            target.remove()


class Bishop(Chess_Piece):

    def get_valid_moves(self):
        moves = []
        x, y = self.position

        for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            for i in range(1, max(self.board_size)):
                next_x, next_y = x + dx * i, y + dy * i
                if not self.is_valid_position((next_x, next_y)):
                    break
                moves.append((next_x, next_y))

        return moves

    def is_valid_position(self, pos):
        return 0 <= pos[0] < self.board_size[0] and 0 <= pos[1] < self.board_size[1]

    def place(self, position):
        if not self.is_valid_position(position):
            return
        self.position = position

    def remove(self):
        self.position = (None, None)


class Rook(Chess_Piece):

    def get_valid_moves(self):
        moves = []
        x, y = self.position

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for i in range(1, max(self.board_size)):
                next_x, next_y = x + dx * i, y + dy * i
                if not self.is_valid_move(next_x, next_y):
                    break
                moves.append((next_x, next_y))

        return moves

    def is_valid_move(self, next_x, next_y):
        if not (0 <= next_x < self.board_size[0] and 0 <= next_y < self.board_size[1]):
            return False

        if next_x != self.position[0] and next_y != self.position[1]:
            return False

        return True

    def place(self, position):
        if not self.is_valid_position(position):
            return
        self.position = position

    def remove(self):
        self.position = (None, None)


class Queen(Rook):

    def get_valid_moves(self):
        moves = []
        x, y = self.position

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),
                       (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            for i in range(1, max(self.board_size)):
                next_x, next_y = x + dx * i, y + dy * i
                if not self.is_valid_position((next_x, next_y)):
                    break
                moves.append((next_x, next_y))

        return moves
