import unittest    # импортируем модуль unittest, который позволяет создавать тесты
import os
import json
from dictionary import Dictionary  # предполагается, что класс Dictionary сохранен в файле dictionary.py


class TestDictionary(unittest.TestCase):    # определяем тестовую среду Dictionary
    # это значит, что класс будет представлять собой набор тестов для Dictionary

    def setUp(self):    # метод setUp() настраивает тестовую среду
        """Здесь мы настраиваем тестовую среду."""
        self.test_language = "Test"       # тестовый язык
        self.dictionary = Dictionary(self.test_language)   # создаем экземпляр класса Dictionary с переданным языком
        self.test_word = "apple"         # тестовое слово
        self.test_definition = "A fruit that grows on trees." # тестовое определение слова
        self.dictionary.filename = "test_dictionary.json"  # путь к файлу для тестов, чтобы не перезаписывать словарь при каждом тесте

    def tearDown(self):  # ето метод tearDown(), который вызывается после каждого теста
        """Здесь мы очищаем ресурсы."""
        if os.path.exists(self.dictionary.filename): # если файл существует
            os.remove(self.dictionary.filename)  # удаляем файл после тестов

    def test_add_word(self):
        """Проверяет, можно ли добавить слово и его определение."""
        self.dictionary.add_word(self.test_word, self.test_definition)  # добавляем слово и его определение
        self.assertIn(self.test_word, self.dictionary.words)  # проверяем, что слово добавлено
        self.assertEqual(self.dictionary.words[self.test_word], [self.test_definition])     # проверяем, что определение слова добавлено

    def test_replace_word(self):
        """Проверяет, можно ли заменить определение слова."""
        new_definition = "A new definition for apple."     # новое определение слова
        self.dictionary.add_word(self.test_word, self.test_definition)  # добавляем слово и его определение
        self.dictionary.replace_word(self.test_word, new_definition)        # заменяем определение слова
        self.assertEqual(self.dictionary.words[self.test_word][0], new_definition)  # проверяем, что определение слова заменено

    def test_delete_word(self):
        """Проверяет, что удаление слова работает корректно."""
        self.dictionary.add_word(self.test_word, self.test_definition)  # добавляем слово и его определение
        self.dictionary.delete_word(self.test_word)        # удаляем слово
        self.assertNotIn(self.test_word, self.dictionary.words)  # проверяем, что слово удалено

    def test_search_definition(self):
        """Проверяет, что поиск определения слова работает корректно."""
        self.dictionary.add_word(self.test_word, self.test_definition)        # добавляем слово и его определение
        definition = self.dictionary.search_definition(self.test_word)        # поиск определения слова
        self.assertEqual(definition, [self.test_definition])        # проверяем, что определение слова найдено

    def test_save_and_load(self):
        """Проверяет, что сохранение и загрузка словаря работает корректно."""
        self.dictionary.add_word(self.test_word, self.test_definition)        # добавляем слово и его определение
        self.dictionary.save()        # сохраняем словарь

        # Создаем новый экземпляр класса Dictionary и загружаем данные из файла
        new_dictionary = Dictionary(self.test_language)         # создаем новый экземпляр класса Dictionary
        new_dictionary.filename = self.dictionary.filename      # используем те же файлы для загрузки
        new_dictionary.load()                                    # загружаем данные из файла

        self.assertIn(self.test_word, new_dictionary.words)      # проверяем, что слово и его определение загружены
        self.assertEqual(new_dictionary.words[self.test_word], [self.test_definition])  # проверяем, что определение слова загружено

    def test_export_word(self):
        """Проверяет, что экспорт слова и его определения работает корректно."""
        self.dictionary.add_word(self.test_word, self.test_definition)        # добавляем слово и его определение
        self.dictionary.export_word(self.test_word)        # экспортируем слово и его определение

        # Проверяем, что файл был создан и содержит правильный контент
        with open(f"{self.test_word}.txt", 'r', encoding='utf-8') as file:        # открываем файл
            content = file.read()

        self.assertEqual(content.strip(), f"{self.test_word}: {self.test_definition}")
        # проверяем, что контент файла соответствует определению слова

        # Очищаем экспортированный файл
        if os.path.exists(f"{self.test_word}.txt"):
            os.remove(f"{self.test_word}.txt")


if __name__ == '__main__':
    unittest.main()
