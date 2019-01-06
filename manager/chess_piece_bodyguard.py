#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/5/2019 11:35 PM
# @Author  : 王金波
# @File    : chess_piece_bodyguard.py


from util import *
from chess_piece import ChessPiece

class ChessPieceBoyguard(ChessPiece):

    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）。穷举法：
        对方
        (0,3)->(1,4)
        (0,5)->(1,4)
        (2,3)->(1,4)
        (2,5)->(1,4)
        (1,4)->(0,3)
        (1,4)->(0,5)
        (1,4)->(2,3)
        (1,4)->(2,5)
        己方
        (9,3)->(8,4)
        (9,5)->(8,4)
        (7,3)->(8,4)
        (7,5)->(8,4)
        (8,4)->(9,3)
        (8,4)->(9,5)
        (8,4)->(7,3)
        (8,4)->(7,5)
    '''
    def get_next_position_list(self, chess_manager):
        print('get_next_position_list：士')
        # 士
        next_pos_list = []  # [(row1, col1), (row2, col2), ...]
        if self.type == TYPE_MYOWN_SIDE and 7 <= self.row <= 9 and 3 <= self.col <= 5:  # 己方棋子
            if (((self.row == 9 and self.col == 3)
                    or (self.row == 9 and self.col == 5)
                    or (self.row == 7 and self.col == 3)
                    or (self.row == 7 and self.col == 5))
                    and (self.type != chess_manager.get_type_at_pos(8, 4))):
                position = (8, 4)
                next_pos_list.append(position)
            if self.row == 8 and self.col == 4:
                if self.type != chess_manager.get_type_at_pos(9, 3):
                    position = (9, 3)
                    next_pos_list.append(position)
                if self.type != chess_manager.get_type_at_pos(9, 5):
                    position = (9, 5)
                    next_pos_list.append(position)
                if self.type != chess_manager.get_type_at_pos(7, 3):
                    position = (7, 3)
                    next_pos_list.append(position)
                if self.type != chess_manager.get_type_at_pos(7, 5):
                    position = (7, 5)
                    next_pos_list.append(position)
        elif self.type == TYPE_ENEMY_SIDE and 0 <= self.row <= 2 and 3 <= self.col <= 5:  # 对方棋子
            if (((self.row == 0 and self.col == 3)
                    or (self.row == 0 and self.col == 5)
                    or (self.row == 2 and self.col == 3)
                    or (self.row == 2 and self.col == 5))
                    and (self.type != chess_manager.get_type_at_pos(1, 4))):
                position = (1, 4)
                next_pos_list.append(position)
            if self.row == 1 and self.col == 4:
                if self.type != chess_manager.get_type_at_pos(0, 3):
                    position = (0, 3)
                    next_pos_list.append(position)
                if self.type != chess_manager.get_type_at_pos(0, 5):
                    position = (0, 5)
                    next_pos_list.append(position)
                if self.type != chess_manager.get_type_at_pos(2, 3):
                    position = (2, 3)
                    next_pos_list.append(position)
                if self.type != chess_manager.get_type_at_pos(2, 5):
                    position = (2, 5)
                    next_pos_list.append(position)

        return next_pos_list
