volume = float(input("Введите объём раствора(мл): "))
salt_mass = volume * 0.009
salt_mass_rounded = round(salt_mass, 2)
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {salt_mass_rounded} г\n")
    file.write(f"Объем воды:  {volume} мл\n")
    print("Рецепт успешно сохранен в файл recipe.txt")