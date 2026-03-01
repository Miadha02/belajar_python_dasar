#type data 

#Angka Satuan integer (int)
data_integer = 100
print("data : ", data_integer)
print("bertype : ", type(data_integer))  # type untuk menentukan type data seperti integer string dll

#type data float : angka dengan koma (float)
data_float = 2.5 #pakai (.)
print("data : ", data_float)
print("bertype",type(data_float))

#type data string (str) : kumpulan karakter
data_string ="iklim 10"
print("data : ",data_string)
print("bertype", type(data_string))

#type data boolean (bool) : binner true/false 
data_bool = True     # True / False
print("data : ", data_bool)
print("bertype : ", type(data_bool))

#tipe data khusus

# bilangan kompleks (complex)
data_complex = complex(5,6)
print("data : ",data_complex)
print("bertype : ",type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double ,c_double, c_char  
data_c_double = c_double(10.5) #double lebih panjang dari float
print("data :", data_c_double)
print("bertype : ",type(data_c_double))

data_c_char = c_char(b'1')
print("data : ", data_c_char)
print("bertype : ", type(c_char))
