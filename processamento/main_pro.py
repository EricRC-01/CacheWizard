import classes_caches as cache
import classe_endereco as end



def main():

    #1
    qnt_bits_enderecar = int(input("insira a quantidade de bits: ")) 
    #2
    qnt_palavras = int(input("Insira a quantidade de palavras: "))
    #3
    tam_palavra = int(input("insira o tamanho da palavra (em bytes): "))
    #4
    qnt_palavra_bloco = int(input("insira a quantidade de palavras por bloco: "))
    #5 
    qnt_conjuntos = int(input("insira a quantidade de conjuntos: "))


    # Livremente Associativo
    if qnt_conjuntos == 1:
        print()
        print()

        cache_liv_associativa = cache.LivrementeAssociativo(qnt_palavras, qnt_palavra_bloco, tam_palavra)
        novo_enderecamento = end.Endereco(cache_liv_associativa, qnt_bits_enderecar, True)

        print(novo_enderecamento)




    # Associativo por conjunto
    elif qnt_conjuntos > 1:
        print()
        print()

        cache_associativo_con = cache.AssociatvaConjunto(qnt_palavras, qnt_palavra_bloco, tam_palavra, qnt_conjuntos)        
        novo_enderecamento = end.Endereco(cache_associativo_con, qnt_bits_enderecar, False)

        print()
        print(novo_enderecamento)


    # Mapeamento direto
    else:
        print()
        print()

        cache_map_direto = cache.MapeamentoDireto(qnt_palavras, qnt_palavra_bloco, tam_palavra)
        novo_enderecamento = end.Endereco(cache_map_direto, qnt_bits_enderecar, False)

        print()
        print(novo_enderecamento)







        






if __name__ == '__main__':
    main()


