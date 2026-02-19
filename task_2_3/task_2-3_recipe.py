sreda_name = input ("Введите название питательной среды: ")
konc_agar = input ("Введите концентрацию агара (%): ")
temp_sterilize = input ("Введите температуру стерилизации (°C): ")
report = f"Питательная среда: {sreda_name}\nКонцентрация агара (%): {konc_agar}\nТемпература стерилизации (°C): {temp_sterilize}"
print(report)
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(report)
    print ('Файл "recipe.txt" успешно сформирован!')