#  coding=utf-8
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'arial'  # выбор семейства шрифтов, поддержающего кириллицу
windows = None  # словарь

try:
    with open('statistics.txt', 'r') as file:
        contentFile = file.read()
        file.close()
    windows = eval(contentFile)
except SyntaxError:
    input('Файл пуст')
    exit()
except FileNotFoundError:
    input('Файл отсутствует')
    exit()

# ПОДГОТОВКА СЛОВАРЯ
windows.pop(0)  # удаление из словаря элемента с ключом '0'
keys = list(windows.keys())  # список ключей из словаря

# ИЗВЛЕЧЕНИЕ ДАННЫХ ДЛЯ ПОСТРОЕНИЯ
finalName = []  # список с именами окон
finalTime = []  # список со временем активности окон
for keys in windows:
    finalTime += [int((str(windows[keys][0]/1).split('.'))[0])]
    finalName += [windows[keys][1]]

# ПОСТРОЕНИЕ ГРАФИКА
plt.pie(finalTime, labels=finalName, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.savefig('plot.png')
plt.show()
