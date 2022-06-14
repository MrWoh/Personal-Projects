def rotate_image():
    import tkinter as tk
    from PIL import Image, ImageTk
    import os

    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'resources')
    img_player_original = Image.open(os.path.join(img_folder, 'tank_main.png'))
    img_path_original = (os.path.join(img_folder, 'tank_main_t.png'))

    def rotate_img(img_path, rt_degr):
        img = Image.open(img_path)
        return img.rotate(rt_degr, expand=1)

    def draw():
        global image
        img_rt_90 = rotate_img(img_path_original, 90)
        img_rt_90.save((os.path.join(img_folder, 'tank_main_t.png')))
        image = ImageTk.PhotoImage(img_rt_90) # update image with rotated one
        label.config(image=image)

    def key_pressed(self, tk_command):
            self.tk_frame = tk_command.widget.tk_frame
            if (tk_command.char == "p") and (self.instance == 0):
                self.write_first_instance() 
                self.timer_clock()
                self.move_player(0,0)
            if (tk_command.char == "f") and (self.player_staff == 1) and (self.player_mp >= 10) and (self.plasma != 1):
                self.launch_plasma_projectile()
                self.player_mp -= 10
            if tk_command.keysym == "1" and (self.player_staff == 1): 
                self.player_staff = 0
                self.player_inventory_staff = 1
            if tk_command.keysym == "2" and (self.player_inventory_staff == 1): 
                self.player_inventory_staff = 0
                self.player_staff = 1
            if tk_command.keysym == "c" and (self.instance != 0): 
                self.start_new_game()
            if tk_command.keysym == "x": 
                self.npc_hp = 0
            if tk_command.keysym == "i": 
                self.world_tesseract_beacon = 1
            if tk_command.keysym == "b": 
                self.npc_b_hp = 0
            if tk_command.keysym == "g": 
                self.npc_d_hp = 0
            if tk_command.keysym == "Up":
                if (self.instance == 1 or self.instance == 2 or self.instance == 3 or self.instance == 4): 
                    self.move_player(-1, 0) 
            if tk_command.keysym == "Down":
                if (self.instance == 1 or self.instance == 2 or self.instance == 3 or self.instance == 4):
                    self.move_player(+1, 0) 
            if tk_command.keysym == "Left":
                if (self.instance == 1 or self.instance == 2 or self.instance == 3 or self.instance == 4):
                    self.move_player(0,-1) 
            if tk_command.keysym == "Right":
                if (self.instance == 1 or self.instance == 2 or self.instance == 3 or self.instance == 4):
                    self.move_player(0,+1)

    root = tk.Tk()
    root.geometry('100x100')
    image = ImageTk.PhotoImage(img_player_original)
    label = tk.Button(image=image)
    label.pack()
    but12 = tk.Button(root, text="Rotate",command=draw)
    but12.pack()
    root.mainloop()

def custom_complex_tkinter():
    import tkinter
    import tkinter.messagebox
    import customtkinter

    customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


    class App(customtkinter.CTk):

        WIDTH = 780
        HEIGHT = 520

        def __init__(self):
            super().__init__()

            self.title("CustomTkinter complex_example.py")
            self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
            self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

            # ============ create two frames ============

            # configure grid layout (2x1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)

            self.frame_left = customtkinter.CTkFrame(master=self,
                                                     width=180,
                                                     corner_radius=0)
            self.frame_left.grid(row=0, column=0, sticky="nswe")

            self.frame_right = customtkinter.CTkFrame(master=self)
            self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

            # ============ frame_left ============

            # configure grid layout (1x11)
            self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
            self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
            self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
            self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

            self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                                  text="CustomTkinter",
                                                  text_font=("Roboto Medium", -16))  # font name and size in px
            self.label_1.grid(row=1, column=0, pady=10, padx=10)

            self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                    text="CTkButton 1",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.button_event)
            self.button_1.grid(row=2, column=0, pady=10, padx=20)

            self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                    text="CTkButton 2",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.button_event)
            self.button_2.grid(row=3, column=0, pady=10, padx=20)

            self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                    text="CTkButton 3",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.button_event)
            self.button_3.grid(row=4, column=0, pady=10, padx=20)

            self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left)
            self.switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

            self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                    text="Dark Mode",
                                                    command=self.change_mode)
            self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

            # ============ frame_right ============

            # configure grid layout (3x7)
            self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
            self.frame_right.rowconfigure(7, weight=10)
            self.frame_right.columnconfigure((0, 1), weight=1)
            self.frame_right.columnconfigure(2, weight=0)

            self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
            self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

            # ============ frame_info ============

            # configure grid layout (1x1)
            self.frame_info.rowconfigure(0, weight=1)
            self.frame_info.columnconfigure(0, weight=1)

            self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                       text="CTkLabel: Lorem ipsum dolor sit,\n" +
                                                            "amet consetetur sadipscing elitr,\n" +
                                                            "sed diam nonumy eirmod tempor" ,
                                                       height=100,
                                                       fg_color=("white", "gray38"),  # <- custom tuple-color
                                                       justify=tkinter.LEFT)
            self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

            self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
            self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

            # ============ frame_right ============

            self.radio_var = tkinter.IntVar(value=0)

            self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                            text="CTkRadioButton Group:")
            self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                               variable=self.radio_var,
                                                               value=0)
            self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                               variable=self.radio_var,
                                                               value=1)
            self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

            self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                               variable=self.radio_var,
                                                               value=2)
            self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

            self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                    from_=0,
                                                    to=1,
                                                    number_of_steps=3,
                                                    command=self.progressbar.set)
            self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

            self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
                                                    command=self.progressbar.set)
            self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

            self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                           height=25,
                                                           text="CTkButton",
                                                           command=self.button_event)
            self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

            self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                           height=25,
                                                           text="CTkButton",
                                                           command=self.button_event)
            self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

            self.checkbox_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                             height=25,
                                                             text="CTkButton",
                                                             border_width=3,   # <- custom border_width
                                                             fg_color=None,   # <- no fg_color
                                                             command=self.button_event)
            self.checkbox_button_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

            self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                         text="CTkCheckBox")
            self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

            self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                         text="CTkCheckBox")
            self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

            self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                                width=120,
                                                placeholder_text="CTkEntry")
            self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

            self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                    text="CTkButton",
                                                    command=self.button_event)
            self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

            # set default values
            self.radio_button_1.select()
            self.switch_2.select()
            self.slider_1.set(0.2)
            self.slider_2.set(0.7)
            self.progressbar.set(0.5)
            self.slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
            self.radio_button_3.configure(state=tkinter.DISABLED)
            self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
            self.check_box_2.select()

        def button_event(self):
            print("Button pressed")

        def change_mode(self):
            if self.switch_2.get() == 1:
                customtkinter.set_appearance_mode("dark")
            else:
                customtkinter.set_appearance_mode("light")

        def on_closing(self, event=0):
            self.destroy()


    if __name__ == "__main__":
        app = App()
        app.mainloop()

def custom_simple_tkinter():
    import tkinter
    import customtkinter

    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = customtkinter.CTk()
    app.geometry("400x580")
    app.title("CustomTkinter simple_example.py")


    def button_callback():
        print("Button click", combobox_1.get())


    def slider_callback(value):
        progressbar_1.set(value)


        frame_1 = customtkinter.CTkFrame(master=app)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
        label_1.pack(pady=12, padx=10)

        progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
        progressbar_1.pack(pady=12, padx=10)

        button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
        button_1.pack(pady=12, padx=10)

        slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
        slider_1.pack(pady=12, padx=10)
        slider_1.set(0.5)

        entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
        entry_1.pack(pady=12, padx=10)

        optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42"])
        optionmenu_1.pack(pady=12, padx=10)
        optionmenu_1.set("CTkOptionMenu")

        combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42"])
        combobox_1.pack(pady=12, padx=10)
        optionmenu_1.set("CTkComboBox")

        checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
        checkbox_1.pack(pady=12, padx=10)

        radiobutton_var = tkinter.IntVar(value=1)

        radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
        radiobutton_1.pack(pady=12, padx=10)

        radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
        radiobutton_2.pack(pady=12, padx=10)

        switch_1 = customtkinter.CTkSwitch(master=frame_1)
        switch_1.pack(pady=12, padx=10)

        app.mainloop()

custom_complex_tkinter()