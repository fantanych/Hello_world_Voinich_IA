researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
experiment_conclusion = input("Введите вывод по эксперименту: ")
report = f"+--------------------------------------------------+\n| Электронный лабораторный журнал                  |\n+--------------------------------------------------+\n| ФИО исследователя : {researcher_name}         |\n| Дата             : {experiment_date}                    |\n| Эксперимент      : {experiment_name}     |\n+--------------------------------------------------+\n| Вывод:   {experiment_conclusion}  |                                      \n+--------------------------------------------------+"
print(report)
with open("journal.txt", "w", encoding="utf-8") as file:
        file.write(report)
print("\nДанные успешно сохранены в journal.txt")