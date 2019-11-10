Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Rahmad Nur Sulistyawan'
>>> NIM = 194
>>> Tinggi = 1.74
>>> Berat = 60
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # merupakan tipe tuple yang berisi sekumpulan data yang memuat TahunLahir, Berat, Tinggi, NIM, dan Nama dan tipe data tuple tidak dapat diubah
>>> Aku[0]
2001
>>> # menampilkan elemen tuple indeks ke-0 yaitu TahunLahir atau data 2001
>>> a = NIM % 4; Aku[a]
1.74
>>> # hasil sisa bagi dari variabel NIM dengan 4 adalah 2 dan disimpan dalam variabel a kemudian Aku[a] akan menjadi Aku[2] dimana akan menampilkan elemen tuple Aku indeks ke-2 atau Tinggi
>>> type(Aku[a])
<class 'float'>
>>> # elemen tuple Aku indeks ke 2(2 merupakan data dari variabel a) atau Tinggi adalah 1.74 dan merupakan data bertipe float atau tipe data angka yang memiliki bagian desimal
>>> Aku[a:4]
(1.74, 194)
>>> #Menampilkan elemen dari tuple Aku mulai dari indeks ke-2 hingga sebelum indeks ke-4 yang berisi Tinggi dan NIM.
>>> type(Aku[4])
<class 'str'>
>>> #Elemen tuple Aku indeks ke-4 merupakan data tipe string karena berisi "Nama".
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> #Terjadi tipe error karena data tipe tuple tidak dapat diubah sedangkan program ingin mengubah elemen tuple indeks ke-0 dari TanggalLahir menjadi 'ok' maka terjadi tipe error.
>>> type(Data)
<class 'list'>
>>> #Variabel Data merupakan data bertipe list karena berisi sekumpulan data atau karakter dan data dalam list dapat diubah.
>>> type(Data[4])
<class 'str'>
>>> #Elemen list indeks ke-4 atau yang berisi "Nama" merupakan data yang bertipe string karena mengandung karakter.
>>> Data[4][5]
'd'
>>> #Elemen list indeks ke-4 atau yang berisi Nama kemudian program akan menjadi Nama[5] atau indeks ke-5 dari data yang telah disimpan dalam variabel Nama yaitu huruf('d').
>>> Data[4][a:6]
'hmad'
>>> #Elemen list Data indeks ke-4 yang berisi Nama kemudian program akan menjadi Nama[a:6] dimana a berisi data 2 maka akan menjadi Nama[2:6] yang akan menampilkan elemen list indeks ke-2 hingga sebelum indeks ke-6 yaitu "hmad".
>>> Data[0] = "ok"; Data
['ok', 60, 1.74, 194, 'Rahmad Nur Sulistyawan']
>>> #Elemen list Data indeks ke-0 diubah dari "TanggalLahir" menjadi 'ok' dan kemudian program menampilkan data dari list Data.
>>> Data[-a]
194
>>> #Variabel a berisi data 2 maka program menjadi Data[-2] yang akan menampilkan elemen list Data indeks ke-3 atau Data Indeks ke-(-2).
>>> range(a)
range(0, 2)
>>> #Varibel a berisi data 2 maka program akan menjadi range(2) dan program akan menampilkan range dari 0 hingga 2 atau jika ditulis dalam program range(0, 2).
