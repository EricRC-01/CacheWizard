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
        cache_map_direto = cache.MapeamentoDireto(qnt_palavras, qnt_palava_bloco, tam_palavra)
        print()
        print()

        novo_enderecamento = end.Endereco(cache_map_direto, qnt_bits_enderecar, False)
        print()
        print(novo_enderecamento)




        






if __name__ == '__main__':
    main()


