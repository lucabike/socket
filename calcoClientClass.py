import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
class Client():
    def genera_richieste(num,address,port):
        sock_service=socket.socket()
        sock_service.connect((address,port))
        return sock_service

    def invia_comandi(self,sock_service):
        while True:
            numero1=input("inserire il numero se si vuole uscire scrivere exit() ") # inserire il numero per fare l'operazione 
            if numero1=="exit()":
                break
            numero1=float(numero1)
            operazione=input("Inserisci l'operazione che si vuole fare  (+,-,*,/,%)")
            numero2=float(input("Digita il secondo numero "))
            messaggio={'numero1':numero1, 'operazione':operazione, 'numero2':numero2}
            messaggio=json.dumps(messaggio)#trasforma il dizionario in un formato per essere inviato 
            sock_service.sendall(messaggio.encode("UTF-8"))
            data=sock_service.recv(1024) # chiama il metodo da ricevere specificando la quantità 1024
            print("Risultato uscito : ",data.decode()) 

c1=Client()
sock_serv=c1.genera_richieste(SERVER_ADDRESS,SERVER_PORT)
c1.invia_comandi(sock_serv)