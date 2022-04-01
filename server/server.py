# !/usr/bin/env python3
# """Server for multithreaded (asynchronous) chat application."""
from http import client
from socket import AF_INET, SocketType, socket, SOCK_STREAM
from threading import Thread

def client_communication(client):
    run = True 
    while run:
        


def wait_for_connection(SERVER):
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            Thread(target=client_communication, args=(client,)).start()
        except: Exception as e:
        print(["FAILURE"], e)
        run = FALSE

HOST = 'localHost'
PORT = 5500
BUFSIZ = 1024
ADDR = (HOST,PORT)


SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


if __name__ == "__main__":
    SERVER.listen(5)  # Listens for 5 connections at max.
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection,*(SERVER))
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()

