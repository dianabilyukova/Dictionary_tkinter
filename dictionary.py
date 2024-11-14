import json                         # модуль для работы с данным форматом
import os                           # модуль для работы с операционной системой, в частности для проверки наличия файла
# some changes

class Dictionary:                    # определяем класс Dictionary, который будет содержать всю информацию о словаре
    def __init__(self, language):                             # конструктор класса, который принимает язык в качестве аргумента
        self.language = language                              # запоминаем язык в качестве атрибута класса
        self.words = {}                                        # создаем словарь для хранения слов и их описаний
        self.filename = f"{language.lower()}_dictionary.json"  # формируем название файла, в котором будет храниться
                                                               # словарь, с использованием переданного языка
                                                               # и создаем имя файла словаря в нижнем регистре
        self.load()                         # вызываем метод, чтобы загрузить существующее содержимое словаря из файла

    def load(self):                                             # Метод для загрузки словаря из файла
        """Загружает словарь из файла."""
        if os.path.exists(self.filename):                       # проверяем, существует ли файл, если файл существует
            with open(self.filename, 'r', encoding='utf-8') as file:        # открываем его для чтения
                try:
                    self.words = json.load(file)        # используем json.load() для загрузки данных из файла self.words
                except json.JSONDecodeError:                       # проверяем, пришла ли ошибка при декодировании json
                    print("Error with loading of dictionary")        # выводим сообщение об ошибке
                    self.words = {}                                 # если ошибка, сохраняем пустой словарь

    def save(self):                             # Метод save()  сохраняет текущее состояние словаря в self.words в файл
        """Сохраняет словарь в файл."""
        with open(self.filename, 'w', encoding='utf-8') as file:    # открываем файл для записи и используем json.dump()
            json.dump(self.words, file, ensure_ascii=False)         # для записи словаря в JSON-файл.
                                                                    # Указываем параметр ensure_ascii=False,
                                 # он позволяет сохранять символы в оригинальном формате, без преобразования в ASCII

    def add_word(self, word, definition):               # метод add_word() добавляет слово и его определение в словарь
        """Добавляет слово и его определение в словарь."""
        if word in self.words:                                   # проверяем, если слово уже есть в словаре
            self.words[word].append(definition)                  # добавляем новое определение к списку
        else:
            self.words[word] = [definition]                      # если нет, создаем новый список с первым определением
        self.save()                                              # в конце вызываем метод save() для сохранения изменений

    def replace_word(self, word, new_definition):      # метод replace_word() заменяет первое определение слова на новое
        """Заменяет определение слова."""
        if word in self.words and self.words[word]:         # проверяем, если слово есть в словаре и есть определение
            self.words[word][0] = new_definition                # заменяем первое определение слова на новое
            self.save()                                          # вызываем метод save() для сохранения изменений

    def delete_word(self, word):                                       # метод delete_word() удаляет слово из словаря
        """Удаляет слово и все его определения из словаря."""
        if word in self.words:                                          # если оно есть
            del self.words[word]
            self.save()                                                 # и сохраняет изменения

    def search_definition(self, word):                         # метод search_definition() возвращает определения слова
        """Ищет определения слова."""                               # если слово есть в словаре
        return self.words.get(word, None)                          # возвращает None, если слово не найдено

    def export_word(self, word):         # метод export_word() экспортирует слово и его определения в отдельный файл.txt
        """Экспортирует слово и его определения в отдельный файл."""
        current_directory = os.getcwd()     # получаем текущий каталог
        with open(f"{word}.txt", 'w', encoding='utf-8') as file:    # создаем и открываем файл с именем слова
            if word in self.words:                                   # если слово есть в словаре
                for definition in self.words[word]:                  # перебираем все определения слова
                    file.write(f"{word}: {definition}\n")             # записываем слово и его определение в файл

        print(f"File saved in:{current_directory}/{word}.txt")     # выводим сообщение о сохранении файла, включая путь
