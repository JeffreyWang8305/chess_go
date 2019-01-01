# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 3:20 PM
# @Author  : 王金波
# @File    : chess_manager.py

from chess_piece import *
from chess_piece_soldier import *
from util import *


class ChessManager:
    pass

    def __init__(self):
        self.chess_piece_list = list()
        self.selected_chess_piece = None

    def get_chess_pieses(self):
        return self.chess_piece_list

    '''
        desc: 随机运行选中的棋子
    '''

    def rand_run(self):
        print('rand_run')
        if self.selected_chess_piece:
            print(self.selected_chess_piece)
            row, col = self.selected_chess_piece.perform_random_go(self)  # 移动选中的棋子，返回移动结束后的row, col
            print(self.selected_chess_piece)
            # 移除被吃掉的棋子
            if row != -1 and col != -1 and 0 <= row <= max_row and 0 <= col <= max_col:
                print('row:', row, 'col:', col, 'max_row:', max_row, 'max_col:', max_col)
                to_be_delete_piece = None
                for chess_piece in self.chess_piece_list:
                    chess_row, chess_col, _category, _type = chess_piece.get_info()
                    # 被吃掉的棋子不能是自己，不能是己方的棋子
                    if row == chess_row and col == chess_col and self.selected_chess_piece.get_type() != chess_piece.get_type():
                        to_be_delete_piece = chess_piece
                        break
                if to_be_delete_piece:
                    self.chess_piece_list.remove(to_be_delete_piece)
        print(len(self.chess_piece_list))

    def get_type_at_pos(self, row, col):
        print('get_type_at_pos:', row, col)
        type = -1
        for chess_piece in self.chess_piece_list:
            chess_row, chess_col, _category, type = chess_piece.get_info()
            print('type:', type, 'category:', _category)
            # 被吃掉的棋子不能是自己，不能是己方的棋子
            if row == chess_row and col == chess_col:
                print('type:', type, 'category:', _category)
                return type
        print('type:', type)
        return type

    def set_selected_chess_piece(self, selected_chess_piece):
        self.selected_chess_piece = selected_chess_piece

    def reset_data(self):
        self.chess_piece_list = list()
        self.chess_piece_list.append(ChessPiece(0, 0, 0, 0))  # 0, 0, '车', green
        self.chess_piece_list.append(ChessPiece(0, 1, 1, 0))  # 0, 1, '马', green
        self.chess_piece_list.append(ChessPiece(0, 2, 3, 0))  # 0, 2, '象', green
        self.chess_piece_list.append(ChessPiece(0, 3, 4, 0))  # 0, 3, '士', green
        self.chess_piece_list.append(ChessPiece(0, 4, 5, 0))  # 0, 4, '将'  green
        self.chess_piece_list.append(ChessPiece(0, 5, 4, 0))  # 0, 5, '士', green
        self.chess_piece_list.append(ChessPiece(0, 6, 3, 0))  # 0, 6, '象', green
        self.chess_piece_list.append(ChessPiece(0, 7, 1, 0))  # 0, 7, '马', green
        self.chess_piece_list.append(ChessPiece(0, 8, 0, 0))  # 0, 8, '车', green
        self.chess_piece_list.append(ChessPiece(2, 1, 2, 0))  # 2, 1, '炮', green
        self.chess_piece_list.append(ChessPiece(2, 7, 2, 0))  # 2, 7, '炮', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 0, 6, 0))  # 3, 0, '兵', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 2, 6, 0))  # 3, 2, '兵', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 4, 6, 0))  # 3, 4, '兵', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 6, 6, 0))  # 3, 6, '兵', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 8, 6, 0))  # 3, 8, '兵', green

        self.chess_piece_list.append(ChessPiece(9, 0, 0, 1))  # 0, 0, '车', red
        self.chess_piece_list.append(ChessPiece(9, 1, 1, 1))  # 0, 1, '马', red
        self.chess_piece_list.append(ChessPiece(9, 2, 3, 1))  # 0, 2, '象', red
        self.chess_piece_list.append(ChessPiece(9, 3, 4, 1))  # 0, 3, '士', red
        self.chess_piece_list.append(ChessPiece(9, 4, 5, 1))  # 0, 4, '将'  red
        self.chess_piece_list.append(ChessPiece(9, 5, 4, 1))  # 0, 5, '士', red
        self.chess_piece_list.append(ChessPiece(9, 6, 3, 1))  # 0, 6, '象', red
        self.chess_piece_list.append(ChessPiece(9, 7, 1, 1))  # 0, 7, '马', red
        self.chess_piece_list.append(ChessPiece(9, 8, 0, 1))  # 0, 8, '车', red
        self.chess_piece_list.append(ChessPiece(7, 1, 2, 1))  # 2, 1, '炮', red
        self.chess_piece_list.append(ChessPiece(7, 7, 2, 1))  # 2, 7, '炮', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 0, 6, 1))  # 3, 0, '兵', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 2, 6, 1))  # 3, 2, '兵', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 4, 6, 1))  # 3, 4, '兵', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 6, 6, 1))  # 3, 6, '兵', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 8, 6, 1))  # 3, 6, '兵', red
        return self.chess_piece_list
