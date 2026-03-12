print("=== Определение среды по значению pH ===")
print("pH может принимать значения от 0 до 14")
ph_value = float(input("Введите значение pH: "))
if ph_value < 0 or ph_value > 14:
            print("Ошибка: pH должен находиться в диапазоне от 0 до 14!")
if ph_value < 7:
            print(f"pH = {ph_value} - это КИСЛАЯ среда")
elif ph_value == 7:
            print(f"pH = {ph_value} - это НЕЙТРАЛЬНАЯ среда")
else:  # ph_value > 7
            print(f"pH = {ph_value} - это ЩЕЛОЧНАЯ среда")            

