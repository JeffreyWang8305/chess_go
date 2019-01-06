#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/2/2019 11:33 PM
# @Author  : 王金波
# @File    : chess_piece_vehicle.py

from chess_piece import *


class ChessPieceVehicle(ChessPiece):

    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）
              车 代码规则不分敌我双方
    '''
    def get_next_position_list(self, chess_manager):
        print('get_next_position_list：车')
        next_pos_list = []
        if 0 <= self.row <= max_row and self.col <= max_col:
            for i in range(1, max_row + 1):
                next_type = chess_manager.get_type_at_pos(self.row - i, self.col)
                if self.type == next_type or self.row - i < 0:
                    break
                postion = (self.row - i, self.col)
                next_pos_list.append(postion)
                if self.type != next_type and next_type != TYPE_VACANCY:  # 只要到对方棋子就确定其为边界
                    break
            for i in range(1, max_row + 1):
                next_type = chess_manager.get_type_at_pos(self.row + i, self.col)
                if self.type == next_type or self.row + i > max_row:
                    break
                postion = (self.row + i, self.col)
                next_pos_list.append(postion)
                if self.type != next_type and next_type != TYPE_VACANCY:  # 只要到对方棋子就确定其为边界
                    break
            for i in range(1, max_col + 1):
                next_type = chess_manager.get_type_at_pos(self.row, self.col - i)
                if self.type == next_type or self.col - i < 0:
                    break
                postion = (self.row, self.col - i)
                next_pos_list.append(postion)
                if self.type != next_type and next_type != TYPE_VACANCY:  # 只要到对方棋子就确定其为边界
                    break
            for i in range(1, max_col + 1):
                next_type = chess_manager.get_type_at_pos(self.row, self.col + i)
                if self.type == next_type or self.col + i > max_col:
                    break
                postion = (self.row, self.col + i)
                next_pos_list.append(postion)
                if self.type != next_type and next_type != TYPE_VACANCY:  # 只要到对方棋子就确定其为边界
                    break
        return next_pos_list
