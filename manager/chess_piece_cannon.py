#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/6/2019 3:39 PM
# @Author  : 王金波
# @File    : chess_piece_cannon.py

from chess_piece import *


class ChessPieceCannon(ChessPiece):

    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）
    '''
    def get_next_position_list(self, chess_manager):
        next_pos_list = []
        if 0 <= self.row <= max_row and self.col <= max_col:

            terminal_row = self.row
            for i in range(1, max_row + 1):
                next_type = chess_manager.get_type_at_pos(self.row - i, self.col)
                if self.type == next_type or (self.type != next_type and next_type != -1) or self.row - i < 0:  # 只要是空的地方就可以走，直到遇到边界
                    break
                postion = (self.row - i, self.col)
                next_pos_list.append(postion)
                terminal_row = self.row - i
            terminal_row -= 1
            # 沿着这个方向继续查找第一个对方棋子，找到可以被炮隔着棋子打的那个
            for i in range(1, max_row + 1):
                next_type = chess_manager.get_type_at_pos(terminal_row - i, self.col)
                if self.type == next_type or terminal_row - i < 0:  # 只要是空的地方就可以走，直到遇到边界
                    break
                if self.type != next_type and next_type != -1:
                    postion = (terminal_row - i, self.col)
                    next_pos_list.append(postion)
                    break
            # ------
            terminal_row = self.row
            for i in range(1, max_row + 1):
                next_type = chess_manager.get_type_at_pos(self.row + i, self.col)
                if self.type == next_type or (self.type != next_type and next_type != -1) or self.row + i > max_row:
                    break
                postion = (self.row + i, self.col)
                next_pos_list.append(postion)
                terminal_row = self.row + i
            terminal_row += 1
            # 沿着这个方向继续查找第一个对方棋子，找到可以被炮隔着棋子打的那个
            for i in range(1, max_row + 1):
                next_type = chess_manager.get_type_at_pos(terminal_row + i, self.col)
                if self.type == next_type or terminal_row + i > max_row:  # 只要是空的地方就可以走，直到遇到边界
                    break
                if self.type != next_type and next_type != -1:
                    postion = (terminal_row + i, self.col)
                    next_pos_list.append(postion)
                    break
            # ------
            terminal_col = self.col
            for i in range(1, max_col + 1):
                next_type = chess_manager.get_type_at_pos(self.row, self.col - i)
                if self.type == next_type or (self.type != next_type and next_type != -1) or self.col - i < 0:
                    break
                postion = (self.row, self.col - i)
                next_pos_list.append(postion)
                terminal_col = self.col - i
            terminal_col -= 1
            for i in range(1, max_col + 1):
                next_type = chess_manager.get_type_at_pos(self.row, terminal_col - i)
                if self.type == next_type or () or terminal_col - i < 0:
                    break
                if self.type != next_type and next_type != -1:
                    postion = (self.row, terminal_col - i)
                    next_pos_list.append(postion)
                    break

            # ------
            terminal_col = self.col
            for i in range(1, max_col + 1):
                next_type = chess_manager.get_type_at_pos(self.row, self.col + i)
                if self.type == next_type or (self.type != next_type and next_type != -1) or self.col + i > max_col:
                    break
                postion = (self.row, self.col + i)
                next_pos_list.append(postion)
                terminal_col = self.col + i
            terminal_col += 1
            for i in range(1, max_col + 1):
                next_type = chess_manager.get_type_at_pos(self.row, terminal_col + i)
                if self.type == next_type or () or terminal_col + i < 0:
                    break
                if self.type != next_type and next_type != -1:
                    postion = (self.row, terminal_col + i)
                    next_pos_list.append(postion)
                    break
        return next_pos_list
