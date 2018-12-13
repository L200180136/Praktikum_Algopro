from Tkinter import Tk, Label, Entry, Button, IntVar

my_app = Tk(className='Bangun Geometri')

L1 = Label(my_app, text='Bangun Geometri', font=('Arial', 24))
L1.grid(row=0, column=0)
L2 = Label(my_app,  text="""Jajar Genjang adalah salah satu bangun geometri dua
            dimensi. Jajar genjang pada umunya memiliki dua pasangan pembentuk,
            yaitu Panjang dan Tinggi. Contoh: Atap, Penghapus bentuk jajar genjang.""")
L2.grid(row=1, column=0)
L3 = Label(my_app, text='Parameter 1 :')
L3.grid(row=2, column=0)
P1 = IntVar()
E1 = Entry(my_app, textvariable=P1)
E1.grid(row=2, column=1)
L4 = Label(my_app, text='Parameter 2 :')
L4.grid(row=3, column=0)
P2 = IntVar()
E2 = Entry(my_app, textvariable=P2)
E2.grid(row=3, column=1)
L5 = Label(my_app, text='')
L5.grid(row=4, column=1)
L6 = Label(my_app, text='Gambar')
L6.grid(row=6, column=0)

def luas():
    'Menghitung luas Jajar genjang'
    _luas = P1.get() * P2.get()
    L5.config(text=_luas)

B = Button(my_app, text='Hitung luas', command=luas)
B.grid(row=4, column=0)



my_app.mainloop()
