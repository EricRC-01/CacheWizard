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

    def bitssByteoffset(self, tam_palavra: int):
        #Resultado em bits 
        return math.log(tam_palavra, 2)
    
    def bitssIndice(self, qnt_blocos: int):
        #Resultado em bits
        return math.log(qnt_blocos, 2)

    def bitssTag(self):
        return self.qnt_bits_endereco - self.byte_offset - self.indice

