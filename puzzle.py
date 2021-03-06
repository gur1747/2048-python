from tkinter import *
from logic import *
from random import *

SIZE = 500
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e",4096:"#f2b179" }
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2",4096:"#f9f6f2" }
FONT = ("Verdana", 40, "bold")

KEY_UP_ALT = "\'\\uf700\'"
KEY_DOWN_ALT = "\'\\uf701\'"
KEY_LEFT_ALT = "\'\\uf702\'"
KEY_RIGHT_ALT = "\'\\uf703\'"

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"

class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        #self.gamelogic = gamelogic
        self.commands = {   KEY_UP: up, KEY_DOWN: down, KEY_LEFT: left, KEY_RIGHT: right,
                            KEY_UP_ALT: up, KEY_DOWN_ALT: down, KEY_LEFT_ALT: left, KEY_RIGHT_ALT: right }

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        background.grid()
        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE/GRID_LEN, height=SIZE/GRID_LEN)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                # font = Font(size=FONT_SIZE, family=FONT_FAMILY, weight=FONT_WEIGHT)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def gen(self):
        return randint(0, GRID_LEN - 1)

    def init_matrix(self):
        self.matrix = new_game(GRID_LEN)

        self.matrix=add_two(self.matrix)
        self.matrix=add_two(self.matrix)

    def update_grid_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_DICT[new_number], fg=CELL_COLOR_DICT[new_number])
        self.update_idletasks()
        
    def tryAgain(self):
        print("try again")
        self.destroy()
        self.__init__()
        
    def game_ending(self):
        self.master.destroy()
        exit()
        print("end")

    def gomenu(self):
        print("gomenu")
        self.destroy()
        
    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix,done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = add_two(self.matrix)
                self.update_grid_cells()
                done=False
                a = GRID_LEN
                if game_state(self.matrix)=='win':
#<<<<<<< HEAD
                    self.grid_cells[a // 2 - 1][a // 2  - 1].configure(text="You",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[a // 2  - 1][a // 2 ].configure(text="Win!",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.game_end_window("Win")
                if game_state(self.matrix)=='lose':
                    self.grid_cells[a // 2  - 1][a // 2  - 1].configure(text="You",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[a // 2  - 1][a // 2 ].configure(text="Lose!",bg=BACKGROUND_COLOR_CELL_EMPTY)
#=======
                    self.game_end_window("Lose")

    def game_end_window(self, state):
        global window
        window= Tk()
        window.title("Game End")
        frame=Frame(window)
        frame.pack()
        endLabel=Label(frame, text="You "+state +"!" , font="Verdana").pack()
        tryAgainB=Button(frame, text="Try Again",width=30, command=self.tryAgain).pack()
        exitB=Button(frame, text="Exit", width=30, command=self.game_ending).pack()
#>>>>>>> 063cf65b15c8ea62f74989fa297c15f1f2c748c0


    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2

#<<<<<<< HEAD
def StartMenu():
    Label(Menu, text="2048",bg="#edc22e",fg="white",font="Verdana 40 bold italic").pack()
    Button(Menu, text="Start",bg="#f67c5f",fg="white",font="Verdana 40 bold italic",command=Start).pack()
    Button(Menu, text="Help",bg="#edcf72",fg="white",font="Verdana 40 bold italic",command=Help).pack()
    Button(Menu, text="Exit",bg="#edc53f",fg="white",font="Verdana 40 bold italic",command=Menu.destroy).pack()
    Menu.mainloop()

def Start():
    cl = Close()
    gamegrid = GameGrid()
    
def Help():
    P_Help = Tk()
    Label(P_Help, text="How To Play?\nw : move up\na : move left\ns : move down\nd : move right",bg="black",fg="white",font="Verdana 40 bold italic").pack()
    Button(P_Help, text="Exit",bg="gray",fg="white",font="Verdana 40 bold italic",command=P_Help.destroy).pack()

def Close():
    Menu.destroy()

Menu = Tk()
game = StartMenu()
            
#=======
#gamegrid = GameGrid()
##test
#>>>>>>> 063cf65b15c8ea62f74989fa297c15f1f2c748c0
