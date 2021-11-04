import os
import sys
import shutil

path = "/Users/mayazorihina/Desktop/Testing"
path_for_guest = "/Users/mayazorihina/Desktop/Testing/Guest"
path_home = "/Users/mayazorihina/Desktop/Testing"


def makeDir():  # Создает папку
    name = input('Введите имя папки - ')
    os.mkdir(path + '/' + name)
    print('make dir - ' + path + '/' + name)
    print('Вы успешно создали папку - ' + name)


def exit():  # Системный выход
    sys.exit()


def removeDir():  # Удаление папки
    name = input('Введите имя папки - ')
    os.rmdir(path + '/' + name)
    print('remove dir - ' + path + '/' + name)
    print('Указанная папка ' + name + ' успешно удалена')


def changeDir():  # переход в указанную папку
    name = input('Введите dir, куда хотите попасть - ')
    os.chdir(name)
    print('Вы были успешно перемещены в папку - ', name)


def whoDir():  # текущая папка
    print('Текущая dir - ', os.getcwd())


def create_file():  # создать файл
    name = input('Введите имя файла, который хотите создать - ')
    question = input('Хотите создать ' + 'пустой' + ' файл или файл на ' + 'запись - ')
    if question == 'пустой':
        new_file1 = open(name + ".txt", "w")
    elif question == 'запись':
        new_file2 = open(name + ".txt", "w+")
        quest = input('Что хотите ввести?')
        new_file2.write(quest)
        new_file2.close()
    print('Вы успешно создали файл - ', name + '.txt')


def readFile():  # просмотреть содержимое текстового файла
    name = input('Введите имя файла, который хотите прочитать - ')
    read_file = open(name + ".txt", "r")
    print(*read_file)


def remFile():  # удалить файл
    name = input('Введите файл, который хотите удалить - ')
    path_for_remFile = "C:/Users/даниэль/For_test"
    os.remove(path_for_remFile + '/' + name + '.txt')
    print('Файл ' + name + ' успешно удален')


def movFile():  # переместить файл
    quest1 = input('Введите файл, который хотите переместить - ')
    quest2 = input('Введите папку, куда хотите переместить файл - ')
    os.replace(quest1 + '.txt', quest2 + '/' + quest1)
    print('Файл ' + quest1 + ' успешно перемещен в папку ' + quest2)


def copyFile():  # копировать файл
    quest1 = input('Введите файл, который хотите скопировать - ')
    quest2 = input('Введите папку, куда хотите перенести файл - ')
    shutil.copy(quest1 + '.txt', quest2)
    print('Файл ' + quest1 + ' успешно скопирован в папку ' + quest2)


def renameFile():  # переим-ть файл
    quest1 = input('Введите файл, который хотите переименовать - ')
    quest2 = input('Введите новое название файла - ')
    os.rename(quest1 + '.txt', quest2 + '.txt')
    print('Вы сменили название файла ' + quest1 + ' на ' + quest2)


def registration():  # регистация пользователя
    name_regist = input('Как вас зовут? - ')
    os.mkdir(path_for_guest + '/' + name_regist)
    guestDir = (path_for_guest + '/' + name_regist)
    print(guestDir)
    shutil.copy("C:/Users/даниэль/For_test/manual" + '.txt', guestDir)
    os.chdir(guestDir)
    about_you = open(name_regist + '.txt', "w")
    quest_for_guest = input('Что хотите ввести? ')
    about_you.write(quest_for_guest)
    about_you.close()
    print('Для вас создана папка ' + name_regist + ' - ')


def homeDir():  # домашняя папка
    os.chdir(path_home)
    print('Вы вернулись в домашнюю папку ')
    print('Ваше текущее расположение - ' + path_home)


def guestDir():  # папка пользователей
    os.chdir(path_for_guest)
    print('Вы попали в папку пользователей ')
    print('Ваше текущее расположение - ' + path_for_guest)


def guestRemDir():  # удаляется папка гостя
    name = input('Введите имя папки - ')
    os.rmdir(path_for_guest + '/' + name)
    print('remove dir - ' + path + '/' + name)
    print('Указанная папка ' + name + ' успешно удалена')


def start_command():
    print('1' + '. Создать папку ')
    print('2' + '. Системный выход ')
    print('3' + '. Удалить папку ')
    print('4' + '. Переместить пользователя в указанную папку ')
    print('5' + '. Текущая папка ')
    print('6' + '. Создать файл ')
    print('7' + '. Просмотреть содержимое текстового файла ')
    print('8' + '. Удалить файл ')
    print('9' + '. Переместить файл ')
    print('10' + '. Скопировать файл ')
    print('11' + '. Переименовать файл ')
    print('12' + '. Регистрация пользователя ')
    print('13' + '. Удалить папку пользователя ')
    print()
    print('home' + ' Вернуться в домашнюю папку ')
    print('guest' + ' Перейти в папку пользователей ')
    print()
    print()


start_command()

command = input('Введите команду - ')

if command == '2':
    exit()
elif command == '1':
    makeDir()
elif command == '3':
    removeDir()
elif command == '4':
    changeDir()
elif command == '5':
    whoDir()
elif command == '6':
    create_file()
elif command == '7':
    readFile()
elif command == '8':
    remFile()
elif command == '9':
    movFile()
elif command == '10':
    copyFile()
elif command == '11':
    renameFile()
elif command == '12':
    registration()
elif command == '13':
    guestRemDir()
elif command == 'home':
    homeDir()
elif command == 'guest':
    guestDir()




else:
    input('Введите команду еще раз - ')