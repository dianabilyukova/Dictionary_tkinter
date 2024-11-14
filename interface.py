import tkinter as tk
from tkinter import messagebox, simpledialog
from dictionary import Dictionary  # предполагается, что класс Dictionary сохранен в файле dictionary.py

class DictionaryApp:
    def __init__(self, master):                   # конструктор класса, который принимает объект master как аргумент
        self.master = master                      # сохраняем ссылку на гласный (root) объект Tkinter
        self.master.title("Defining Dictionaries App")  # устанавливаем заголовок окна

        self.current_dict = None        # текущий словарь будет храниться в этой переменной,
                                        # которая будет инициализирована в методе create_dictionary()
        # метка для выбора языка
        self.language_label = tk.Label(master, text="Language:", font=("Arial", 22), fg="blue")
        self.language_label.pack()      # размещаем метку в окне

        self.language_entry = tk.Entry(master)  # поле для ввода языка
        self.language_entry.pack()             # размещаем поле ввода в окне

        self.create_button = tk.Button(master, text="Create Dictionary",
                                       command=self.create_dictionary,
                                       font=("Arial", 18), fg="purple")  # кнопка для создания словаря
        self.create_button.pack()             # размещаем кнопку в окне

           # другие кнопки, которые будут активны после создания словаря
        self.add_word_button = tk.Button(master, text="Add Word",
                                         command=self.add_word, state=tk.DISABLED,
                                         font=("Arial", 18), fg="green")    # кнопка для добавления слова
        self.add_word_button.pack()                                          # размещаем кнопку в окне

        self.replace_word_button = tk.Button(master, text="Replace Word",
                                             command=self.replace_word, state=tk.DISABLED,
                                             font=("Arial", 18), fg="green")    # кнопка для замены слова
        self.replace_word_button.pack()                                       # размещаем кнопку в окне

        self.delete_word_button = tk.Button(master, text="Delete Word",
                                            command=self.delete_word, state=tk.DISABLED,
                                            font=("Arial", 18), fg="green")    # кнопка для удаления слова
        self.delete_word_button.pack()                                       # размещаем кнопку в окне

        self.search_word_button = tk.Button(master, text="Search Definition",
                                            command=self.search_definition, state=tk.DISABLED,
                                            font=("Arial", 18), fg="green")    # кнопка для поиска определения
        self.search_word_button.pack()                                       # размещаем кнопку в окне

        self.export_word_button = tk.Button(master, text="Export Word",
                                            command=self.export_word, state=tk.DISABLED,
                                            font=("Arial", 18), fg="green")    # кнопка для экспорта слова
        self.export_word_button.pack()                                       # размещаем кнопку в окне

    def create_dictionary(self):         # метод create_dictionary() создает словарь для выбранного языка
        lang = self.language_entry.get()    # получаем выбранный язык
        if lang:                           # если язык не пустой
            self.current_dict = Dictionary(lang)        # создаем словарь для выбранного языка
            messagebox.showinfo("Success", f"Dictionary for {lang} created!")    # выводим сообщение о создании словаря
            # активируем кнопки после создания словаря
            self.add_word_button.config(state=tk.NORMAL)
            self.replace_word_button.config(state=tk.NORMAL)
            self.delete_word_button.config(state=tk.NORMAL)
            self.search_word_button.config(state=tk.NORMAL)
            self.export_word_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Warning", "Please enter a language.")  # предупреждаем, если язык не введен

    def add_word(self):                 # метод add_word() добавляет слово и его определение в словарь
        word = simpledialog.askstring("Input", "Enter word:")    # получаем слово из пользователя
        definition = simpledialog.askstring("Input", "Enter definition:")    # получаем определение из пользователя
        if word and definition:         # если слово и определение не пустые
            self.current_dict.add_word(word, definition)    # добавляем слово и его определение в словарь
            messagebox.showinfo("Success", f"Added: {word} -> {definition}")    # выводим сообщение о добавлении слова

    def replace_word(self):             # метод replace_word() заменяет первое определение слова на новое
        word = simpledialog.askstring("Input", "Enter word to replace:")    # получаем слово из пользователя
        new_definition = simpledialog.askstring("Input", "Enter new definition:")    # получаем новое определение из пользователя
        if word and new_definition:      # если слово и новое определение не пустые
            self.current_dict.replace_word(word, new_definition)
            messagebox.showinfo("Success", f"Replaced definition for: {word}")  # выводим сообщение о замене определения

    def delete_word(self):              # метод delete_word() удаляет слово из словаря
        word = simpledialog.askstring("Input", "Enter word to delete:")    # получаем слово из пользователя
        if word:                         # если слово не пустое
            self.current_dict.delete_word(word)    # удаляем слово из словаря
            messagebox.showinfo("Success", f"Deleted: {word}")    # выводим сообщение об удалении слова

    def search_definition(self):        # метод search_definition() возвращает определения слова
        word = simpledialog.askstring("Input", "Enter word to search:")    # получаем слово из пользователя
        if word:
            definitions = self.current_dict.search_definition(word)        # поиск определения слова
            if definitions:     # если определения найдены
                messagebox.showinfo("Definition", f"{word}: {', '.join(definitions)}") # выводим сообщение о найденных определениях
            else:
                messagebox.showinfo("Not Found", f"No definitions found for: {word}") # выводим сообщение о ненайденных определениях

    def export_word(self):              # метод export_word() экспортирует слово и его определения в отдельный файл.txt
        word = simpledialog.askstring("Input", "Enter word to export:")    # получаем слово из пользователя
        if word:
            self.current_dict.export_word(word)    # экспортируем слово и его определения в отдельный файл.txt
            messagebox.showinfo("Success", f"Exported: {word} to {word}.txt")    # выводим сообщение об экспорте слова

