import tkinter.ttk as ttk
import tkinter.messagebox
from random import randint

secret_number = randint(0, 9)
number_guesses = 0


class GuessNumber:
    def __init__(self, master=None):
        # build ui
        self.frame = ttk.Frame(master)
        self.frame_label = ttk.Labelframe(self.frame)
        self.button_1 = ttk.Button(self.frame_label, text="1", command=lambda: self.button_event(user_select=1))
        self.button_1.grid(column=0, row=1)
        self.button_2 = ttk.Button(self.frame_label, text="2", command=lambda: self.button_event(user_select=2))
        self.button_2.grid(column=1, row=1)
        self.button_3 = ttk.Button(self.frame_label, text="3", command=lambda: self.button_event(user_select=3))
        self.button_3.grid(column=2, row=1)
        self.button_4 = ttk.Button(self.frame_label, text="4", command=lambda: self.button_event(user_select=4))
        self.button_4.grid(column=0, row=2)
        self.button_5 = ttk.Button(self.frame_label, text="5", command=lambda: self.button_event(user_select=5))
        self.button_5.grid(column=1, row=2)
        self.button_6 = ttk.Button(self.frame_label, text="6", command=lambda: self.button_event(user_select=6))
        self.button_6.grid(column=2, row=2)
        self.button_7 = ttk.Button(self.frame_label, text="7", command=lambda: self.button_event(user_select=7))
        self.button_7.grid(column=0, row=3)
        self.button_8 = ttk.Button(self.frame_label, text="8", command=lambda: self.button_event(user_select=8))
        self.button_8.grid(column=1, row=3)
        self.button_9 = ttk.Button(self.frame_label, text="9", command=lambda: self.button_event(user_select=9))
        self.button_9.grid(column=2, row=3)
        self.title = ttk.Label(self.frame_label, text="")
        self.title.grid(column=1, row=0)
        self.button_0 = ttk.Button(self.frame_label, text="0", command=lambda: self.button_event(user_select=0))
        self.button_0.grid(column=1, row=4)
        self.tries_label = ttk.Label(self.frame_label, text="0/5")
        self.tries_label.grid(column=0, row=4)
        self.frame_label.configure(
            height="200", padding="3", text="Guess the number", width="200"
        )
        self.frame_label.pack(side="top")
        self.frame.configure(height="200", width="200")
        self.frame.pack(side="top")

        # Main widget
        self.main_window = self.frame

    def run(self):
        self.main_window.mainloop()

    def button_event(self, user_select):
        run_button_event = True
        # Variables
        buttons = [self.button_0, self.button_1, self.button_2, self.button_3, self.button_4,
                   self.button_5, self.button_6, self.button_7, self.button_8, self.button_9]
        player_guess = user_select
        global number_guesses
        # Main game logic loop
        while run_button_event:
            number_guesses += 1
            if player_guess == secret_number:
                print('win')
                confirm_exit = tkinter.messagebox.showinfo("showinfo", "You Won!")
                if confirm_exit == "ok":
                    root.quit()
                break
            elif player_guess > secret_number:
                self.title['text'] = f'{player_guess} is too high.'
                self.tries_label['text'] = f'{number_guesses}/5'
                buttons[player_guess]['state'] = 'disabled'
                break
            else:
                self.title['text'] = f'{player_guess} is too low.'
                self.tries_label['text'] = f'{number_guesses}/5'
                buttons[player_guess]['state'] = 'disabled'
                break
        if number_guesses > 4:
            print('Lose')
            confirm_exit = tkinter.messagebox.showinfo("showinfo", "You lost!")
            if confirm_exit == "ok":
                root.quit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry('250x165')
    root.resizable(False, False)
    app = GuessNumber(root)
    app.run()
