import json
import socket

SERVER_ADDRESS='127.0.0.1' # indirizzo server
SERVER_PORT=22224  # porta del server 

def invia_comandi(sock_service):
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

def  connessione_server(address, port):
    sock_service=socket.socket()
    sock_service.connect((address, port))
    print("Connesso a " + str((address, port)))
    invia_comandi(sock_service)

if __name__=='__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT)