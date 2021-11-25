from tkinter import *
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class login_window:
    def __init__(self, main):
        self.canvas = Canvas(
            main,
            bg="#1E507E",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            380.0, 5.684341886080802e-14, 762.0, 600.0, fill="#FFFFFF", outline=""
        )
    
        self.entry_image_1 = PhotoImage(file=relative_to_assets("password_entry.png"))
        self.entry_bg_1 = self.canvas.create_image(567.5, 333.99999999999994, image=self.entry_image_1)
        self.entry_1 = Entry(show='*', bd=0, bg="#F1F1F1", highlightthickness=0)
        self.entry_1.place(x=414.0, y=311.99999999999994 + 17, width=307.0, height=25.0)
    
        self.canvas.create_text(
            430.0,
            309.99999999999994,
            anchor="nw",
            text="Пароль",
            fill="#000000",
            font=("OpenSans Regular", 18 * -1),
        )
    
        self.canvas.create_text(
            387.0,
            158.99999999999994,
            anchor="nw",
            text="Введите данные для входа",
            fill="#000000",
            font=("OpenSans Light", 24 * -1),
        )
    
        self.entry_image_2 = PhotoImage(file=relative_to_assets("login_entry.png"))
        self.entry_bg_2 = self.canvas.create_image(567.5, 243.99999999999994, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#F1F1F1", highlightthickness=0)
        self.entry_2.place(x=414.0, y=221.99999999999994 + 17, width=307.0, height=25.0)
    
        self.canvas.create_text(
            430.0,
            219.99999999999994,
            anchor="nw",
            text="Логин",
            fill="#000000",
            font=("OpenSans Regular", 18 * -1),
        )
    
        self.button_image_1 = PhotoImage(file=relative_to_assets("login_button.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(self.entry_1.get()),
            relief="flat",
        )
        self.button_1.place(
            x=479.2112731933594, y=401.99999999999994, width=174.78872680664062, height=38.0
        )
    
        self.canvas.create_text(
            24.99999999999997,
            5.999999999999943,
            anchor="nw",
            text="Информационная система",
            fill="#F4F4F4",
            font=("OpenSans Regular", 24 * -1),
        )
    
        self.canvas.create_text(
            26.99999999999997,
            45.99999999999994,
            anchor="nw",
            text="“Отдел сотрудников университета” ",
            fill="#F4F4F4",
            font=("OpenSans Regular", 18 * -1),
        )
    