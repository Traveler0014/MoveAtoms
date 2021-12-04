from tkinter import Frame, Label, CENTER
from logic import Space
import constants as c
from functools import partial


class GameGrid(Frame, Space):
    def __init__(self):
        Frame.__init__(self)
        Space.__init__(self)

        self.grid()
        self.master.title('MoveAtoms')
        # self.master.bind('<ButtonRelease-1>', self.key_down)

        # self.space = Space()
        self.space = []

        self.commands = {
            '<ButtonRelease-1>': self.separate,
            '<ButtonRelease-3>': self.merge
        }
        self.draw_grid()
        self.master.mainloop()

    def draw_grid(self):
        for item in self.space:
            # print(item)
            item.destroy()
        HSIZE = (c.GRID_SIZE + c.GRID_PADDING) * self.length + c.GRID_PADDING
        VSIZE = c.GRID_SIZE + 2 * c.GRID_PADDING
        background = Frame(self,
                           bg=c.BACKGROUND_COLOR_GAME,
                           width=HSIZE,
                           height=VSIZE)
        background.grid()
        self.space.append(background)

        for i in range(self.length):
            amount = self.status[i]
            cell = Frame(background,
                         bg=c.BACKGROUND_COLOR_DICT[amount],
                         width=c.GRID_SIZE,
                         height=c.GRID_SIZE)

            # cell.bind('<Key>', self.key_down)
            # cell.bind('<ButtonRelease-1>', partial(self.separate, i=i))
            cell.grid(row=0,
                      column=i,
                      padx=c.GRID_PADDING,
                      pady=c.GRID_PADDING)
            t = Label(master=cell,
                      text=str(amount),
                      bg=c.BACKGROUND_COLOR_DICT[amount],
                      fg=c.CELL_COLOR_DICT[amount],
                      justify=CENTER,
                      font=c.FONT,
                      width=1,
                      height=1)
            for key, opt in self.commands.items():
                t.bind(key, partial(opt, i=i))
            # t.bind('<ButtonRelease-3>', self.key_down)
            t.grid()
            self.space.append(cell)

    def key_down(self, event):
        print(event)
        key = event.keysym
        if key == c.KEY_QUIT: exit()

    def separate(self, event, i):
        print(event)
        super().separate(i)
        self.draw_grid()
    
    def merge(self, event, i):
        print(event)
        super().merge(i)
        self.draw_grid()

# print(GameGrid.__mro__)
game_grid = GameGrid()