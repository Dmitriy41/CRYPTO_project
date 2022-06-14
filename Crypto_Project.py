import pyAesCrypt
import os
from pyfiglet import  Figlet
def func_shipher(file_name, password):
    buffer_size = 5012*1024
    shipher_file = pyAesCrypt.encryptFile(

        str(file_name),
        str(file_name)+'.crp',
        password,
        buffer_size
    )

    print("Файл "+os.path.splitext(file_name)[0]+" зашифрован")

    os.remove(file_name)
def deshipher(file_name, password):
    bufer_size = 512*1024
    deshipher_file = pyAesCrypt.decryptFile(

        str(file_name),
        str(os.path.splitext(file_name)[0]),
        password,
        bufer_size
    )
    print("ФАЙЛ-"+os.path.splitext(file_name)[0]+" Дешифрован")




previev = Figlet(font="slant")
print(previev.renderText("Crypto_____Project" ))
print('''Developed by KODEL_ite''')

flag = '0'
while flag!='3':
    print("Выберите действие: 1-Зашифровать, 2 - расшифровать")
    a = input()
    if a=='1':
        print("Введите пароль для шифрования")
        pas = input()
        print("Введите имя файла, который необходимо зашифровать")
        name = input()
        func_shipher(file_name=name, password=pas)

    if a=='2':
        print("Введите пароль для ДЕшифрования")
        pas = input()
        print("Введите имя файла, который необходимо ДЕшифровать")
        name = input()
        deshipher(file_name=name, password=pas)

    print('''
    
        Чтобы начать заново нажмите любую клавишу
        Чтобы выйти нажмите клавишу 3''')



