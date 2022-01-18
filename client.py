import socket 
import json


HOST="127.0.0.1"
PORT=65432
# af_inet indica il tipo di protocollo,socket_stream indica che tipo di socket è 
#lui tiene aperta il socket e una volta che finisce il with automaticamente chiuderà la connessione con il server 
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        primoNumero=input("inserisci il primo numero. exit() per uscire ")
        if primoNumero=="exit()":
            break
        primoNumero=float(primoNumero)
        operazione=input("inserisci l'operazione (+,-,*,/,%)")
        secondoNumero=float(input("inserisci il secondo numero"))
        messaggio={'primoNumero':primoNumero,'operazione':operazione,'secondoNumero':secondoNumero}
        messaggio=json.dumps(messaggio)
        s.sendall(messaggio.encode("UTF-8"))
        data=s.recv(1024)
        print("Risultato: ",data.decode()) #traforma il vettore di byte in String 
