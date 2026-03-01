a = 8
b = 4

#operasi tambah
hasil = a + b
print(a, " + ", b , " = ",hasil)

#operasi kurang
hasil = a - b
print(a ," - ", b, " = ",hasil)

#operasi bagi
hasil = a / b
print(a, ": ", b ," = ", hasil)

#operasi pangkat
hasil = a**b
print(a," ^ ",b ," = ", hasil)

#operasi modulus %
hasil = a % b
print(a, " % ", b ," = ", hasil )

#operasi floor division // dibulatkan dari / , misal 3.14 , jadi 3
hasil = a // b
print(a , " // ", b , " = ",hasil)


#prioritas operasi
#urutannya pengerjaan :
# 1. tanda buka kurung () 
# 2. eksponen (pangkat) (**)
# 3. perkalian (*) / pembagian (/) / modulus (%) / floor division (//)
# 4. pertambahan (+) / pengurangan (-) 

x= 3
y=2
z=5

hasil = x ** y * (z + x) / y // x % z *x
print ( x , '**' , y , '*' , z , '+' , x , '/' , y , '//' , x , '%' , z , '*' , x ,"hasil : ",hasil)

#contoh
hasil = (x + y) * z         # dikerjakan didalam kurung dulu , baru dikalikan dengan z
print ("hasilnya : ", hasil ) 

hasil = x + y * z       # dikerjakan perkalian dulu baru di tambah , karena sesuai urutan pengerjaan
print ("hasil : ", hasil )

hasil = x + y ** z  # dikerjakan pangkat dahulu lalu di tambah , sesuai urutan pengerjaan
print("hasil : ", hasil)