import tkinter as tk    # импортируем модуль tkinter, чтобы создать окно и кнопки
from interface import DictionaryApp    # импортируем класс DictionaryApp, который будет содержать всю информацию о приложении

def main():    # функция main() создает окно и класс DictionaryApp
    root = tk.Tk()    # создаем окно
    app = DictionaryApp(root)    # создаем класс DictionaryApp и передаем ему окно
    root.mainloop()    # запускаем главный цикл приложения

if __name__ == "__main__":    # если этот файл выполняется как скрипт, то запускаем функцию main()
    main()    # запускаем функцию main()

