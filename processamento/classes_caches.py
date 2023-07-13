import math



class Cache:

    qnt_bits_enderecar: int
    tam_palavra: int

    qnt_bits_tag: int
    qnt_bits_byteoffset: int
    

    def __init__(self):
        pass



class MapeamentoDireto(Cache):
    
    
    qnt_bits_indices: int
    
    qnt_palavras: int # quantidade de palavras 
    qnt_palava_bloco: int # quantidade de palavras por bloco 
    qnt_blocos: int # quantidade de blocos

    # A função retorna o endereçamento da memória  
    def __init__(self, 
            qnt_bits_enderecar: int, 
            qnt_palavras: int, 
            qnt_palava_bloco: int,
            tam_palavra: int
        ) :

        self.qnt_palavras = qnt_palavras
        self.qnt_palava_bloco = qnt_palava_bloco
        self.qnt_blocos = self.qnt_palava_bloco
        self.qnt_blocos = qnt_palavras / qnt_palava_bloco
        self.tam_palavra = tam_palavra
        self.qnt_bits_enderecar = qnt_bits_enderecar



    def enderecoByteoffset(self):
        #Resultado em bits 
        return math.log( self.tam_palavra, 2)
    
    def enderecoIndice(self):
        #Resultado em bits
        return math.log( self.qnt_blocos, 2)

    def enderecoTag(self):
        return self.qnt_bits_enderecar - self.enderecoByteoffset() - self.enderecoIndice()

















