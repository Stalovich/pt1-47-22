"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


str_in = input('Введите строку:').replace(' ', '')
s_new = []
for i in str_in:
    if i not in s_new:
        s_new.append(i)
print('Уникальные символы в строке следующие:', ''.join(s_new))




