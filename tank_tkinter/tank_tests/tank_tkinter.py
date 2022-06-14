
import tkinter as tk
import tkinter.ttk as ttk
import os

# Variables
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'resources')
tank_enemy = 0
tank_player = 0


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
        self.frame2 = ttk.Frame(self.label_frame)

        # Grid placement
        self.img_bg = tk.PhotoImage(file=os.path.join(img_folder, 'dirt.png'))
        self.img_enemy = tk.PhotoImage(file=os.path.join(img_folder, 'tankEnemy.png'))
        self.img_player = tk.PhotoImage(file=os.path.join(img_folder, 'tankBase.png'))
        self.b_1x1 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_1x1.grid(column=0, row=0)
        self.b_1x2 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_1x2.grid(column=0, row=1)
        self.b_1x3 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_1x3.grid(column=0, row=2)
        self.b_1x4 = ttk.Button(self.frame2, image=self.img_enemy)
        self.b_1x4.grid(column=0, row=3)
        self.b_1x5 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_1x5.grid(column=0, row=4)
        self.b_2x1 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_2x1.grid(column=1, row=0)
        self.b_2x2 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_2x2.grid(column=1, row=1)
        self.b_2x3 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_2x3.grid(column=1, row=2)
        self.b_2x4 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_2x4.grid(column=1, row=3)
        self.b_2x5 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_2x5.grid(column=1, row=4)
        self.b_3x1 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_3x1.grid(column=2, row=0)
        self.b_3x2 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_3x2.grid(column=2, row=1)
        self.b_3x3 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_3x3.grid(column=2, row=2)
        self.b_3x4 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_3x4.grid(column=2, row=3)
        self.b_3x5 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_3x5.grid(column=2, row=4)
        self.b_4x1 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_4x1.grid(column=3, row=0)
        self.b_4x2 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_4x2.grid(column=3, row=1)
        self.b_4x3 = ttk.Button(self.frame2, image=self.img_player)
        self.b_4x3.grid(column=3, row=2)
        self.b_4x4 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_4x4.grid(column=3, row=3)
        self.b_4x5 = ttk.Button(self.frame2, image=self.img_bg)
        self.b_4x5.grid(column=3, row=4)
        self.b5x1 = ttk.Button(self.frame2, image=self.img_bg)
        self.b5x1.grid(column=4, row=0)
        self.b5x2 = ttk.Button(self.frame2, image=self.img_bg)
        self.b5x2.grid(column=4, row=1)
        self.b5x3 = ttk.Button(self.frame2, image=self.img_bg)
        self.b5x3.grid(column=4, row=2)
        self.b5x4 = ttk.Button(self.frame2, image=self.img_bg)
        self.b5x4.grid(column=4, row=3)
        self.b5x5 = ttk.Button(self.frame2, image=self.img_bg)
        self.b5x5.grid(column=4, row=4)

        self.frame2.configure(height="200", width="200")
        self.frame2.grid(column=0, row=0)
        self.label_frame.configure(height="200", text="labelframe1", width="200")
        self.label_frame.grid(column=0, columnspan=3, row=0)
        self.main.configure(height="200", width="200")
        self.main.pack(side="top")
        self.main.grid_anchor("n")

        # Main widget
        self.main_window = self.main

    def run(self):
        self.main_window.mainloop()
        buttons = []
        for index in range(0, 25):
            button = tk.Button(self.main, text=index, state=tk.DISABLED)
            buttons.append(button)

    # def button_event(self, user_select):
    #     run_button_event = True
    #     # Variables
    #     buttons = []
    #     for index in range(0, 25):
    #         button = tk.Button(self.main, text=index, state=tk.DISABLED)
    #         buttons.append(button)


        # Main game logic loop
        # while run_button_event:
        #     number_guesses += 1
        #     if player_guess == secret_number:
        #         print('win')
        #         confirm_exit = tkinter.messagebox.showinfo("showinfo", "You Won!")
        #         if confirm_exit == "ok":
        #             root.quit()
        #         break
        #     elif player_guess > secret_number:
        #         self.title['text'] = f'{player_guess} is too high.'
        #         self.tries_label['text'] = f'{number_guesses}/5'
        #         buttons[player_guess]['state'] = 'disabled'
        #         break
        #     else:
        #         self.title['text'] = f'{player_guess} is too low.'
        #         self.tries_label['text'] = f'{number_guesses}/5'
        #         buttons[player_guess]['state'] = 'disabled'
        #         break
        # if number_guesses > 4:
        #     print('Lose')
        #     confirm_exit = tkinter.messagebox.showinfo("showinfo", "You lost!")
        #     if confirm_exit == "ok":
        #         root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = TankTkinterApp(root)
    app.run()
