# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 3:20 PM
# @Author  : 王金波
# @File    : chess_manager.py

import random
import time
from chess_piece import *
from chess_piece_soldier import *
from chess_piece_vehicle import *
from chess_piece_prince import *
from chess_piece_bodyguard import *
from chess_piece_elephant import *
from chess_piece_horse import *
from chess_piece_cannon import *
from util import *


class ChessManager:
    pass

    def __init__(self):
        self.chess_piece_list = list()
        self.selected_chess_piece = None
        self.is_my_turn = True
        self.chess_board = None

    def get_chess_pieses(self):
        return self.chess_piece_list

    '''
        desc: 随机运行选中的棋子
    '''

    def predict(self):
        if self.selected_chess_piece:
            next_pos_list = self.selected_chess_piece.get_next_position_list(self)  # 移动选中的棋子，返回移动结束后的row, col
            print(next_pos_list)
        return next_pos_list

    def random_run(self, next_pos_list):
        row = -1
        col = -1
        if next_pos_list and next_pos_list[0]:
            [(row, col)] = random.sample(next_pos_list, 1)  # TODO： 现在是随机选择，后续修改此处
        return row, col

    def go_next(self, row, col):
        if self.selected_chess_piece and row > -1 and col > -1:
            self.selected_chess_piece.set_pos(row, col)
            # 移除被吃掉的棋子
            if row != -1 and col != -1 and 0 <= row <= max_row and 0 <= col <= max_col:
                to_be_delete_piece = None
                for chess_piece in self.chess_piece_list:
                    chess_row, chess_col, _category, _type = chess_piece.get_info()
                    # 被吃掉的棋子不能是自己，不能是己方的棋子
                    if row == chess_row and col == chess_col and self.selected_chess_piece.get_type() != chess_piece.get_type():
                        to_be_delete_piece = chess_piece
                        break
                if to_be_delete_piece:
                    self.chess_piece_list.remove(to_be_delete_piece)
        else:
            print('can not go next, maybe not select, or pos error!!! row:', row, 'col:', col)

    def auto_run(self):
        print('chess manager: auto_run')
        cnt = 500
        while cnt > 0:
            if self.is_my_turn:
                print('my turn')
                self.select_chess_by_type_and_go(TYPE_MYOWN_SIDE)
                self.is_my_turn = False
            else:
                print('not my turn')
                self.select_chess_by_type_and_go(TYPE_ENEMY_SIDE)
                self.is_my_turn = True
            # time.sleep(1)  # sleep N 秒
            cnt -= 1
        print('complete!')

    def select_chess_by_type_and_go(self, type):
        chess_list = []
        for chess_piece in self.chess_piece_list:
            if type == chess_piece.get_type():
                chess_list.append(chess_piece)
        print('len', len(chess_list), 'type', type)
        if chess_list and chess_list[0]:
            [self.selected_chess_piece] = random.sample(chess_list, 1)  # TODO： 现在是随机选择，后续修改此处
        if self.selected_chess_piece:
            self.chess_board.select_and_predict(self.selected_chess_piece)
            # time.sleep(1)  # sleep N 秒
            self.chess_board.go_next()

    def get_type_at_pos(self, row, col):
        for chess_piece in self.chess_piece_list:
            chess_row, chess_col, _category, type = chess_piece.get_info()
            # 被吃掉的棋子不能是自己，不能是己方的棋子
            if row == chess_row and col == chess_col:
                return type
        return -1

    def set_selected_chess_piece(self, selected_chess_piece):
        self.selected_chess_piece = selected_chess_piece
        print('set_selected_chess_piece:', selected_chess_piece)

    def reset_data(self):
        self.chess_piece_list = list()
        self.chess_piece_list.append(ChessPieceVehicle(0, 0, 0, 0))  # 0, 0, '车', green
        self.chess_piece_list.append(ChessPieceHorse(0, 1, 1, 0))  # 0, 1, '马', green
        self.chess_piece_list.append(ChessPieceElephant(0, 2, 3, 0))  # 0, 2, '象', green
        self.chess_piece_list.append(ChessPieceBoyguard(0, 3, 4, 0))  # 0, 3, '士', green
        self.chess_piece_list.append(ChessPiecePrince(0, 4, 5, 0))  # 0, 4, '将'  green
        self.chess_piece_list.append(ChessPieceBoyguard(0, 5, 4, 0))  # 0, 5, '士', green
        self.chess_piece_list.append(ChessPieceElephant(0, 6, 3, 0))  # 0, 6, '象', green
        self.chess_piece_list.append(ChessPieceHorse(0, 7, 1, 0))  # 0, 7, '马', green
        self.chess_piece_list.append(ChessPieceVehicle(0, 8, 0, 0))  # 0, 8, '车', green
        self.chess_piece_list.append(ChessPieceCannon(2, 1, 2, 0))  # 2, 1, '炮', green
        self.chess_piece_list.append(ChessPieceCannon(2, 7, 2, 0))  # 2, 7, '炮', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 0, 6, 0))  # 3, 0, '兵', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 2, 6, 0))  # 3, 2, '兵', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 4, 6, 0))  # 3, 4, '兵', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 6, 6, 0))  # 3, 6, '兵', green
        self.chess_piece_list.append(ChessPieceSoldier(3, 8, 6, 0))  # 3, 8, '兵', green

        self.chess_piece_list.append(ChessPieceVehicle(9, 0, 0, 1))  # 0, 0, '车', red
        self.chess_piece_list.append(ChessPieceHorse(9, 1, 1, 1))  # 0, 1, '马', red
        self.chess_piece_list.append(ChessPieceElephant(9, 2, 3, 1))  # 0, 2, '象', red
        self.chess_piece_list.append(ChessPieceBoyguard(9, 3, 4, 1))  # 0, 3, '士', red
        self.chess_piece_list.append(ChessPiecePrince(9, 4, 5, 1))  # 0, 4, '将'  red
        self.chess_piece_list.append(ChessPieceBoyguard(9, 5, 4, 1))  # 0, 5, '士', red
        self.chess_piece_list.append(ChessPieceElephant(9, 6, 3, 1))  # 0, 6, '象', red
        self.chess_piece_list.append(ChessPieceHorse(9, 7, 1, 1))  # 0, 7, '马', red
        self.chess_piece_list.append(ChessPieceVehicle(9, 8, 0, 1))  # 0, 8, '车', red
        self.chess_piece_list.append(ChessPieceCannon(7, 1, 2, 1))  # 2, 1, '炮', red
        self.chess_piece_list.append(ChessPieceCannon(7, 7, 2, 1))  # 2, 7, '炮', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 0, 6, 1))  # 3, 0, '兵', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 2, 6, 1))  # 3, 2, '兵', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 4, 6, 1))  # 3, 4, '兵', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 6, 6, 1))  # 3, 6, '兵', red
        self.chess_piece_list.append(ChessPieceSoldier(6, 8, 6, 1))  # 3, 6, '兵', red
        return self.chess_piece_list

    def set_chess_board(self, chess_board):
        self.chess_board = chess_board