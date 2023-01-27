import tkinter as tk
import tkinter.messagebox
from login_form import Main

font = ('Aerial Bold', 30)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(text='Login', font=font,
                             command=self.open_login)
        self.btn.pack(pady=20, padx=50)
        self.open_login()

    def open_login(self):
        login_form = Main(self)
        post = login_form.open()
        if post:
            print("Login Complete!")
        else:
            tk.messagebox.showerror(title='Login not complete',
                                 message='Не верный логи или пароль')
            self.open_login()

if __name__ == "__main__":
    root = MainWindow()
    root.title("База Данных")
    root.mainloop()
