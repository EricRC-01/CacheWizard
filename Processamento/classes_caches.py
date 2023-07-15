import math



class Cache:

    tam_palavra: int  #Tamanho (em bytes) da palavra
    qnt_palavras: int # quantidade de palavras



    def __init__(self):
        pass


class LivrementeAssociativo(Cache):

    def __init__(self, 
            qnt_palavras: int, 
            qnt_palavra_bloco: int,
            tam_palavra: int,
        ) :
        self.qnt_palavras = qnt_palavras
        self.qnt_palavra_bloco = qnt_palavra_bloco
        self.tam_palavra = tam_palavra


class AssociatvaConjunto(Cache):
    
    qnt_conjuntos: int

    def __init__(self, 
            qnt_palavra_bloco: int,
            qnt_blocos_conjunto: int, 
            qnt_conjuntos: int,
            tam_palavra: int,
        ) :
        self.qnt_blocos_conjunto = qnt_blocos_conjunto
        self.qnt_palavra_bloco = qnt_palavra_bloco
        self.tam_palavra = tam_palavra
        self.qnt_conjuntos = qnt_conjuntos  

class MapeamentoDireto(Cache):
    
    qnt_palavra_bloco: int
    qnt_blocos: int   # Quantidade de blocos

    # A função retorna o endereçamento da memória  
    def __init__(self, 
            qnt_palavras: int, 
            qnt_palavra_bloco: int,
            tam_palavra: int,
        ) :
        self.qnt_palavras = qnt_palavras
        self.qnt_palavra_bloco = qnt_palavra_bloco
        self.tam_palavra = tam_palavra

        self.qnt_blocos = qnt_palavras / qnt_palavra_bloco
        
    