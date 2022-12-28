import tkinter as tk
from api.resolvers import check_login


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.font = ('Aerial Bold', 20)

        lbl_main = tk.Label(self, text='Вход', font=self.font)
        lbl_login = tk.Label(self, text='Логин', font=self.font)
        lbl_password = tk.Label(self, text='Пароль', font=self.font)
        entry_login = tk.Entry(self, font=self.font, textvariable=self.username)
        entry_password = tk.Entry(self, font=self.font, textvariable=self.password)
        btn_enter = tk.Button(self, text='Вход', font=self.font)
        btn_close = tk.Button(self, text='Отмена', font=self.font)

        lbl_main.grid(row=0, column=1)
        lbl_login.grid(row=1, column=0)
        entry_login.grid(row=1, column=1,)
        lbl_password.grid(row=2, column=0)
        entry_password.grid(row=2, column=1)
        btn_enter.grid(row=3, column=1)
        btn_close.grid(row=3, column=1)
        btn_close.grid(row=3, column=2)

    def open(self):
        self.grab_set()
        self.wait_window()
        post = check_login(login=self.username.get(),
                           password=self.userpassword.get())
        return post