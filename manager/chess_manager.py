# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 3:20 PM
# @Author  : 王金波
# @File    : chess_manager.py

from chess_piece import *
from util import *


class ChessManager:
    pass

    def __init__(self):
        self.chess_piece_list = list()

    def get_chess_pieses(self):
        return self.chess_piece_list

    def rand_run(self):
        print('rand_run')
        selected_chess_piece = None
        for chess_piece in self.chess_piece_list:
            category = chess_piece.get_category()
            if category == soldier:
                selected_chess_piece = chess_piece
                break
        row = col = -1
        if selected_chess_piece:
            print(selected_chess_piece)
            row, col = selected_chess_piece.perform_go()
            print(selected_chess_piece)
        if row != -1 and col != -1 and row <= max_row and col <= max_col:
            print('row:', row, 'col:', col, 'max_row:', max_row, 'max_col:', max_col)
            to_be_delete_piece = None
            for chess_piece in self.chess_piece_list:
                chess_row, chess_col, _category, _type = chess_piece.get_info()
                if row == chess_row and col == chess_col and selected_chess_piece.get_id() != chess_piece.get_id():
                    to_be_delete_piece = chess_piece
                    break
            if to_be_delete_piece:
                self.chess_piece_list.remove(to_be_delete_piece)
        print(len(self.chess_piece_list))

    def reset(self):
        if not self.chess_piece_list:
            self.chess_piece_list = list()
        self.chess_piece_list.append(ChassPiece(0, 0, 0, 0))  # 0, 0, '车', green
        self.chess_piece_list.append(ChassPiece(0, 1, 1, 0))  # 0, 1, '马', green
        self.chess_piece_list.append(ChassPiece(0, 2, 3, 0))  # 0, 2, '象', green
        self.chess_piece_list.append(ChassPiece(0, 3, 4, 0))  # 0, 3, '士', green
        self.chess_piece_list.append(ChassPiece(0, 4, 5, 0))  # 0, 4, '将'  green
        self.chess_piece_list.append(ChassPiece(0, 5, 4, 0))  # 0, 5, '士', green
        self.chess_piece_list.append(ChassPiece(0, 6, 3, 0))  # 0, 6, '象', green
        self.chess_piece_list.append(ChassPiece(0, 7, 1, 0))  # 0, 7, '马', green
        self.chess_piece_list.append(ChassPiece(0, 8, 0, 0))  # 0, 8, '车', green
        self.chess_piece_list.append(ChassPiece(2, 1, 2, 0))  # 2, 1, '炮', green
        self.chess_piece_list.append(ChassPiece(2, 7, 2, 0))  # 2, 7, '炮', green
        self.chess_piece_list.append(ChassPiece(3, 0, 6, 0))  # 3, 0, '兵', green
        self.chess_piece_list.append(ChassPiece(3, 2, 6, 0))  # 3, 2, '兵', green
        self.chess_piece_list.append(ChassPiece(3, 4, 6, 0))  # 3, 4, '兵', green
        self.chess_piece_list.append(ChassPiece(3, 6, 6, 0))  # 3, 6, '兵', green
        self.chess_piece_list.append(ChassPiece(3, 8, 6, 0))  # 3, 8, '兵', green

        self.chess_piece_list.append(ChassPiece(9, 0, 0, 1))  # 0, 0, '车', red
        self.chess_piece_list.append(ChassPiece(9, 1, 1, 1))  # 0, 1, '马', red
        self.chess_piece_list.append(ChassPiece(9, 2, 3, 1))  # 0, 2, '象', red
        self.chess_piece_list.append(ChassPiece(9, 3, 4, 1))  # 0, 3, '士', red
        self.chess_piece_list.append(ChassPiece(9, 4, 5, 1))  # 0, 4, '将'  red
        self.chess_piece_list.append(ChassPiece(9, 5, 4, 1))  # 0, 5, '士', red
        self.chess_piece_list.append(ChassPiece(9, 6, 3, 1))  # 0, 6, '象', red
        self.chess_piece_list.append(ChassPiece(9, 7, 1, 1))  # 0, 7, '马', red
        self.chess_piece_list.append(ChassPiece(9, 8, 0, 1))  # 0, 8, '车', red
        self.chess_piece_list.append(ChassPiece(7, 1, 2, 1))  # 2, 1, '炮', red
        self.chess_piece_list.append(ChassPiece(7, 7, 2, 1))  # 2, 7, '炮', red
        self.chess_piece_list.append(ChassPiece(6, 0, 6, 1))  # 3, 0, '兵', red
        self.chess_piece_list.append(ChassPiece(6, 2, 6, 1))  # 3, 2, '兵', red
        self.chess_piece_list.append(ChassPiece(6, 4, 6, 1))  # 3, 4, '兵', red
        self.chess_piece_list.append(ChassPiece(6, 6, 6, 1))  # 3, 6, '兵', red
        self.chess_piece_list.append(ChassPiece(6, 8, 6, 1))  # 3, 6, '兵', red
        return self.chess_piece_list
