import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "Server sudah siap"
data = ''
kamus = {'nama' : 'Muhammad Riza Radyaka Susanto', 'NIM' : 'L200180136', 'alamat'
        : 'Maaf, perintah tidak dimengerti','angkatan' : '2018', 'keluar' :
         'siap!!'}

while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            s.close()
            break
        print 'Perintah: ', data
        if kamus.has_key(data):
            komm.send(kamus[data])
