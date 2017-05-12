###########################
#                         #
#           TRIS          #
#    written in Python    #
#          v.1.2.3        #
#                         #
###########################

from random import randint
import os.path
def vintoono(vincitore):
    if (vincitore=="g1"):
        return "G1"
    elif (vincitore=="g2"):
        return "G2"
    elif (vincitore=="PC"):
        return "PC"
    return ""
def aggiungiMossa(m,mossa,mossasucc): #funzionante
    if (mossasucc=="g1"):
        simbolo="O"
        m[int(mossa[0])][int(mossa[1])]=simbolo
    else:
        simbolo="X"
        m[int(mossa[0])][int(mossa[1])]=simbolo
def creatabellone(m): #funzionante
    cont=0
    print("\t",cont,"\t",cont+1,"\t",cont+2)
    for i in m:
        print(cont,end="\t")
        for d in i:
          print(d,end="\t")
        cont=cont+1
        print()
    print()
def vittoriaono(m,mossasucc): #...
    simbolovitt=""
    if ((m[0][0]=="X" and m[0][1]=="X" and m[0][2]=="X") or
        (m[0][0]=="O" and m[0][1]=="O" and m[0][2]=="O")):
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[1][0]=="X" and m[1][1]=="X" and m[1][2]=="X") or
        (m[1][0]=="O" and m[1][1]=="O" and m[1][2]=="O")):
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[2][0]=="X" and m[2][1]=="X" and m[2][2]=="X") or
        (m[2][0]=="O" and m[2][1]=="O" and m[2][2]=="O")):
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[0][0]=="X" and m[1][0]=="X" and m[2][0]=="X") or
        (m[1][0]=="O" and m[1][0]=="O" and m[2][0]=="O")):
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[0][1]=="X" and m[1][1]=="X" and m[2][1]=="X") or
        (m[0][1]=="O" and m[1][1]=="O" and m[2][1]=="O")):
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[2][0]=="X" and m[2][1]=="X" and m[2][2]=="X") or
        (m[2][0]=="O" and m[2][1]=="O" and m[2][2]=="O")):
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[0][0]=="X" and m[1][1]=="X" and m[2][2]=="X") or
        (m[0][0]=="O" and m[1][1]=="O" and m[2][2]=="O")):
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[0][2]=="X" and m[1][1]=="X" and m[2][0]=="X") or
        (m[0][2]=="O" and m[1][1]=="O" and m[2][0]=="O")):
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    return simbolovitt
def vittoriaono2(m,mossasucc): #...
    simbolovitt=""
    if ((m[0][0]=="X" and m[0][1]=="X" and m[0][2]=="X") or
        (m[0][0]=="O" and m[0][1]=="O" and m[0][2]=="O")):
        if (mossasucc=="PC"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[1][0]=="X" and m[1][1]=="X" and m[1][2]=="X") or
        (m[1][0]=="O" and m[1][1]=="O" and m[1][2]=="O")):
        if (mossasucc=="PC"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[2][0]=="X" and m[2][1]=="X" and m[2][2]=="X") or
        (m[2][0]=="O" and m[2][1]=="O" and m[2][2]=="O")):
        if (mossasucc=="PC"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[0][0]=="X" and m[1][0]=="X" and m[2][0]=="X") or
        (m[1][0]=="O" and m[1][0]=="O" and m[2][0]=="O")):
        if (mossasucc=="PC"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[0][1]=="X" and m[1][1]=="X" and m[2][1]=="X") or
        (m[0][1]=="O" and m[1][1]=="O" and m[2][1]=="O")):
        if (mossasucc=="PC"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[2][0]=="X" and m[2][1]=="X" and m[2][2]=="X") or
        (m[2][0]=="O" and m[2][1]=="O" and m[2][2]=="O")):
        if (mossasucc=="PC"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[0][0]=="X" and m[1][1]=="X" and m[2][2]=="X") or
        (m[0][0]=="O" and m[1][1]=="O" and m[2][2]=="O")):
        if (mossasucc=="PC"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if ((m[0][2]=="X" and m[1][1]=="X" and m[2][0]=="X") or
        (m[0][2]=="O" and m[1][1]=="O" and m[2][0]=="O")):
        if (mossasucc=="PC"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    return simbolovitt
def modalita1(g1,g2,f): #....
    m=[["","",""],["","",""],["","",""]]
    simbolovitt="S"
    v="G0"
    vincitore="G0"
    while (v!="G1" or v!="G2"):
        creatabellone(m)
        if m==[["","",""],["","",""],["","",""]]:
          print("LANCIO DELLA MONETA!")
          if (randint(0,1)==0):
            print("INIZIA IL GIOCATORE 1!")
            mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
            mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
            mossa1=(mossa1X,mossa1Y)
            mossasucc="g2"
            while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
            aggiungiMossa(m,mossa1,mossasucc)
          else:
            print("INIZIA IL GIOCATORE 2!")
            mossa2X=int(input("Giocatore 2, inserisci la riga dove vuoi fare la tua mossa: "))
            mossa2Y=int(input("Giocatore 2, inserisci la colonna dove vuoi fare la tua mossa: "))            
            mossa2=(mossa2X,mossa2Y)
            mossasucc="g1"
            while (m[mossa2X][mossa2Y]=="O" or m[mossa2X][mossa2Y]=="X"):
                print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                mossa2X=int(input("Giocatore 2, inserisci la riga dove vuoi fare la tua mossa: "))
                mossa2Y=int(input("Giocatore 2, inserisci la colonna dove vuoi fare la tua mossa: "))            
                mossa2=(mossa2X,mossa2Y)
            else:
                aggiungiMossa(m,mossa2,mossasucc)
        else:
            if (mossasucc=="g1"):
                mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="g2"
                while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
                    mossa1=(mossa1X,mossa1Y)
                aggiungiMossa(m,mossa1,mossasucc)
            else:
                mossa2X=int(input("Giocatore 2, inserisci la riga dove vuoi fare la tua mossa: "))
                mossa2Y=int(input("Giocatore 2, inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa2=(mossa2X,mossa2Y)
                mossasucc="g1"
                while (m[mossa2X][mossa2Y]=="O" or m[mossa2X][mossa2Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa2X=int(input("Giocatore 2, inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa2Y=int(input("Giocatore 2, inserisci la colonna dove vuoi fare la tua mossa: "))            
                    mossa2=(mossa2X,mossa2Y)
                aggiungiMossa(m,mossa2,mossasucc)
        simbolovitt=vittoriaono(m,mossasucc)
        if (simbolovitt=="X"):
            vincitore="g1"
        if (simbolovitt=="O"):
            vincitore="g2"
        v=vintoono(vincitore)
        if (v=="G1"):
            print("\n","CONGRATULAZIONI GIOCATORE 1!!! HAI VINTO!!!!")
            creatabellone(m)
            break
        elif (v=="G2"):
            print("\n","CONGRATULAZIONI GIOCATORE 2!!! HAI VINTO!!!!")
            creatabellone(m)
            break
        f.write("m")
    print()
    return "PARTITA TERMINATA"
def controllocellenemiche(m): #GMO
    simbolovitt=""
    if (m[0][0]=="X" and m[0][1]=="X"):
        if(m[0][2]==""):
            m[0][2]=="O"
    elif (m[0][0]=="X" and m[0][2]=="X"):
        if(m[0][1]==""):
            m[0][1]=="O"
    elif (m[0][1]=="X" and m[0][2]=="X"):
        if(m[0][0]==""):
            m[0][0]=="O"
    elif (m[1][0]=="X" and m[1][1]=="X"):
        if(m[1][2]==""):
            m[1][2]=="O"
    elif (m[1][1]=="X" and m[1][2]=="X"):
        if(m[1][0]==""):
            m[1][0]=="O"
    elif (m[1][0]=="X" and m[1][2]=="X"):
        if(m[1][1]==""):
            m[1][1]=="O"
    elif (m[2][0]=="X" and m[2][1]=="X"):
        if(m[2][2]==""):
            m[2][2]=="O"
    elif (m[2][1]=="X" and m[2][2]=="X"):
        if(m[2][0]==""):
            m[2][0]=="O"
    elif (m[2][0]=="X" and m[2][2]=="X"):
        if(m[2][1]==""):
            m[2][1]=="O"
    elif (m[0][0]=="X" and m[1][0]=="X"):
        if(m[2][0]==""):
            m[2][0]=="O"
    elif (m[1][0]=="X" and m[2][0]=="X"):
        if(m[0][0]==""):
            m[0][0]=="O"
    elif (m[0][0]=="X" and m[2][0]=="X"):
        if(m[1][0]==""):
            m[1][0]=="O"
    elif (m[0][1]=="X" and m[1][1]=="X"):
        if(m[2][1]==""):
            m[2][1]=="O"
    elif (m[1][1]=="X" and m[2][1]=="X"):
        if(m[0][1]==""):
            m[0][1]=="O"
    elif (m[0][1]=="X" and m[2][1]=="X"):
        if(m[1][1]==""):
            m[1][1]=="O"
    elif (m[0][2]=="X" and m[1][2]=="X"):
        if(m[2][2]==""):
            m[2][2]=="O"
    elif (m[1][2]=="X" and m[2][2]=="X"):
        if(m[0][2]==""):
            m[0][2]=="O"
    elif (m[0][2]=="X" and m[2][2]=="X"):
        if(m[1][2]==""):
            m[1][2]=="O"
    elif (m[1][1]=="X" and m[2][2]=="X"):
        if(m[0][0]==""):
            m[0][0]=="O"
    elif (m[0][2]=="X" and m[1][1]=="X"):
        if(m[2][0]==""):
            m[2][0]=="O"
    elif (m[0][0]=="X" and m[2][2]=="X"):
        if(m[1][1]==""):
            m[1][1]=="O"
    elif (m[0][0]=="X" and m[1][1]=="X"):
        if(m[2][2]==""):
            m[2][2]=="O"
    elif (m[0][2]=="X" and m[2][0]=="X"):
        if(m[1][1]==""):
            m[1][1]=="O"
    elif (m[1][1]=="X" and m[2][0]=="X"):
        if(m[0][2]==""):
            m[0][2]=="O"
    return False
def controllocelle(m): #TBO e RCE
    #righe:
    if (m[0][0]=="O" and m[0][1]=="O"):
        if (m[0][2]==""):
            m[0][2]=="O"
    elif (m[0][1]=="O" and m[0][2]=="O"):
        if (m[0][0]==""):
            m[0][0]=="O"
    elif (m[0][2]=="O" and m[0][0]=="O"):
        if (m[0][1]==""):
            m[0][1]=="O"
    elif (m[1][0]=="O" and m[1][1]=="O"):
        if(m[1][2]==""):
            m[1][2]="O"
    elif (m[1][1]=="O" and m[1][2]=="O"):
        if(m[1][0]==""):
            m[1][0]="O"
    elif (m[1][2]=="O" and m[1][0]=="O"):
        if(m[1][1]==""):
            m[1][1]="O"
    elif (m[2][0]=="O" and m[2][1]=="O"):
        if(m[2][2]==""):
            m[2][2]="O"
    elif (m[2][1]=="O" and m[2][2]=="O"):
        if(m[2][0]==""):
            m[2][0]="O"
    elif (m[2][2]=="O" and m[2][0]=="O"):
       if(m[2][1]==""): 
        m[2][1]="O"
    #colonne:
    elif (m[0][0]=="O" and m[1][0]=="O"):
        if(m[2][0]==""):
            m[2][0]="O"
    elif (m[1][0]=="O" and m[2][0]=="O"):
        if(m[0][0]==""):
            m[0][0]="O"
    elif (m[2][0]=="O" and m[0][0]=="O"):
        if(m[1][0]==""):
            m[1][0]="O"
    elif (m[0][1]=="O" and m[1][1]=="O"):
        if(m[2][1]==""):
            m[2][1]="O"
    elif (m[1][1]=="O" and m[2][1]=="O"):
        if(m[0][0]==""):
            m[0][0]="O"
    elif (m[2][1]=="O" and m[0][1]):
        if(m[1][1]==""):
            m[1][1]="O"
    elif (m[0][2]=="O" and m[1][2]=="O"):
        if(m[2][0]==""):
            m[2][0]="O"
    elif (m[1][2]=="O" and m[2][2]=="O"):
        if(m[0][2]==""):
            m[0][2]="O"
    elif (m[2][2]=="O" and m[0][2]):
        if(m[1][2]==""):
            m[1][2]="O"
    #diagonali:
    elif (m[0][0]=="O" and m[1][1]=="O"):
        if(m[2][2]==""):
            m[2][2]="O"
    elif (m[1][1]=="O" and m[2][2]=="O"):
        if(m[0][0]==""):
            m[0][0]="O"
    elif (m[2][2]=="O" and m[0][0]=="O"):
        if(m[1][1]==""):
            m[1][1]="O"
    elif (m[0][2]=="O" and m[1][1]=="O"):
        if(m[2][0]==""):
            m[2][0]="O"
    elif (m[2][0]=="O" and m[1][1]=="O"):
        if(m[0][2]==""):
            m[0][2]="O"
    elif (m[1][1]=="O" and m[0][2]=="O"):
        if(m[2][0]==""):
            m[2][0]="O"
    return False
def attaccocasuale(m,mossasucc): #GMO e MBA
    riga=randint(0,2)
    colonna=randint(0,2)
    while (m[riga][colonna]=="X" or m[riga][colonna]=="O"):
        riga=randint(0,2)
        colonna=randint(0,2)
    mossa2=(riga,colonna)
    aggiungiMossa(m,mossa2,mossasucc)
def modalita2(g1,f):
    m=[["","",""],["","",""],["","",""]]
    simbolovitt="S"
    v="G0"
    vincitore="G0"
    while (v!="G1" or v!="G2"):
        creatabellone(m)
        if m==[["","",""],["","",""],["","",""]]:
            print("LANCIO DELLA MONETA!")
            if (randint(0,1)==0):
                print("INIZIA IL GIOCATORE 1!")
                mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="PC"
                while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
                    mossa1=(mossa1X,mossa1Y)
                aggiungiMossa(m,mossa1,mossasucc)
            else:
                mossasucc="g1"
                print("INIZIA IL PC!")
                if (not(controllocelle(m)==True)):
                    if (not(controllocellenemiche(m)==True)):
                        attaccocasuale(m,mossasucc)
        else:
            if (mossasucc=="g1"):
                mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="PC"
                while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
                    mossa1=(mossa1X,mossa1Y)
                aggiungiMossa(m,mossa1,mossasucc)
            else:
                mossasucc="g1"
                print("TOCCA AL PC!")
                if (not(controllocelle(m)==True)):
                    if (not(controllocellenemiche(m)==True)):
                        attaccocasuale(m,mossasucc)
        simbolovitt=vittoriaono2(m,mossasucc)
        if (simbolovitt=="X"):
            vincitore="g1"
        if (simbolovitt=="O"):
            vincitore="PC"
        v=vintoono(vincitore)
        if (v=="G1"):
            print("\n","CONGRATULAZIONI GIOCATORE 1!!! HAI VINTO!!!!")
            creatabellone(m)
            break
        elif (v=="PC"):
            print("\n","CONGRATULAZIONI PC!!! HAI VINTO!!!!, MI DISPIACE GIOCATORE 1 HAI PERSO!!")
            creatabellone(m)
            break
        f.write("m")
    print()
    return "PARTITA TERMINATA"
##### APERTURA FILE ECC.. #####
if not(os.path.exists(r"tabellone.txt")):
    f=open(r"tabellone.txt","w")
    f.close()
f=open(r"tabellone.txt","r+")
##### MENU PROGRAMMA #####
print("BENVENUTO IN TRIS SIMULATOR!")
scelta=-1
while (scelta!=-2):
    print("LE MODALITA' DI GIOCO POSSIBILI SONO:","\n","0:G1 vs G2","\n","1:G1 vs PC","\n","2:G1 vs Super PC","\n","-2: Esci dal gioco")
    scelta=int(input("Inserisci la tua scelta: "))
    if scelta==0:
        g1="X"
        g2="O"
        print(modalita1(g1,g2,f))
    if (scelta==1):
        g1="X"
        print(modalita2(g1,f))
    if (scelta==2):
        print(modalita3())
f.close()
