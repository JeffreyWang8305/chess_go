#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 1:05 PM
# @Author  : 王金波
# @File    : chess_piece.py

# id = -1
# pos_x = -1
# pos_y = -1
# type = 0        # 0-red, 1-green

# categories:
vehicle = 0     # 车
horse = 1       # 马
cannon = 2      # 炮
elephant = 3    # 象
bodyguard = 4   # 仕
prince = 5      # 将
soldier = 6     # 兵

class ChassPiece():


    def __init__(self, chess_row, chess_col, chess_category, chess_type):
        self._id = str(chess_category) + str(chess_type)
        self.category = chess_category
        self.type = chess_type
        self.row = chess_row
        self.col = chess_col

    def get_category(self):
        return self.category

    def get_type(self):
        return self.type

    def get_pos(self):
        return self.row, self.col

    def get_id(self):
        return self._id

    def get_name_by_category(self, category_num):
        result = ''
        if category_num == vehicle:
            result = '车'
        elif category_num == horse:
            result = '马'
        elif category_num == cannon:
            result = '炮'
        elif category_num == elephant:
            result = '象'
        elif category_num == bodyguard:
            result = '仕'
        elif category_num == prince:
            result = '将'
        elif category_num == soldier:
            result = '兵'
        return result

    def get_info(self):
        return self.row, self.col, self.get_name_by_category(self.category), self.type