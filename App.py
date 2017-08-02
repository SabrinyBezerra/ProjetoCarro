from Carro import Carro
from Hibrido import *

def main():
    carro1 =  Carro ("Branco", "fox", "2017")
    carro2 = Carro ("preto","siena","2016")
    carro3 = carro1
    print(carro1)
    print(carro2)
    print(carro3)

    if __name__=="__main__":
        main()
