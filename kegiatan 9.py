###!/usr/bin/python
### Menulis data ke dalam berkas
##berkas = open("L200180136", "w")
##berkas.write("NIM = L200180136 " "\n")
##berkas.write("Tangal lahir  = 18-10-1999 " "\n")
##berkas.write("Nama lengkap = Muhammad Riza Radyaka Susanto")
##berkas.close()

###!/usr/bin/python
### Menulis data ke berkas L200180136
##import shelve
##R = shelve.open("L200180136")
##R["Nama"] = ["Muhammad Riza Radyaka Susanto"]
##R["TTL"] = ["Surakarta 10/18/1999"]
##R["NIM"] = ["L200180136"]
##R.close()
##
##R = shelve.open("L20180136")
##print "Nama: ", R["Nama"]
##print "TTL: ", R["TTL"]
##print "NIM: ". R["NIM"]
##R.close()

#!/usr/bin/python
# Membaca berkas teks
berkas=open("L200180136", "w")
berkas.write("NIM = L200180136\n ")
berkas.write("Tanggal lahir  = 10/18/1999\n ")
berkas.write("Nama lengkap = Muhammad Riza Radyaka Susanto\n")
berkas.write("Kota = Surakarta\n")
berkas.close()

##berkas = open("L200180136")
##print berkas.readlines()
##berkas.close()

import shelve
a=open("L200180136", "r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
print Nama
print Kota,TL
print NIM
a.close()

##a = shelve.open("Riza")
##a["b"] = [NIM, TL, Nama]
##print a["b"][0]
##print a["b"][1]
##print a["b"][2]
##a.close()
