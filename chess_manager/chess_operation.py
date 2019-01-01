# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 3:20 PM
# @Author  : 王金波
# @File    : chess_operation.py

from chess_piece import ChassPiece

class ChessOperation():
    pass

    def __init__(self):
        pass

    def reset(self):
        chess_piece_list = []
        chess_piece_list.append(ChassPiece(0, 0, 0, 0))  # 0, 0, '车', green
        chess_piece_list.append(ChassPiece(0, 1, 1, 0))  # 0, 1, '马', green
        chess_piece_list.append(ChassPiece(0, 2, 3, 0))  # 0, 2, '象', green
        chess_piece_list.append(ChassPiece(0, 3, 4, 0))  # 0, 3, '士', green
        chess_piece_list.append(ChassPiece(0, 4, 5, 0))  # 0, 4, '将'  green
        chess_piece_list.append(ChassPiece(0, 5, 4, 0))  # 0, 5, '士', green
        chess_piece_list.append(ChassPiece(0, 6, 3, 0))  # 0, 6, '象', green
        chess_piece_list.append(ChassPiece(0, 7, 1, 0))  # 0, 7, '马', green
        chess_piece_list.append(ChassPiece(0, 8, 0, 0))  # 0, 8, '车', green
        chess_piece_list.append(ChassPiece(2, 1, 2, 0))  # 2, 1, '炮', green
        chess_piece_list.append(ChassPiece(2, 7, 2, 0))  # 2, 7, '炮', green
        chess_piece_list.append(ChassPiece(3, 0, 6, 0))  # 3, 0, '兵', green
        chess_piece_list.append(ChassPiece(3, 2, 6, 0))  # 3, 2, '兵', green
        chess_piece_list.append(ChassPiece(3, 4, 6, 0))  # 3, 4, '兵', green
        chess_piece_list.append(ChassPiece(3, 6, 6, 0))  # 3, 6, '兵', green
        chess_piece_list.append(ChassPiece(3, 8, 6, 0))  # 3, 8, '兵', green

        chess_piece_list.append(ChassPiece(9, 0, 0, 1))  # 0, 0, '车', red
        chess_piece_list.append(ChassPiece(9, 1, 1, 1))  # 0, 1, '马', red
        chess_piece_list.append(ChassPiece(9, 2, 3, 1))  # 0, 2, '象', red
        chess_piece_list.append(ChassPiece(9, 3, 4, 1))  # 0, 3, '士', red
        chess_piece_list.append(ChassPiece(9, 4, 5, 1))  # 0, 4, '将'  red
        chess_piece_list.append(ChassPiece(9, 5, 4, 1))  # 0, 5, '士', red
        chess_piece_list.append(ChassPiece(9, 6, 3, 1))  # 0, 6, '象', red
        chess_piece_list.append(ChassPiece(9, 7, 1, 1))  # 0, 7, '马', red
        chess_piece_list.append(ChassPiece(9, 8, 0, 1))  # 0, 8, '车', red
        chess_piece_list.append(ChassPiece(7, 1, 2, 1))  # 2, 1, '炮', red
        chess_piece_list.append(ChassPiece(7, 7, 2, 1))  # 2, 7, '炮', red
        chess_piece_list.append(ChassPiece(6, 0, 6, 1))  # 3, 0, '兵', red
        chess_piece_list.append(ChassPiece(6, 2, 6, 1))  # 3, 2, '兵', red
        chess_piece_list.append(ChassPiece(6, 4, 6, 1))  # 3, 4, '兵', red
        chess_piece_list.append(ChassPiece(6, 6, 6, 1))  # 3, 6, '兵', red
        chess_piece_list.append(ChassPiece(6, 8, 6, 1))  # 3, 6, '兵', red
        return chess_piece_list