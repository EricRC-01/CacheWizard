import tkinter as tk

class CacheInterface:

    def __init__(self,nome,root):
        self.frameCache = tk.Frame(root,highlightthickness = True,bd = 3,height = 10)
        self.frameCache.pack_propagate(True)

        self.labelNome = tk.Label(self.frameCache,text = nome,font = ("Arial",15))

        self.labelQtdPalavras = tk.Label(self.frameCache,text = 'Quantidade de palavras p/ bloco: ')
        self.labelQtdConjuntos = tk.Label(self.frameCache,text = 'Quantidade de conjuntos: ')
        self.labelQtdBlocos = tk.Label(self.frameCache,text = 'Quantidade de blocos: ')
                
        self.txtQtdPalavras = tk.Text(self.frameCache,height = 1,width = 10)
        self.txtQtdConjuntos = tk.Text(self.frameCache,height = 1,width = 10)
        self.txtQtdBlocos = tk.Text(self.frameCache,height = 1,width = 10)

       
    def pack(self):

        self.labelNome.pack(side='left')

        self.labelQtdPalavras.pack(side='left')
        self.txtQtdPalavras.pack(side='left')

        self.labelQtdBlocos.pack(side = 'left')
        self.txtQtdBlocos.pack(side = 'left')

        self.labelQtdConjuntos.pack(side = 'left')
        self.txtQtdConjuntos.pack(side = 'left')

        
        self.frameCache.pack(side = 'left')

    def get(self):
        try:
            res = (int(self.txtQtdPalavras.get('1.0','end-1c')),int(self.txtQtdBlocos.get('1.0','end-1c')),int(self.txtQtdConjuntos.get('1.0','end-1c')))
            return res
        except:
            print("Os valores devem ser inteiros")

        return None
    

    
