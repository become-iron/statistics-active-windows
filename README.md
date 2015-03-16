# Сбор статистики по активным окнам
Скрипт подсчитывает, как долго было активно окно. По окончанию выводится диаграмма, а также сохраняется её копия в корневой папке
![](https://github.com/become-iron/statistics-active-windows/blob/master/plot.png)

Для работы скрипта необходимы модули [win32gui](http://sourceforge.net/projects/pywin32/files/pywin32/) и [numpy](http://sourceforge.net/projects/numpy/files/NumPy)

Для работы скрипта нужно открыть файл **checking_active_window.pyw**. Он запустится в фоновом режиме и начнёт собирать статистику. Статистика записывается в файл **statistic.txt**. Для построения графика необходимо "убить" процесс со скриптом через Диспетчер задач, затем запустить файл **plot.py**.

##TODO LIST
* Лучшая работа с программами
* Получение названий процессов для лучшей работы
* Лучший вывод графика