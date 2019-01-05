#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 10:18 PM
# @Author  : 王金波
# @File    : chess_piece_soldier.py

from chess_piece import *


class ChessPieceSoldier(ChessPiece):

    def append_north_position(self, output_pos_list):
        if self.row > 0:  # 只要没走到上边尽头，就可以走
            position = (self.row - 1, self.col)
            output_pos_list.append(position)

    def append_south_position(self, output_pos_list):
        if self.row < max_row:  # 只要没走到底部尽头，就可以走
            position = (self.row + 1, self.col)
            output_pos_list.append(position)

    def append_left_position(self, output_pos_list):
        if self.col > 0:  # 只要没走到左侧尽头，就可以走
            position = (self.row, self.col - 1)
            output_pos_list.append(position)

    def append_right_position(self, output_pos_list):
        if self.col < max_col:  # 只要没走到右侧尽头，就可以走
            position = (self.row, self.col + 1)
            output_pos_list.append(position)

    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）
    '''
    def get_next_position_list(self, chess_manager):
        # 兵
        horizontal_res = 1
        # if self.category == soldier:
        print('perform go, row:', self.row)

        north_type = chess_manager.get_type_at_pos(self.row - 1, self.col)
        south_type = chess_manager.get_type_at_pos(self.row + 1, self.col)
        left_type = chess_manager.get_type_at_pos(self.row, self.col - 1)
        right_type = chess_manager.get_type_at_pos(self.row, self.col + 1)

        next_pos_list = []  # [(row1, col1), (row2, col2), ...]
        if self.type == 1 and self.row >= 0 and self.col >= 0:  # 己方棋子
            if self.row <= 4:  # 红方棋子过河了
                if north_type != self.type:  # 竖着走下一步不为己方棋子，可以走
                    self.append_north_position(next_pos_list)
                # 横着走:
                self.update_go_horizontal_position(left_type, next_pos_list, right_type)
            else:  # 红方棋子未过河, 只能竖着走
                if north_type != self.type:  # 竖着走下一步不为己方棋子，可以走
                    self.append_north_position(next_pos_list)

        elif self.type == 0 and self.row <= max_row and self.col <= max_col:  # 对方棋子
            if self.row >= 6:  # 绿方棋子过河了
                if south_type != self.type:  # 竖着走下一步不为己方棋子，可以走
                    self.append_south_position(next_pos_list)
                # 横着走:
                self.update_go_horizontal_position(left_type, next_pos_list, right_type)
            else:  # 绿方棋子未过河, 只能竖着走
                if south_type != self.type:  # 竖着走下一步不为己方棋子，可以走
                    self.append_south_position(next_pos_list)
        return next_pos_list

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

    #         # 判断可以走到的三个位置的棋子类型
    #
    #         if north_type == self.type:  # 下一步为己方棋子，不能走
    #             print('next step is our chess, go horizontal!!!')
    #             horizontal_res = self.solder_go_horizontal(chess_manager)
    #         else:
    #             if self.row <= 4:  # 红方棋子过河了
    #                 rand = random.randint(0, 1)
    #                 # print(rand)
    #                 if rand == 0:  # 50% 概率, 横着走
    #                     horizontal_res = self.solder_go_horizontal(chess_manager)
    #                 else:  # 50% 概率，继续往前走
    #                     if self.row > 0:
    #                         self.row -= 1
    #                     else:  # 走到底，只能横着走了
    #                         horizontal_res = self.solder_go_horizontal(chess_manager)
    #             else:  # 没过河，只能继续往前走
    #                 if self.row > 0:
    #                     self.row -= 1
    #                 else:  # 走到底，只能横着走了
    #                     horizontal_res = self.solder_go_horizontal(chess_manager)
    #
    #     elif self.type == 0 and self.row <= max_row and self.col <= max_col:  # 对方棋子
    #         north_type = chess_manager.get_type_at_pos(self.row + 1, self.col)
    #         if north_type == self.type:  # 下一步为己方棋子，不能走
    #             print('next step is our chess, go horizontal!!!')
    #             horizontal_res = self.solder_go_horizontal(chess_manager)
    #         else:
    #             if self.row >= 6:  # 绿方棋子过河了
    #                 rand = random.randint(0, 1)
    #                 # print(rand)
    #                 if rand == 0:  # 50% 概率, 横着走
    #                     horizontal_res = self.solder_go_horizontal(chess_manager)
    #                 else:  # 50% 概率，继续往前走
    #                     if self.row < max_row:
    #                         self.row += 1
    #                     else:  # 走到底，只能横着走了
    #                         horizontal_res = self.solder_go_horizontal(chess_manager)
    #             else:  # 没过河，只能继续往前走
    #                 if self.row < max_row:
    #                     self.row += 1
    #                 else:  # 走到底，只能横着走了
    #                     horizontal_res = self.solder_go_horizontal(chess_manager)
    #     if horizontal_res == 0:
    #         print('stay dont move')
    #     return self.row, self.col, horizontal_res
    #
    # def solder_go_horizontal(self, chess_manager):
    #
    #     result = 1
    #     next_col_left_type = chess_manager.get_type_at_pos(self.row, self.col - 1)
    #     next_col_right_type = chess_manager.get_type_at_pos(self.row, self.col + 1)
    #     if next_col_left_type == self.type and next_col_right_type != self.type:  # 左面为己方棋子，只能往右走
    #         if self.col < max_col:
    #             self.col += 1
    #         else:
    #             result = 0
    #     elif next_col_right_type == self.type and next_col_left_type != self.type:  # 右面为己方棋子，只能往左走
    #         if self.col > 0:
    #             self.col -= 1
    #         else:
    #             result = 0
    #     elif next_col_left_type == next_col_right_type == self.type:  # 无处走
    #         result = 0
    #     else:
    #         rand_horizontal = random.randint(0, 1)
    #         if rand_horizontal == 0:  # 横着走，50%概率 往左走
    #             if self.col > 0:
    #                 self.col -= 1
    #             else:  # 已经走到头了，只能往右走了
    #                 self.col += 1
    #         else:  # 50%概率 横着往右走
    #             if self.col < max_col:
    #                 self.col += 1
    #             else:
    #                 self.col -= 1  # 已经走到头了，只能往左走了
    #     return result