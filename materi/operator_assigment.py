#operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assigment

a = 5 # ini adalah assigment

print("nilai a : ",a)

a += 1 # artinya a = a + 1
print("nilai a += : ",a)

a -= 2
print ("nilai a -= : ",a)

a *= 5
print ("nilai a *= =",a)

b = 10
print ("nilai b = ",b)

#modulus dan floor division
b %= 3
print ("nilai b %= = ",b)

b = 10
print ("nilai b = ",b)

b //= 5
print("nilai b //= ",b)

#pangkat
b **= 3
print("nilai b **= : ",b)

#operasi bitwase
#OR
c = True
print("\n nilai c = ",c)
c |= False
print("nilai c |= = ",c)

c = False
print("\n nilai c = ",c)
c |= False
print("nilai c menjadi : ",c)

#And
e = True
print("\n nilai e : ",e)
e &= False
print("nilai e  &= menjadi = ",e)

#geser geser

f =0b100
print("\n nilai d = ",f,format(f,"08b"))

f >>= 2
print("nilai f >>= menjadi : ",format(f,"08b"))

g =0b100
print("\n nilai g : ", g, format(g,"08b"))

g <<= 2
print("nilai g <<= adalah : ",format(g,"08b"))
