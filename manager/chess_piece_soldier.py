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
                # self.row -= 1
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
        elif self.category == vehicle:
            pass
        return self.row, self.col

    def solder_go_horizontal(self, chess_manager):
        rand_horizontal = random.randint(0, 1)
        if rand_horizontal == 0:  # 横着走，50%概率 往左走
            if self.col > 0:
                self.col -= 1
            else:  # 已经走到头了，只能往右走了
                self.col += 1
        else:  # 50%概率 横着往右走
            if self.col < max_col:
                self.col += 1
            else:
                self.col -= 1  # 已经走到头了，只能往左走了