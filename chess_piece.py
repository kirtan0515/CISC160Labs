from abc import ABC, abstractmethod


class Chess_Piece(ABC):

    def __init__(self, ID, position, color, direction, board_size=(8, 8)):
        self.id = ID
        self.position = position
        self.color = color
        self.direction = direction
        self.board_size = board_size

    def get_ID(self):
        return self.id

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def get_direction(self):
        return self.direction

    def get_board_size(self):
        return self.board_size

    def is_piece_on_board(self):
        if self.position == (None, None):
            return False
        else:
            return True

    def place(self, new_pos):
        if not self.is_valid_position(new_pos):
            return
        self.position = new_pos

    def is_valid_position(self, pos):
        return 0 <= pos[0] < self.board_size[0] and 0 <= pos[1] < self.board_size[1]

    @abstractmethod
    def get_valid_moves(self):
        pass

    def place(self, position):
        self.position = position

    def move(self, target_pos):
        if not self.is_valid_position(target_pos):
            return
        self.position = target_pos

    def remove(self):
        self.position = (None, None)

    def take(self, target):
        if target.position in self.get_valid_moves():
            self.position = target.position
            target.remove()
        else:
            print(f"Invalid take of {target} at {target.position} by {self}")

