Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Rahmad Nur Sulistyawan'
>>> NIM = 'L200190194'
>>> x = '1' + NIM[7:]
>>> a = int(x)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #Menampilkan tipe data dari variabel a
>>> type(b)
<class 'int'>
>>> #Menampilkan tipe data dari variabel b
>>> a/b
54.27272727272727
>>> #Menampilkan hasil operasi pembagian variabel a dan b
>>> a//b
54
>>> #Menampilkan pembulatan hasil bagi variabel a dan b
>>> 10 * (a - 999)
1950
>>> #Menampilkan hasil operasi hitung
>>> b ** 2
484
>>> #Menampilkan hasil pemangkatan variabel 2
>>> a % b
6
>>> #Menampilkan modulus atau sisa bagi dari variabel a dan b
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #Menampilkan tipe data c
>>> a/c
95.52
>>> #Menampilkan hasil pembagian dari variabel a dan c
>>> a//c
95.0
>>> #Menampilkan pembulatan hasil variabel a dan c
>>> a % c
6.5
>>> #Menampilkan modulus dari variabel a dan c
>>> c > b
False
>>> #Membuktikan apakah variabel c dengan b lebih besar atau tidak
>>> type(c > b)
<class 'bool'>
>>> #Menampilkan tipe data dari c apakah lebih besar dari b atau tidak
>>> a > b and b > c
True
>>> #Membuktikan apakah variabel a lebih besar dari b DAN apakah variabel b lebih besar dari c
>>> a > 1100 or b < 10
True
>>> #Membuktikan True or False
