operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")
log_entry = f"{operator_name}\t\t{pressure_value}"
with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write("ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    file.write(log_entry)
print("Данные успешно сохранены в sensor_log.txt")  