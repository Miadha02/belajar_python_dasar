"""
operasi logika atau boolean
simbol simbolnya ada : 
1. not = kebalikan data awal
2. or = jika ada true maka true / jika ada satu yang true maka true
3. and = jika ada false maka false
4. xor = jika beda maka true
"""

#NOT
print("===NOT===")
a = True
c = not a  # yang a = true , maka kebalikan dari true akan menghasilkan false

print("data boolean = ", a)
print("---NOT---")
print("data c =", c)


#OR
print("\n=====OR=====")
a = True
b = False
c = a or b     #jika ada True diantara kedua objek maka hasilnya true True ,
                # a = True  b = false , kan ada a nya true maka hasilnya true 
print(a, " OR ",b,"=", c)

a = True 
b = True 
c = a or b       # jika True keduanya maka hasilnya True
print(a,"OR",b,"=",c) 

a = False
b = False
c = a or b  #jika keduanya False maka hasilnya False
print(a,"OR ",b,"=",c)


#AND , jika dua buah nilai bernilai True , maka hasilnya True
print("===AND===")

a = False
b = False
c = a and b    # kalau semua False , maka False 
print(a,"AND",b,"=",c)

a = True
b = False
c = a and b #kalau ada salah satu yang false , maka false
print(a,"AND",b,"=",c)

a = False
b = True
c = a and b #kalau ada salah satu yang false, maka false
print(a,"AND ",b,"=",c)

a = True
b = True
c = a and b #jika semua bernilai True , maka hasilnya True
print(a,"AND",b,"=",c)

#XOR , akan true jika salah satu true , sisanya false
print("===XOR (^)===")

a = False
b = False
c = a ^ b #keduanya sama maka hasilnya false
print(a,"XOR",b,"=",c)

a = False
b = True
c = a ^ b #keduanya berbeda maka hasilnya True
print(a,"XOR",b,"=",c)

a = True
b = False
c = a ^ b #keduanya berbeda maka hasilnya true
print(a,"XOR",b,"=",c)

a = True
b = True
c = a ^ b #keduanya sama maka hasilnya false
print(a,"XOR",b,"=",c)