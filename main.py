#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
from gui.chass_board import ChassBoard
from operation.chess_piece import ChassPiece
from operation.util import *



#
# master = Tk()
# screenwidth = master.winfo_screenwidth()
# screenheight = master.winfo_screenheight()
# size = '%dx%d+%d+%d' % (canvas_width, canvas_height, (screenwidth - canvas_width)/2, (screenheight - canvas_height)/2)
# master.geometry(size)
# # 设置主窗口对象的*标题
# master.title("中国象棋AI")
# w = Canvas(master, width=canvas_width, height=canvas_height, bg="yellow")
# w.pack()
# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
# w.create_rectangle(50, 25, 150, 75, fill="blue")

# fm1 = Frame(root, width=canvas_width, height=canvas_height, bg="yellow")

# bg_label = Label(fm1)
# theLabel = Label(master, text="兵")
def b1_motion_callback(event):
  current_x = event.x
  current_y = event.y
  theLabel.place(x=current_x, y=current_y, anchor='nw')
  print "clicked at", event.x, event.y

def main():
  print('hello world!')

  chass_board = ChassBoard()
  master = chass_board.get_master()
  chass_board.init_window()

  chess_piece_list = []
  for i in range(chess_total_cnt):
      chess_piece = ChassPiece(vehicle, 1, 0, 0)
      chess_piece_list.append(chess_piece)

  chass_board.draw_chess_pieces(0, 0, '车', False)
  chass_board.draw_chess_pieces(0, 1, '马', False)
  chass_board.draw_chess_pieces(0, 2, '象', False)
  chass_board.draw_chess_pieces(0, 3, '士', False)
  chass_board.draw_chess_pieces(0, 4, '将', False)
  chass_board.draw_chess_pieces(0, 5, '士', False)
  chass_board.draw_chess_pieces(0, 6, '象', False)
  chass_board.draw_chess_pieces(0, 7, '马', False)
  chass_board.draw_chess_pieces(0, 8, '车', False)
  chass_board.draw_chess_pieces(2, 1, '炮', False)
  chass_board.draw_chess_pieces(2, 7, '炮', False)
  chass_board.draw_chess_pieces(3, 0, '兵', False)
  chass_board.draw_chess_pieces(3, 2, '兵', False)
  chass_board.draw_chess_pieces(3, 4, '兵', False)
  chass_board.draw_chess_pieces(3, 6, '兵', False)
  chass_board.draw_chess_pieces(3, 8, '兵', False)

  chass_board.draw_chess_pieces(9, 0, '车', True)
  chass_board.draw_chess_pieces(9, 1, '马', True)
  chass_board.draw_chess_pieces(9, 2, '象', True)
  chass_board.draw_chess_pieces(9, 3, '士', True)
  chass_board.draw_chess_pieces(9, 4, '将', True)
  chass_board.draw_chess_pieces(9, 5, '士', True)
  chass_board.draw_chess_pieces(9, 6, '象', True)
  chass_board.draw_chess_pieces(9, 7, '马', True)
  chass_board.draw_chess_pieces(9, 8, '车', True)
  chass_board.draw_chess_pieces(9 - 2, 1, '炮', True)
  chass_board.draw_chess_pieces(9 - 2, 7, '炮', True)
  chass_board.draw_chess_pieces(9 - 3, 0, '兵', True)
  chass_board.draw_chess_pieces(9 - 3, 2, '兵', True)
  chass_board.draw_chess_pieces(9 - 3, 4, '兵', True)
  chass_board.draw_chess_pieces(9 - 3, 6, '兵', True)
  chass_board.draw_chess_pieces(9 - 3, 8, '兵', True)


  # 创建一个主窗口，用于容纳整个GUI程序

  # 添加一个Label组件，Label组件是GUI程序中最常用的组件之一
  # Label组件可以显示文本、图标或者图片
  # 在这里我们让他们显示指定文本

  # bg_label_canvas = Canvas(bg_label, bg="yellow", width=canvas_width, height=canvas_height)
  # bg_label_canvas.pack()

  # y = int(canvas_height / 2)
  # padding = 10
  # w.create_line(0 + padding, 0 + padding, 0 + padding, canvas_width - padding, fill="#476042")
  # w.create_line(0 + padding, 0 + padding, canvas_height - padding, 0 + padding, fill="#476042")



  # theLabel.bind("<B1-Motion>", b1_motion_callback)

  # 然后调用Label组建的pack()方法，用于自动调节组件自身的尺寸
  # fm1.pack()
  # theLabel.pack()
  # bg_label.pack()

  # li = ['C', 'python', 'php', 'html', 'SQL', 'java']
  # movie = ['CSS', 'jQuery', 'Bootstrap']
  # listb = tk.Listbox(root)  # 创建两个列表组件
  # listb2 = tk.Listbox(root)
  # for item in li:  # 第一个小部件插入数据
  #   listb.insert(0, item)
  #
  # for item in movie:  # 第二个小部件插入数据
  #   listb2.insert(0, item)
  #
  # listb.pack()  # 将小部件放置到主窗口中
  # listb2.pack()

  # 注意，这时候窗口还是不会显示的...
  # 除非执行下面的这条代码！！！！！

  master.mainloop()

if __name__ == '__main__':
  main()