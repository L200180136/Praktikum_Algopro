data = { "NIM" :"L200180136" , "Nama" : """Muhammad Riza Radyaka Susanto""" , "Alamat"
       : "Mutihan" , "Umur" : 19 , "Prodi" : "Informatika" , "Kodepos" : 57147 ,
      "Asal" : "Surakarta" }

def z () :
    "Menampilkan NIM"
    print ("NIM : " , data["NIM"])
    return;
def s () :
    "Menampilkan Nama"
    print ("Nama : " , data["Nama"])
    return;
def c () :
    "Menampilkan Alamat"
    print ("Alamat : " , data["Alamat"])
    return;
def v () :
    "Menampilkan Umur"
    print ("Umur : " , data["Umur"])
    return;
def b () :
    "Menampilkan Prodi"
    print ("Prodi : " , data["Prodi"])
    return;
def n () :
    "Menampilkan Kodepos"
    print ("Kode pos : " , data["Kodepos"])
    return;
def m () :
    "Menampilkan Asal"
    print ("Asal : " , data["Asal"])
    return;

print ("""Pilihan yang tersedia :
        h menampilkan bantuan ini
        a menampilkan NIM
        b menampilkan Nama
        c menampilkan Alamat
        d menampilkan Umur
        e menampilkan Prodi
        f menampilkan Kode pos
        g menampilkan Asal""")

x = "s"
while x != "k":
    x = str(input("Masukan Pilihan: "))
    if x == "h":
     print ("""Pilihan yang tersedia :
        h menampilkan bantuan ini
        a menampilkan NIM
        b menampilkan Nama
        c menampilkan Alamat
        d menampilkan Umur
        e menampilkan Prodi
        f menampilkan Kode pos
        g menampilkan Asal""")
     
    elif x == "a" :
        print("Pilihan Anda : a")
        z()
    elif x == "b" :
        print("Pilihan Anda : b")
        s()
    elif x == "c" :
        print("Pilihan Anda : c")
        c()
    elif x == "d" :
        print("Pilihan Anda : d")
        v()
    elif x == "e" :
        print("Pilihan Anda : e")
        b()
    elif x == "f" :
        print("Pilihan Anda : f")
        n()
    elif x == "g" :
        print("Pilihan Anda : g")
        m()
    elif x == "K" :
        print("Keluar !!!")
    else :
        print("Pilihan tidak diketahui")
