import os
import sys
import requests
import psutil

print("Запущен апдейтер скрипта matrp-help-supporter")

print("Проверяем, запущен ли процесс скрипта")

for proc in psutil.process_iter():
    name = proc.name()
    if name == "matrp-help-supporter.exe":
        os.kill(proc.pid)

print("Проверяем, существует ли файл скрипта")

if (os.path.exists(os.getcwd() + "\\matrp-help-supporter.exe") and os.path.isfile(os.getcwd() + "\\matrp-help-supporter.exe")):
    os.remove(os.getcwd() + "\\matrp-help-supporter.exe")

print("Начало скачивания файла скрипта")

response = requests.get("https://dl.klysrvs.ml/api/matrp/matrp-help-supporter/matrp-help-supporter.exe", stream=True)
open(os.getcwd() + "matrp-help-supporter.exe", "wb").write(response.content)

os.startfile(os.getcwd() + "\\matrp-help-supporter.exe")

exit(-1)