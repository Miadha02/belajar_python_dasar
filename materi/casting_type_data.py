#merubah satu tipe ke tipe lain
#type data = int , float, string(str), boolean (bool)

#integer
print("integer")
data_int = 9
print("data : ",data_int, "type : ", type(data_int))

data_float = float(data_int) # integer 9 berubah menjadi float 9,0
data_str = str(data_int)  #integer 9 berubah menjadi string 9
data_bool =bool(data_int) #integer 9 berubah menjaadi True , kalau di ubah 0 akan false , jika angka lain maka True
print("data : ", data_float, " bertype : ", type(data_float))
print("data : ",data_str, "bertype : ", type(data_str))
print("data : ",data_bool,"bertype : , ", type(data_bool),"\n")


#Float
print("float")
data_float = 10.1
print("data : ", data_float, "type ", type(data_float))

data_int = int(data_float) #float 10.1 berubah menjadi int 10
data_str = str(data_float) #float 10.1 berubah menjadi string 10.1
data_bool = bool(data_float) #float 10.1 berubah menjadi True , kalau 0 akan False

print ("data : ", data_int, "bertype : ", type(data_int))
print("data : ", data_str, "bertype : ",type(data_str))
print("data : ", data_bool, "bertype : ", type(data_bool),"\n")

#Boolean
print("Boolean")
data_bool = True
print("data : ", data_bool, "Bertype : ",type(data_bool))

data_int = int(data_bool) # Boolean True berubah menjadi integer 1 , karena True =1 , False = 0
data_str = str(data_bool) # Boolean True berubah menjadi string True
data_float = float(data_bool) #Boolean True Berubah menjadi float 1.0

print("data : ", data_int, "bertype : ", type(data_int))
print("data : ", data_str , "bertype : ", type(data_str))
print("data : ", data_float , "bertype : ", type (data_float),"\n")

#String
print("String")

data_str = "a"
print("data : ", data_str, "bertype : ", type(data_str))

data_int = int(data_str) #string harus angka , kalau tidak hasilnya error
data_float =float(data_str) #string harus angka 
data_bool = bool(data_str) # kalau isi string tidak ada maka false , kalau ada isi maka true

print("data : ", data_int, "Bertype : ", type(data_int))
print("data : ", data_float , "Bertype : ", type(data_float))
print("data : ", data_bool, "Bertype : ", type(data_bool))