# !/usr/bin/env python3
# """Server for multithreaded (asynchronous) chat application."""
from http import client
from pickle import GLOBAL
from socket import AF_INET, SocketType, socket, SOCK_STREAM
from threading import Thread
from tkinter import Variable
from person import Person

# GLOBAL CONSTANTS
person = []  
HOST = 'localHost'
PORT = 5500
ADDR = (HOST,PORT)
# BUFSIZ -> how many bits of data to receive
BUFSIZ = 512

def broadcast(msg, name):
    """
    send new messages to all clients
    :param msg: bytes["utf8"]
    :param name: str
    :return:
    """
    for person in persons:
        client = person.client
        try:
            client.send(bytes(name, "utf8") + msg)
        except Exception as e:
            print("[EXCEPTION]", e)



#  
def client_communication(client):
    """
    Thread to handle all messages from client
    :PARAM client: socket
    :return:  None
    """
    run = True 
    client = person.client
    name = person.name 
    addr = person.addr
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            client.close()
        else: 
            



def wait_for_connection():
    """
    Wait for connecton from new clients, start new thread once connected
    :return: None
    """

    while True:
        try:
            client, addr = SERVER.accept()  # wait for any new connections
            person = Person(addr, client)  # create new person for connection
            persons.append(person)

            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            break

    print("SERVER CRASHED")



SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
MAX_CONNECTIONS = 10 


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)  # Listens for connections.
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()

