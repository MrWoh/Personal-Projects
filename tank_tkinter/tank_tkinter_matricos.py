from random import randrange
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from PIL import ImageTk, Image
import os

# Variables
tank_enemy_x, tank_enemy_y = 0, 0
tank_player_x, tank_player_y = 0, 0
player_axis = 360
enemy_axis = 0
grid_buttons = []

# Sprites
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'resources')
img_path_original = (os.path.join(img_folder, 'tank_main_t.png'))
img_player_original = Image.open(os.path.join(img_folder, 'tank_main.png'))
img_enemy_original = Image.open(os.path.join(img_folder, 'tank_enemy.png'))
img_player_copy = img_player_original.rotate(player_axis)
img_enemy_copy = img_enemy_original.rotate(player_axis)
img_player_copy.save(os.path.join(img_folder, 'tank_main_t.png'))
img_enemy_copy.save(os.path.join(img_folder, 'tank_enemy_t.png'))


def exit_game():
    confirm_exit = tkinter.messagebox.askyesno("Quit!", "Are You sure want to Quit?")
    if confirm_exit:
        root.quit()


# Image rotate function
def rotate_img(img_path, rt_degrees):
    img = Image.open(img_path)
    return img.rotate(rt_degrees, expand=True)


class TankTkinterApp:
    def __init__(self, master=None):

        # Sprites
        self.img_key_w = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'w-Key.png')))
        self.img_key_s = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 's-Key.png')))
        self.img_key_a = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'a-Key.png')))
        self.img_key_d = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'd-Key.png')))
        self.img_key_q = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'q-Key.png')))
        self.img_key_e = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'e-Key.png')))
        self.img_key_x = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'X-Key.png')))

        # User controls
        self.main = ttk.Frame(master)
        self.up = ttk.Button(self.main, text="Up", command=lambda: self.move_up(), image=self.img_key_w)
        # self.up.bind('<Key-2>', lambda event: self.move_up())
        self.up.grid(column=1, pady=3, row=1)
        self.left = ttk.Button(self.main, text="Left", command=lambda: self.move_left(), image=self.img_key_a)
        # self.up.bind('<Key-2>', lambda event: self.move_left())
        self.left.grid(column=0, row=2, sticky='e')
        self.fire = ttk.Button(self.main, text="Fire", command=lambda: self.player_shoot(), image=self.img_key_x)
        self.fire.grid(column=1, pady=3, row=2)
        self.right = ttk.Button(self.main, text="Right", command=lambda: self.move_right(), image=self.img_key_d)
        # self.up.bind('<Key-2>', lambda event: self.move_right())
        self.right.grid(column=2, row=2, sticky='w')
        self.down = ttk.Button(self.main, text="Down", command=lambda: self.move_down(), image=self.img_key_s)
        # self.up.bind('<Key-2>', lambda event: self.move_down())
        self.down.grid(column=1, pady="3", row=3)
        self.turn_l = ttk.Button(self.main, text="Turn L", command=lambda: self.turn_left(), image=self.img_key_q)
        self.turn_l.grid(column=0, row=1, sticky="e")
        self.turn_r = ttk.Button(self.main, text="Turn R", command=lambda: self.turn_right(), image=self.img_key_e)
        self.turn_r.grid(column=2, row=1, sticky="w")
        self.reset = ttk.Button(self.main, text="Reset", command=lambda: self.reset_game())
        self.reset.grid(column=0, row=4, sticky="e")
        self.reset = ttk.Button(self.main, text="Start", command=lambda: self.start_game())
        self.reset.grid(column=1, row=4)
        self.exit = ttk.Button(self.main, text="Exit", command=lambda: exit_game())
        self.exit.grid(column=2, row=4, sticky="w")
        self.label_frame = ttk.Labelframe(self.main)
        self.shmup_frame = ttk.Frame(self.label_frame)

        # Grid buttons
        # Units
        self.img_bg = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'dirt.png')))
        self.img_player_copy = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'tank_main_t.png')))
        # self.img_enemy_copy = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'tank_enemy_t.png')))

        # Grid tiles
        for index in range(0, 25):
            self.button = ttk.Button(self.shmup_frame, image=self.img_bg)
            grid_buttons.append(self.button)

        i = 0
        for row_x in (range(0, 5)):
            for col_y in (range(0, 5)):
                grid_buttons[i].grid(row=row_x, column=col_y)
                i += 1

        # Units
        self.button_player = ttk.Button(self.shmup_frame, image=self.img_player_copy)
        # self.button_enemy = ttk.Button(self.shmup_frame, image=self.img_enemy_copy)

        # Frame
        self.shmup_frame.configure(height="200", width="200")
        self.shmup_frame.grid(column=0, row=0)
        self.label_frame.configure(height="200", text="Tank Shmup", width="200")  # , font='Arial 16 bold'
        self.label_frame.grid(column=0, columnspan=3, row=0)
        self.main.configure(height="200", width="200")
        self.main.pack(side="top")
        self.main.grid_anchor("n")

        # Main widget
        self.main_window = self.main

    def run(self):
        self.main_window.mainloop()

# Reset game
    def reset_game(self):
        confirm_reset = tkinter.messagebox.askyesno("Reset!", "Are You sure want to Reset?")
        if confirm_reset:
            self.button_player.destroy()
            # self.button_enemy.destroy()

# Movement player unit
    def move_up(self):
        global tank_player_y, tank_player_x
        if tank_player_y in range(1, 4):
            tank_player_y -= 1
        self.button_player.grid(column=tank_player_x, row=tank_player_y)

    def move_down(self):
        global tank_player_y
        if tank_player_y in range(0, 4):
            tank_player_y += 1
        self.button_player.grid(column=tank_player_x, row=tank_player_y)

    def move_left(self):
        global tank_player_x
        if tank_player_x in range(0, 4):
            tank_player_x -= 1
        self.button_player.grid(column=tank_player_x, row=tank_player_y)

    def move_right(self):
        global tank_player_x
        if tank_player_x in range(0, 4):
            tank_player_x += 1
        self.button_player.grid(column=tank_player_x, row=tank_player_y)

# Rotate player unit
    def turn_left(self):
        global img_player_copy
        img_rt_90 = rotate_img(img_path_original, 90)
        img_rt_90.save((os.path.join(img_folder, 'tank_main_t.png')))
        img_player_copy = ImageTk.PhotoImage(img_rt_90)  # update image with rotated one
        self.button_player.config(image=img_player_copy)

# Rotate player unit
    def turn_right(self):
        global img_player_copy
        img_rt_90 = rotate_img(img_path_original, -90)
        img_rt_90.save((os.path.join(img_folder, 'tank_main_t.png')))
        img_player_copy = ImageTk.PhotoImage(img_rt_90)  # update image with rotated one
        self.button_player.config(image=img_player_copy)

    def player_shoot(self):
        print('Fire')

    def win_game(self):
        print('win')

    def lose_game(self):
        print('Lose')

    def draw_game(self):
        print('draw')

# Game start/unit creation
    def start_game(self):
        global tank_player_x, tank_player_y, tank_enemy_x, tank_enemy_y
        tank_player_x, tank_player_y = (randrange(0, 4)), (randrange(3, 4))
        # tank_enemy_x, tank_enemy_y = (randrange(0, 4)), (randrange(0, 2))
        self.button_player.grid(column=tank_player_x, row=tank_player_y)
        # self.button_enemy.grid(column=tank_enemy_x, row=tank_enemy_y)

    def game_running(self):
        pass


# Class init/app run
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = TankTkinterApp(root)
    app.run()
