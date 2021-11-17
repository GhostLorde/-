import socket

from threading import Thread
from time import sleep


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setblocking(True)


def add_new_user():
    name = str(input("Введите имя : "))
    client.send(name.encode())
    password = str(input("Введите пароль : "))
    client.send(password.encode())






def input_password():
    data = 0
    while (data != "4"):
        password = str(input(f"Введите пароль: "))
        client.send(password.encode())
        data = client.recv(1024).decode("UTF-8")


def printmsg():
    while (True):
        try:
            name = client.recv(1024).decode("UTF-8")
            if (name == "1"):
                add_new_user()
                continue
            elif (name == "2"):
                input_password()
                continue
            data = client.recv(1024).decode("UTF-8")
            print(f"Message from {name}: {data}")
        except (KeyboardInterrupt, ConnectionAbortedError):
            print("Exit")
            break



client.connect(("localhost", 9098))
checkdata = Thread(target=printmsg, daemon=True)
checkdata.start()
i = 0
while True:
    try:
        if (i == 0):
            sleep(5)
            i += 1
        msg = input()
        client.send(msg.encode())
    except ConnectionAbortedError:
        print("Connection disable")
        break

client.close()

