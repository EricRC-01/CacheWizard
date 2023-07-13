
class Endereco:
    tag: int 
    byte_ofset: int
    indice: int


    def __init__(self, byte_ofset, tag, indice = -1):
        self.byte_ofset = byte_ofset
        self.tag = tag 
        self.indice = indice

    def __str__(self) -> str:
        str_final = "[ Tag: "
        str_final += str(self.tag) + " | "

        str_final += "Byte offset: " + str(self.byte_ofset) 

        if self.indice != -1:
            str_final += " | "
            str_final += "Indice: " + str(self.indice) 
        
        str_final += + "]"

        return str_final

