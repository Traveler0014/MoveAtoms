from tkinter import Frame, Label, CENTER
import logic


class GameGrid(Frame):
    def __init__(self):
        super().__init__()

        self.grid()
        self.master.title('MoveAtoms')
        self.master.bind('<Key>', self.key_down)

        self.commands = {

        }

        self.grid = []
        self.init_grid()
        