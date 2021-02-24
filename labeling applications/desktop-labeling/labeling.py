mycolor2 = '#40E0D0'
label_color="#ffe45e"
acil1_color="#FF0008"
acil2_color="#FF575C"
acil3_color="#FF9397"
neg_color="#0091ad"
notr_color="#a6a2a2"
sıradaki_color="#ffe45e"
pos_color="#06d6a0"

from tkinter import *
from tkinter import ttk
data=""
kaydedilecek=""
id=0

kontrol=0
basla_kontrol=0
from tkinter import *


def get_input():
    global kontrol
    global data
    global id
    data = entry1.get()
    id=int(entry2.get())
    print("{0}. satırdan başlanacak".format(id))
    kontrol=1
    root.destroy()

root = Tk()
root.title(" Giriş Bilgileri")
root.geometry("300x300")
label1 = Label(root,text = "csv tam path")
label1.pack()
label1.config(justify = CENTER)

entry1 = Entry(root, width = 100)
entry1.pack(pady=10,padx=10)


label2 = Label(root, text="Başlanılacak satır sayısı (id)")
label2.pack()
label2.config(justify = CENTER)

entry2 = Entry(root, width = 100)
entry2.pack(pady=10,padx=10)


run = Button(root, text = 'Çalıştır',bg="lightblue")
run.pack() 
run.config(command = get_input)

root.mainloop()

try:
    import pandas as pd
    df = pd.read_csv(r"{0}".format(data))
    df["TICKET_DESC"]=df["TICKET_DESC"].astype(str)
except Exception as a:
    print("hata ",a)



satır_kontrol=0
for i in df.columns:
    if(i=="duygu") | (i=="aciliyet"):
        satır_kontrol=1
if(satır_kontrol==0):
    df["aciliyet"]=""
    df["duygu"]=""
    print("duygu ve aciliyet columları oluşturuldu, bu işlem 1 kez gerçekleşiyor")
    

from tkinter import *
from tkinter import ttk

root=Tk()
root.title(" Veri Etiketleme")
root.geometry("700x500")
root.config(background='black')
## create a main frame
main_frame=Frame(root)
main_frame.pack(fill=BOTH,expand=1)
#create a canvas
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
## add a scrollbar to the canvas
my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
## configura the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
## create another frame inside the canvas
second_frame=Frame(my_canvas)
third_frame=Frame(my_canvas)
my_canvas.create_window((0,0),window=second_frame,anchor="nw")



def acil1_fonk():
    global basla_kontrol
    if(basla_kontrol==1):
        global id
        df["aciliyet"].iloc[id]=1

def acil2_fonk():
    global basla_kontorl
    if(basla_kontrol==1):
        global id
        df["aciliyet"].iloc[id]=2

    
def acil3_fonk():
    global basla_kontrol
    if(basla_kontrol==1):
        global id
        df["aciliyet"].iloc[id]=3


def acil_degil_fonk():
    global basla_kontrol
    if(basla_kontrol==1):
        global id
        df["aciliyet"].iloc[id]=0


def negative_fonk():
    global basla_kontrol
    if(basla_kontrol==1):
        global id
        df["duygu"].iloc[id]="neg"
        df.to_csv('{0}'.format(data), index=False)
        print("{0}. satır kaydedildi >>  [{1}]  [{2}]".format(id,df["aciliyet"].iloc[id],"neg"))
        id=id+1
        my_text=df["TICKET_DESC"].iloc[id].replace("\n"," ")
        text.configure(text=my_text)
        text2.configure(text=id)
        


def notr_fonk():
    global basla_kontrol
    if(basla_kontrol==1):
        global id
        df["duygu"].iloc[id]="notr"
        df.to_csv('{0}'.format(data), index=False)
        print("{0}. satır kaydedildi >>  [{1}]  [{2}]".format(id,df["aciliyet"].iloc[id],"notr"))
        id=id+1
        my_text=df["TICKET_DESC"].iloc[id].replace("\n"," ")
        text.configure(text=my_text)
        text2.configure(text=id)


def pozitif_fonk():
    global basla_kontrol
    if(basla_kontrol==1):
        global id
        df["duygu"].iloc[id]="pos"
        df.to_csv('{0}'.format(data), index=False)
        print("{0}. satır kaydedildi >>  [{1}]  [{2}]".format(id,df["aciliyet"].iloc[id],"pos"))
        id=id+1
        my_text=df["TICKET_DESC"].iloc[id].replace("\n"," ")
        text.configure(text=my_text)
        text2.configure(text=id)


def siradaki_fonk():
    global basla_kontrol
    if(basla_kontrol==1):
        global id
        print("{0}. satır pas geçildi".format(id))
        id=id+1
        my_text=df["TICKET_DESC"].iloc[id].replace("\n"," ")
        text.configure(text=my_text)
        text2.configure(text=id)

def basla_fonk():
    global id
    global basla_kontrol
    my_text=df["TICKET_DESC"].iloc[id].replace("\n"," ")
    text.configure(text=my_text)
    text2.configure(text=id)
    basla.destroy()
    acil1.configure(bg=acil1_color)
    acil2.configure(bg=acil2_color)
    acil3.configure(bg=acil3_color)
    acil_degil.configure(bg=notr_color)
    negatif.configure(bg=neg_color)
    notr.configure(bg=notr_color)
    pos.configure(bg=pos_color)
    sıradaki.configure(bg=sıradaki_color)
    kaydet.pack(side=LEFT,padx=50)
    basla_kontrol=1
    
    
def kaydet_ve_cık():
    global id
    df.to_csv('{0}'.format(data), index=False)
    print("En son {0}. satır etiketlendi !! {1} den devam edebilirsin".format(id-1,id))
    root.destroy()
    
    
text = Label(second_frame,text = "mesaj buraya gelecek",wraplength=600)
text.pack(pady=5)

text2 = Label(second_frame,height=1,width=6,text = "id", borderwidth=1,relief="solid")
text2.pack(pady=5)

label1 = Label(second_frame,height=2,width=100,text = 'Aciliyet sıralaması = 1 > 2 > 3',bg=label_color)
label1.pack(fill=X)
label1.config(justify = CENTER)

acil1 = Button(second_frame,height=1,width=20, text = 'Acil 1',bg="grey")
acil1.config(command = acil1_fonk)
acil1.pack( pady=5)

acil2 = Button(second_frame,height=1,width=20, text = 'Acil 2',bg="grey")
acil2.config(command = acil2_fonk)
acil2.pack( pady=5)

acil3 = Button(second_frame,height=1,width=20, text = 'Acil 3',bg="grey")
acil3.config(command = acil3_fonk)
acil3.pack(pady=5)

acil_degil = Button(second_frame,height=1,width=20, text = 'ACİL DEĞİL',bg="grey")
acil_degil.config(command = acil_degil_fonk)
acil_degil.pack(pady=5)

label1 = Label(second_frame,height=2,text = 'Bu mesaj ???',bg=label_color)
label1.pack(fill=X)
label1.config(justify = CENTER)

negatif = Button(second_frame,height=1,width=20, text = 'Negatif',bg="grey")
negatif.config(command = negative_fonk)
negatif.pack( pady=5)

notr = Button(second_frame,height=1,width=20, text = 'Nötr',bg="grey")
notr.config(command = notr_fonk)
notr.pack(pady=5)

pos = Button(second_frame,height=1,width=20, text = 'Pozitif',bg="grey")
pos.config(command = pozitif_fonk)
pos.pack(pady=5)

sıradaki = Button(second_frame,height=1,width=10, text = 'PAS',bg="grey")
sıradaki.config(justify = CENTER,command =siradaki_fonk) 
sıradaki.pack(side=RIGHT,padx=50)

basla = Button(second_frame,height=1,width=10, text = 'BAŞLA',bg=sıradaki_color)
basla.config(justify = CENTER,command =basla_fonk) 
basla.pack(side=LEFT,padx=50)

kaydet = Button(second_frame,height=1,width=10, text = 'Kaydet ve Çık',bg="lightblue")
kaydet.config(justify = CENTER,command =kaydet_ve_cık) 
kaydet.pack_forget()
if(kontrol==1):
    root.mainloop()
