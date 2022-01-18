import socket 
import json 

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT)) # indica su che porta deve essere in ascolto 
    s.listen()
    print("[*] In ascolto su %s: %d "%(HOST,PORT)) 
    #il server deve accettare il client 
    clientsocket, address=s.accept() #restituisce la variabile che gestisce il socket e l'address 
    with clientsocket as cs:
        print("Conessione da ",address)
        while True:
            data=cs.recv(1024)
            if not data:  #se data è un vettore vuoto usciamo dal ciclo 
                break
            data=data.decode()
            data=json.loads(data)
            primoNumero=data['primoNumero']
            operazione=data['operazione']
            secondoNumero=data['secondoNumero']
            ris=""
            if operazione=="+":
                ris=primoNumero+secondoNumero
            elif operazione=="-":
                ris=primoNumero+secondoNumero
            elif operazione=="*":
                ris=primoNumero*secondoNumero
            elif operazione=="/":
                if secondoNumero==0:
                    ris="non puoi divere per 0 "
                else:
                    ris=primoNumero/secondoNumero
            elif operazione=="%":
                ris=primoNumero%secondoNumero
            else:
                ris="Operazione non riconosciuta"
            ris=str(ris)
            cs.sendall(ris.encode("UTF-8"))  # manda il vettore in risposta al client 


            
