x = 5

print(x)

data_integer = 1
data_float = 2.5

print("data ",type(data_integer))
print("data",type(data_float))

datafloat = float(data_integer)
print(datafloat)
#data = int(input("masukkan data : "))
#print(data)
#print(type(data))

#biner = bool(int(input("masukkan data : ")))
#print(biner,type(biner))

a = 5
b = 5

hasil = a+b
print(hasil)

hasil = a*b
print(hasil)

a = 2
b = 1
c=1
hasil = a > b
print(hasil)
hasil = a<b
print(hasil)
hasil = b >= c
print(hasil)

hasil = a != b
print(hasil)
hasil = b != c
print(hasil)

hasil = b == c
print(hasil)
hasil = a== c
print(hasil)

x = 5
y = 5
hasil = x is y
print(hasil)
hasil = x is not y
print(hasil)

a = True
b = False
d = True
e = False
c = not a
print(c)

#jika salah 1 true maka true
oor = a or b
print(oor)
oor = a or d
print(oor)
oor = b or e
print(oor)

#and jika salah satu false maka false
andd = a and b
print(andd)
andd =a and d
print(andd)
andd =  b and e
print(andd)

#xor , jika salah satu true maka true , sisanya false
xoor = a ^ b
print(xoor)

#operasi bitwise
a = 9
b = 5
#or jika salah satu true maka true
c = a | b
print(format(c,'08b'))

#and jika salah satu false maka false
c = a & b
print(format(c,'08b'))

#xor
c = a ^ b
print(format(c,'08b'))

#not
c = ~a
print(format(c,'08b'))

teks = 'iklim iklil lil bahlil kolil solil relil'

teksnya = teks.upper()
print(teksnya)
teksnya = teks.lower()
print(teksnya)

check = teks.isupper()
print(check)
check = teks.islower()
print(check)

check = teks.isalpha()
print(check)

judul = 'Fermin Lopez'
check = judul.replace(" ",'')
print(check)
check1 = check.isalpha()
print(check1)
panjang = len(judul)
print(panjang)

angka = max(1,1,3)
print(angka)

kanan = 'kanan'.rjust(10)
print(kanan)

kiri = 'kiri'.ljust(10)
print(kiri)

tengah = 'tengah'.center(10,'-')
print(tengah)

panjang = max(1,2,5,1)
print(panjang)

#format
nama = 'iklil'
format = f'hello {nama}'
print(format)
print(type(format))

huruf = '123'
format = f"angka {angka}"
print(format)

boolean = False
format = f"boolean {boolean}"
print(format)

angka = 15.5
format = f'angka {angka}'
print(format)

angka = 2000000
format = f"ribuan = {angka:,}"
print(format)

angka = 2005.54321
format = f"desimal = {angka:.2f}"
print(format)

abgka = 2005.54321
format = f"desimal = {abgka:020.3f}"
print(format)

angka = -100
angkaplus = 100
format = f'angka = {angka}'
formatp = f'angkaplus = {angkaplus:+d}'
print(format)
print(formatp)

persen = 0.045
format = f'persen = {persen:.2%}'
print(format)

print(f"ga \n ga {5*'='}")
print(f'''
{'doko ni iruno':>20}
garasuno newo
''')

import datetime as dt
hari = dt.date.today()
print(hari)

tanggal = dt.date(2005,10,10)
print(tanggal)

#for
listi = [1,2,3,4,5,6,7]
for i in listi:
    print(f'i nya {i}')

for i in range(5):
    print(f'range nya {i}')    

for i in range(0,5,2):
    print(f'range i tambah2 : {i}')
    print('watashi')

data_str = 'iklim ganteng'
for i in data_str:
    print(f'huruf {i}')

# while (boolean) 
angka = 0
while angka < 5:
    angka += 1
    print(f"angka ke {angka}")
print('end')

# continue , pass , break

#pass -> sebagai dummy tidak akan dieksekusi
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass #ini tidak akan dieksekusi sama sekali / masih akan terprint
    print(angka)

#continue 
angka = 0
while angka < 5:
    angka += 1
    print(f'angka sekarang {angka}')
    if angka == 3:
        print('nice')
        continue # akan membuat loop meloncat ke step selanjutnya , aksi 1 , aksi 2 akan ke skip
    print('wasshup') # aksi 2
print('end')

#break 

angka = 0

while angka < 5:
    angka +=1
    print(f"angka sekarang {angka}")

    if angka == 3:
        print("nice")
        break
    print("wassup")

print("cukup finish")

angka = 0
batas = 10
while True:
    
    if angka < 0:
        print('gabisa kurang dari 0')
        break

    angka +=1
    print(f'angka sekarang {angka}')

    if angka == batas:
        print('selesai')
        break
    

    print('belum selesai !')

print('cukup finish')



#list (kumpulan data)

data_angka = [1,2,3,5,3,4,1]
print(data_angka)

data_str = ['back','cot','come','you']
print(data_str)

data_bool = [False,True,False,True,True]
print(data_bool)

data_campur = [1,'back',2,'cot',True]
print(data_campur)

#alternatif
data_range = range(0,10)
print(data_range)
data_list = list(data_range)
print(data_list)

#list dengan for loop(list comprehension)
list_for = [i for i in range(0,10)]
print(list_for)
list_for = [i**2 for i in range(0,10)]
print(list_for)

#list pakai for pake if
list_pake_for_if = [i for i in range(0,10) if i %2==0]
print(list_pake_for_if)
list_pake_forif = [i for i in range(0,10) if i %2 == 1]
print(list_pake_forif)

#operasi list
#      0(-4)   1(-3)  2(-2)  3(-1)
data = ['back','cot','come','you']

#mengambil data dari list
data_0 = data[0]
print(f'index pertama(0) : {data_0}')

data_terakhir = data[-1]
print(f'index terakhir (-1) : {data_terakhir}')

data_come = data[2]
print(f'data come : {data_come}')

#mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'panjang data = {panjang_data}')

#manipulasi data list
#menambahkan item pada list
print(f"data sebelum ditambah = {data}")
data.insert(1,'baby')
print(f'data sesudah ditambah {data}')

#menambah diakhir list
data.append('iya')
print(f'data ditambah diakhir : {data}')

#menambah list dengan list
data_baru = ['iklil','indah','azka']
data.extend(data_baru)
print(f'data gabungan : {data}')

#merubah data 
#ubah data 2 (baby) menjadi (grow)
data[1] = 'grow'
print(f'datta rubah : {data}')

#menghapus data (meremove data)

#data.remove('Cot')
#print(f'data remove {data}') tidak bisa
data.remove('you')
print(f'data di hapus you : {data}')

#menghapus data paling belakang
data.pop()
print(f'data akhir = {data}') #paling belakang dihapus

data_akhir = data.pop() #mengambil data yang dihapus lalu di 
print(f'{data_akhir}')  #diprint

#operasi list
data_angka = [2,4,3,5,6,8,7,4,3,5,6,4,3,2,1,2,3,4,5,7]

print(f'ini data angka {data_angka}')

#count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f'jumlah data 4 : {jumlah_data_4}')
print(f'jumlah data 3 : {jumlah_data_3}')

#ambil posisi data
data = ['iklil','adha','baik','jahat','raja','iblis']
print(f'data : {data}')

index_raja = data.index('raja') 
print(f'posisi index si raja : {index_raja}')

#mengurutkan list(sort)
print(f'data angka sebelum diurut (sort) : {data_angka}')
data_angka.sort()
print(f'data angka setelah diurut (sort) : {data_angka}') # diurut menjadi 1,2,3,4

print(f'data huruf sebelum diurut (sort) : {data}')
data.sort()
print(f'data huruf setelah diurut (sort) : {data}') # diurut dimulai dari a,b,c,d

#balik list
data_angka.reverse()
data.reverse()
print(f'data angka di reverse = {data_angka}')
print(f'data huruf di reverse = {data}')

#copy list
##teknik menduplikat list
a = ['iklil','adha','baik','sekali','orangnya']
print(f'a = {a}')

b=a
print(f'b = {b}')

#kita akan merubah member dari a
#ini akan merubah kedua list
a[1]= 'imam' 
print(f'\na = {a}')
print(f'b = {b}')

#address dari kedua list
print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')# address nya sama dengan a

#menduplikat list dengan copy
print('membuat list c dengan a.copy()')
c = a.copy()

print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')
print(f'address c = {hex(id(c))}') # akan membuat list baru dengan address yang berbeda

c[0] ='ikan'
a[0] = 'sarden'
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')



#nested list 
data_0 =[1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print(f'data list biasa {data_list_biasa}')

list_2d = [data_0,data_1,data_list_biasa,4,5] #list dalam list
print(f'list 2d : {list_2d}')

#contoh penggunaan
peserta_0 =['iklil',25,'laki']
peserta_1 = ['adha',20,'perempuan']
peserta_2 = ['abah',20,'laki']

list_peserta =[peserta_0,peserta_1,peserta_2]

for peserta in list_peserta:
    print(f'nama : {peserta[0]}')
    print(f'umur : {peserta[1]}')
    print(f'gender : {peserta[2]}')

#dengan reference

list_copy = list_peserta.copy()
print(f'peserta = {list_copy}')

peserta_0[0] = 'ujang'
print(f'peserta = {list_copy}')
print(f'peserta = {list_peserta}') 

#deep copy
data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0,data_1,10]
data_2d_copy = data_2d.copy()

print(f'data 2d : {data_2d}')
print(f'data 2d copy = {data_2d_copy}')
#mengambil data dari nested list
data = data_2d[0][0]
print(f'data = {data}')

#address semuanya
print(f'address asli = {hex(id(data_2d))}')
print(f'address copy = {hex(id(data_2d_copy))}')#address nya udah beda yang list

print('address dari member ke 1')
print(f'address asli = {hex(id(data_2d[0]))}') #address member 1 masih sama
print(f'address copy = {hex(id(data_2d_copy[0]))}') #address member 1 masih sama dengan asli

data_2d[1][0] = 5
data_2d[2]= 9 # diluar list akan dicopy tidak ikut di copy
print(f'data 2 d : {data_2d}') #tetap 9
print(f'data copy : {data_2d_copy}') #maka akan ikut berubah juga, yang 9 tidak berubah tetap 10

#deep copy
from copy import deepcopy

data_2d = [data_0,data_1,10]
data_2d_deepcopy = deepcopy(data_2d)

print(f'address asli = {hex(id(data_2d))}')
print(f'address copy = {hex(id(data_2d_deepcopy))}')

print('address dari member ke 1')
print(f'address asli = {hex(id(data_2d[0]))}') #
print(f'address deepcopy = {hex(id(data_2d_deepcopy[0]))}') #address nya amaka akan berubah kalau pakai deepcopy

data_2d[1][0] = 30
print(f'data 2 d : {data_2d}') # berubah jadi 30
print(f'data copy : {data_2d_deepcopy}') #maka akan tetap 5


#looping list
#looping dari list
kumpulan_angka = [5,6,8,7,4,3,7,1,2,3,4,5,3,1]
#for loop
print('for loop')
for angka in kumpulan_angka:
    print(f'angka = {angka}')

peserta = ['iklil','adha','mamang','garok']

for nama in peserta:
    print(f'nama : {nama}')

#for loop and range
print('for loop and range')
kumpulan_angka = [10,5,4,3,2,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'angka = {kumpulan_angka[i]}')

#while
print('while loop')
kumpulan_angka = [1,2,4,2,5,6]
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

#list comprehension
print('list comprehension')

data = ['iklim',1,2,3,'adha']
[print(i) for i in data]
[print(f'data : {i}')for i in data]

angka = [10,5,6,7]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

#enumerate
print('enumerate')
data_list = ['iklil',3,4,5,'raja']

for index,data in enumerate(data_list):
    print(f'index = {index} , data = {data}')

