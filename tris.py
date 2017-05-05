from random import randint
def aggiungiMossa(mossa,mossasucc): #mossa=(0,1)
    
    if (mossasucc=="g1"):
        simbolo="O"
        m[int(mossa[0])][int(mossa[1])]=simbolo
    else:
        simbolo="X"
        m[int(mossa[0])][int(mossa[1])]=simbolo

def creatabellone(m):
    cont=0
    print("\t",cont,"\t",cont+1,"\t",cont+2)
    for i in m:
        print(cont, end="\t")
        for d in i:
          print(d,end="\t")
        cont=cont+1
        print()
    print()
f=open(r"tabellone.txt","w")
f.close()
f=open(r"tabellone.txt","r+")
m=[[0,0,0],[0,0,0],[0,0,0]]
global m
f.write(str(m))
def vittoriaono(m,mossasucc):
    if(m[0][0]==m[0][1]==m[0][2]):
        vittoria=True
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if(m[1][0]==m[1][1]==m[1][2]):
        vittoria=True
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if(m[1][0]==m[1][1]==m[1][2]):
        vittoria=True
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if(m[0][0]==m[1][0]==m[2][0]):
        vittoria=True
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if(m[1][0]==m[1][1]==m[1][2]):
        vittoria=True
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if(m[2][0]==m[2][1]==m[2][2]):
        vittoria=True
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if(m[0][0]==m[1][1]==m[2][2]):
        vittoria=True
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    if(m[0][2]==m[1][1]==[2][0]):
        vittoria=True
        if (mossasucc=="g2"):
            simbolovitt="X"
        else:
            simbolovitt="O"
    return simbolovitt
    
def modalita1():
    vittoria=False
    global vittoria
    while (vittoria!=True):
        creatabellone(m)
        if m==[[0,0,0],[0,0,0],[0,0,0]]:
          if (randint(0,1)==0):
            mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
            mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
            mossa1=(mossa1X,mossa1Y)
            mossasucc="g2"
            aggiungiMossa(mossa1,mossasucc)
          else:
            mossa2X=int(input("Giocatore 2, inserisci la riga dove vuoi fare la tua mossa: "))
            mossa2Y=int(input("Giocatore 2, inserisci la colonna dove vuoi fare la tua mossa: "))            
            mossa2=(mossa2X,mossa2Y)
            mossasucc="g1"
            aggiungiMossa(mossa2,mossasucc)
        else:
            if (mossasucc=="g1"):
                mossa1X=int(input("Giocatore 1, inserisci la riga dove vuoi fare la tua mossa: "))
                mossa1Y=int(input("Giocatore 1, inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa1=(mossa1X,mossa1Y)
                mossasucc="g2"
                aggiungiMossa(mossa1,mossasucc)
            else:
                mossa2X=int(input("Giocatore 2, inserisci la riga dove vuoi fare la tua mossa: "))
                mossa2Y=int(input("Giocatore 2, inserisci la colonna dove vuoi fare la tua mossa: "))
                mossa2=(mossa2X,mossa2Y)
                mossasucc="g1"
                aggiungiMossa(mossa2,mossasucc)
        simbolovitt=vittoriaono(m,mossasucc)
        if (simbolovitt=="X"):
            vincitore="g1"
            vittoria=True
            print("G1 HA VINTO!!")
        elif (simbolovitt=="O"):
            vincitore="g2"
            vittoria=True
            print("G2 HA VINTO!!")
    
simbolovitt="L"
global simbolovitt
  
print("BENVENUTO IN TRIS SIMULATOR!")
scelta=-1
while (scelta!=-2):
    print("LE MODALITA' DI GIOCO POSSIBILI SONO:","\n","0:G1 vs G2","\n","1:G1 vs PC","\n","2:G1 vs Super PC","\n","-2: Esci dal gioco")
    scelta=int(input("Inserisci la tua scelta: "))
    if scelta==0:
        g1="X"
        global g1
        g2="O"
        global g2
        print(modalita1())
        
    if (scelta==1):
        print(modalita2())
    if (scelta==2):
        print(modalita3())
