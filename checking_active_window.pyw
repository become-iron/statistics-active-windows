#  coding=utf-8

from win32gui import GetWindowText, GetForegroundWindow
from time import sleep, time

windows = {}  # {descriptor: [total work time, window name]}
names = '', 'Пуск', 'ACMON', 'Program Manager'
descWin = GetForegroundWindow()  # декскриптор последнего активного окна
pause = 30  # пауза между получением дескрипторов
shareFile = 'statistics.txt'  # файл обмена

# очистка файла обмена или его создание в случае отсутствия
with open(shareFile, 'w') as file:
    file.close()
while True:
    '''
    descWinTemp - локальная переменная для временного хранения дескриптора активного окна
    '''
    descWinTemp = GetForegroundWindow()  # получаем дескриптор активного окна
    timeWinTemp = time()
    sleep(pause)
    if GetWindowText(descWinTemp) in names:  # если окно имеет имя из списка
        continue
    if descWinTemp not in windows:  # если нет ключа 'дескриптор_активного_окна' в словаре, создаём его
        windows.update({descWinTemp: [0, GetWindowText(descWinTemp)]})
    if descWin == descWinTemp:  # если дескр. посл. активн. окна равен дискр. обраб-го окна
        windows[descWinTemp][0] = windows[descWinTemp][0] + time() - timeWinTemp
        descWin = descWinTemp
    else:
        descWin = GetForegroundWindow()

    # считывание словаря в текстовом файле
    with open(shareFile, 'r') as file:
        fileContent = file.read()
        if fileContent not in ['', None]:
            fileContent = eval(fileContent)
        else:
            fileContent = {0: 0}
        file.close()
    # обновить словарь и записать в файл
    with open(shareFile, 'w') as file:
        fileContent.update(windows)
        file.write(str(fileContent))
        file.close()
