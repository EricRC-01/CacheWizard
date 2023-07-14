import classes_caches as cache
import classe_endereco as end





# Função para caclular o endereçamento de um level de uma cache  
def calcCache(
        qnt_palavra_bloco, 
        qnt_conjuntos, 
        tam_palavra, 
        qnt_blocos,
        qnt_bits_enderecar,
        tipo_cache #  1: livremente associativo, 2: Por Ass conjunto, 3: Mapeamento direto 
    ):

    novo_enderecamento: end
    qnt_palavras = qnt_blocos * qnt_palavra_bloco 
    
    # Livremente Associativo
    #if tipo_cache == 1: pass
    if qnt_conjuntos == 1:
        print()
        print()

        cache_liv_associativa = cache.LivrementeAssociativo(qnt_palavras, qnt_palavra_bloco, tam_palavra)
        novo_enderecamento = end.Endereco(cache_liv_associativa, qnt_bits_enderecar, True)

        print(novo_enderecamento)




    # Associativo por conjunto
    #elif tipo_cache == 2: pass
    elif qnt_conjuntos > 1:
        print()
        print()

        cache_associativo_con = cache.AssociatvaConjunto(qnt_palavras, qnt_palavra_bloco, tam_palavra, qnt_conjuntos)        
        novo_enderecamento = end.Endereco(cache_associativo_con, qnt_bits_enderecar, False)

        print()
        print(novo_enderecamento)


    # Mapeamento direto
    #elif tipo_cache == 3: pass
    else:
        print()
        print()

        cache_map_direto = cache.MapeamentoDireto(qnt_palavras, qnt_palavra_bloco, tam_palavra)
        novo_enderecamento = end.Endereco(cache_map_direto, qnt_bits_enderecar, False)

        print()
        print(novo_enderecamento)

    # else: print("comando (tipo de cache) não reconhcido")



    return novo_enderecamento





def main():

    
    # Entrada da linha 1
    print("insira a quantidade de bits: ")
    qnt_bits_enderecar = int(input()) 
    
    # Entrada da linha 2
    print("Insira a quantidade de palavras: ")
    qnt_palavras = int(input())
    
    # Entrada da linha 3
    print("insira o tamanho da palavra (em bytes): ")
    tam_palavra = int(input())
    
    # Entrada da linha 4
    print("insira a quantidade de palavras por bloco: ")
    qnt_palavra_bloco = int(input())
    
    # Entrada da linha 5 
    print("insira a quantidade de conjuntos: ")
    qnt_conjuntos = int(input())


    #Caclulo da quantidade de blocos 
    qnt_blocos = qnt_palavras/qnt_palavra_bloco 
    
    #Obs. outra forma de fazer isso seria:
    # qnt_palavras = qnt_blocos * qnt_palavra_bloco 

    enderecoL1 = calcCache(qnt_palavra_bloco, qnt_conjuntos, tam_palavra, qnt_blocos, qnt_bits_enderecar, 1)
    enderecoL2 = calcCache(qnt_palavra_bloco, qnt_conjuntos, tam_palavra, qnt_blocos, qnt_bits_enderecar, 2)
    enderecoL3 = calcCache(qnt_palavra_bloco, qnt_conjuntos, tam_palavra, qnt_blocos, qnt_bits_enderecar, 3)


if __name__ == '__main__':
    main()