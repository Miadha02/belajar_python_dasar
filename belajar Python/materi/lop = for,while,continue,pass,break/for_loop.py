#perulangan loop
'''
for kondisi:
aksi

saat kondisinya True akan melakukan aksi
'''
#ini dengan list
angka_list =[0,9,8,5,4]
print(angka_list)

for i in angka_list :
    print(f"angka list sekarang {i}")
    
print('akhir dari program')

#ini dengen range
angka = range(5) # dimulai dari 0 - sampai 4
angka2 = range(1,5) #dimulai dari 1- sampai 4
for i in angka :
    print(f"angka range sekarang {i}")
print("akhir dari program")

for i in angka2 :
    print(f"saya keren {i}")

#menggunakan string
data_str = "saya ganteng"

for huruf in data_str : # melooping per huruf
    print(huruf)