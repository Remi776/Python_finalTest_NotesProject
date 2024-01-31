import Python_finalTest_NotesProject.UI.menuTemplates as m


def menu_console():
    m.printMenuTitle("Главное меню\n           ЖУРНАЛ ЗАМЕТОК")
    print("1 - вывод журнала \n"
          "2 - вывод заметки по id \n"
          "3 - выбор заметки по дате\n"
          "4 - редактирование заметки"
          " \n5 - добавление заметки\n"
          "6 - удаление заметки\n"
          "7 - выход")
    m.printMenuLine()
    print("\n введите пункт из меню ")
