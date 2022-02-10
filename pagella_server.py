import socket 
import json 

HOST="127.0.0.1"
PORT=65435
 students = {
        "Giuseppe Gullo":[("Matematica",9,0),("Italiano",7,3),("inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
        "Antonio Barbera":[("Matematica",8,1),("Italiano",6,1),("inglese",9.5,0),("Storia",8,2),("Geografia",5,7)],
        "Nicola Spina":[("Matematica",7.5,2),("Italiano",6,2),("inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]
    }
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

    s.bind((HOST,PORT)) # indica su che porta deve essere in ascolto 
    s.listen()
    print("[*] In ascolto su %s: %d "%(HOST,PORT)) 
    #il server deve accettare il client 
    clientsocket, address=s.accept() #restituisce la variabile che gestisce il socket e l'address 
   
while True:
     clientsocket, address=s.accept() #restituisce la variabile che gestisce il socket e l'address 
     print("Conessione da ",address)
        while True:
            data=cs.recv(1024)
            data=data.decode()
            data=data.strip()
            print("[*] Received: %s" % data)
            if data == "#list":
            elif data.find('#get') != -1:
            elif data.find('#put') != -1: 
            elif data.find('#set') != -1: 
            elif data == "#close" != -1:
            print(clientsocket.getpeername())
            pp=pprint.PrettyPrinter(indent=4)
            pp.pprint(students)

        clientsocket.close()




    #
           # print("stringa ricevuta "+ stringa)
            #   if stringa!="KO":
               # ris=stringa+" "+str(contatore)
               # contatore+=1
           ris=str(ris)
            cs.sendall(ris.encode("UTF-8"))  # manda il vettore in risposta al client 