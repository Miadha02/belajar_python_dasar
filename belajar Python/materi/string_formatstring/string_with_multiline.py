#width multilane

# data

data_nama = "ucup surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

#string standar
data_string = f"nama : {data_nama} , data_umur : {data_umur}, data_tinggi : {data_tinggi}, data_nomor_sepatu : {data_nomor_sepatu}"
print(5*"="+"data_string" +5 *"=")
print(data_string)

#string multilane
data_string = f"nama : {data_nama}, \n data_umur : {data_umur}, \n data_tinggi : {data_tinggi},\n data_nomor_sepatu : {data_nomor_sepatu}"
print("\n"+5*"="+"data multilane"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""
nama      = {data_nama} 
umur      = {data_umur} 
tinggi    = {data_tinggi} 
no sepatu = {data_nomor_sepatu}
"""
print(5*"="+ "data_string "+ 5*"=")
print(data_string)

#mengatur lebar
data_nama = "iklim"
data_string = f'''
nama = {data_nama :>5}
umur = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu}

'''
print(5*"="+"data_string",5*"=")
print(data_string)