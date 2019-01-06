#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/6/2019 12:08 AM
# @Author  : 王金波
# @File    : chess_piece_elephant.py

from util import *
from chess_piece import ChessPiece

class ChessPieceElephant(ChessPiece):

    def append_north_west_position(self, output_pos_list):
        if self.row > 0 and self.col > 0:  # 只要没走到上边尽头，就可以走
            position = (self.row - 2, self.col - 2)
            output_pos_list.append(position)

    def append_north_east_position(self, output_pos_list):
        if self.row > 0 and self.col < max_col:  # 只要没走到上边尽头，就可以走
            position = (self.row - 2, self.col + 2)
            output_pos_list.append(position)

    def append_south_west_position(self, output_pos_list):
        if ((self.type == TYPE_ENEMY_SIDE and self.row < 4) or (self.type == TYPE_MYOWN_SIDE and self.row < max_row))and self.col > 0:  # 只要没走到上边尽头，就可以走
            position = (self.row + 2, self.col - 2)
            output_pos_list.append(position)

    def append_south_east_position(self, output_pos_list):
        if ((self.type == TYPE_ENEMY_SIDE and self.row < 4) or (self.type == TYPE_MYOWN_SIDE and self.row < max_row))and self.col < max_col:  # 只要没走到上边尽头，就可以走
            position = (self.row + 2, self.col + 2)
            output_pos_list.append(position)
    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）。
    '''
    def get_next_position_list(self, chess_manager):
        # 象
        north_west_type = chess_manager.get_type_at_pos(self.row - 2, self.col - 2)
        north_east_type = chess_manager.get_type_at_pos(self.row - 2, self.col + 2)
        south_west_type = chess_manager.get_type_at_pos(self.row + 2, self.col - 2)
        south_east_type = chess_manager.get_type_at_pos(self.row + 2, self.col + 2)

        north_west_obstacle_type = chess_manager.get_type_at_pos(self.row - 1, self.col - 1)
        north_east_obstacle_type = chess_manager.get_type_at_pos(self.row - 1, self.col + 1)
        south_west_obstacle_type = chess_manager.get_type_at_pos(self.row + 1, self.col - 1)
        south_east_obstacle_type = chess_manager.get_type_at_pos(self.row + 1, self.col + 1)

        next_pos_list = []  # [(row1, col1), (row2, col2), ...]
        if self.type == TYPE_MYOWN_SIDE and 5 <= self.row <= 9 and 0 <= self.col <= 8:  # 己方棋子
            if self.row != 5:
                if north_west_type != self.type and north_west_obstacle_type == TYPE_VACANCY:  # 竖着走下一步不为己方棋子，可以走
                    self.append_north_west_position(next_pos_list)

                if north_east_type != self.type and north_east_obstacle_type == TYPE_VACANCY:  # 竖着走下一步不为己方棋子，可以走
                    self.append_north_east_position(next_pos_list)

            if south_west_type != self.type and south_west_obstacle_type == TYPE_VACANCY:  # 竖着走下一步不为己方棋子，可以走
                self.append_south_west_position(next_pos_list)

            if south_east_type != self.type and south_east_obstacle_type == TYPE_VACANCY:  # 竖着走下一步不为己方棋子，可以走
                self.append_south_east_position(next_pos_list)

        elif self.type == TYPE_ENEMY_SIDE and 0 <= self.row <= 4 and 0 <= self.col <= 8:  # 对方棋子
            if north_west_type != self.type and north_west_obstacle_type == TYPE_VACANCY:  # 竖着走下一步不为己方棋子，可以走
                self.append_north_west_position(next_pos_list)

            if north_east_type != self.type and north_east_obstacle_type == TYPE_VACANCY:  # 竖着走下一步不为己方棋子，可以走
                self.append_north_east_position(next_pos_list)

            if self.row != 4:
                if south_west_type != self.type and south_west_obstacle_type == TYPE_VACANCY:  # 竖着走下一步不为己方棋子，可以走
                    self.append_south_west_position(next_pos_list)

                if south_east_type != self.type and south_east_obstacle_type == TYPE_VACANCY:  # 竖着走下一步不为己方棋子，可以走
                    self.append_south_east_position(next_pos_list)

        return next_pos_list
