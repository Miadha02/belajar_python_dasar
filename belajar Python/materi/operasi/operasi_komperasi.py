# setiap hasil dari operasi komperasi adalah boolean  (True/false)
#simbol simbolnya : (>),(<),(>=),(<=),(==),(!=),(is),(is not) 
# 

#contoh
a = 4
b = 2
c = 4
d = 2
#lebih besar dari ( > )
print("lebih besar dari ( > )")
hasil = a > 2
print(a,">",b,"=",hasil)

hasil = b > a
print(a," > ", b ,"=",hasil)

#kurang dari ( < )
print("kurang dari ( < )")
hasil = b < a
print(b,"<",a,"=",hasil)

hasil = a < b
print(a,"<",b,"=",hasil)

#lebih dari sama dengan (>=)
print ("lebih dari sama dengan (>=)")
hasil = a >= c
print(a,">=",c,"=", hasil)

hasil = a >= b
print(a,">= ",b,"=",hasil)

hasil = b >= a
print(b,">= ",a ,"=",hasil)

#kurang dari sama dengan <=
print("kurang dari sama dengan >=")

hasil = b <= d
print(b,"<=",d,"= ",hasil)

hasil = b <= a
print(b,"<=",a,"=",hasil)

hasil = a <= b
print(a,"<=",b,"=",hasil)

# sama dengan (==)
print("sama dengan (==)")
hasil = a == c
print(a,"==", c,"=",hasil)

hasil = a == b
print(a,"==",b,"=",hasil)

#tidak sama dengan (!=) ,kebalikan == 
print("tidak sama dengan (!=)")
hasil = a != c
print(a,"!=",c,"=",hasil)

hasil = a != b
print(a,"!=",b,"= ",hasil)



#is sebagai komperasi objek identity , yang harus ada x=5 , ga direkomendasi langsung ditulis 5
print("objek identity (is)")
x = 5 #ini adalah assigment membuat objek
y = 5 #ini adalah assigemnt membuat objek 
z = 4 
#nilai x dengan y sama maka disimpan di id yang sama

print("nilai x = ",x," id = ",hex(id(x))) #jika nilai x dan y sama , maka disimpan di id yang sama
print("nilai y = ", y , "id = ",hex(id(y)))

hasil = x is y     #nilai x dan y sama maka hasilnya true  
print("x is y = ",hasil)

hasil = y is z  #nilai y dan z tidak sama maka hasilnya false
print("y is z = ",hasil)



# is not , kebalikan dari is , jika objek tidak sama maka hasilnya true
hasil = x is not y  # kebalikan is maka jadinya false
print("x is not y = ", hasil)

hasil = x is not z #nilai x dan z tidak sama maka hasilnya true 
print("x is not z =", hasil)