#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/6/2019 3:08 PM
# @Author  : 王金波
# @File    : chess_piece_horse.py

from util import *
from chess_piece import ChessPiece

class ChessPieceHorse(ChessPiece):

    def append_north_west1_position(self, output_pos_list):
        if self.row > 1 and self.col > 0:  # 只要没走到上边尽头，就可以走
            position = (self.row - 2, self.col - 1)
            output_pos_list.append(position)

    def append_north_west2_position(self, output_pos_list):
        if self.row > 0 and self.col > 1:  # 只要没走到上边尽头，就可以走
            position = (self.row - 1, self.col - 2)
            output_pos_list.append(position)

    def append_north_east1_position(self, output_pos_list):
        if self.row > 1 and self.col < max_col:  # 只要没走到上边尽头，就可以走
            position = (self.row - 2, self.col + 1)
            output_pos_list.append(position)

    def append_north_east2_position(self, output_pos_list):
        if self.row > 0 and self.col < max_col - 1:  # 只要没走到上边尽头，就可以走
            position = (self.row - 1, self.col + 2)
            output_pos_list.append(position)

    def append_south_west1_position(self, output_pos_list):
        if self.row < max_row and self.col > 1:  # 只要没走到上边尽头，就可以走
            position = (self.row + 1, self.col - 2)
            output_pos_list.append(position)

    def append_south_west2_position(self, output_pos_list):
        if self.row < max_row - 1 and self.col > 0:  # 只要没走到上边尽头，就可以走
            position = (self.row + 2, self.col - 1)
            output_pos_list.append(position)

    def append_south_east1_position(self, output_pos_list):
        if self.row < max_row - 1 and self.col < max_col:  # 只要没走到上边尽头，就可以走
            position = (self.row + 2, self.col + 1)
            output_pos_list.append(position)

    def append_south_east2_position(self, output_pos_list):
        if self.row < max_row and self.col < max_col - 1:  # 只要没走到上边尽头，就可以走
            position = (self.row + 1, self.col + 2)
            output_pos_list.append(position)

    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）。
    '''
    def get_next_position_list(self, chess_manager):
        print('get_next_position_list：马')
        # 马
        north_west1_type = chess_manager.get_type_at_pos(self.row - 2, self.col - 1)
        north_west2_type = chess_manager.get_type_at_pos(self.row - 1, self.col - 2)
        north_east1_type = chess_manager.get_type_at_pos(self.row - 2, self.col + 1)
        north_east2_type = chess_manager.get_type_at_pos(self.row - 1, self.col + 2)
        south_west1_type = chess_manager.get_type_at_pos(self.row + 1, self.col - 2)
        south_west2_type = chess_manager.get_type_at_pos(self.row + 2, self.col - 1)
        south_east1_type = chess_manager.get_type_at_pos(self.row + 2, self.col + 1)
        south_east2_type = chess_manager.get_type_at_pos(self.row + 1, self.col + 2)

        # print(north_west1_type, north_west2_type, north_east1_type, north_east2_type, south_west1_type, south_west2_type, south_east1_type, south_east2_type)

        north_west1_obstacle_type = chess_manager.get_type_at_pos(self.row - 1, self.col)
        north_west2_obstacle_type = chess_manager.get_type_at_pos(self.row, self.col - 1)
        north_east1_obstacle_type = chess_manager.get_type_at_pos(self.row - 1, self.col)
        north_east2_obstacle_type = chess_manager.get_type_at_pos(self.row, self.col + 1)
        south_west1_obstacle_type = chess_manager.get_type_at_pos(self.row, self.col - 1)
        south_west2_obstacle_type = chess_manager.get_type_at_pos(self.row + 1, self.col)
        south_east1_obstacle_type = chess_manager.get_type_at_pos(self.row + 1, self.col)
        south_east2_obstacle_type = chess_manager.get_type_at_pos(self.row, self.col + 1)

        next_pos_list = []  # [(row1, col1), (row2, col2), ...]
        if 0 <= self.row <= 9 and 0 <= self.col <= 8:

            if north_west1_type != self.type and north_west1_obstacle_type == TYPE_VACANCY:
                self.append_north_west1_position(next_pos_list)
            if north_west2_type != self.type and north_west2_obstacle_type == TYPE_VACANCY:
                self.append_north_west2_position(next_pos_list)

            if north_east1_type != self.type and north_east1_obstacle_type == TYPE_VACANCY:
                self.append_north_east1_position(next_pos_list)
            if north_east2_type != self.type and north_east2_obstacle_type == TYPE_VACANCY:
                self.append_north_east2_position(next_pos_list)

            if south_west1_type != self.type and south_west1_obstacle_type == TYPE_VACANCY:
                self.append_south_west1_position(next_pos_list)
            if south_west2_type != self.type and south_west2_obstacle_type == TYPE_VACANCY:
                self.append_south_west2_position(next_pos_list)

            if south_east1_type != self.type and south_east1_obstacle_type == TYPE_VACANCY:
                self.append_south_east1_position(next_pos_list)
            if south_east2_type != self.type and south_east2_obstacle_type == TYPE_VACANCY:
                self.append_south_east2_position(next_pos_list)

        return next_pos_list
