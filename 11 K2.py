from Tkinter import Tk, Label, Entry, Button, IntVar

my_app = Tk(className='Kalkulator Sederhana')

def tambah():
    "Menambah Angka 1 dengan Angka 2"
    _tambah = int1.get() + int2.get()
    L4.config(text=_tambah)

def kurang():
    "Mengurang Angka 1 dengan Angka 2"
    _kurang = int1.get() - int2.get()
    L4.config(text=_kurang)
    
def kali():
    "Mengali Angka 1 dengan Angka 2"
    _kali = int1.get() * int2.get()
    L4.config(text=_kali)

def bagi():
    "Membagi Angka 1 dengan Angka 2"
    _bagi = int1.get() / int2.get()
    L4.config(text=_bagi)
    
B1 = Button(my_app, text="+", command=tambah)
B1.grid(row=2, column=0)
B2 = Button(my_app, text="-", command=kurang)
B2.grid(row=2, column=1)
B3 = Button(my_app, text="x", command=kali)
B3.grid(row=2, column=2)
B4 = Button(my_app, text=":", command=bagi)
B4.grid(row=2, column=3)


L1 = Label(my_app, text="Angka 1")
L1.grid(row=0, column=0)
int1 = IntVar()
E1 = Entry(my_app, textvariable=int1)
E1.grid(row=0, column=1)
L2 = Label(my_app, text="Angka 2")
L2.grid(row=1, column=0)
int2 = IntVar()
E2 = Entry(my_app, textvariable=int2)
E2.grid(row=1, column=1)
L3 = Label(my_app, text="Hasil")
L3.grid(row=3, column=0)
L4 = Label(my_app, )
L4.grid(row=3, column=1)







my_app.mainloop()
