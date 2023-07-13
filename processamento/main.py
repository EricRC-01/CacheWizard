import classes_caches as cache
import classe_endereco as end






def main():


    qnt_bits_enderecar = int(input("insira a quantidade de bits: ")) 

    qnt_palavras = int(input("Insira a quantidade de palavras: "))
    tam_palavra = int(input("insira o tamanho da palavra (em bytes): "))
    qnt_palava_bloco = int(input("insira a quantidade de palavras por bloco: "))

    qnt_conjuntos = int(input("insira a quantidade de conjuntos: "))



    # Associativo
    if qnt_conjuntos == 1:
        pass


    # Associativo por conjunto
    elif qnt_conjuntos > 1:
        pass


    # Mapeamento direto
    else:
        nova_cache = cache.MapeamentoDireto(qnt_bits_enderecar, qnt_palavras, qnt_palava_bloco, tam_palavra)
        print()
        print()

        print("Printando o Tag", nova_cache.enderecoTag())
        print()

        print("Printando o Indice", nova_cache.enderecoIndice())
        print()

        print("Printando o byteoffset", nova_cache.enderecoByteoffset())
        print()



        






if __name__ == '__main__':
    main()


