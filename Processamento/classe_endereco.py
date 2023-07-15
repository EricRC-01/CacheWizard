import Processamento.classes_caches as cache
from math import *



class Endereco:
    qnt_bits_endereco: int
    tag: int 
    byte_offset: int
    indice: int


    def __init__(self, nova_cache: cache.Cache, qnt_bits_endereco: int, livremente_associativo = False):

        self.qnt_bits_endereco = qnt_bits_endereco
        self.word_offset = self.bitssWordOffset(nova_cache.qnt_palavra_bloco)

        self.byte_offset = self.bitssByteoffset(nova_cache.tam_palavra)
        
        self.indice = 0
        if not livremente_associativo:
            self.indice = self.bitssIndice(nova_cache.qnt_conjuntos)
            


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
        return ceil(log(tam_palavra/8, 2))
    
    # Retorna o número nescessario de bits para endereçar o wordOffset
    def bitssWordOffset(self,qtd_palavras):
        return ceil(log(qtd_palavras,2))
    
    # Retorna o número nescessario de bits para endereçar o indice 
    def bitssIndice(self, qnt_blocos: int):
        return ceil(log(qnt_blocos, 2))

    # Retorna o número nescessario de bits para endereçar o indice 
    def bitssIndiceConjunto(self, qnt_conjunto: int):
        return ceil(log(qnt_conjunto, 2))

    # Retorna o número nescessario de bits para endereçar a tag 
    def bitssTag(self):
        return self.qnt_bits_endereco - self.byte_offset - self.indice

