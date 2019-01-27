#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 3:28 AM
# @Author  : 王金波
# @File    : util.py

# chess_total_cnt:
chess_total_cnt = 32
max_row = 9
max_col = 8

TYPE_MYOWN_SIDE = 1  # 己方
TYPE_ENEMY_SIDE = 0  # 對方
TYPE_VACANCY = -1    # 空白

OPEN_ANIMATION = False
EPOCH = 400
ONE_EPOCH_TIME = 0.01
PREDICT_TIME = 0.01

def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value

def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value