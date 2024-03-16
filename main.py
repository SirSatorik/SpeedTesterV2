#Импорт библиотек
from tkinter import *
from speedtest import Speedtest
import threading as th
import webbrowser as wb

#Измерение скорости
def button():
        global warningLabel
        warningLabel = Label(window, text='We are measuring speed,please wait...', font=35)
        warningLabel.pack(side=BOTTOM, pady=40)
        trapAsync = th.Thread(target=asyncButton)
        trapAsync.start()

#Ассинхронная функция
def asyncButton():
    global warningLabel
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    #Изменение текста
    download_lable.config(text='Download speed:\n' + str(download_speed) + 'MbPs')
    upload_lable.config(text='Upload speed:\n' + str(upload_speed) + 'MbPs')

    #Удаление предупреждения (неработает)
    warningLabel.event_delete()

#Кнопка перехода на исходный код (если будете удалять эту кнопку то удалите 5 строку тоже)
def sourceButton():
    wb.open('https://github.com/SirSatorik/SpeedTesterV2')

#Основная часть
window = Tk()
#Иконка (Убрать хештег только если в папке с exe есть иконка с названием app в формате .ico)
#window.iconbitmap(r'app.ico')
#Название
window.title('SpeedTester')
#Размер окна
window.geometry('300x400')

#Создание кнопки
button = Button(window, text='Start', font=40, command=button)
button.pack(side=BOTTOM, pady=40)

#Кнопка отправляющая на исходник
button = Button(window, text='Source', font=40, command=sourceButton)
button.pack(side=BOTTOM, pady=30)

#Создание текста
download_lable = Label(window, text='Download speed:\n-', font=35)
download_lable.pack(pady=(50, 0))
upload_lable = Label(window, text='Upload speed:\n-', font=35)
upload_lable.pack(pady=(10, 0))

window.mainloop()
