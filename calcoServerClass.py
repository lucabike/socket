import socket
import json
from threading import Thread

SERVER_ADDRESS='127.0.0.1'   # indirizzo del server 
SERVER_PORT=22224 # porta del server 

class Server():
    def __init__(self,address,port):
        self.address=address
        self.port=port
    

    def ricevi_comandi(self,sock_service, addr_client):
        print("avviato")
        while True:
            data=sock_service.recv(1024)
            if not data: #se data è un vettore vuoto usciamo dal ciclo 
                break
            data=data.decode()
            data=json.loads(data) # viene ritrasformato in dizionario se non non può essere ricevuto 
            numero1=data['numero1'] #inserisce il numero 1
            operazione=data['operazione']
            numero2=data['numero2'] # inserisce il numero 2
            ris=""
            if operazione=="+": # se l'operazione da fare è +
                ris=numero1+numero2
            elif operazione=="-": # se l'operazione da fare è -
                ris=numero1-numero2
            elif operazione=="*": # se l'operazione da fare è *
                ris=numero1*numero2
            elif operazione=="/": # se l'operazione da fare è 
                if numero2==0:
                    ris="Impossibile dividere per 0"
                else:
                    ris=numero1/numero2
            elif operazione=="%":
                ris=numero1%numero2
            else:
                ris="Operazione non riuscita"
            ris=str(ris)
            sock_service.sendall(ris.encode("UTF-8"))  # manda il vettore in risposta al client 

        sock_service.close()

    def ricevi_connessioni(self,sock_listen):
        while True:
            sock_service, addr_client=sock_listen.accept()
            print("\nConnessione ricevuta da "+str(addr_client))
            print("\nCreo un thread per servire le richieste ")
            try:
                Thread(target=self.ricevi_comandi, args=(sock_service, addr_client)).start()
            except Exception as e:
                print(e)
                print("il thread non si avvia ")
                sock_listen.close()

    def avvia_server(self):
        sock_listen=socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_listen.bind((self.address,self.port))
        sock_listen.listen(5)
        print("Server in ascolto su %s." % str((self.address,self.port)))
        return sock_listen
        


    

s1=Server(SERVER_ADDRESS,SERVER_PORT)
sock_lis=s1.avvia_server()
s1.ricevi_connessioni(sock_lis)
