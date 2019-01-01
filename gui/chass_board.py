
# -*- coding: UTF-8 -*-

from Tkinter import *

canvas_width = 920
canvas_height = 1020
cell_margin = 100
padding_outsize = 55
padding_inside = 60

class ChassBoard():

    def __init__(self):
        self.master = Tk()
        self.bg_canvas = Canvas(self.master, width=canvas_width, height=canvas_height, bg="white")

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

        # w.create_line(0, 0, 200, 100)
        # w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        # w.create_rectangle(50, 25, 150, 75, fill="blue")

    def draw_chess_pieces(self, row, col, txt, type):
        x0 = padding_inside + 10 - cell_margin/2 + cell_margin * col
        y0 = padding_inside + 10 - cell_margin/2 + cell_margin * row
        x1 = padding_inside - 10 - cell_margin/2 + cell_margin * (col + 1)
        y1 = padding_inside - 10 - cell_margin/2 + cell_margin * (row + 1)

        text_color = 'black'
        fill_color = '#FFA000'
        internal_outline_color = '#666666'
        if type == 1:
            text_color = 'red'
            fill_color = '#FF7000'
            internal_outline_color = '#333333'
        self.bg_canvas.create_oval(x0, y0, x1, y1, fill=fill_color, outline=fill_color)
        self.bg_canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill=fill_color, outline=internal_outline_color) # internal circle

        padding_internal = 41
        self.bg_canvas.create_text(x0 + padding_internal, y0 + padding_internal, text = txt, fill=text_color, font="time 35 bold")

    def draw_chess_board(self):

        # the outer lines:
        self.bg_canvas.create_rectangle(padding_outsize, padding_outsize, canvas_width - padding_outsize,
                                        canvas_height - padding_outsize, width=3)
        self.bg_canvas.create_rectangle(padding_inside, padding_inside, canvas_width - padding_inside,
                                        canvas_height - padding_inside, width=2)

        # horizontal lines:
        pos_y = 0 + padding_inside
        for _ in range(9):
            self.bg_canvas.create_line(padding_inside, pos_y, canvas_width - padding_inside, pos_y)
            pos_y += cell_margin
        pos_x = 0 + padding_inside
        # vertical lines which break at '楚河' and '汉界'
        for _ in range(9):
            self.bg_canvas.create_line(pos_x, padding_inside, pos_x, padding_inside + cell_margin * 4)
            pos_x += cell_margin
        pos_x = 0 + padding_inside
        for _ in range(9):
            self.bg_canvas.create_line(pos_x, padding_inside + cell_margin * 5, pos_x,
                                       padding_inside + cell_margin * 9)
            pos_x += cell_margin
        self.bg_canvas.create_line(padding_inside + cell_margin * 3, padding_inside,
                                   padding_inside + cell_margin * 5, padding_inside + cell_margin * 2, dash=(4, 4))
        self.bg_canvas.create_line(padding_inside + cell_margin * 5, padding_inside,
                                   padding_inside + cell_margin * 3, padding_inside + cell_margin * 2, dash=(4, 4))
        self.bg_canvas.create_line(padding_inside + cell_margin * 3, padding_inside + cell_margin * 7,
                                   padding_inside + cell_margin * 5, padding_inside + cell_margin * 9, dash=(4, 4))
        self.bg_canvas.create_line(padding_inside + cell_margin * 5, padding_inside + cell_margin * 7,
                                   padding_inside + cell_margin * 3, padding_inside + cell_margin * 9, dash=(4, 4))

        # Text such as '楚河' and '汉界'
        self.bg_canvas.create_text(padding_inside + cell_margin * 1.5, padding_inside + cell_margin * 4.5,
                                   text='楚 河', font="隶书 40 bold")
        self.bg_canvas.create_text(padding_inside + cell_margin * 6.5, padding_inside + cell_margin * 4.5,
                                   text='汉 界', font="隶书 40 bold")

        # lable under '炮' and '兵'
        self.cannon_label(2, 1)
        self.cannon_label(2, 7)
        self.cannon_label(7, 1)
        self.cannon_label(7, 7)

        self.cannon_label(3, 2)
        self.cannon_label(3, 4)
        self.cannon_label(3, 6)

        self.cannon_label(6, 2)
        self.cannon_label(6, 4)
        self.cannon_label(6, 6)

        self.soldier_label(3, 0, True)
        self.soldier_label(6, 0, True)

        self.soldier_label(3, 8, False)
        self.soldier_label(6, 8, False)

    def cannon_label(self, row, col):
        # vertical lines:
        self.bg_canvas.create_line(padding_inside - 5 + cell_margin * col,
                                   padding_inside - 5 + cell_margin * row - 20,
                                   padding_inside - 5 + cell_margin * col,
                                   padding_inside - 5 + cell_margin * row)
        self.bg_canvas.create_line(padding_inside + 5 + cell_margin * col,
                                   padding_inside - 5 + cell_margin * row - 20,
                                   padding_inside + 5 + cell_margin * col,
                                   padding_inside - 5 + cell_margin * row)
        self.bg_canvas.create_line(padding_inside + 5 + cell_margin * col,
                                   padding_inside + 5 + cell_margin * row + 20,
                                   padding_inside + 5 + cell_margin * col,
                                   padding_inside + 5 + cell_margin * row)
        self.bg_canvas.create_line(padding_inside - 5 + cell_margin * col,
                                   padding_inside + 5 + cell_margin * row + 20,
                                   padding_inside - 5 + cell_margin * col,
                                   padding_inside + 5 + cell_margin * row)
        # horizontal lines:
        self.bg_canvas.create_line(padding_inside - 5 + cell_margin * col - 20,
                                   padding_inside - 5 + cell_margin * row,
                                   padding_inside - 5 + cell_margin * col,
                                   padding_inside - 5 + cell_margin * row)
        self.bg_canvas.create_line(padding_inside - 5 + cell_margin * col - 20,
                                   padding_inside + 5 + cell_margin * row,
                                   padding_inside - 5 + cell_margin * col,
                                   padding_inside + 5 + cell_margin * row)
        self.bg_canvas.create_line(padding_inside + 5 + cell_margin * col + 20,
                                   padding_inside - 5 + cell_margin * row,
                                   padding_inside + 5 + cell_margin * col,
                                   padding_inside - 5 + cell_margin * row)
        self.bg_canvas.create_line(padding_inside + 5 + cell_margin * col + 20,
                                   padding_inside + 5 + cell_margin * row,
                                   padding_inside + 5 + cell_margin * col,
                                   padding_inside + 5 + cell_margin * row)

    def soldier_label(self, row, col, is_left):
        if is_left:
            self.bg_canvas.create_line(padding_inside + 5 + cell_margin * col,
                                       padding_inside - 5 + cell_margin * row - 20,
                                       padding_inside + 5 + cell_margin * col,
                                       padding_inside - 5 + cell_margin * row)
            self.bg_canvas.create_line(padding_inside + 5 + cell_margin * col,
                                       padding_inside + 5 + cell_margin * row + 20,
                                       padding_inside + 5 + cell_margin * col,
                                       padding_inside + 5 + cell_margin * row)

            self.bg_canvas.create_line(padding_inside + 5 + cell_margin * col + 20,
                                       padding_inside - 5 + cell_margin * row,
                                       padding_inside + 5 + cell_margin * col,
                                       padding_inside - 5 + cell_margin * row)
            self.bg_canvas.create_line(padding_inside + 5 + cell_margin * col + 20,
                                       padding_inside + 5 + cell_margin * row,
                                       padding_inside + 5 + cell_margin * col,
                                       padding_inside + 5 + cell_margin * row)
        else:
            # vertical lines:
            self.bg_canvas.create_line(padding_inside - 5 + cell_margin * col,
                                       padding_inside - 5 + cell_margin * row - 20,
                                       padding_inside - 5 + cell_margin * col,
                                       padding_inside - 5 + cell_margin * row)

            self.bg_canvas.create_line(padding_inside - 5 + cell_margin * col,
                                       padding_inside + 5 + cell_margin * row + 20,
                                       padding_inside - 5 + cell_margin * col,
                                       padding_inside + 5 + cell_margin * row)
            # horizontal lines:
            self.bg_canvas.create_line(padding_inside - 5 + cell_margin * col - 20,
                                       padding_inside - 5 + cell_margin * row,
                                       padding_inside - 5 + cell_margin * col,
                                       padding_inside - 5 + cell_margin * row)
            self.bg_canvas.create_line(padding_inside - 5 + cell_margin * col - 20,
                                       padding_inside + 5 + cell_margin * row,
                                       padding_inside - 5 + cell_margin * col,
                                       padding_inside + 5 + cell_margin * row)


    def get_screen_size(window):
        return window.winfo_screenwidth(), window.winfo_screenheight()

    def get_window_size(window):
        return window.winfo_reqwidth(), window.winfo_reqheight()

