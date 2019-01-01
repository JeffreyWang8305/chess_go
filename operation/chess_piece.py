# -*- coding: UTF-8 -*-

# categories, defined by util
# vehicle = 0     # 车
# horse = 1       # 马
# cannon = 2      # 炮
# elephant = 3    # 象
# bodyguard = 4   # 仕
# prince = 5      # 将
# soldier = 6     # 兵

# id = -1
# pos_x = -1
# pos_y = -1
# type = 0        # 0-red, 1-green


class ChassPiece():


    def __init__(self, chess_category, chess_type, chess_row, chess_col):
        _id = str(chess_category) + str(chess_type)
        category = chess_category
        type = chess_type
        row = chess_row
        col = chess_col

    def get_category(self):
        return self.category

    def get_type(self):
        return self.type

    def get_pos(self):
        return self.row, self.col

    def get_id(self):
        return _id