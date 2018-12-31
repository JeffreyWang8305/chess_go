
# -*- coding: UTF-8 -*-

from Tkinter import *

current_x = 0
current_y = 0
canvas_width = 920
canvas_height = 1020
cell_margin = 100
padding_outsize = 55
draw_chess_board = 60

class ChassBoard():
    master = Tk()
    bg_canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="yellow")

    def get_master(self):
        return self.master

    def init_window(self):
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        size = '%dx%d+%d+%d' % (
        canvas_width, canvas_height, (screenwidth - canvas_width) / 2, (screenheight - canvas_height) / 2)
        self.master.geometry(size)
        # 设置主窗口对象的*标题
        self.master.title("中国象棋AI")

        self.bg_canvas.pack()

        self.draw_chess_board()

        self.draw_chess_pieces()

        # w.create_line(0, 0, 200, 100)
        # w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        # w.create_rectangle(50, 25, 150, 75, fill="blue")

    def draw_chess_pieces(self):
        self.bg_canvas.create_oval(0, 0, 60, 60)

    def draw_chess_board(self):
        self.bg_canvas.create_rectangle(padding_outsize, padding_outsize, canvas_width - padding_outsize,
                                        canvas_height - padding_outsize, width=3)
        self.bg_canvas.create_rectangle(draw_chess_board, draw_chess_board, canvas_width - draw_chess_board,
                                        canvas_height - draw_chess_board, width=2)
        pos_y = 0 + draw_chess_board
        for _ in range(9):
            self.bg_canvas.create_line(draw_chess_board, pos_y, canvas_width - draw_chess_board, pos_y)
            pos_y += cell_margin
        pos_x = 0 + draw_chess_board
        for _ in range(9):
            self.bg_canvas.create_line(pos_x, draw_chess_board, pos_x, draw_chess_board + cell_margin * 4)
            pos_x += cell_margin
        pos_x = 0 + draw_chess_board
        for _ in range(9):
            self.bg_canvas.create_line(pos_x, draw_chess_board + cell_margin * 5, pos_x,
                                       draw_chess_board + cell_margin * 9)
            pos_x += cell_margin
        self.bg_canvas.create_line(draw_chess_board + cell_margin * 3, draw_chess_board,
                                   draw_chess_board + cell_margin * 5, draw_chess_board + cell_margin * 2, dash=(4, 4))
        self.bg_canvas.create_line(draw_chess_board + cell_margin * 5, draw_chess_board,
                                   draw_chess_board + cell_margin * 3, draw_chess_board + cell_margin * 2, dash=(4, 4))
        self.bg_canvas.create_line(draw_chess_board + cell_margin * 3, draw_chess_board + cell_margin * 7,
                                   draw_chess_board + cell_margin * 5, draw_chess_board + cell_margin * 9, dash=(4, 4))
        self.bg_canvas.create_line(draw_chess_board + cell_margin * 5, draw_chess_board + cell_margin * 7,
                                   draw_chess_board + cell_margin * 3, draw_chess_board + cell_margin * 9, dash=(4, 4))
        # ft = Font(family="Helvetica", size=36, weight="bold")
        self.bg_canvas.create_text(draw_chess_board + cell_margin * 1.5, draw_chess_board + cell_margin * 4.5,
                                   text='楚河', font="time 30 bold")
        self.bg_canvas.create_text(draw_chess_board + cell_margin * 6.5, draw_chess_board + cell_margin * 4.5,
                                   text='汉界', font="time 30 bold")

    def get_screen_size(window):
        return window.winfo_screenwidth(), window.winfo_screenheight()

    def get_window_size(window):
        return window.winfo_reqwidth(), window.winfo_reqheight()


