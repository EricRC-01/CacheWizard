from abc import ABC, abstractmethod
import classes_caches as cache
import math



class Endereco:
    qnt_bits_endereco: int
    tag: int 
    byte_offset: int
    indice: int


    def __init__(self, nova_cache: cache.Cache, qnt_bits_endereco: int, livremente_associativo = False):

        self.qnt_bits_endereco = qnt_bits_endereco

        self.byte_offset = self.bitssByteoffset(nova_cache.tam_palavra)
        
        if not livremente_associativo:
            self.indice = self.bitssIndice(nova_cache.qnt_blocos)
        
        else:
            self.indice = -1


        self.tag = self.bitssTag()

    def __str__(self) -> str:
        str_final = "[ Tag: "
        str_final += str(self.tag) + " | "

        str_final += "Byte offset: " + str(self.byte_offset) 

        if self.indice != -1:
            str_final += " | "
            str_final += "Indice: " + str(self.indice) 
        
        str_final += "]"

        return str_final

    # Retorna o número nescessario de bits para endereçar o byteoffset 
    def bitssByteoffset(self, tam_palavra: int):
        return math.log(tam_palavra, 2)
    
    # Retorna o número nescessario de bits para endereçar o indice 
    def bitssIndice(self, qnt_blocos: int):
        return math.log(qnt_blocos, 2)

    # Retorna o número nescessario de bits para endereçar o indice 
    def bitssIndiceConjunto(self, qnt_conjunto: int):
        return math.log(qnt_conjunto, 2)

    # Retorna o número nescessario de bits para endereçar a tag 
    def bitssTag(self):
        return self.qnt_bits_endereco - self.byte_offset - self.indice

