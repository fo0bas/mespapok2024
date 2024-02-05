import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime, timedelta

class FolderCreatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Создание папок от f0bas")
        self.master.resizable(False, False)  # Запрет изменения размера окна

        self.years = list(range(2024, 2036))
        self.months = self.generate_months()

        self.folder_path = tk.StringVar()
        self.selected_month = tk.StringVar(value=self.months[0])
        self.selected_year = tk.IntVar(value=self.years[0])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Выбрать папку:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.folder_path, state="readonly").grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.master, text="Обзор", command=self.browse_folder).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(self.master, text="Выберите год:").grid(row=1, column=0, padx=10, pady=10)
        tk.OptionMenu(self.master, self.selected_year, *self.years).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Выберите месяц:").grid(row=2, column=0, padx=10, pady=10)
        tk.OptionMenu(self.master, self.selected_month, *self.months).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.master, text="Создать папки", command=self.create_folders).grid(row=3, column=0, columnspan=3, pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def generate_months(self):
        return [
            'Январь', 'Февраль', 'Март', 'Апрель',
            'Май', 'Июнь', 'Июль', 'Август',
            'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        ]

    def create_folders(self):
        selected_month = self.selected_month.get()
        selected_year = self.selected_year.get()

        if not selected_month:
            tk.messagebox.showwarning("Предупреждение", "Выберите месяц.")
            return

        base_folder = self.folder_path.get()
        if not base_folder:
            tk.messagebox.showwarning("Предупреждение", "Выберите папку для создания месяцев.")
            return

        # Преобразуем месяц в число (1 - 12)
        month_number = self.generate_months().index(selected_month) + 1

        days_in_month = (datetime(selected_year, month_number, 28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

        for day in range(1, days_in_month.day + 1):
            day_datetime = datetime(selected_year, month_number, day)
            day_folder_name = day_datetime.strftime("%d.%m.%Y")
            day_folder_path = os.path.join(base_folder, day_folder_name)

            try:
                os.makedirs(day_folder_path)
            except FileExistsError:
                tk.messagebox.showwarning("Предупреждение", f"Папка {day_folder_name} уже существует.")

        tk.messagebox.showinfo("Информация", "Папки успешно созданы.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderCreatorApp(root)
    root.mainloop()
