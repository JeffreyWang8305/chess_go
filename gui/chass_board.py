#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/1/2019 11:42 AM
# @Author  : 王金波
# @File    : chess_board.py

from Tkinter import *
from manager.util import *

canvas_width = 920
canvas_height = 1020
cell_margin = 100
padding_outsize = 55
padding_inside = 60

padding_bottom = 60
padding_internal = 41

class ChassBoard:

    def __init__(self, chess_manager):
        self.master = Tk()

        self.master.maxsize(canvas_width, canvas_height + padding_bottom)
        self.master.minsize(canvas_width, canvas_height + padding_bottom)

        self.chess_board = Label(self.master)
        self.chess_board.pack()
        self.bg_canvas = Canvas(self.chess_board, width=canvas_width, height=canvas_height, bg="white")
        self.bg_canvas.bind("<Button-1>", self.chess_board_onclick)

        self.start_btn = Button(self.master, text="Reset", command=self.perform_reset)
        self.start_btn.pack(side=LEFT, padx=10)

        self.start_btn = Button(self.master, text="AutoRun", command=self.auto_run)
        self.start_btn.pack(side=LEFT, padx=10)

        self.start_btn = Button(self.master, text="GoNext", command=self.go_next)
        self.start_btn.pack(side=LEFT, padx=10)

        self.chess_board.pack()

        self.chess_manager = chess_manager

        self.predict_pos = (-1, -1)

    def perform_reset(self):
        self.clear_chess_board()
        chess_piece_list = self.chess_manager.reset_data()

        for chess_piece in chess_piece_list:
            row, col, name, type = chess_piece.get_info()
            self.draw_chess_pieces(row, col, name, type)

    def auto_run(self):
        self.chess_manager.auto_run()

    '''
        desc: 将选中的棋子进行随机的移动；需要根据棋子的类型来确定其移动范围
    '''
    def predict_next(self):
        next_pos_list = self.chess_manager.predict()
        # 画出来predict的可走的下一步的全部路线：
        if OPEN_ANIMATION:
            if next_pos_list and next_pos_list[0]:
                for (row, col) in next_pos_list:
                    self.draw_predicted_piece_border(row, col)

        row, col = self.chess_manager.random_run(next_pos_list)
        self.predict_pos = (row, col)
        return row, col

    def clear_and_re_draw(self):
        self.clear_chess_board()
        for chess_piece in self.chess_manager.get_chess_pieses():
            row, col, name, type = chess_piece.get_info()
            self.draw_chess_pieces(row, col, name, type)

    def chess_board_onclick(self, events):
        # print(events.x, events.y)
        clicked_row, clicked_col = self.xy_convert_to_row_col(events.x, events.y)
        print('clicked on: ', clicked_row, clicked_col)
        selected_chess_piece = None
        if self.chess_manager.get_chess_pieses():
            for chess_piece in self.chess_manager.get_chess_pieses():
                if chess_piece:
                    row, col, _name, _type = chess_piece.get_info()
                    x0, x1, y0, y1 = self.row_col_convert_to_xy(col, row)
                    if x0 <= events.x <= x1 and y0 <= events.y <= y1:
                        selected_chess_piece = chess_piece
                        break
            print('selected row:', row, 'column:', col)
            self.select_and_predict(selected_chess_piece)

    def select_and_predict(self, selected_chess_piece):
        if selected_chess_piece:

            self.chess_manager.set_selected_chess_piece(selected_chess_piece)
            row, col, _name, _type = selected_chess_piece.get_info()
            if OPEN_ANIMATION:
                self.clear_and_re_draw()
                self.draw_selected_piece_border(row, col)
                self.master.update_idletasks()
            self.predict_next()


    def go_next(self):
        # print("perform_next")
        (row, col) = self.predict_pos
        # print('go_next', row, col)
        is_game_over, success_type = self.chess_manager.go_next(row, col)
        if OPEN_ANIMATION:
            self.clear_and_re_draw()
            self.master.update_idletasks()
        return is_game_over, success_type

    def get_master(self):
        return self.master

    def init_window(self):
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        size = '%dx%d+%d+%d' % (
        canvas_width, canvas_height + padding_bottom, (screenwidth - canvas_width) / 2, (screenheight - canvas_height - padding_bottom) / 2)
        self.master.geometry(size)
        # 设置主窗口对象的*标题
        self.master.title("中国象棋AI")

        self.bg_canvas.pack()

        self.draw_chess_board()

    def clear_chess_board(self):
        self.bg_canvas.delete("all")
        self.draw_chess_board()

    def draw_chess_pieces(self, row, col, txt, type):
        x0, x1, y0, y1 = self.row_col_convert_to_xy(col, row)

        text_color = 'black'
        fill_color = '#FFA000'
        internal_outline_color = '#666666'
        if type == 1:
            text_color = 'red'
            fill_color = '#FF7000'
            internal_outline_color = '#333333'
        self.bg_canvas.create_oval(x0, y0, x1, y1, fill=fill_color, outline=fill_color)
        self.bg_canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill=fill_color, outline=internal_outline_color) # internal circle

        self.bg_canvas.create_text(x0 + padding_internal, y0 + padding_internal, text = txt, fill=text_color, font="time 35 bold")

    def row_col_convert_to_xy(self, col, row):
        x0 = padding_inside + 10 - cell_margin / 2 + cell_margin * col
        y0 = padding_inside + 10 - cell_margin / 2 + cell_margin * row
        x1 = padding_inside - 10 - cell_margin / 2 + cell_margin * (col + 1)
        y1 = padding_inside - 10 - cell_margin / 2 + cell_margin * (row + 1)
        return x0, x1, y0, y1

    def xy_convert_to_row_col(self, x, y):
        converted_x = x - padding_inside
        converted_y = y - padding_inside
        col = (converted_x + cell_margin/2)/cell_margin
        row = (converted_y + cell_margin/2)/cell_margin
        return row, col

    def draw_predicted_piece_border(self, row, col):
        x_start = padding_inside - cell_margin / 2 + col * cell_margin
        x_end = x_start + 100
        y_start = padding_inside - cell_margin / 2 + row * cell_margin
        y_end = y_start + 100
        length = 30
        shift = 10
        x_start = x_start + shift
        x_end = x_end - shift
        y_start = y_start + shift
        y_end = y_end - shift
        self.bg_canvas.create_line(x_start , y_start, x_start + length, y_start, fill="red", width=1, dash=(5, 5))
        self.bg_canvas.create_line(x_end - length, y_start, x_end, y_start, fill="red", width=1, dash=(5, 5))
        self.bg_canvas.create_line(x_start, y_end, x_start + length, y_end, fill="red", width=1, dash=(5, 5))
        self.bg_canvas.create_line(x_end - length, y_end, x_end, y_end, fill="red", width=1, dash=(5, 5))

        self.bg_canvas.create_line(x_start, y_start, x_start, y_start + length, fill="red", width=1, dash=(5, 5))
        self.bg_canvas.create_line(x_start, y_end - length, x_start, y_end, fill="red", width=1, dash=(5, 5))
        self.bg_canvas.create_line(x_end, y_start, x_end, y_start + length, fill="red", width=1, dash=(5, 5))
        self.bg_canvas.create_line(x_end, y_end - length, x_end, y_end, fill="red", width=1, dash=(5, 5))

    def draw_selected_piece_border(self, row, col):
        x_start = padding_inside - cell_margin/2 + col * cell_margin
        x_end = x_start + 100
        y_start = padding_inside - cell_margin/2 + row * cell_margin
        y_end = y_start + 100
        length = 20
        self.bg_canvas.create_line(x_start, y_start, x_start + length, y_start, fill="red", width=3)
        self.bg_canvas.create_line(x_end - length, y_start, x_end, y_start, fill="red", width=3)
        self.bg_canvas.create_line(x_start, y_end, x_start + length, y_end, fill="red", width=3)
        self.bg_canvas.create_line(x_end - length, y_end, x_end, y_end, fill="red", width=3)

        self.bg_canvas.create_line(x_start, y_start, x_start, y_start + length, fill="red", width=3)
        self.bg_canvas.create_line(x_start, y_end - length, x_start, y_end, fill="red", width=3)
        self.bg_canvas.create_line(x_end, y_start, x_end, y_start + length, fill="red", width=3)
        self.bg_canvas.create_line(x_end, y_end - length, x_end, y_end, fill="red", width=3)

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

