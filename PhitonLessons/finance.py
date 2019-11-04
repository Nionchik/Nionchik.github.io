import tkinter as tk
from tkinter import ttk
# from module import *

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg="#d7d8e0", bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="add.gif")
        btn_open_dialog = tk.Button(toolbar, text="Добавить позицию", command=self.open_dialog, bg="#d7d8e0", bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=("ID", "description", "costs", "total"), height=15, show="headings")

        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("description", width=365, anchor=tk.CENTER)
        self.tree.column("costs", width=150, anchor=tk.CENTER)
        self.tree.column("total", width=100, anchor=tk.CENTER)

        self.tree.heading("ID", text="ID")
        self.tree.heading("description", text="Наименование")
        self.tree.heading("costs", text="Статья дохода\расхода")
        self.tree.heading("total", text="Сумма")

        self.tree.pack()

    def open_dialog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Добавить доходы\расходы")
        self.geometry("400x220+400+300")
        self.resizable(False, False)

        lable_descriptions = tk.Label(self, text="Наименование:")
        lable_descriptions.place(x=50, y=50)
        lable_select = tk.Label(self, text="Статья дохода\расхода:")
        lable_select.place(x=50, y=80)
        lable_sum = tk.Label(self, text="Сумма:")
        lable_sum.place(x=50, y=110)

        self.entry_descriptions = ttk.Entry(self)
        self.entry_descriptions.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=[u"Доход", u"Расход"])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)


        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Семейный бюджет за месяц')
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()