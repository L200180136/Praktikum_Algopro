Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama ='Muhammad Riza Radyaka Susanto'
>>> NIM ='L200180136'
>>> X ='1' + NIM[7:]
>>> a =int(X)
>>> b =len(Nama)
>>> type(a)
<class 'int'>
>>> #(a) termasuk kelas integer
>>> type(b)
<class 'int'>
>>> #(b) termasuk kelas integer
>>> a/b
39.172413793103445
>>> #(a/b) nilai a di bagi nilai b
>>> a//b
39
>>> #(a//b) nilai bulat dari a dibagi b
>>> b**2
841
>>> #(b**2) nilai dari b dikali 2
>>> a%b
5
>>> #(a%b) sisa hasil dari a dibagi b
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #(c) termasuk nilai float
>>> a/c
90.88
>>> #(a/c) hasil dari a dibagi c
>>> a//c
90.0
>>> #(a//c) nilai bulat dari a dibagi c
>>> a%c
11.0
>>> #(a%c) sisa hasil dari a dibagi c
>>> c>b
False
>>> #(c>b) nilai c lebih besar dari b adalah salah(False)
>>> type(c>b)
<class 'bool'>
>>> #(c>b) termasuk kelas boolean
>>> a>b and b>c
True
>>> #(a>b and b>c) nilai a>b dan b>c adalah benar(True)
>>> a>1100 or b<10
True
>>> #(a>1100 or b<10) nilai dari a>1100 atau b<10 adalah benar(True)
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
=============================== RESTART: Shell ===============================
>>> Nama = 'Muhammad Riza Radyaka Susanto'
>>> NIM = '136'
>>> Tinggi = '165'
>>> Berat = '63'
>>> TahunLahir = '1999'
>>> 
=============================== RESTART: Shell ===============================
>>> Nama = 'Muhammad Riza Radyaka Susanto'
>>> NIM = 136
>>> Tinggi = 165
>>> Berat 63
SyntaxError: invalid syntax
>>> Berat = 63
>>> 
=============================== RESTART: Shell ===============================
>>> Nama = 'Muhammad Riza Radyaka Susanto'
>>> NIM = 136
>>> Tinggi = 165
>>> Berat = 63
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #(Aku) termasuk kelas tuple
>>> Aku[0]
1999
>>> #(Aku[o]) index ke 0 dari Aku = TahunLahir = 1999
>>> a = NIM % 4; Aku[a]
1999
>>> #(Aku[a])index nilai (0) hasil dari sisa nilai NIM dibagi 4
>>> type(Aku[a])
<class 'int'>
>>> #(Aku[a]) nilai AKu[a] adalah 1999, sehinga termasuk integer
>>> Aku[a:4]
(1999, 63, 165, 136)
>>> #(Aku[a:4]) nilai slicing dari Aku dari indeks a sampai 4
>>> type(Aku[4])
<class 'str'>
>>> #(Aku[4]) nilai dari Aku[4] termasuk string
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #(Aku[o]) nilai dari Aku[0] adalah tuple, sehingga string 'ok' tidak bisa diganti pada tuple
>>> 
KeyboardInterrupt
>>> 
