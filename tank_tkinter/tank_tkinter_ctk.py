from random import randrange
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from turtle import bgcolor
from PIL import ImageTk, Image
import os
import customtkinter as ctk

# Variables
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
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
        app.quit()

# Image rotate function
def rotate_img(img_path, rt_degr):
    img = Image.open(img_path)
    return img.rotate(rt_degr, expand=True)


class App(ctk.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self,master=None):
        super().__init__()   

        # Frame Variables
        self.title("Tank Tkinter")
        # self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        # Sprites
        # self.img_key_w = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'w-Key.png')))
        # self.img_key_s = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 's-Key.png')))
        # self.img_key_a = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'a-Key.png')))
        # self.img_key_d = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'd-Key.png')))
        # self.img_key_q = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'q-Key.png')))
        # self.img_key_e = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'e-Key.png')))
        # self.img_key_x = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'X-Key.png')))

        # # User controls
        self.main = ctk.CTkFrame(master)
        self.up = ctk.CTkButton(self.main, text="W", command=lambda: self.move_up(), width=32, fg_color=("gray75", "gray30"))
        self.up.grid(column=1, row=1)
        self.left = ctk.CTkButton(self.main, text="A", command=lambda: self.move_left(), width=32, fg_color=("gray75", "gray30"))
        self.left.grid(column=1, row=2, sticky='w')
        self.fire = ctk.CTkButton(self.main, text="X", command=lambda: self.player_shoot(), width=32, fg_color=("gray75", "gray30"))
        self.fire.grid(column=1, row=2)
        self.right = ctk.CTkButton(self.main, text="D", command=lambda: self.move_right(), width=32, fg_color=("gray75", "gray30"))
        self.right.grid(column=1, row=2, sticky='e')
        self.down = ctk.CTkButton(self.main, text="S", command=lambda: self.move_down(), width=32, fg_color=("gray75", "gray30"))
        self.down.grid(column=1, row=3)
        self.turn_l = ctk.CTkButton(self.main, text="Q", command=lambda: self.turn_left(), width=32, fg_color=("gray75", "gray30"))
        self.turn_l.grid(column=1, row=1, sticky='w')
        self.turn_r = ctk.CTkButton(self.main, text="E", command=lambda: self.turn_right(), width=32, fg_color=("gray75", "gray30"))
        self.turn_r.grid(column=1, row=1, sticky='e')
        self.reset = ctk.CTkButton(self.main, text="Reset", command=lambda: self.reset_game(), width=36, fg_color=("gray75", "gray30"))
        self.reset.grid(column=0, row=4)
        self.reset = ctk.CTkButton(self.main, text="Start", command=lambda: self.start_game(), width=36, fg_color=("gray75", "gray30"))
        self.reset.grid(column=1, row=4)
        self.exit = ctk.CTkButton(self.main, text="Exit", command=lambda: exit_game(), width=36, fg_color=("gray75", "gray30"))
        self.exit.grid(column=2, row=4)
        self.switch_2 = ctk.CTkSwitch(self.main, text="Light Mode", command=lambda: self.change_mode())
        self.switch_2.grid(column=1, row=7)
        self.label_frame = ctk.CTkFrame(self.main)
        self.shmup_frame = ctk.CTkFrame(self.label_frame)

        # Grid buttons
        # Units
        self.img_bg = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'bg.png')))
        self.img_player_copy = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'tank_main_t.png')))
        # self.img_enemy_copy = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, 'tank_enemy_t.png')))

        # Grid tiles
        for index in range(0, 25):
            self.button = tk.Label(self.shmup_frame, text='', image=self.img_bg, height= 46, width=46)
            grid_buttons.append(self.button)

        i = 0
        for row_x in (range(0, 5)):
            for col_y in (range(0, 5)):
                grid_buttons[i].grid(row=row_x, column=col_y)
                i += 1

        # Units
        self.button_player = ctk.CTkButton(self.shmup_frame, image=self.img_player_copy, text='', height=10, width=10, fg_color='#0a0705')
        # self.button_enemy = ttk.Button(self.shmup_frame, image=self.img_enemy_copy, text='')

        # Frame
        # self.shmup_frame.configure(height="250", width="300")
        self.shmup_frame.grid(column=0, row=0)
        # self.label_frame.configure(height="250", width="300")  # , font='Arial 16 bold', text="Tank Shmup"
        self.label_frame.grid(column=0, columnspan=3, row=0)
        self.main.configure(height="250", width="450")
        self.main.pack(side="top")
        self.main.grid_anchor("n")

        # Main widget
        self.main_window = self.main

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

    def change_mode(self):
        if self.switch_2.get() == 1:
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")

if __name__ == "__main__":
    app = App()
    app.resizable(0, 0)
    app.mainloop()