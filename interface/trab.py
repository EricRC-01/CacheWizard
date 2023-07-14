import tkinter as tk
import cacheInterface as ci
import sys

sys.path.append('processamento')

import classes_caches as cache
import classe_endereco as end



# Função para caclular o endereçamento de um level de uma cache  
def calcCache(
        qnt_palavra_bloco, 
        qnt_conjuntos, 
        tam_palavra, 
        qnt_blocos,
        qnt_bits_enderecar,
        tipo_cache #[1: livremente associativo, 2: Por Ass conjunto, 3: Mapeamento direto ]
    ):

    novo_enderecamento: end
    qnt_palavras = qnt_blocos * qnt_palavra_bloco 
    
    # Livremente Associativo
    if tipo_cache == 1: pass
    if qnt_conjuntos == 1:
        print()
        print()

        cache_liv_associativa = cache.LivrementeAssociativo(qnt_palavras, qnt_palavra_bloco, tam_palavra)
        novo_enderecamento = end.Endereco(cache_liv_associativa, qnt_bits_enderecar, True)

        print(novo_enderecamento)




    # Associativo por conjunto
    if tipo_cache == 2: pass
    elif qnt_conjuntos > 1:
        print()
        print()

        cache_associativo_con = cache.AssociatvaConjunto(qnt_palavras, qnt_palavra_bloco, tam_palavra, qnt_conjuntos)        
        novo_enderecamento = end.Endereco(cache_associativo_con, qnt_bits_enderecar, False)

        print()
        print(novo_enderecamento)


    # Mapeamento direto
    if tipo_cache == 3: pass
    else:
        print()
        print()

        cache_map_direto = cache.MapeamentoDireto(qnt_palavras, qnt_palavra_bloco, tam_palavra)
        novo_enderecamento = end.Endereco(cache_map_direto, qnt_bits_enderecar, False)

        print()
        print(novo_enderecamento)

    return novo_enderecamento



def Submit(L1,L2,L3,tamPalavra):
    print(L1.get())


    l1 = L1.get()
    l2 = L2.get()
    l3 = L3.get()

    # Converter o tamanhho da palavra na quantidade de bits de endereçamento
    qnt_bits_enderecar = tamPalavra  
    # Mudar o tamanho da palavra pra quantidade de bits
    tam_palavra = tamPalavra/8

    # Calcular endereçamento
    enderecamento_L1 = calcCache(l1[0], l1[2], tam_palavra, l1[1], qnt_bits_enderecar)
    enderecamento_L2 = calcCache(l2[0], l2[2], tam_palavra, l2[1], qnt_bits_enderecar)
    enderecamento_L3 = calcCache(l3[0], l3[2], tam_palavra, l3[1], qnt_bits_enderecar)


root = tk.Tk()

root.geometry("1920x1080")

parametros = tk.Frame(root,height = 500)

l1 = tk.Frame(parametros)
L1 = ci.CacheInterface('cache L1',l1)
L1.pack()
l1.pack(side = 'top')

l2 = tk.Frame(parametros)
L2 = ci.CacheInterface('cache L2',l2)
L2.pack()
l2.pack(side = 'top')

l3 = tk.Frame(parametros)
L3 = ci.CacheInterface('cache L3',l3)
L3.pack()
l3.pack(side = 'top')

parametros.pack(side = 'top')

variable = tk.StringVar(root,'Tamanho da Palavra')
optTamPalavra = tk.OptionMenu(root,variable,*[8,16,32,64])
optTamPalavra.config(width = 20)
optTamPalavra.pack()

submit = tk.Button(root,text='Submit',command = lambda: Submit(L1,L2,L3, int(variable.get())))
submit.pack()




root.mainloop()




