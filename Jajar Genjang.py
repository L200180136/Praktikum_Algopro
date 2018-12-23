def hitung_luas():
    "fungsi menghitung luas dari segitiga"
    s = p * t
    return s

print "<!DOCTYPE html>"
print
print """<html>
    <head><title>Menghitung Luas Bangun Geometri</title></head>
    <body>"""
p = 5
t = 10
print """<table>
    <tr>
        <td rowspan="7"> Foto</td>
        <th align="left">Bangun Geometri</th>
    </tr>
    <tr>
        <td>Nama bangun : Jajar Genjang</td>
    </tr>
    <tr>
        <td>Dimensi (2D/3D): 2D</td>
    </tr>
    <tr>
        <td>Rumus luas : Panjang x Tinggi</td>
    </tr>
    <tr>
        <td>Parameter 1 : {}</td>
    </tr>
    <tr>
        <td>Parameter 2 : {}</td>
    </tr
    <tr>
        <td>Luas : """.format(p, t)
print hitung_luas(), """</td>
</tr></table></body>"""
print "</html>"
