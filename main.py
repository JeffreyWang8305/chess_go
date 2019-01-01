#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 9:12 AM
# @Author  : 王金波
# @File    : main.py

from Tkinter import *
from gui.chass_board import ChassBoard
from chess_manager.chess_piece import ChassPiece
from chess_manager.util import *
from chess_manager.chess_operation import ChessOperation


def b1_motion_callback(event):
  current_x = event.x
  current_y = event.y
  theLabel.place(x=current_x, y=current_y, anchor='nw')
  print "clicked at", event.x, event.y

def main():
  print('hello world!')

  chess_operation = ChessOperation()
  chass_board = ChassBoard(chess_operation)
  master = chass_board.get_master()
  chass_board.init_window()
  # chass_board.perform_reset()

  master.mainloop()

if __name__ == '__main__':
  main()