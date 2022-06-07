import tkinter as tk
import tkinter.ttk as ttk
import os

main_folder = os.path.dirname(__file__)
image_folder = os.path.join(main_folder, 'resources')
print(image_folder)


class MainFrame:

    def __init__(self, master=None):
        # build ui
        self.frame1 = ttk.Frame(master, class_="main")
        self.skelbimas_1 = ttk.Labelframe(self.frame1)
        self.notebook = ttk.Notebook(self.skelbimas_1)
        self.image_1 = ttk.Label(self.notebook)
        self.img_house = tk.PhotoImage(file=(os.path.join(image_folder, 'house.png')))
        self.image_1.configure(
            compound="right", image=self.img_house, text="Picture", width=""
        )
        self.image_1.pack(side="left")
        self.notebook.add(
            self.image_1, compound="center", padding="2", state="normal", text="Image"
        )
        self.info_1 = ttk.Label(self.notebook)
        self.info_1.configure(text="Type: House\nRooms: 4\nSize: 124kvm", width="160")
        self.info_1.grid(column="0", row="0")
        self.notebook.add(
            self.info_1, padding="2", state="normal", sticky="n", text="Text"
        )
        self.notebook.configure(height="160", padding="2", width="200")
        self.notebook.grid(column="0", row="0")
        self.skelbimas_1.configure(
            borderwidth="3", height="200", text="Skelbimas #1\n", width="200"
        )
        self.skelbimas_1.grid(column="0", row="1")
        self.skelbimas_3 = ttk.Labelframe(self.frame1)
        self.notebook2 = ttk.Notebook(self.skelbimas_3)
        self.image_2 = ttk.Label(self.notebook2)
        self.image_2.configure(
            compound="right", image=self.img_house, text="Nuotrauka", width="160"
        )
        self.image_2.pack(side="left")
        self.notebook2.add(
            self.image_2,
            compound="top",
            padding="2",
            state="normal",
            sticky="n",
            text="Image",
        )
        self.info_2 = ttk.Label(self.notebook2)
        self.info_2.configure(text="Type: House\nRooms: 4\nSize: 124kvm", width="160")
        self.info_2.pack()
        self.notebook2.add(
            self.info_2, padding="2", state="normal", sticky="n", text="Text"
        )
        self.notebook2.configure(height="160", width="200")
        self.notebook2.pack()
        self.skelbimas_3.configure(
            borderwidth="3", height="200", text="Skelbimas #3\n", width="200"
        )
        self.skelbimas_3.grid(column="1", row="2")
        self.skelbimas_4 = ttk.Labelframe(self.frame1)
        self.notebook4 = ttk.Notebook(self.skelbimas_4)
        self.image_3 = ttk.Label(self.notebook4)
        self.image_3.configure(
            compound="right", image=self.img_house, text="Nuotrauka", width="160"
        )
        self.image_3.pack()
        self.notebook4.add(
            self.image_3,
            compound="top",
            padding="2",
            state="normal",
            sticky="n",
            text="Image",
        )
        self.info_3 = ttk.Label(self.notebook4)
        self.info_3.configure(text="Type: House\nRooms: 4\nSize: 124kvm", width="160")
        self.info_3.pack()
        self.notebook4.add(
            self.info_3, padding="2", state="normal", sticky="n", text="Text"
        )
        self.notebook4.configure(height="160", width="200")
        self.notebook4.pack()
        self.skelbimas_4.configure(
            borderwidth="3", height="200", text="Skelbimas #4\n", width="200"
        )
        self.skelbimas_4.grid(column="0", row="2")
        self.skelbimas_2 = ttk.Labelframe(self.frame1)
        self.notebook3 = ttk.Notebook(self.skelbimas_2)
        self.image_4 = ttk.Label(self.notebook3)
        self.image_4.configure(
            compound="right", image=self.img_house, text="Nuotrauka", width="160"
        )
        self.image_4.grid(column="0", row="0")
        self.notebook3.add(
            self.image_4,
            compound="top",
            padding="2",
            state="normal",
            sticky="n",
            text="Image",
        )
        self.info_4 = ttk.Label(self.notebook3)
        self.info_4.configure(text="Type: House\nRooms: 4\nSize: 124kvm", width="160")
        self.info_4.pack()
        self.notebook3.add(
            self.info_4, padding="2", state="normal", sticky="n", text="Text"
        )
        self.notebook3.configure(height="160", width="200")
        self.notebook3.grid(column="0", row="0")
        self.skelbimas_2.configure(
            borderwidth="3", height="200", text="Skelbimas #2\n", width="200"
        )
        self.skelbimas_2.grid(column="1", row="1")
        self.prev_butt = ttk.Button(self.frame1)
        self.prev_butt.configure(default="normal", text="Previous")
        self.prev_butt.grid(column="0", row="3", sticky="nw")
        self.next_butt = ttk.Button(self.frame1)
        self.next_butt.configure(text="Next")
        self.next_butt.grid(column="1", row="3", sticky="ne")
        self.frame3 = ttk.Frame(self.frame1)
        self.options_frame = ttk.Labelframe(self.frame3)
        self.search = ttk.Label(self.options_frame)
        self.search.configure(text="Search Keywords")
        self.search.grid(column="0", row="0", sticky="w")
        self.entry1 = ttk.Entry(self.options_frame)
        self.entry1.configure(state="normal")
        self.entry1.grid(column="0", row="1")
        self.label9 = ttk.Label(self.options_frame)
        self.label9.configure(text="Price range")
        self.label9.grid(column="0", row="2", sticky="w")
        self.scale1 = ttk.Scale(self.options_frame)
        self.scale1.configure(orient="horizontal", state="normal")
        self.scale1.grid(column="0", columnspan="2", row="3")
        self.label10 = ttk.Label(self.options_frame)
        self.label10.configure(text="From:\n10e")
        self.label10.grid(column="0", row="3", sticky="w")
        self.label11 = ttk.Label(self.options_frame)
        self.label11.configure(text="To:\n400e")
        self.label11.grid(column="1", row="3")
        self.checkbutton3 = ttk.Checkbutton(self.options_frame)
        self.checkbutton3.configure(state="normal", text="Petfree")
        self.checkbutton3.grid(column="0", row="8", sticky="w")
        self.checkbutton2 = ttk.Checkbutton(self.options_frame)
        self.checkbutton2.configure(state="normal", text="Balcony")
        self.checkbutton2.grid(column="0", row="9", sticky="w")
        self.checkbutton5 = ttk.Checkbutton(self.options_frame)
        self.checkbutton5.configure(state="normal", text="Agent fee")
        self.checkbutton5.grid(column="0", row="10", sticky="w")
        self.checkbutton4 = ttk.Checkbutton(self.options_frame)
        self.checkbutton4.configure(state="normal", text="Deposit")
        self.checkbutton4.grid(column="0", row="11", sticky="w")
        self.separator2 = ttk.Separator(self.options_frame)
        self.separator2.configure(orient="horizontal", takefocus=False)
        self.separator2.grid(
            column="0", columnspan="2", padx="100", pady="30", row="2", rowspan="2"
        )
        self.checkbutton1 = ttk.Checkbutton(self.options_frame)
        self.checkbutton1.configure(state="normal", text="Parking")
        self.checkbutton1.grid(column="0", row="12", sticky="w")
        self.options_frame.configure(height="200", text="Options", width="200")
        self.options_frame.grid(column="2", columnspan="4", row="1", rowspan="4")
        self.frame3.configure(height="200", width="200")
        self.frame3.grid(column="2", columnspan="1", row="1", rowspan="1")
        self.frame1.configure(
            borderwidth="3", height="650", padding="2", takefocus=True
        )
        self.frame1.configure(width="450")
        self.frame1.grid()

        # Main widget
        self.mainwindow = self.frame1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainFrame(root)
    app.run()
