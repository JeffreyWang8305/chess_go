#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
from gui.chass_board import ChassBoard
from chess_manager.chess_piece import ChassPiece
from chess_manager.util import *
from chess_manager.chess_operation import ChessOperation



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

  chess_operation = ChessOperation()
  chess_piece_list = chess_operation.reset()

  print(len(chess_piece_list))
  for chess_piece in chess_piece_list:
    row, col, name, type = chess_piece.get_info()
    chass_board.draw_chess_pieces(row, col, name, type)



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