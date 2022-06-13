from random import randrange
import tkinter as tk
import tkinter.ttk as ttk
import os

# Variables
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'resources')
tank_enemy_x = (randrange(0, 5))
tank_enemy_y = (randrange(0, 5))
tank_player_x = (randrange(0, 5))
tank_player_y = (randrange(0, 5))
grid_buttons = []


class TankTkinterApp:
    def __init__(self, master=None):
        # build ui
        self.main = ttk.Frame(master)
        self.up = ttk.Button(self.main, text="Up")
        self.up.grid(column=1, pady="3", row=1)
        self.left = ttk.Button(self.main, text="Left")
        self.left.grid(column=0, row=2, sticky='e')
        self.fire = ttk.Button(self.main, text="Fire")
        self.fire.grid(column=1, pady="3", row=2)
        self.right = ttk.Button(self.main, text="Right")
        self.right.grid(column=2, row=2, sticky='w')
        self.down = ttk.Button(self.main, text="Down")
        self.down.grid(column=1, pady="3", row=3)
        self.turn_l = ttk.Button(self.main, text="Turn L")
        self.turn_l.grid(column=0, row=1, sticky="e")
        self.turn_r = ttk.Button(self.main, text="Turn R")
        self.turn_r.grid(column=2, row=1, sticky="w")
        self.reset = ttk.Button(self.main, text="Reset")
        self.reset.grid(column=0, row=4, sticky="e")
        self.exit = ttk.Button(self.main, text="Exit")
        self.exit.grid(column=2, row=4, sticky="w")
        self.label_frame = ttk.Labelframe(self.main)
        self.shmup_frame = ttk.Frame(self.label_frame)

        # grid buttons
        self.img_bg = tk.PhotoImage(file=os.path.join(img_folder, 'dirt.png'))
        self.img_enemy = tk.PhotoImage(file=os.path.join(img_folder, 'tankEnemy.png'))
        self.img_player = tk.PhotoImage(file=os.path.join(img_folder, 'tankBase.png'))

        for index in range(0, 25):
            self.button = ttk.Button(self.shmup_frame, image=self.img_bg)
            grid_buttons.append(self.button)

        i = 0
        for row_x in (range(0, 5)):
            for col_y in (range(0, 5)):
                grid_buttons[i].grid(row=row_x, column=col_y)
                i += 1
        
        # Units
        self.button_player = ttk.Button(self.shmup_frame, image=self.img_player)
        self.button_player.grid(column=tank_player_x, row=tank_player_y)
        self.button_enemy = ttk.Button(self.shmup_frame, image=self.img_enemy)
        self.button_enemy.grid(column=tank_enemy_x, row=tank_enemy_y)

        self.shmup_frame.configure(height="200", width="200")
        self.shmup_frame.grid(column=0, row=0)
        self.label_frame.configure(height="200", text="Tank Shmup", width="200")
        self.label_frame.grid(column=0, columnspan=3, row=0)
        self.main.configure(height="200", width="200")
        self.main.pack(side="top")
        self.main.grid_anchor("n")

        # Main widget
        self.main_window = self.main

    def run(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = TankTkinterApp(root)
    app.run()
