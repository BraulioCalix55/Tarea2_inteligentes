
from http.client import FORBIDDEN


class Matriz:
    
    def __init__(self):
        global Matri
        Matri=[
            ["X"," ","X"," "," "," "],
            [" "," "," "," ","X"," "],
            ["X"," ","X","I"," "," "],
            [" "," ","X","X"," ","X"],
            [" ","X","X"," "," "," "],
            ["S","X"," "," ","X"," "]
                    ]
        return Matri
    def imprimir(self):    
    
        for i in range(6):
            for j in range(6):
                print("[",Matri[i][j],"]", end=" ")
            print()
        print(Matri [2][3],"<-")
        