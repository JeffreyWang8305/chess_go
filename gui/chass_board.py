
# -*- coding: UTF-8 -*-

from Tkinter import *

current_x = 0
current_y = 0
canvas_width = 920
canvas_height = 1020
cell_margin = 100
padding_outsize = 55
padding_inside = 60

class ChassBoard():
    master = Tk()
    bg_canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="white")

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

        self.draw_chess_pieces(8, 9, '兵', True)
        self.draw_chess_pieces(3, 4, '车', False)

        # w.create_line(0, 0, 200, 100)
        # w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        # w.create_rectangle(50, 25, 150, 75, fill="blue")

    def draw_chess_pieces(self, row, col, txt, is_red):
        x0 = padding_inside + 10 - cell_margin/2 + cell_margin * row
        y0 = padding_inside + 10 - cell_margin/2 + cell_margin * col
        x1 = padding_inside - 10 - cell_margin/2 + cell_margin * (row + 1)
        y1 = padding_inside - 10 - cell_margin/2 + cell_margin * (col + 1)

        text_color = 'black'
        fill_color = '#FFA000'
        internal_outline_color = '#666666'
        if is_red:
            text_color = 'red'
            fill_color = '#FF7000'
            internal_outline_color = '#333333'
        self.bg_canvas.create_oval(x0, y0, x1, y1, fill=fill_color, outline=fill_color)
        self.bg_canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill=fill_color, outline=internal_outline_color) # internal circle

        padding_internal = 41
        self.bg_canvas.create_text(x0 + padding_internal, y0 + padding_internal, text = txt, fill=text_color, font="time 35 bold")

    def draw_chess_board(self):
        self.bg_canvas.create_rectangle(padding_outsize, padding_outsize, canvas_width - padding_outsize,
                                        canvas_height - padding_outsize, width=3)
        self.bg_canvas.create_rectangle(padding_inside, padding_inside, canvas_width - padding_inside,
                                        canvas_height - padding_inside, width=2)
        pos_y = 0 + padding_inside
        for _ in range(9):
            self.bg_canvas.create_line(padding_inside, pos_y, canvas_width - padding_inside, pos_y)
            pos_y += cell_margin
        pos_x = 0 + padding_inside
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
        # ft = Font(family="Helvetica", size=36, weight="bold")
        self.bg_canvas.create_text(padding_inside + cell_margin * 1.5, padding_inside + cell_margin * 4.5,
                                   text='楚河', font="time 30 bold")
        self.bg_canvas.create_text(padding_inside + cell_margin * 6.5, padding_inside + cell_margin * 4.5,
                                   text='汉界', font="time 30 bold")

    def get_screen_size(window):
        return window.winfo_screenwidth(), window.winfo_screenheight()

    def get_window_size(window):
        return window.winfo_reqwidth(), window.winfo_reqheight()


