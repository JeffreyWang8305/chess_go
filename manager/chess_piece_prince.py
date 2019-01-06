#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/5/2019 11:13 PM
# @Author  : 王金波
# @File    : chess_piece_prince.py

from util import *
from chess_piece import ChessPiece

class ChessPiecePrince(ChessPiece):

    def append_north_position(self, output_pos_list):
        if (self.type == TYPE_MYOWN_SIDE and self.row > 7) or (self.type == TYPE_ENEMY_SIDE and self.row > 0):  # 只要没走到上边尽头，就可以走
            position = (self.row - 1, self.col)
            output_pos_list.append(position)

    def append_south_position(self, output_pos_list):
        if (self.type == TYPE_MYOWN_SIDE and self.row < max_row) or (self.type == TYPE_ENEMY_SIDE and self.row < 2):  # 只要没走到底部尽头，就可以走
            position = (self.row + 1, self.col)
            output_pos_list.append(position)

    def append_left_position(self, output_pos_list):
        if self.col > 3:  # 只要没走到左侧尽头，就可以走
            position = (self.row, self.col - 1)
            output_pos_list.append(position)

    def append_right_position(self, output_pos_list):
        if self.col < 5:  # 只要没走到右侧尽头，就可以走
            position = (self.row, self.col + 1)
            output_pos_list.append(position)

    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）
    '''
    def get_next_position_list(self, chess_manager):
        print('get_next_position_list：将')
        # 将
        north_type = chess_manager.get_type_at_pos(self.row - 1, self.col)
        south_type = chess_manager.get_type_at_pos(self.row + 1, self.col)
        left_type = chess_manager.get_type_at_pos(self.row, self.col - 1)
        right_type = chess_manager.get_type_at_pos(self.row, self.col + 1)

        next_pos_list = []  # [(row1, col1), (row2, col2), ...]
        if self.type == TYPE_MYOWN_SIDE and 7 <= self.row <= 9 and 3 <= self.col <= 5:  # 己方棋子

            # 竖着走：
            self.update_go_vertical_position(next_pos_list, north_type, south_type)
            # 横着走:
            self.update_go_horizontal_position(left_type, next_pos_list, right_type)

        elif self.type == TYPE_ENEMY_SIDE and 0 <= self.row <= 2 and 3 <= self.col <= 5:  # 对方棋子
            # 竖着走：
            self.update_go_vertical_position(next_pos_list, north_type, south_type)
            # 横着走:
            self.update_go_horizontal_position(left_type, next_pos_list, right_type)
        return next_pos_list

    def update_go_vertical_position(self, next_pos_list, north_type, south_type):
        if north_type == self.type and south_type != self.type:  # 上面为己方棋子，下面不是己方棋子，可以往下走;
            self.append_south_position(next_pos_list)
        elif south_type == self.type and north_type != self.type:  # 下面为己方棋子，上面不是己方棋子，可以往上走
            self.append_north_position(next_pos_list)
        elif north_type == south_type == self.type:  # 无处走
            pass
        else:  # 上下均可走
            self.append_south_position(next_pos_list)
            self.append_north_position(next_pos_list)

    def update_go_horizontal_position(self, left_type, output_pos_list, right_type):
        if left_type == self.type and right_type != self.type:  # 左面为己方棋子，右面不是己方棋子，可以往右走;
            self.append_right_position(output_pos_list)
        elif right_type == self.type and left_type != self.type:  # 右面为己方棋子，左面不是己方棋子，可以往左走
            self.append_left_position(output_pos_list)
        elif left_type == right_type == self.type:  # 无处走
            pass
        else:  # 左右均可走
            self.append_left_position(output_pos_list)
            self.append_right_position(output_pos_list)
