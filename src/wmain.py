from tkinter import *
import window_manager as wm


def main():

    root = Tk()
    root.title("Информационная система")
    root.geometry("800x600")
    root.configure(bg = "#1E507E")


    w = wm.login_window(root)


    root.mainloop()


if __name__ == "__main__":
    main()