#nome del file : pagellaClientMulti.py
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except Exception as e:
        print(e)
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    studenti=random.randint(1,5)
    materie=random.randint(1,5)
    voti=random.randint(1,10)
    assenza=random.randint(1,5)
    if studenti==1:
        studente="Fare"
    elif studenti==2:
        studente="Rossi"
    elif studenti==3:
        studente="bianchi"
    elif studenti==4:
        studente="Verdi"
    else:
        studente="Pippo"

    if materie==1:
        materia="Matematica"
    elif materie==2:
        materia="Italiano"
    elif materie==3:
        materia="Inglese"
    elif materie==4:
        materia="Storia"
    else:
        materia="Geografia"
    
    messaggio={'studente':studente, 'materia':materia, 'voti':voti,'assenza':assenza}
    messaggio=json.dumps(messaggio)#trasforma il dizionario in un formato per essere inviato 
    print(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024) # chiama il metodo da ricevere specificando la quantità 1024
    data = data.decode()
    print("Risultato uscito : ",data)

    #1. Generazione casuale:
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    #   di un voto (valori ammessi 1 ..10)
    #   delle assenze (valori ammessi 1..5) 
    #2. comporre il messaggio, inviarlo come json
    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
        print(f"{threading.current_thread().name}: La valutazione di {data[0]} in {data[1]} è {data[2]} ") # trasforma il vettore di byte in stringa
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)
    

#Versione 2 
def genera_richieste2(num,address,port):
    #start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except Exception as e:
        print(e)
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    studenti=['studente0','studente1','studente2','studente3','studente4']
    materie=['Matematica','Italiano','Inglese','Storia']
    studente=studenti[random.randint(0,4)]
    pagella=[]
    for m in materie:
        voto=random.randint(1,10)
        assenze=random.randint(1,5)
        pagella.append((m,voto,assenze))

    messaggio={'studente':studente, 'pagella':pagella}
    messaggio=json.dumps(messaggio)#trasforma il dizionario in un formato per essere inviato 
    print(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024) # chiama il metodo da ricevere specificando la quantità 1024
    print("Risultato uscito : ",data.decode())
    
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
         print(f"{threading.current_thread().name}: La studente {data['studente']} ha una media di  {data['media']:.2f} e un totale di assenze {data['assenze']} ") # trasforma il vettore di byte in stringa
    s.close()
    #end_time_thread=time.time()
    #print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)


    
  #....
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
  #2. comporre il messaggio, inviarlo come json
  #3  ricevere il risultato come json {'studente': 'Cognome1', 'media': 8.0, 'assenze': 8}


#Versione 3
def genera_richieste3(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except Exception as e:
        print(e)
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    studenti=['studente0','studente1','studente2','studente3','studente4']
    materie=['Matematica','Italiano','Inglese','Storia']
    tabellone={}
    for stud in studenti:
        pagella=[]
        for m in materie:
            voto=random.randint(1,10)
            assenze=random.randint(1,5)
            pagella.append((m,voto,assenze))
        tabellone[stud]=pagella

    pp.print(tabellone)
    tabella=json.dumps(tabellone)#trasforma il dizionario in un formato per essere inviato 
    s.sendall(tabella.encode("UTF-8"))
    data=s.recv(1024) # chiama il metodo da ricevere specificando la quantità 1024
    print("Risultato uscito : ",data.decode())
    pp.pprint(data)

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        for data2 in data:
            print(f"{threading.current_thread().name}: La studente {data2['studente']} ha una media di  {data2['media']:.2f} e un totale di assenze {data2['assenze']} ") # trasforma il vettore di byte in stringa
    s.close()
    #end_time_thread=time.time()
    #print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)


    


  #....
  #   1. Per ognuno degli studenti ammessi: 5 cognomi a caso scelti da una lista
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: tabellone={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,3), ("Storia",8,2), ("Geografia",8,1)],
  #                       "Cognome2":[("Matematica",7,2), ("Italiano",5,3), ("Inglese",4,12), ("Storia",5,2), ("Geografia",4,1)],
  #                        .....}
  #2. comporre il messaggio, inviarlo come json
  #3  ricevere il risultato come json e stampare l'output come indicato in CONSOLE CLIENT V.3

if __name__ == '__main__':
    start_time=time.time()
    for num in range(NUM_WORKERS):
        genera_richieste1(num,SERVER_ADDRESS,SERVER_PORT)
        #genera_richieste2(num,SERVER_ADDRESS,SERVER_PORT)
        #genera_richieste3(num,SERVER_ADDRESS,SERVER_PORT)
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    for num in range (NUM_WORKERS):
        t1=threading.Thread(target=genera_richieste1,args=(num,SERVER_ADDRESS,SERVER_PORT))
        #t2=threading.Thread(target=genera_richieste2,args=(num,SERVER_ADDRESS,SERVER_PORT))
        #t3=threading.Thread(target=genera_richieste3,args=(num,SERVER_ADDRESS,SERVER_PORT))
        threads.append(t1)
        #threads.append(t2)
        #threads.append(t3)
    # 5 avvio tutti i thread
    for t1 in threads:
        t1.start()
    # 6 aspetto la fine di tutti i thread 
    for t1 in threads:
        t1.join()

    #for t2 in threads:
      #  t2.start()
    # 6 aspetto la fine di tutti i thread 
    #for t2 in threads:
     #   t2.join()
    
    #for t3 in threads:
    #    t3.start()
    # 6 aspetto la fine di tutti i thread 
    #for t3 in threads:
    #    t3.join()
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    for num in range (NUM_WORKERS):
        pro=multiprocessing.Process(target=genera_richieste1,args=(num,SERVER_ADDRESS,SERVER_PORT))
        #pro2=multiprocessing.Process(target=genera_richieste2,args=(num,SERVER_ADDRESS,SERVER_PORT))
        #pro3=multiprocessing.Process(target=genera_richieste3,args=(num,SERVER_ADDRESS,SERVER_PORT))
        #process.append(pro)
        #process.append(pro2)
        #process.append(pro3)
    # 8 avvio tutti i processi
    for pro in process:
        pro.start()
    # 9 aspetto la fine di tutti i processi 
    for pro in process:
        pro.join()

    for pro2 in process:
        pro2.start()
    # 9 aspetto la fine di tutti i processi 
    for pro2 in process:
        pro2.join()

    for pro3 in process:
        pro3.start()
    # 9 aspetto la fine di tutti i processi 
    for pro3 in process:
        pro3.join()

    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)