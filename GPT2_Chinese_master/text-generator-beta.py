from os import name, terminal_size
import tkinter as tk
from generate import *
import threading, time

class Threader(threading.Thread):
    def __init__(self,keyword,length,samples):
        super(Threader,self).__init__()
        self.keyword=keyword
        self.length=length
        self.samples=samples
        self.res=[]
        self.daemon=True
        self.start()
    
    def run(self):
        self.res=main(self.keyword,self.length,self.samples)
class text_generator:

    def __init__(self,window):
        self.window=window
        window.title('Text-Generator-Beta')

        self.keyword_label = tk.Label(
            window,
            text='請輸入關鍵字 : ',
            font=('微軟正黑體', 12),
            width=15, height=2
        )
        self.keyword_label.pack()

        self.keyword = tk.StringVar()
        self.keyword_entry = tk.Entry(
            window,
            textvariable=self.keyword,
            width=20
        )
        self.keyword_entry.pack()

        self.industry = tk.StringVar(window)
        self.industry.set('選擇產業別')
        industry_list = ['美妝保養']
        self.industry_option = tk.OptionMenu(
            window, self.industry, *industry_list)
        self.industry_option.pack()

        self.length_label = tk.Label(
            text='請輸入文章長度(最多至512) : ',
            font=('微軟正黑體', 12)
        )
        self.length_label.pack()

        self.length=tk.StringVar(window)
        self.length_entry = tk.Entry(
            window,
            textvariable=self.length,
            width=20
        )
        self.length_entry.pack()

        self.samples_label=tk.Label(
            text='請輸入產生段落數',
            font=('微軟正黑體',12)
        )
        self.samples_label.pack()

        self.samples=tk.StringVar(window)
        self.samples_entry = tk.Entry(
            window,
            textvariable=self.samples,
            width=20
        )
        self.samples_entry.pack()

        self.button = tk.Button(
            window,
            text='一鍵生成',
            command=self.getOutput
        )
        self.button.pack()

        self.output=tk.Text(
            window,
            height=30,
            width=100,
        )
        self.output.pack()
    def getOutput(self):
        self.output.insert(1.0,'生成中請稍後...')
        res=Threader('[CLS]'+self.keyword.get(),int(self.length.get()),int(self.samples.get()))
        for paragraph in res:
            self.output.insert('1.0','\n'+paragraph.replace('[UNK]','')+'\n')

if __name__=='__main__':
    window=tk.Tk()
    gui=text_generator(window)
    window.mainloop()