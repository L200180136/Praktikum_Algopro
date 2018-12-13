from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className='Data diri')

L1 = Label(my_app, text="Data diri", font=('Arial', 24))
L1.grid(row=0, column=0)
L2 = Label(my_app, text="Nama")
L2.grid(row=1, column=0)
L3 = Label(my_app, text='Muhammad Riza Radyaka Susanto')
L3.grid(row=1, column=1)
L4 = Label(my_app, text="NIM")
L4.grid(row=2, column=0)
L5 = Label(my_app, text='L200180136')
L5.grid(row=2, column=1)
L6 = Label(my_app, text="Buku favorit")
L6.grid(row=3, column=0)
L7 = Label(my_app, text='Negeri 5 Menara')
L7.grid(row=3, column=1)
L8 = Label(my_app, text="Idola di kalangan sahabat")
L8.grid(row=4, column=0)
L9 = Label(my_app, text='Abu Bakar As-Shidiq')
L9.grid(row=4, column=1)
L10 = Label(my_app, text="Motto")
L10.grid(row=5, column=0)
L11 = Label(my_app, text='Belajar!!!')
L11.grid(row=5, column=1)

def tutup():
    "Menutup aplikasi Tkinter"
    my_app.destroy()
    

B1 = Button(my_app, text="Tutup", command=tutup)
B1.grid(row=6, column=1)
           
my_app.mainloop()
