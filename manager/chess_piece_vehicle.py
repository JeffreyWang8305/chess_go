#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/2/2019 11:33 PM
# @Author  : 王金波
# @File    : chess_piece_vehicle.py

from chess_piece import *


class ChessPieceVehicle(ChessPiece):

    '''
        desc: 将当前棋子随机移动。（不同category棋子移动规律与范围不同）
    '''
    def get_next_position_list(self, chess_manager):
        next_pos_list = []
        return next_pos_list
