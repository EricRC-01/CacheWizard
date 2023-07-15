import tkinter as tk
from tkinter import messagebox
from Processamento.classe_endereco import *
from Processamento.classes_caches import *
from Interface.cacheGUI import *



corBg = '#8f7f7e'
textoInfo = 'Lembre-se que apesar de dividirmos em três tipos, o mapeamento direto e o mapeamento associativo\n\
             são apenas casos particulares do mapeamento associativo por conjunto. Ou seja:\n\
             * Quando quantidade de conjuntos = 1 -> mapeamento associativo\n\
             * Quando quantidade de blocos por conjunto = 1 -> mapeamento direto'


def calcular_divisao(bin1,c1,c2,c3,t1,t2,t3,tam,canvas):

    canvas.delete("all")

    try:
        binario = bin(int(bin1))[2:]
        binario = binario.zfill(tam)

        if len(binario) > tam:
            messagebox.showerror('Entrada Inválida','Valor decimal digitado excede os limites da palavra')
            return

    
        cacheAux = AssociatvaConjunto(*c1.get(),tam)
        end = Endereco(cacheAux,tam)

        byteOffset = end.byte_offset
        qtdBlocos = 0

        wordOffset = end.word_offset
        index = end.indice
        t1.atualizarBits(byteOffset,wordOffset,index, tam - byteOffset - wordOffset - index)
        mostrarEndereco(binario,(wordOffset,qtdBlocos,index),byteOffset,tam,canvas,30)

        cacheAux = AssociatvaConjunto(*c2.get(),tam)
        end = Endereco(cacheAux,tam)
        wordOffset = end.word_offset
        index = end.indice
        t2.atualizarBits(byteOffset,wordOffset,index, tam - byteOffset - wordOffset - index)
        mostrarEndereco(binario,(wordOffset,qtdBlocos,index),byteOffset,tam,canvas,110)

        cacheAux = AssociatvaConjunto(*c3.get(),tam)
        end = Endereco(cacheAux,tam)
        wordOffset = end.word_offset
        index = end.indice
        t3.atualizarBits(byteOffset,wordOffset,index, tam - byteOffset - wordOffset - index)
        mostrarEndereco(binario,(wordOffset,qtdBlocos,index),byteOffset,tam,canvas,190)
    except:
        messagebox.showerror('Entrada Inválida','Preencha os valores corretamente')

def mostrarEndereco(binario,dados,bOffset,tamPalavra,canvas,posVertical):
    # Posicionamento inicial
    y = posVertical
    x = ((1920/20) - tamPalavra) * 10

    byteOffset = bOffset
    wordOffset = dados[0]
    index = dados[2]

    for i, char in enumerate(binario):
        if len(binario) - i > byteOffset + wordOffset + index:
            color = 'red'
        elif len(binario) - i > byteOffset + wordOffset:
            color = 'blue'
        elif len(binario) - i > byteOffset:
            color = 'purple'
        else:
            color = 'orange'

        canvas.create_text(x, y, text=char, font=("Arial", 20),fill = color)
        x += 20

def on_shift_keypress(event):
    # Verificar se a tecla Shift foi pressionada
    if event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
        # Verificar se o widget atual é um Entry
        if isinstance(event.widget, tk.Entry):
            # Mover o foco para o próximo widget Entry
            event.widget.tk_focusNext().focus_set()

def showInfo(label):
    label.configure(foreground = 'black')

def hideInfo(label):
    label.configure(foreground = corBg)

# Criação da janela principal
window = tk.Tk()
window.geometry("1920x1080")
window.minsize(width=1200, height=600)
window.state("zoomed")
window.title("CacheWizard")
window.configure(background= corBg)
window.bind('<Shift-KeyPress>', on_shift_keypress)

fr = tk.Frame(window,background= corBg,borderwidth=0,pady = 10,width= 1920)

# Criação do OptionMenu para selecionar o tamanho da palavra
option_var = tk.StringVar(fr)
option_var.set("32")  # Valor padrão

tamanho_palavra_label = tk.Label(fr, text="Tamanho da Palavra:",font = ("Arial",14,'bold'),background= corBg)
tamanho_palavra_label.grid(row=1, column=0,columnspan=1)
tamanho_palavra_option = tk.OptionMenu(fr, option_var, "16", "32", "64")
tamanho_palavra_option.configure(width = 2,borderwidth=0)
tamanho_palavra_option.grid(row=1, column=1, columnspan=1,sticky='w',padx = 25)

# Criação das caches
cache1 = CacheInterface(fr, 2,1)
cache2 = CacheInterface(fr, 3,2)
cache3 = CacheInterface(fr, 4,3)

canvas = tk.Canvas(window, width=1920, height=200, background= corBg,borderwidth=0,bd = 0,highlightthickness=0)

# label e entry para receber qual o endereço
palavraLabel = tk.Label(fr,text = 'Endereço (em decimal):',font = ("Arial",13,'bold'),background=corBg)
palavraLabel.grid(row=5, column = 2)
palavra = tk.Entry(fr)
palavra.grid(row=5, column = 3)

# criação botao
imageBtn = tk.PhotoImage(file='Interface/button_calcular.png')
calcular_button = tk.Button(fr,image=imageBtn,borderwidth=0,background=corBg,activebackground=corBg)
calcular_button.grid(row=6, columnspan=7, pady=40)

# ajuste do tamanho das colunas
fr.grid_columnconfigure(1,minsize=200)
fr.grid_columnconfigure(3,minsize=200)
fr.grid_columnconfigure(5,minsize=200)
fr.pack(side='top')

# # Criação do canvas para o texto
canvas.pack()

# frame dos resultados de cada cache + labelInformação
frameRes = tk.Frame(window,background=corBg)
cL1 = cacheFrame(frameRes,0,1)
cL2 = cacheFrame(frameRes,1,2)
cL3 = cacheFrame(frameRes,2,3)
frameRes.pack(side = 'top', pady = (150,0))

# Botao mostrar informação
imageInfo = tk.PhotoImage(file='Interface/info2.png')
imageInfo = imageInfo.subsample(round(50/512 * 100))
btnInfo = tk.Button(window,image = imageInfo,background=corBg,activebackground=corBg,borderwidth=0)
btnInfo.pack(side = 'left')
btnInfo.configure(state='active')

tooltip = CreateToolTip(btnInfo,textoInfo)


# btnInfo.bind('<Enter>',lambda self: labelInfo.configure(foreground = 'black'))
# btnInfo.bind('<Leave>',lambda self: labelInfo.configure(foreground = corBg))


# Execução da interface
calcular_button.configure(command = lambda: calcular_divisao(palavra.get(),cache1,cache2,cache3,cL1,cL2,cL3,int(option_var.get()),canvas)) # configurar metodo do botao
window.bind('<Return>', lambda self: calcular_divisao(palavra.get(),cache1,cache2,cache3,cL1,cL2,cL3,int(option_var.get()),canvas)) # apertar enter = apertar botao
window.mainloop()
