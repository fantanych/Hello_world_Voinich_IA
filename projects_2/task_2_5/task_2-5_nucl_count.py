print("=== Анализ последовательности ДНК ===")
dna = input("Введите последовательность ДНК: ")
upper_seq = dna.upper()
count_A = upper_seq.count("A")
count_T = upper_seq.count("T")
count_G = upper_seq.count("G")
count_C = upper_seq.count("C")
print("Последовательность в верхнем регистре:", upper_seq)
print("Подсчёт нуклеотидов: ")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")
total_length = len(dna)
print(f"Общая длина: {total_length}")
if total_length > 0:
        percent_a = (count_A / total_length) * 100
        percent_t = (count_T / total_length) * 100
        percent_g = (count_G / total_length) * 100
        percent_c = (count_C / total_length) * 100
else:
        percent_a = percent_t = percent_g = percent_c = 0
print("Процентное содержание:")
print("А: ", percent_a, "%")
print("T: ", percent_t, "%")
print("G: ", percent_g, "%")
print("C: ", percent_c, "%")