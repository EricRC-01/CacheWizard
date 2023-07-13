import math



class Cache:

    tam_palavra: int
    qnt_palavras: int # quantidade de palavras

    qnt_blocos: int 



    def __init__(self):
        pass


class Associativo(Cache):
    pass


class MapeamentoDireto(Cache):
    
    qnt_palavras_bloco: int

    # A função retorna o endereçamento da memória  
    def __init__(self, 
            qnt_palavras: int, 
            qnt_palavras_bloco: int,
            tam_palavra: int,
        ) :
        self.qnt_palavras = qnt_palavras
        self.qnt_palavras_bloco = qnt_palavras_bloco
        self.tam_palavra = tam_palavra

        self.qnt_blocos = qnt_palavras / qnt_palavras_bloco
        
        
















