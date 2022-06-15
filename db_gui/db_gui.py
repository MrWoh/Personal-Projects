import tkinter as tk
import tkinter.ttk as ttk
# import tkinter.messagebox
import sqlite3
import os

# File Paths
main_folder = os.path.dirname(__file__)
db_folder = os.path.join(main_folder, 'resources')

# Data base
conn = sqlite3.connect(os.path.join(db_folder, 'person.db'))
c = conn.cursor()
with conn:
    c.execute("SELECT * FROM person")
    person_list = c.fetchall()


class DbApp:
    def __init__(self, master):
        # build ui
        self.new_window = None
        self.master = master
        self.main_frame = ttk.Frame()
        self.submit_frame = ttk.Labelframe(self.main_frame, height="200", text="Submit Person", width="200")

        # Entry
        self.entry_name = ttk.Entry(self.submit_frame)
        self.entry_name.grid(column=2, row=1)
        self.entry_surname = ttk.Entry(self.submit_frame)
        self.entry_surname.grid(column=2, row=2)
        self.entry_mail = ttk.Entry(self.submit_frame)
        self.entry_mail.grid(column=2, row=3)
        self.entry_company = ttk.Entry(self.submit_frame)
        self.entry_company.grid(column=2, row=4)

        # Label
        self.label_name = ttk.Label(self.submit_frame, text="Name")
        self.label_name.grid(column=1, row=1, sticky="w")
        self.label_surname = ttk.Label(self.submit_frame, text="Surname")
        self.label_surname.grid(column=1, row=2, sticky="w")
        self.label_mail = ttk.Label(self.submit_frame, text="Mail")
        self.label_mail.grid(column=1, row=3, sticky="w")
        self.label_company = ttk.Label(self.submit_frame, text="Company")
        self.label_company.grid(column=1, row=4, sticky="w")
        self.label_gender = ttk.Label(self.submit_frame, text="Gender")
        self.label_gender.grid(column=1, row=5, sticky="w")
        self.combobox_gender = ttk.Combobox(self.submit_frame, values=['male', 'female'], width=17)
        self.combobox_gender.grid(column=2, row=5)
        self.list_scroll = tk.Scrollbar(self.submit_frame, orient="vertical")
        self.list_scroll.grid(column=3, row=1, rowspan=8, sticky="nse")
        self.list_database = tk.Listbox(self.submit_frame, width=100, yscrollcommand=self.list_scroll.set,
                                        selectbackground="black")
        self.list_database.insert(tk.END, *person_list)
        self.list_database.grid(column=3, row=1, rowspan=8)

        # Button
        self.button_submit = ttk.Button(self.submit_frame, text="Submit", width=8, command=self.submit_person)
        self.button_submit.grid(column=1, row=6)
        self.button_delete = ttk.Button(self.submit_frame, text="Delete", width=8, command=self.delete_person)
        self.button_delete.grid(column=2, row=8, sticky="w")
        self.button_edit = ttk.Button(self.submit_frame, text="Edit", width=8, command=self.edit_person,
                                      state='disabled')
        self.button_edit.grid(column=2, row=8, sticky="e")
        self.separator = ttk.Separator(self.submit_frame, orient="horizontal", takefocus=True)
        self.separator.grid(column=1, columnspan=2, pady="2", row=7, sticky="ew")
        self.submit_frame.grid(column=1, row=1)
        self.main_frame.grid(column=0, row=0)

        # Main widget
        self.main_window = self.main_frame

    def edit_person(self):
        self.new_window = PopUp(self)

    def submit_person(self):
        new_person = (self.entry_name.get(), self.entry_surname.get(),
                      self.entry_mail.get(), self.entry_company.get(), self.combobox_gender.get())
        with conn:
            c.execute(f"INSERT INTO person VALUES {new_person}")
            c.execute("SELECT * FROM person")
            refresh_list = c.fetchall()
            self.list_database.delete(0, tk.END)
            self.list_database.insert(tk.END, *refresh_list)

    def delete_person(self):
        for items in self.list_database.curselection():
            with conn:
                c.execute(f"DELETE from person WHERE rowid={items + 1}")
                c.execute("SELECT * FROM person")
                refresh_list = c.fetchall()
                self.list_database.delete(0, tk.END)
                self.list_database.insert(tk.END, *refresh_list)

    def run(self):
        self.main_window.mainloop()


class PopUp:
    def __init__(self, master):
        # build ui
        self.master = master
        self.toplevel = tk.Tk()
        self.toplevel.resizable(False, False)

        # Entry
        self.entry_name_t = ttk.Entry(self.toplevel)
        self.entry_name_t.grid(column=2, row=1)
        self.entry_surname_t = ttk.Entry(self.toplevel)
        self.entry_surname_t.grid(column=2, row=2)
        self.entry_mail_t = ttk.Entry(self.toplevel)
        self.entry_mail_t.grid(column=2, row=3)
        self.entry__company_t = ttk.Entry(self.toplevel)
        self.entry__company_t.grid(column=2, row=4)

        # Label
        self.label_name_t = ttk.Label(self.toplevel, text="Name")
        self.label_name_t.grid(column=1, row=1, sticky="w")
        self.label_surname_t = ttk.Label(self.toplevel, text="Surname")
        self.label_surname_t.grid(column=1, row=2, sticky="w")
        self.label_mail_t = ttk.Label(self.toplevel, text="Mail")
        self.label_mail_t.grid(column=1, row=3, sticky="w")
        self.label_company_t = ttk.Label(self.toplevel, text="Company")
        self.label_company_t.grid(column=1, row=4, sticky="w")
        self.label_gender_t = ttk.Label(self.toplevel, text="Gender")
        self.label_gender_t.grid(column=1, row=5)
        self.combobox_gender_t = ttk.Combobox(self.toplevel, values=['male', 'female'], width=17)
        self.combobox_gender_t.grid(column=2, row=5)
        self.separator_t = ttk.Separator(self.toplevel, orient="horizontal", takefocus=True)
        self.separator_t.grid(column=1, columnspan=2, pady=2, row=6, sticky="ew")

        # Button
        self.button_edit_t = ttk.Button(self.toplevel, text="Edit", width=8)
        self.button_edit_t.grid(column=1, row=7)
        self.button_cancel = tk.Button(self.toplevel, text="Cancel")  # command=self.cancel
        self.button_cancel.grid(column=2, row=7, sticky="e")

    # def cancel(self):
    #     confirm_exit = tkinter.messagebox.askyesno("Cancel!", "Are You sure want to Cancel?")
    #     if confirm_exit:
    #         self.new_window.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = DbApp(root)
    root.resizable(False, False)
    app.run()
