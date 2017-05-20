###########################
#                         #
#           TRIS          #
#    written in Python    #
#        v. 2.2           #
#                         #
###########################

from tkinter import *
import tkinter.messagebox
from random import randint
import os.path
def vintoono(vincitore): #MBA
    if (vincitore=="g1"):
        return "G1"
    elif (vincitore=="g2"):
        return "G2"
    elif (vincitore=="PC"):
        return "PC"
    return ""
def aggiungiMossa(m,mossa,mossasucc): #MBA e TBO
    if (mossasucc=="g1"):
        simbolo="O"
        m[int(mossa[0])][int(mossa[1])]=simbolo
    else:
        simbolo="X"
        m[int(mossa[0])][int(mossa[1])]=simbolo
def creatabellone(m): #MBA e TBO
    cont=0
    print("\t",cont,"\t",cont+1,"\t",cont+2)
    for i in m:
        print(cont,end="\t")
        for d in i:
          print(d,end="\t")
        cont=cont+1
        print()
    print()
def vittoriaono(m,mossasucc): #MBA e TBO
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
        (m[0][0]=="O" and m[1][0]=="O" and m[2][0]=="O")):
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
    if ((m[0][2]=="X" and m[1][2]=="X" and m[2][2]=="X") or
        (m[0][2]=="O" and m[1][2]=="O" and m[2][2]=="O")):
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
def controllotabpieno(m): #MBA
    if ((m[0][0]=="X" or m[0][0]=="O") and
        (m[0][1]=="X" or m[0][1]=="O") and
        (m[0][2]=="X" or m[0][2]=="O") and
        (m[1][0]=="X" or m[1][0]=="O") and
        (m[1][1]=="X" or m[1][1]=="O") and
        (m[1][2]=="X" or m[1][2]=="O") and
        (m[2][0]=="X" or m[2][0]=="O") and
        (m[2][1]=="X" or m[2][1]=="O") and
        (m[2][2]=="X" or m[2][2]=="O")):
        return True
    else:
        return False
def vittoriaono2(m,mossasucc): #MBA (copia e incolla da sopra)
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
        (m[0][0]=="O" and m[1][0]=="O" and m[2][0]=="O")):
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
    if ((m[0][2]=="X" and m[1][2]=="X" and m[2][2]=="X") or
        (m[0][2]=="O" and m[1][2]=="O" and m[2][2]=="O")):
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
def modalita1(): #MBA e TBO
    global f
    f=open(r"tabellone.txt","a")
    m=[["","",""],["","",""],["","",""]]
    simbolovitt="S"
    v="G0"
    vincitore="G0"
    while (v!="G1" or v!="G2"):
        creatabellone(m)
        if m==[["","",""],["","",""],["","",""]]:
          print("LANCIO DELLA MONETA!")
          if (randint(0,1)==0):
            print("INIZIA", g1,"!")
            mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
            mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
            mossa1=(mossa1X,mossa1Y)
            mossasucc="g2"
            while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
            aggiungiMossa(m,mossa1,mossasucc)
          else:
            print("INIZIA IL GIOCATORE 2!")
            mossa2X=int(input(g2+", inserisci la riga dove vuoi fare la tua mossa: "))
            mossa2Y=int(input(g2+", inserisci la colonna dove vuoi fare la tua mossa: "))            
            mossa2=(mossa2X,mossa2Y)
            mossasucc="g1"
            while (m[mossa2X][mossa2Y]=="O" or m[mossa2X][mossa2Y]=="X"):
                print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                mossa2X=int(input(g2+", inserisci la riga dove vuoi fare la tua mossa: "))
                mossa2Y=int(input(g2+", inserisci la colonna dove vuoi fare la tua mossa: "))            
                mossa2=(mossa2X,mossa2Y)
            else:
                aggiungiMossa(m,mossa2,mossasucc)
        else:
            if (mossasucc=="g1"):
                mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="g2"
                while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                    mossa1=(mossa1X,mossa1Y)
                aggiungiMossa(m,mossa1,mossasucc)
            else:
                mossa2X=int(input(g2+", inserisci la riga dove vuoi fare la tua mossa: "))
                mossa2Y=int(input(g2+", inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa2=(mossa2X,mossa2Y)
                mossasucc="g1"
                while (m[mossa2X][mossa2Y]=="O" or m[mossa2X][mossa2Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa2X=int(input(g2+", inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa2Y=int(input(g2+", inserisci la colonna dove vuoi fare la tua mossa: "))            
                    mossa2=(mossa2X,mossa2Y)
                aggiungiMossa(m,mossa2,mossasucc)
        simbolovitt=vittoriaono(m,mossasucc)
        if (simbolovitt=="X"):
            vincitore="g1"
        if (simbolovitt=="O"):
            vincitore="g2"
        v=vintoono(vincitore)
        if (v=="G1"):
            print("\n","CONGRATULAZIONI", g1," HAI VINTO!!!!")
            creatabellone(m)
            break
        elif (v=="G2"):
            print("\n","CONGRATULAZIONI", g2," HAI VINTO!!!!")
            creatabellone(m)
            break
        elif (controllotabpieno(m)==True):
            print("\n","NESSUN GIOCATORE HA VINTO! ANDRA' MEGLIO LA PROSSIMA VOLTA!!")
            creatabellone(m)
            break
        #Scrittura su file del numero del tabellone
        f.write(str(m)+"\n")
    f.close()
    return "PARTITA TERMINATA"
def controllocellenemiche(m): #GMO
    simbolovitt=""
    if (m[0][0]=="X" and m[0][1]=="X" and m[0][2]==""):
        m[0][2]="O"
    elif (m[0][0]=="X" and m[0][2]=="X" and m[0][1]==""):
        m[0][1]="O"
    elif (m[0][1]=="X" and m[0][2]=="X" and m[0][0]==""):
        m[0][0]="O"
    elif (m[1][0]=="X" and m[1][1]=="X" and m[1][2]==""):
        m[1][2]="O"
    elif (m[1][1]=="X" and m[1][2]=="X" and m[1][0]==""):
        m[1][0]="O"
    elif (m[1][0]=="X" and m[1][2]=="X" and m[1][1]==""):
        m[1][1]="O"
    elif (m[2][0]=="X" and m[2][1]=="X" and m[2][2]==""):
        m[2][2]="O"
    elif (m[2][1]=="X" and m[2][2]=="X" and m[2][0]==""):
        m[2][0]="O"
    elif (m[2][0]=="X" and m[2][2]=="X" and m[2][1]==""):
        m[2][1]="O"
    elif (m[0][0]=="X" and m[1][0]=="X" and m[2][0]==""):
        m[2][0]="O"
    elif (m[1][0]=="X" and m[2][0]=="X" and m[0][0]==""):
        m[0][0]="O"
    elif (m[0][0]=="X" and m[2][0]=="X" and m[1][0]==""):
        m[1][0]="O"
    elif (m[0][1]=="X" and m[1][1]=="X" and m[2][1]==""):
        m[2][1]="O"
    elif (m[1][1]=="X" and m[2][1]=="X" and m[0][1]==""):
        m[0][1]="O"
    elif (m[0][1]=="X" and m[2][1]=="X" and m[1][1]==""):
        m[1][1]="O"
    elif (m[0][2]=="X" and m[1][2]=="X" and m[2][2]==""):
        m[2][2]="O"
    elif (m[1][2]=="X" and m[2][2]=="X" and m[0][2]==""):
        m[0][2]="O"
    elif (m[0][2]=="X" and m[2][2]=="X" and m[0][2]==""):
        m[1][2]="O"
    elif (m[1][1]=="X" and m[2][2]=="X" and m[0][0]==""):
        m[0][0]="O"
    elif (m[0][2]=="X" and m[1][1]=="X" and m[2][0]==""):
        m[2][0]="O"
    elif (m[0][0]=="X" and m[2][2]=="X" and m[1][1]==""):
        m[1][1]="O"
    elif (m[0][0]=="X" and m[1][1]=="X" and m[2][2]==""):
        m[2][2]="O"
    elif (m[0][2]=="X" and m[2][0]=="X" and m[1][1]==""):
        m[1][1]="O"
    elif (m[1][1]=="X" and m[2][0]=="X" and m[0][2]==""):
        m[0][2]="O"
    else:
        return False
    return True
def controllocelle(m): #TBO e RCE
    if (m[0][0]=="O" and m[0][1]=="O" and m[0][2]==""):
        m[0][2]="O"
    elif (m[0][1]=="O" and m[0][2]=="O" and m[0][0]==""):
        m[0][0]="O"
    elif (m[0][2]=="O" and m[0][0]=="O" and m[0][1]==""):
        m[0][1]="O"
    elif (m[1][0]=="O" and m[1][1]=="O" and m[1][2]==""):
        m[1][2]="O"
    elif (m[1][1]=="O" and m[1][2]=="O" and m[1][0]==""): 
        m[1][0]="O"
    elif (m[1][2]=="O" and m[1][0]=="O" and m[1][1]==""):
        m[1][1]="O"
    elif (m[2][0]=="O" and m[2][1]=="O" and m[2][2]==""):
        m[2][2]="O"
    elif (m[2][1]=="O" and m[2][2]=="O" and m[2][0]==""):
        m[2][0]="O"
    elif (m[2][2]=="O" and m[2][0]=="O" and m[2][1]==""):
        m[2][1]="O"
    elif (m[0][0]=="O" and m[1][0]=="O" and m[2][0]==""):
        m[2][0]="O"
    elif (m[1][0]=="O" and m[2][0]=="O" and m[0][0]==""):
        m[0][0]="O"
    elif (m[2][0]=="O" and m[0][0]=="O" and m[1][0]==""):
        m[1][0]="O"
    elif (m[0][1]=="O" and m[1][1]=="O" and m[2][1]==""):
        m[2][1]="O"
    elif (m[1][1]=="O" and m[2][1]=="O" and m[0][1]==""):
        m[0][1]="O"
    elif (m[2][1]=="O" and m[0][1]=="O" and m[1][1]==""):
        m[1][1]="O"
    elif (m[0][2]=="O" and m[1][2]=="O" and m[2][0]==""):
        m[2][0]="O"
    elif (m[1][2]=="O" and m[2][2]=="O" and m[0][2]==""):
        m[0][2]="O"
    elif (m[2][2]=="O" and m[0][2]=="O" and m[1][2]==""):
        m[1][2]="O"
    elif (m[0][0]=="O" and m[1][1]=="O" and m[2][2]==""):
        m[2][2]="O"
    elif (m[1][1]=="O" and m[2][2]=="O" and m[0][0]==""):
        m[0][0]="O"
    elif (m[2][2]=="O" and m[0][0]=="O" and m[1][1]==""):
        m[1][1]="O"
    elif (m[0][2]=="O" and m[1][1]=="O" and m[2][0]==""):
        m[2][0]="O"
    elif (m[2][0]=="O" and m[1][1]=="O" and m[0][2]==""):
        m[0][2]="O"
    elif (m[1][1]=="O" and m[0][2]=="O" and m[2][0]==""):
        m[2][0]="O"
    else:
        return False
    return True
def attaccocasuale(m,mossasucc): #GMO e MBA
    riga=randint(0,2)
    colonna=randint(0,2)
    while (m[riga][colonna]=="X" or m[riga][colonna]=="O"):
        riga=randint(0,2)
        colonna=randint(0,2)
    mossa2=(riga,colonna)
    aggiungiMossa(m,mossa2,mossasucc)
def modalita2(): #MBA, GMO, TBO, RCE
    global f
    f=open(r"tabellone.txt","a")
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
                mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="PC"
                while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                    mossa1=(mossa1X,mossa1Y)
                aggiungiMossa(m,mossa1,mossasucc)
            else:
                mossasucc="g1"
                print("INIZIA IL PC!")
                if (controllocelle(m)==False):
                    if (controllocellenemiche(m)==False):
                        attaccocasuale(m,mossasucc)
        else:
            if (mossasucc=="g1"):
                mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="PC"
                while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                    mossa1=(mossa1X,mossa1Y)
                aggiungiMossa(m,mossa1,mossasucc)
            else:
                mossasucc="g1"
                print("TOCCA AL PC!")
                c1=controllocelle(m)
                if (c1==False):
                    c2=controllocellenemiche(m)
                    if (c2==False):
                        attaccocasuale(m,mossasucc)
        simbolovitt=vittoriaono2(m,mossasucc)
        if (simbolovitt=="X"):
            vincitore="g1"
        if (simbolovitt=="O"):
            vincitore="PC"
        v=vintoono(vincitore)
        if (v=="G1"):
            print("\n","CONGRATULAZIONI", g1," HAI VINTO!!!!")
            creatabellone(m)
            break
        elif (v=="PC"):
            print("\n","CONGRATULAZIONI PC!!! HAI VINTO!!!!, MI DISPIACE", g1," HAI PERSO!!")
            creatabellone(m)
            break
        elif (controllotabpieno(m)==True):
            print("\n","NESSUN GIOCATORE HA VINTO! ANDRA' MEGLIO LA PROSSIMA VOLTA!!")
            creatabellone(m)
            break
        #Scrittura su file del numero del tabellone
        f.write(str(m)+"\n")
    f.close()
    print()
    return "PARTITA TERMINATA"
def controllotabellone(cont): #TBO, RCE e MBA
    mold=[]
    mold1=[]                                 #f="XO ,O X, OX" mold1=["XO "] mold=[X,O,""]
    riga=f.readline()
    i=0
    while (riga!="" and i<cont):
        mold=list(riga[:-2])
        i+=1
    return mold
def attaccoByTabVecchio(m,mOld): #GMO
    i=0
    i1=0
    cont=0
    cont2=0
    while (i<m):
        if (m[i][i1]!=mOld[cont][cont2]):
            if (mOld[cont][cont2]=="X"):
                m[i][i1]=="O"
            if (i1==2 or cont2==2):
                i=i+1
                cont=cont+1
                i1=0
                cont2=0
            i1=i1+1
            cont2=cont2+1
def modalita3():
    global f
    f=open(r"tabellone.txt","r+")
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
                mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="PC"
                while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                    mossa1=(mossa1X,mossa1Y)
                aggiungiMossa(m,mossa1,mossasucc)
            else:
                mossasucc="g1"
                print("INIZIA IL PC!")
                if (m==controllotabellone(0)):
                    mOld=controllotabellone(1)
                    attaccoByTabVecchio(m,mOld)
                elif (controllocelle(m)==False):
                    if (controllocellenemiche(m)==False):
                        attaccocasuale(m,mossasucc)
        else:
            if (mossasucc=="g1"):
                mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="PC"
                while (m[mossa1X][mossa1Y]=="O" or m[mossa1X][mossa1Y]=="X"):
                    print("NON PUOI SOVRASCRIVERE UN SIMBOLO GIA' ESISTENTE!!")
                    mossa1X=int(input(g1+", inserisci la riga dove vuoi fare la tua mossa: "))
                    mossa1Y=int(input(g1+", inserisci la colonna dove vuoi fare la tua mossa: "))
                    mossa1=(mossa1X,mossa1Y)
                aggiungiMossa(m,mossa1,mossasucc)
            else:
                mossasucc="g1"
                print("TOCCA AL PC!")
                if (m==controllotabellone(0)):
                    mOld=controllotabellone(1)
                    attaccoByTabVecchio(m,mOld)
                elif (controllocelle(m)==False):
                    if (controllocellenemiche(m)==False):
                        attaccocasuale(m,mossasucc)
        simbolovitt=vittoriaono2(m,mossasucc)
        if (simbolovitt=="X"):
            vincitore="g1"
        if (simbolovitt=="O"):
            vincitore="PC"
        v=vintoono(vincitore)
        if (v=="G1"):
            print("\n","CONGRATULAZIONI,",g1," HAI VINTO!!!!")
            creatabellone(m)
            break
        elif (v=="PC"):
            print("\n","CONGRATULAZIONI PC!!! HAI VINTO!!!!, MI DISPIACE", g1," HAI PERSO!!")
            creatabellone(m)
            break
        elif (controllotabpieno(m)==True):
            print("\n","NESSUN GIOCATORE HA VINTO! ANDRA' MEGLIO LA PROSSIMA VOLTA!!")
            creatabellone(m)
            break
        #Scrittura su file del numero del tabellone
        f.write(str(m)+"\n")
    f.close()
    print()
    return "PARTITA TERMINATA"
def addsimbolo00():
    if (m[0][0]==""):
        if (turno==0):
            simb="X"
            m[0][0]="X"
        elif (turno==1):
            simb="O"
            m[0][0]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un'altra posizione")
        return False
    w1.quit()
def addsimbolo01():
    if (m[0][1]==""):
        if (turno==0):
            simb="X"
            m[0][1]="X"
        elif (turno==1):
            simb="O"
            m[0][1]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un altra posizione")
        return False
    w1.quit()
def addsimbolo02():
    if (m[0][2]==""):
        if (turno==0):
            simb="X"
            m[0][2]="X"
        elif (turno==1):
            simb="O"
            m[0][2]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un altra posizione")
        return False
    w1.quit()
def addsimbolo10():
    if (m[1][0]==""):
        if (turno==0):
            simb="X"
            m[1][0]="X"
        elif (turno==1):
            simb="O"
            m[1][0]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un altra posizione")
        return False
    w1.quit()
def addsimbolo11():
    if (m[1][1]==""):
        if (turno==0):
            simb="X"
            m[1][1]="X"
        elif (turno==1):
            simb="O"
            m[1][1]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un altra posizione")
        return False
    w1.quit()
def addsimbolo12():
    if (m[1][2]==""):
        if (turno==0):
            simb="X"
            m[1][2]="X"
        elif (turno==1):
            simb="O"
            m[1][2]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un altra posizione")
        return False
    w1.quit()
def addsimbolo20():
    if (m[2][0]==""):
        if (turno==0):
            simb="X"
            m[2][0]="X"
        elif (turno==1):
            simb="O"
            m[2][0]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un altra posizione")
        return False
    w1.quit()
def addsimbolo21():
    if (m[2][1]==""):
        if (turno==0):
            simb="X"
            m[2][1]="X"
        elif (turno==1):
            simb="O"
            m[2][1]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un altra posizione")
        return False
    w1.quit()
def addsimbolo22():
    if (m[2][2]==""):
        if (turno==0):
            simb="X"
            m[2][2]="X"
        elif (turno==1):
            simb="O"
            m[2][2]="O"
    else:
        tkinter.messagebox.showerror(title="Errore di sovrascrittura simbolo",message="Non puoi sovrascrivere un simbolo già esistente! Scegliere un altra posizione")
        return False
    w1.quit()
def tabgraph1(): #MBA
    global turno
    vincitore="G0"
    turno=randint(0,1)
    while turno!=-1:
        if (turno==0):
            g=g1
            mossasucc="g2"
        elif (turno==1):
            g=g2
            mossasucc="g1"
        global w1
        w1=Tk()
        w1.title("PYTRIS G1 VS G2")
        w1.geometry("%dx%d+%d+%d" % (200, 200, 600, 250))
        intest=Label(w1,text="TABELLONE (G1 VS G2)",font="Tahoma 12 bold")
        intest.pack()
        f1=Frame(w1)
        f1.pack()
        b00=Button(f1,text=m[0][0],command=addsimbolo00)
        b01=Button(f1,text=m[0][1],command=addsimbolo01)
        b02=Button(f1,text=m[0][2],command=addsimbolo02)
        b10=Button(f1,text=m[1][0],command=addsimbolo10)
        b11=Button(f1,text=m[1][1],command=addsimbolo11)
        b12=Button(f1,text=m[1][2],command=addsimbolo12)
        b20=Button(f1,text=m[2][0],command=addsimbolo20)
        b21=Button(f1,text=m[2][1],command=addsimbolo21)
        b22=Button(f1,text=m[2][2],command=addsimbolo22)
        b00.grid(row=0,column=0)
        b01.grid(row=0,column=1)
        b02.grid(row=0,column=2)
        b10.grid(row=1,column=0)
        b11.grid(row=1,column=1)
        b12.grid(row=1,column=2)
        b20.grid(row=2,column=0)
        b21.grid(row=2,column=1)
        b22.grid(row=2,column=2)
        fg=Frame(w1)
        fg.pack()
        tg="Turno di "+g
        giocatore=Label(fg,text=tg)
        giocatore.pack()
        w1.mainloop()
        w1.destroy()
        if (turno==1):
            turno=-1
        if (controllotabpieno(m)==True):
            tkinter.messagebox.showinfo(title="PAREGGIO!!", message="Nessun giocatore ha vinto! Andrà meglio la prossim volta!!")
            break
        if (vittoriaono(m,mossasucc)=="X"):
            vincitore="g1"
        if (vittoriaono(m,mossasucc)=="O"):
            vincitore="g2"
        if (vintoono(vincitore)=="G1"):
            tkinter.messagebox.showinfo(title="VITTORIA!!", message="CONGRATULAZIONI "+g1+" HAI VINTO!!!!")
            break
        elif (vintoono(vincitore)=="G2"):
            tkinter.messagebox.showinfo(title="VITTORIA!!", message="CONGRATULAZIONI "+g2+" HAI VINTO!!!!")
            break
        turno+=1
        #Scrittura su file del numero del tabellone
        f.write(str(m)+"\n")
    f.close()
def mod1graph(): #MBA
    global f
    f=open(r"tabellone.txt","a")
    global m
    m=[["","",""],["","",""],["","",""]]
    simbolovitt="S"
    v="G0"
    vincitore="G0"
    while (v!="G1" or v!="G2"):
        tabgraph1()
        break
    tkinter.messagebox.showinfo(title="PARTITA TERMINATA", message="Partita terminata!")
def tabgraph2(): #MBA
    global turno
    vincitore="G0"
    turno=randint(0,1)
    while turno!=-1:
        if (turno==0):
            g=g1
            mossasucc="g2"
            global w1
            w1=Tk()
            w1.title("PYTRIS G1 VS PC")
            w1.geometry("%dx%d+%d+%d" % (200, 200, 600, 250))
            intest=Label(w1,text="TABELLONE (G1 VS PC)",font="Tahoma 12 bold")
            intest.pack()
            f1=Frame(w1)
            f1.pack()
            b00=Button(f1,text=m[0][0],command=addsimbolo00)
            b01=Button(f1,text=m[0][1],command=addsimbolo01)
            b02=Button(f1,text=m[0][2],command=addsimbolo02)
            b10=Button(f1,text=m[1][0],command=addsimbolo10)
            b11=Button(f1,text=m[1][1],command=addsimbolo11)
            b12=Button(f1,text=m[1][2],command=addsimbolo12)
            b20=Button(f1,text=m[2][0],command=addsimbolo20)
            b21=Button(f1,text=m[2][1],command=addsimbolo21)
            b22=Button(f1,text=m[2][2],command=addsimbolo22)
            b00.grid(row=0,column=0)
            b01.grid(row=0,column=1)
            b02.grid(row=0,column=2)
            b10.grid(row=1,column=0)
            b11.grid(row=1,column=1)
            b12.grid(row=1,column=2)
            b20.grid(row=2,column=0)
            b21.grid(row=2,column=1)
            b22.grid(row=2,column=2)
            fg=Frame(w1)
            fg.pack()
            tg="Turno di "+g
            giocatore=Label(fg,text=tg)
            giocatore.pack()
            w1.mainloop()
            w1.destroy()
        elif (turno==1):
            g=g2
            mossasucc="g1"
            if (controllocelle(m)==False):
                if (controllocellenemiche(m)==False):
                    attaccocasuale(m,mossasucc)
        if (turno==1):
            turno=-1
        if (controllotabpieno(m)==True):
            tkinter.messagebox.showinfo(title="PAREGGIO!!", message="Nessun giocatore ha vinto! Andrà meglio la prossima volta!!")
            break
        if (vittoriaono(m,mossasucc)=="X"):
            vincitore="g1"
        if (vittoriaono(m,mossasucc)=="O"):
            vincitore="g2"
        if (vintoono(vincitore)=="G1"):
            tkinter.messagebox.showinfo(title="VITTORIA!!", message="CONGRATULAZIONI "+g1+" HAI VINTO!!!!")
            break
        elif (vintoono(vincitore)=="G2"):
            tkinter.messagebox.showinfo(title="VITTORIA!!", message="CONGRATULAZIONI "+g2+" HAI VINTO!!!!")
            break
        turno+=1
        #Scrittura su file del numero del tabellone
        f.write(str(m)+"\n")
    f.close()
def mod2graph(): #MBA
    global f
    f=open(r"tabellone.txt","a")
    global m
    m=[["","",""],["","",""],["","",""]]
    simbolovitt="S"
    v="G0"
    vincitore="G0"
    while (v!="G1" or v!="G2"):
        tabgraph2()
        break
    tkinter.messagebox.showinfo(title="PARTITA TERMINATA", message="Partita terminata!")
def tabgraph3(): #MBA
    global turno
    vincitore="G0"
    turno=randint(0,1)
    while turno!=-1:
        if (turno==0):
            g=g1
            mossasucc="g2"
            global w1
            w1=Tk()
            w1.title("PYTRIS G1 VS PC")
            w1.geometry("%dx%d+%d+%d" % (200, 200, 600, 250))
            intest=Label(w1,text="TABELLONE (G1 VS PC)",font="Tahoma 12 bold")
            intest.pack()
            f1=Frame(w1)
            f1.pack()
            b00=Button(f1,text=m[0][0],command=addsimbolo00)
            b01=Button(f1,text=m[0][1],command=addsimbolo01)
            b02=Button(f1,text=m[0][2],command=addsimbolo02)
            b10=Button(f1,text=m[1][0],command=addsimbolo10)
            b11=Button(f1,text=m[1][1],command=addsimbolo11)
            b12=Button(f1,text=m[1][2],command=addsimbolo12)
            b20=Button(f1,text=m[2][0],command=addsimbolo20)
            b21=Button(f1,text=m[2][1],command=addsimbolo21)
            b22=Button(f1,text=m[2][2],command=addsimbolo22)
            b00.grid(row=0,column=0)
            b01.grid(row=0,column=1)
            b02.grid(row=0,column=2)
            b10.grid(row=1,column=0)
            b11.grid(row=1,column=1)
            b12.grid(row=1,column=2)
            b20.grid(row=2,column=0)
            b21.grid(row=2,column=1)
            b22.grid(row=2,column=2)
            fg=Frame(w1)
            fg.pack()
            tg="Turno di "+g
            giocatore=Label(fg,text=tg)
            giocatore.pack()
            w1.mainloop()
            w1.destroy()
        elif (turno==1):
            g=g2
            mossasucc="g1"
            if (m==controllotabellone(0)):
                mOld=controllotabellone(1)
                attaccoByTabVecchio(m,mOld)
            elif (controllocelle(m)==False):
                if (controllocellenemiche(m)==False):
                    attaccocasuale(m,mossasucc)
        if (turno==1):
            turno=-1
        if (controllotabpieno(m)==True):
            tkinter.messagebox.showinfo(title="PAREGGIO!!", message="Nessun giocatore ha vinto! Andrà meglio la prossima volta!!")
            break
        if (vittoriaono(m,mossasucc)=="X"):
            vincitore="g1"
        if (vittoriaono(m,mossasucc)=="O"):
            vincitore="g2"
        if (vintoono(vincitore)=="G1"):
            tkinter.messagebox.showinfo(title="VITTORIA!!", message="CONGRATULAZIONI "+g1+" HAI VINTO!!!!")
            break
        elif (vintoono(vincitore)=="G2"):
            tkinter.messagebox.showinfo(title="VITTORIA!!", message="CONGRATULAZIONI "+g2+" HAI VINTO!!!!")
            break
        turno+=1
        #Scrittura su file del numero del tabellone
        f.write(str(m)+"\n")
    f.close()
def mod3graph(): #MBA
    global f
    f=open(r"tabellone.txt","r+")
    global m
    m=[["","",""],["","",""],["","",""]]
    simbolovitt="S"
    v="G0"
    vincitore="G0"
    while (v!="G1" or v!="G2"):
        tabgraph3()
        break
    tkinter.messagebox.showinfo(title="PARTITA TERMINATA", message="Partita terminata!")
def showmexinfo():
    tkinter.messagebox.showinfo(title="INFO IMPOSTAZIONI",message="Per modificare le impostazioni chiudere la versione grafica del gioco e salvare da quella testuale. Poi, rientrare nella versione grafica")
def welcomegraph(): #MBA
    #Creazione finestra GUI
    w=Tk()
    w.title("PYTRIS")
    f=Frame(w)
    logo=PhotoImage(file=r"pytris_logo.gif")
    title=Label(f,image=logo)
    f.pack()
    title.pack()
    subtitle=Label(f,text="created by Battistini Maicol, Botticelli Tommaso, Censi Riccardo e Morolli Giada")
    subtitle.pack()
    mod1=Button(f,text="Modalità 1: G1 VS G2",command=mod1graph)
    mod1.pack()
    mod2=Button(f,text="Modalità 2: G1 VS PC",command=mod2graph)
    mod2.pack()
    mod3=Button(f,text="Modalità 3: G1 VS SUPER PC",command=mod3graph)
    mod3.pack()
    bs=Button(f,text="IMPOSTAZIONI",command=showmexinfo)
    bs.pack()
    disgraph=Button(f,text="ESCI DALLA VERSIONE GRAFICA",command=w.destroy)
    disgraph.pack()
    i=Label(f,text="*Questo pulsante fa tornare alla versione testuale dalla shell di Python")
    i.pack()
    w.mainloop()
##### APERTURA FILE ECC.. #####
global st
global f
if not(os.path.exists(r"tabellone.txt")):
    f=open(r"tabellone.txt","w")
    f.close()
if not(os.path.exists(r"settings.txt")):
    sts=open(r"settings.txt","w") #creazione file impostazioni
    st={"g1":"Giocatore 1","g2":"Giocatore 2"} #inizializzazione impostazioni
    ch=list(st.keys())
    i=0
    while i<len(ch):
        val=ch[i]+":"+str(st[ch[i]])+"\n"
        sts.write(val)
        i=i+1
    sts.close()
sts=open(r"settings.txt","r")
r=sts.readlines()
st={}
for c in range(len(r)):
    r[c]=r[c][:len(r[c])-1]
for i in range(len(r)):
    val=r[i].split(":")
    if val[1]=="True" or val[1]=="False":
        val[1]=bool(val[1])
    st[val[0]]=val[1]
sts.close()
global g1
global g2
g1=st["g1"]
g2=st["g2"]
##### MENU PROGRAMMA ##### by GMO e MBA
print("BENVENUTO IN PYTRIS!")
scelta=-1
#Creazione finestra GUI #MBA
welcomegraph()
while (scelta!=-2):
    g1=st["g1"]
    g2=st["g2"]
    print("LE MODALITA' DI GIOCO POSSIBILI SONO:")
    print("\n","0:G1 vs G2")
    print("1:G1 vs PC")
    print("2:G1 vs Super PC")
    print("3: APRI/PASSA ALL' INTERFACCIA GRAFICA")
    print("4: IMPOSTAZIONI")
    print("-2: Esci dal gioco")
    scelta=int(input("Inserisci la tua scelta: "))
    if scelta==0:
        print(modalita1())
    elif (scelta==1):
        print(modalita2())
    elif (scelta==2):
        print(modalita3())
    elif (scelta==3):
        #Creazione finestra GUI #MBA
        welcomegraph()
    elif (scelta==4):
        print("\n","QUALE DELLE SEGUENTI IMPOSTAZIONI VUOI MODIFICARE? (PER MODIFICARE I SIMBOLI DEI GIOCATORI SCRIVERE simboli)")
        print(st)
        scs=str(input("Inserire il nome del parametro da modificare: "))
        while not(scs in st):
            scs=str(input("ERRORE!! Il parametro inserito non esiste!! Reinserirlo corretto: "))
            scs=str(input("Reinserire il nome del parametro da modificare: "))
        if (scs in st and (st[scs]==True or st[scs]==False)):
            nv=bool(input("Inserire il nuovo valore del parametro inserito: "))
            st[scs]=nv
        elif (scs in st):
            nv=str(input("Inserire il nuovo valore del parametro inserito: "))
            st[scs]=nv
        print("SALVATAGGIO AVVENUTO CORRETTAMENTE!","\n")
        ##### AGGIORNAMENTO FILES E CHIUSURA #####
        sts=open(r"settings.txt","w")
        ch=list(st.keys())
        i=0
        while i<len(ch):
            val=ch[i]+":"+str(st[ch[i]])+"\n"    
            sts.write(val)
            i=i+1
        sts.close()
print("GRAZIE PER AVER UTILIZZATO PYTRIS v. 2.2")
