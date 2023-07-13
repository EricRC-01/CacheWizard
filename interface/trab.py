import tkinter as tk
import cacheInterface as ci
import sys

sys.path.append('processamento')

import classes_caches as cache
import classe_endereco as end


def calcCache(qnt_palavra_bloco, qnt_conjuntos, tam_palavra, qnt_blocos,qnt_bits_enderecar):

    qnt_palavras = qnt_blocos * qnt_palavra_bloco 
    
    # Associativo
    if qnt_conjuntos == 1:
        pass


    # Associativo por conjunto
    elif qnt_conjuntos > 1:
        pass


    # Mapeamento direto
    else:
        cache_map_direto = cache.MapeamentoDireto(qnt_palavras, qnt_palavra_bloco, tam_palavra)
        print()
        print()

        novo_enderecamento = end.Endereco(cache_map_direto, qnt_bits_enderecar, False)
        print()
        print(novo_enderecamento)



def Submit(L1,L2,L3,tamPalavra):
    print(L1.get())


    l1 = L1.get()

    qnt_bits_enderecar = tamPalavra #Pode ser melhor definir como 32 por padrão 
    tam_palavra = tamPalavra/8
    print("tam_palavra = ", tam_palavra)


    calcCache(l1[0], l1[2], tam_palavra, l1[1], qnt_bits_enderecar)


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




