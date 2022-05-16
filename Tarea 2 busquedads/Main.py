from webbrowser import get
from Arbol import arbol
from Arbol import casilla
from Matriz import Matriz
#arbo=arbol.creararbol()
#arbol.imprime(arbo)
matris=Matriz.__init__(0)
#Matriz.imprimir(matris)
#Matriz.imprimir(0)
casillas=[]
##implementacion antigua para ver casillas
#casillas.append(casilla("2,3",["1,3","2,4"]))
#casillas.append(casilla("2,4",["2,3","2,5","3,4"]))
#casillas.append(casilla("2,5",["1,5","2,4"]))
#for i in casillas:
#    i.ver()
    
#si ya se que se en la matriz cada casilla tiene  sus vecionos, voy a recorrer toda la matriz
#creando una casilla en cada iteracion, dando el nombre, que sera la (x,y) actual y asignando
#vecinos con x+1 x-1 y+1 y-1 para sacar los cuatro vecinos, si un vecino tiene una "X"
#no los agregare 
#porque in range(6)? porque ya se el tamano de la matriz
print("antes del for")
cont=0
for i in range(6):
    for j in range(6):
        if matris[i][j]!="X" and i+1<6 and j+1<6 and i-1>-1 and j-1>-1:
            a=i,j
            a=str(a)
            a=a.replace(" ","")
            casillas.append(casilla(a)) 
            if matris [i-1][j]!="X":
                a=i-1,j
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if matris [i+1][j]!="X":
                a=i+1,j
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if matris [i][j-1]!="X":
                a=i,j-1
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if matris [i][j+1]!="X":
                a=i,j+1
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            cont+=1   
        if matris [i][j]!="X"and i==0:
            a=i,j
            a=str(a)
            a=a.replace(" ","")
            casillas.append(casilla(a))  
            if matris [i+1][j]!="X":
                a=i+1,j
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if j<5 and matris [i][j+1]!="X":
                a=i,j+1
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if j>0 and matris[i][j-1]!="X":
                a=i,j-1
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            cont+=1
        if j==0 and matris [i][j]!="X" :
            a=i,j
            a=str(a)
            a=a.replace(" ","")
            casillas.append(casilla(a)) 
            if i<5 and matris [i+1][j]!="X":
                a=i+1,j
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if matris [i][j+1]!="X":
                a=i,j+1
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if i>0 and matris [i-1][j]!="X":
                a=i-1,j
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            cont+=1
        if j==5 and matris [i][j]!="X" :
            a=i,j
            a=str(a)
            a=a.replace(" ","")
            casillas.append(casilla(a)) 
            if i<5 and matris [i+1][j]!="X":
                a=i+1,j
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if matris [i][j-1]!="X":
                a=i,j-1
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            if i>0 and matris [i-1][j]!="X":
                a=i-1,j
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            cont+=1
        if matris [i][j]!="X"and i==5:
            a=i,j
            a=str(a)
            a=a.replace(" ","")
            casillas.append(casilla(a))  
            if matris [i-1][j]!="X":
                a=i-1,j
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            elif j<5 and matris [i][j+1]!="X":
                a=i,j+1
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            elif j>0 and matris[i][j-1]!="X":
                a=i,j-1
                a=str(a)
                a=a.replace(" ","")
                casillas[cont].add_vecino(a)
            cont+=1  
             
#for v in casillas:
 #   print (v.nombre)
  #  for b in v.get_vecinos():
   #     print ("--",b)
print (casillas.__len__())
print ("posicion inicial: ")
Incio = input()
Incio=str(Incio)
print ("posicion final: ")
meta=input()
meta=str(meta)
print ("in: ",Incio, "final: ",meta)
 