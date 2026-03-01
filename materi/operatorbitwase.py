# operator bitwise , operasi biner , binary

'''
bitwise adalah operasi masing masing bit
contoh
int 2 -> 00000010   diubah menjadi biner
int 1 -> 00000001  
int 5 -> 00000101

contoh 
2 | 1 -> 2 -> 00000010
         1 -> 00000001
             ----------  or |
              00000011
                    2^1 2 ^0 -> 3
'''

a = 9
b = 5

# bitwise OR (|)
c = a | b
print("====OR======")
print("nilai : ",a," , binary : ",format(a,"08b")) 
print("nilai : ",b," , binary : ",format(b,"08b"))
print("============================(|)")
print("nilai : ",c," , binary : ",format(c,"08b"))


#bitwise and (&)
c = a & b
print("=====AND====")
print("nilai : ", a , " , binary : ", format(a,"08b"))
print("nilai : ", b ," , binary : ",format(b,"08b"))
print("===============AND(&)")
print("nilai : ", c , " binary : ", format(c,"08b"))

#bitwise xor (^)
c = a ^ b
print("====xor===")
print("nilai : ",a , "binary : ",format(a,"08b"))
print("nilai : ", b," , binary : ",format(b,"08b"))
print("==============XOR(^)")
print("nilai : ",c ,"binary : ",format(c,"08b"))

#bitwise not (~)
c = ~ a
print("=======NOT=======")
print("nilai : ",a ," , binary : ",format(a,"08b"))
print("===========not(~)")
print("nilai : ", c , ", binary : ",format(c,"08b"))
print("===========(^)")
d = 0b0000001001   # kalau mau di flip bisa pakai not 
e = 0b1011111111   # 1 1 = 0 ,  0 1 = 1  , 0 0 = 0
print("nilai : ", e ^ d, " , binary : ",format(e^d,"08b"))

# shifting 
# shift right (>>)    menggeser ke kanan 00000010 menjadi 00000001

print("====shift right ======")
c = a >> 2         # menggeser  ke kanan dua kali
print("nilai : ",a , "binary : ",format(a,"08b"))
print("============Shift right(>>)")
print("nilai : ",c , "binary : ",format (c,"08b"))

#shift left (<<)
print("======shift left==== ")
c = a << 2
print("nilai : ",a , "binary : ", format(a,"08b"))
print("=========shift left (<<)")
print("nilai : ",c,"binary : ", format(c,"08b"))
