###########################
#                         #
#           TRIS          #
#    written in Python    #
#        v. 2.1.1b        #
#                         #
###########################

from tkinter import *
import tkinter.messagebox
from random import randint
import os.path
def savesettings(): #MBA
    if s1in.get()!=s2in.get():
        st["simbolo_g1"]=s1in.get()
        st["simbolo_g2"]=s2in.get()
        tkinter.messagebox.showinfo(title="SALVATAGGIO RIUSCITO",message="SALVATAGGIO AVVENUTO CON SUCCESSO!")
    else:
        tkinter.messagebox.showerror(title="SIMBOLI IN CONFLITTO!",message="Hai inserito due simboli uguali.")
def settingsgraph(): #MBA
    w1=Tk()
    w1.title("PYTRIS IMPOSTAZIONI")
    f1=Frame(w1)
    f1.pack()
    toptext=Label(f1,text="IMPOSTAZIONI:")
    toptext.pack()
    fs=Frame(f1)
    fs.pack()
    s1=Label(fs,text="Simbolo del giocatore 1: ")
    s2=Label(fs,text="Simbolo del giocatore 2: ")
    s1.grid(row=0,column=0)
    s2.grid(row=1,column=0)
    s1in=Entry(fs,text=st["simbolo_g1"])
    s1in.grid(row=0,column=1)
    s2in=Entry(fs)
    s2in.grid(row=1,column=1)
    bsave=Button(fs,text="SALVA",command=savesettings)
    bsave.grid(row=2,column=0)
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
    mod1=Button(f,text="Modalità 1: G1 VS G2",command=modalita1)
    mod1.pack()
    mod2=Button(f,text="Modalità 2: G1 VS PC",command=modalita2)
    mod2.pack()
    mod3=Button(f,text="Modalità 3: G1 VS SUPER PC",command=modalita3)
    mod3.pack()
    settings=Button(f,text="IMPOSTAZIONI",command=settingsgraph)
    settings.pack()
    disgraph=Button(f,text="ESCI DALLA VERSIONE GRAFICA",command=w.destroy)
    disgraph.pack()
    i=Label(f,text="*Questo pulsante fa tornare alla versione testuale dalla shell di Python")
    i.pack()
    w.mainloop()
def tabgraph(m): #MBA
    p=0
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
def modalita1(g1,g2,f): #MBA e TBO
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
        elif (controllotabpieno(m)==True):
            print("\n","NESSUN GIOCATORE HA VINTO! ANDRA' MEGLIO LA PROSSIMA VOLTA!!")
            creatabellone(m)
            break
        #Scrittura su file del numero del tabellone
        ts=""
        i=0
        while (i<len(m)): # m=[["X","O",""],["O","","X"],..],.. => "XO O X
            c=0
            while (c<len(m[i])):
                s=m[i][c]
                if (s==""):
                    s==" "
                ts=ts+s
                c+=1
            i+=1
        f.write(ts+"\n")
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
def attaccocasuale(m,mossasucc): #GMO e MBA
    riga=randint(0,2)
    colonna=randint(0,2)
    while (m[riga][colonna]=="X" or m[riga][colonna]=="O"):
        riga=randint(0,2)
        colonna=randint(0,2)
    mossa2=(riga,colonna)
    aggiungiMossa(m,mossa2,mossasucc)
def modalita2(g1,f): #MBA, GMO, TBO, RCE
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
                if (controllocelle(m)==False):
                    if (controllocellenemiche(m)==False):
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
                c1=controllocellenemiche(m)
                if (c1==False):
                    c2=controllocelle(m)
                    if (c2==False):
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
        elif (controllotabpieno(m)==True):
            print("\n","NESSUN GIOCATORE HA VINTO! ANDRA' MEGLIO LA PROSSIMA VOLTA!!")
            creatabellone(m)
            break
        #Scrittura su file del numero del tabellone
        ts=""
        i=0
        while (i<len(m)): # m=[["X","O",""],["O","","X"],..],.. => "XO O X
            c=0
            while (c<len(m[i])):
                s=m[i][c]
                if (s==""):
                    s==" "
                ts=ts+s
                c+=1
            i+=1
        f.write(ts+"\n")
    f.close()
    print()
    return "PARTITA TERMINATA"
def controllotabellone(cont): #TBO e RCE
    mold=[]
    mold1=[]                                 #f="XO ,O X, OX" mold1=["XO "] mold=[X,O,""]
    riga=f.readline()
    cont2=0
    while (riga!=""):
        while (cont2<cont):
            riga=f.readline()
            cont2=cont2+1
        while (len(riga[0:3])-1>cont):
            mold1.append(riga[cont])
            if (cont==2):
                mold.append(mold1)
                mold1=[]
            cont=cont+1
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
            i1=i1+1
            cont2=cont2+1
            if (i1==2 or cont2==2):
                i=i+1
                cont=cont+1
                i1=0
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
                if (m==controllotabellone(0)):
                    mOld=controllotabellone(1)
                    attaccoByTabVecchio(m,mOld)
                elif (controllocelle(m)==False):
                    if (controllocellenemiche(m)==False):
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
                c1=controllocellenemiche(m)
                if (c1==False):
                    c2=controllocelle(m)
                    if (c2==False):
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
        elif (controllotabpieno(m)==True):
            print("\n","NESSUN GIOCATORE HA VINTO! ANDRA' MEGLIO LA PROSSIMA VOLTA!!")
            creatabellone(m)
            break
        #Scrittura su file del numero del tabellone
        ts=""
        i=0
        while (i<len(m)): # m=[["X","O",""],["O","","X"],..],.. => "XO O X
            c=0
            while (c<len(m[i])):
                s=m[i][c]
                if (s==""):
                    s==" "
                ts=ts+s
                c+=1
            i+=1
        f.write(ts+"\n")
    f.close()
    print()
    return "PARTITA TERMINATA"
##### APERTURA FILE ECC.. #####
global st
global f
if not(os.path.exists(r"tabellone.txt")):
    f=open(r"tabellone.txt","w")
    f.close()
if not(os.path.exists(r"settings.txt")):
    sts=open(r"settings.txt","w") #creazione file impostazioni
    st={"simbolo_g1":"X","simbolo_g2":"O"} #inizializzazione impostazioni
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
g1=st[list(st.keys())[0]]
g2=st[list(st.keys())[1]]
##### MENU PROGRAMMA ##### by GMO e MBA
print("BENVENUTO IN PYTRIS!")
scelta=-1
#Creazione finestra GUI #MBA
welcomegraph()
while (scelta!=-2):
    print("LE MODALITA' DI GIOCO POSSIBILI SONO:")
    print("\n","0:G1 vs G2")
    print("1:G1 vs PC")
    print("2:G1 vs Super PC")
    print("3: APRI/PASSA ALL' INTERFACCIA GRAFICA")
    print("4: IMPOSTAZIONI")
    print("-2: Esci dal gioco")
    scelta=int(input("Inserisci la tua scelta: "))
    if scelta==0:
        print(modalita1(g1,g2))
    elif (scelta==1):
        print(modalita2(g1))
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
        while (scs=="simbolo_g1" or scs=="simbolo_g2"):
            print("ATTENZIONE!!! SCRIVERE simboli PER MODIFICARE I SIMBOLI")
            scs=str(input("Reinserire il nome del parametro da modificare: "))
        if (scs in st and (st[scs]==True or st[scs]==False)):
            nv=bool(input("Inserire il nuovo valore del parametro inserito: "))
            st[scs]=nv
        elif (scs in st):
            nv=str(input("Inserire il nuovo valore del parametro inserito: "))
            st[scs]=nv
        elif (scs=="simboli"):
            sg1=str(input("Inserire il simbolo del giocatore 1: "))
            sg2=str(input("Inserire il simbolo del giocatore 2: "))
            st["simbolo_g1"]=sg1.upper()
            st["simbolo_g2"]=sg2.upper()
        print("SALVATAGGIO AVVENUTO CORRETTAMENTE!","\n")
print("GRAZIE PER AVER UTILIZZATO PYTRIS v. 2.1.1b")
##### AGGIORNAMENTO FILES E CHIUSURA #####
sts=open(r"settings.txt","w")
ch=list(st.keys())
i=0
while i<len(ch):
    val=ch[i]+":"+str(st[ch[i]])+"\n"    
    sts.write(val)
    i=i+1
sts.close()
