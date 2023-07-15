import tkinter as tk
corBg = '#8f7f7e'

class CacheInterface:
    def __init__(self, window, row,n):
        self.window = window

        self.label = tk.Label(window, text=f"Memória Cache L{n}:",font = ("Arial",15,'bold'),background=corBg)
        self.label.grid(row=row, column=0, pady=10)

        self.palavras_bloco_label = tk.Label(window, text="Palavras por Bloco:",font = ("Arial",12,'bold'),background=corBg)
        self.palavras_bloco_label.grid(row=row, column=1)
        self.palavras_bloco_text = tk.Entry(window)
        self.palavras_bloco_text.grid(row=row, column=2,sticky='w')

        self.blocos_conjunto_label = tk.Label(window, text="Blocos por Conjunto:",font = ("Arial",12,'bold'),background=corBg)
        self.blocos_conjunto_label.grid(row=row, column=3,sticky='w')
        self.blocos_conjunto_text = tk.Entry(window)
        self.blocos_conjunto_text.grid(row=row, column=4,sticky='w')

        self.conjuntos_label = tk.Label(window, text="Conjuntos:",font = ("Arial",12,'bold'),background=corBg)
        self.conjuntos_label.grid(row=row, column=5)
        self.conjuntos_text = tk.Entry(window)
        self.conjuntos_text.grid(row=row, column=6,sticky='w')

    def get(self):
        try:
            res = (int(self.palavras_bloco_text.get()),int(self.blocos_conjunto_text.get()),int(self.conjuntos_text.get()))
            return res
        except ValueError:
            print('Input invalido')
            return None
        
class cacheFrame:
    def __init__(self,window,coluna,n):
        padx = (40,10)
        padx2 = (10,40)
        pady = 15

        fr = tk.Frame(window, background=corBg,borderwidth = 3,highlightthickness=True)
        
        self.labelNome = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,text = f'cache L{n}')
        self.labelNome.grid(row=0,column=0,columnspan = 2)

        self.labelBOffset = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,foreground='orange',text = 'Byte Offset:')
        self.labelBOffset.grid(row=1,column=0,padx = padx, pady = pady, sticky = 'e')
        self.labelBOffsetRes = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,foreground='orange',text = '_ bits')
        self.labelBOffsetRes.grid(row=1,column=1,padx = padx2, pady = pady)

        self.labelWOffset = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,foreground='purple',text = 'Word Offset:')
        self.labelWOffset.grid(row=2,column=0,padx = padx, pady = pady,sticky = 'e')
        self.labelWOffsetRes = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,foreground='purple',text = '_ bits')
        self.labelWOffsetRes.grid(row=2,column=1, padx = padx2, pady = pady)
            

        self.labelIndex = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,foreground='blue',text = 'Index:')
        self.labelIndex.grid(row=3,column=0, padx = padx, pady = pady,sticky = 'e')
        self.labelIndexRes = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,foreground='blue',text = '_ bits')
        self.labelIndexRes.grid(row=3,column=1, padx = padx2, pady = pady)

        self.labelTag = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,foreground='red',text = 'Tag:')
        self.labelTag.grid(row=4,column=0, padx = padx, pady=pady,sticky = 'e')
        self.labelTagRes = tk.Label(fr,font = ('Arial',12,'bold'),background=corBg,foreground='red',text = '_ bits')
        self.labelTagRes.grid(row=4,column=1, padx = padx2, pady=pady)
        fr.grid(row = 0,column = coluna)

    def atualizarBits(self,bitsBOffset,bitsWOffset,bitsIndex,bitsTag):
        self.labelBOffsetRes.config(text = str(bitsBOffset) + ' bits')
        self.labelWOffsetRes.config(text = str(bitsWOffset) + ' bits')
        self.labelIndexRes.config(text = str(bitsIndex) + ' bits')
        self.labelTagRes.config(text = str(bitsTag) + ' bits')

class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 600   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y - 100))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()