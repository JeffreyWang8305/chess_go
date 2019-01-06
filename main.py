#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 9:12 AM
# @Author  : 王金波
# @File    : main.py

from gui.chass_board import ChassBoard
from manager.chess_manager import ChessManager


def main():
  chess_manager = ChessManager()
  chass_board = ChassBoard(chess_manager)
  chess_manager.set_chess_board(chass_board)
  master = chass_board.get_master()
  chass_board.init_window()
  chass_board.perform_reset()
  master.mainloop()

if __name__ == '__main__':
  main()