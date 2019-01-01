#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 10:18 PM
# @Author  : 王金波
# @File    : chess_piece_soldier.py

from chess_piece import *


class ChessPieceSoldier(ChessPiece):

    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）
    '''
    def perform_random_go(self, chess_manager):
        # 兵
        if self.category == soldier:
            print('perform go, row:', self.row)

            if self.type == 1 and self.row >= 0 and self.col >= 0:
                # 判断可以走到的三个位置的棋子类型
                next_row_type = chess_manager.get_type_at_pos(self.row - 1, self.col)
                if next_row_type == self.type:  # 下一步为己方棋子，不能走
                    self.solder_go_horizontal(chess_manager)
                else:
                    if self.row <= 4:  # 红方棋子过河了
                        rand = random.randint(0, 1)
                        print(rand)
                        if rand == 0:  # 50% 概率, 横着走
                            self.solder_go_horizontal(chess_manager)
                        else:  # 50% 概率，继续往前走
                            if self.row > 0:
                                self.row -= 1
                            else:  # 走到底，只能横着走了
                                self.solder_go_horizontal(chess_manager)
                    else:  # 没过河，只能继续往前走
                        if self.row > 0:
                            self.row -= 1
                        else:  # 走到底，只能横着走了
                            self.solder_go_horizontal(chess_manager)

            elif self.type == 0 and self.row <= max_row and self.col <= max_col:
                next_row_type = chess_manager.get_type_at_pos(self.row + 1, self.col)
                if next_row_type == self.type:
                    self.solder_go_horizontal(chess_manager)
                else:
                    if self.row >= 6:  # 绿方棋子过河了
                        rand = random.randint(0, 1)
                        print(rand)
                        if rand == 0:  # 50% 概率, 横着走
                            self.solder_go_horizontal(chess_manager)
                        else:  # 50% 概率，继续往前走
                            if self.row < max_row:
                                self.row += 1
                            else:  # 走到底，只能横着走了
                                self.solder_go_horizontal(chess_manager)
                    else:  # 没过河，只能继续往前走
                        if self.row < max_row:
                            self.row += 1
                        else:  # 走到底，只能横着走了
                            self.solder_go_horizontal(chess_manager)
        return self.row, self.col

    def solder_go_horizontal(self, chess_manager):

        next_col_left_type = chess_manager.get_type_at_pos(self.row, self.col - 1)
        next_col_right_type = chess_manager.get_type_at_pos(self.row, self.col + 1)
        rand_horizontal = random.randint(0, 1)
        if rand_horizontal == 0:  # 横着走，50%概率 往左走
            if self.col > 0 and next_col_left_type != self.type:
                self.col -= 1
            elif next_col_right_type != self.type:  # 已经走到头了，只能往右走了
                self.col += 1
        else:  # 50%概率 横着往右走
            if self.col < max_col and next_col_right_type != self.type:
                self.col += 1
            elif next_col_left_type != self.type:
                self.col -= 1  # 已经走到头了，只能往左走了