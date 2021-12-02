import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import db_client as cl

client = None


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Информационная система")
        self['background'] = '#EEEEEC'
        # self.geometry('800x600')
        self.resizable(False, False)
        self.conf = {'padx': 10, 'pady': 10}
        self.put_login_frame()

    def put_login_frame(self):
        LoginFrame(self).grid(row=0, column=0, padx=10, pady=10)

    def put_menu_frame(self):
        UserMenu(self).grid(row=0, column=0, padx=10, pady=10)

    def clean(self):
        all_widgets = [f for f in self.children]
        for f_name in all_widgets:
            self.nametowidget(f_name).destroy()


class LoginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.info_label = tk.Label(
            background=self.master['background'],
            text="Введите данные для входа",
            font='Helvetica 12',
            cnf=self.master.conf,
        )
        self.info_label.grid(row=0, column=0, columnspan=2)

        self.login_label = tk.Label(
            background=self.master['background'],
            text="Логин",
            font='Helvetica 11',
            cnf=self.master.conf,
        )
        self.login_entry = tk.Entry()
        self.login_label.grid(row=1, column=0, sticky='w', cnf=self.master.conf)
        self.login_entry.grid(row=1, column=1, sticky='e', cnf=self.master.conf)

        self.pass_label = tk.Label(
            background=self.master['background'],
            text="Пароль",
            font='Helvetica 11',
            cnf=self.master.conf,
        )
        self.pass_entry = tk.Entry(show='*')
        self.pass_label.grid(row=2, column=0, sticky='w', cnf=self.master.conf)
        self.pass_entry.grid(row=2, column=1, sticky='e', cnf=self.master.conf)

        self.button = tk.Button(text="Войти", font='Helvetica 12', command=self.login)
        self.button.grid(row=3, column=0, columnspan=2, sticky='s', cnf=self.master.conf)

    def login(self):
        username = self.login_entry.get()
        password = self.pass_entry.get()
        try:
            global client
            client = cl.db_client(username=username, password=password)
            messagebox.showinfo("Login successful", f"Добро пожаловать, {username}")
            self.master.clean()
            self.master.put_menu_frame()
        except Exception as _ex:
            messagebox.showwarning(
                "Login failure", "Проверьте правильность вводимых данных"
            )
            print(_ex)


class UserMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.table_content = []
        self.put_widgets()

    def get_user_actions(self):
        global client
        _ = list()
        for act in client.user_actions:
            _.append(act)

        return _

    def get_all_teachers(self):
        global client
        inst_name = self.inst_entry.get()
        if inst_name != '':
            self.table_content = client.get_all_teachers(inst_name)
            print(self.table_content)
            self.refresh()
        else:
            messagebox.showerror('Ошибка', 'Введите название института')

    def exec_action(self):
        global client
        action_name = self.actions_combobox.get() 
        getattr(self, action_name)()
        # client.user_actions[self.actions_combobox.get()]()

    def refresh(self):
        all_w = [w for w in self.children]
        for w_name in all_w:
            self.nametowidget(w_name).destroy()
        self.put_widgets()

    def put_widgets(self):
        # self.edit_frame = EditFrame(self).grid(row=0, column=0, cnf=self.master.conf)
        # self.actions_frame = ActionsFrame(self).grid(row=0, column=1, cnf=self.master.conf)
        # self.table_frame = TableFrame(self).grid(row=1, column=0, columnspan=2, cnf=self.master.conf)
        self.actions_frame = tk.Frame(self.master, bg='green', width=400, height=200)
        self.edit_frame = tk.Frame(self.master, bg='yellow', width=400, height=200)
        self.table_frame = tk.Frame(self.master, bg='blue', width=800, height=400)

        self.edit_frame.grid(row=0, column=0, sticky='w', cnf=self.master.conf)
        self.actions_frame.grid(row=0, column=1, sticky='e', cnf=self.master.conf)
        self.table_frame.grid(
            row=1, column=0, columnspan=2, sticky='s', cnf=self.master.conf
        )

        # ========================= Actions Frame
        self.info_label = tk.Label(
            master=self.actions_frame,
            text='Доступные функции',
            font='Helvetica 12',
            padx=10,
            pady=10,
        )
        self.info_label.grid(
            row=0, column=0, columnspan=2, sticky='e', cnf=self.master.conf
        )

        self.actions_combobox = ttk.Combobox(master=self.actions_frame)
        self.actions_combobox['state'] = 'readonly'
        self.actions_combobox['values'] = self.get_user_actions()
        self.actions_combobox.grid(row=1, column=0, sticky='w', cnf=self.master.conf)

        self.do_action = tk.Button(
            master=self.actions_frame,
            text='Выполнить',
            font='Helvetica 12',
            command=self.exec_action,
        )
        self.do_action.grid(row=1, column=1, sticky='e', cnf=self.master.conf)

        # ============================ Edit Frame
        self.inst_label = tk.Label(
            master=self.edit_frame,
            text='Название института',
            font='Helvetica 11',
            padx=10,
        )
        self.inst_entry = tk.Entry(master=self.edit_frame)
        self.inst_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.inst_entry.grid(row=0, column=1, sticky='e', padx=10, pady=10)

        self.dep_label = tk.Label(
            master=self.edit_frame, text='Название кафедры', font='Helvetica 11', padx=10
        )
        self.dep_entry = tk.Entry(master=self.edit_frame)
        self.dep_label.grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.dep_entry.grid(row=1, column=1, sticky='e', padx=10, pady=10)

        # ============================ Table Frame
        heads = ['id', 'Имя', 'Фамилия', 'Отчество', 'Номер телефона', 'Институт']

        self.table = ttk.Treeview(master=self.table_frame, show='headings')
        self.table['columns'] = heads
        for header in heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center')

        for row in self.table_content:
            self.table.insert('', 'end', values=row)

        self.table.pack()