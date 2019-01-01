#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 9:12 AM
# @Author  : 王金波
# @File    : main.py

from gui.chass_board import ChassBoard
from manager.chess_manager import ChessManager


def main():
  print('hello world!')
  chess_manager = ChessManager()
  chass_board = ChassBoard(chess_manager)
  master = chass_board.get_master()
  chass_board.init_window()

  master.mainloop()

if __name__ == '__main__':
  main()