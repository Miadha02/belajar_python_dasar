# operasi dan manipulasi string

#1. menyambung string (concatenate) , contoh
# misal string sama string , contoh iklim + adha
# ga boleh str + int     
# ga boleh str + float

nama_pertama = "iklim"
nama_tengah = "adha"
nama_akhir = "ganteng"

nama_lengkap = nama_pertama +" " +nama_tengah +" " + nama_akhir # harus string semua 
print(nama_lengkap)

#2. operasi menghitung panjang string ,
#  pakai 
# (leng())
panjang = len(nama_lengkap)
print("panjang dari : " + nama_lengkap + " = "+ str(panjang)) # string semua , jika tidak di strkan maka error
                                                             # di str kan karena panjang adalah number
                                                            # sama aja kayak pakai = 


#3. operator untuk string
# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap     # d ada di, iklim a(d)ha ganteng , ada d di adha , maka hasilnya True
print("string "+ d +" ada di "+ nama_lengkap +str(status))

d = "D"
status = d in nama_lengkap    #D tidak ada di, iklim adha ganteng , maka hasilnya false
print("string "+d+" ada di "+ nama_lengkap + str(status))

#mengulang string
print("wk"*10) # ngeprint wk menjadi 10 , wkwkwkwkwkwkwkwkwkwk
print(15*"wk") # ngeprint wk menjadi 15 , wkwkwkwkwkwkwkwkwkwk

#indexing 
print("index ke -0 : " + nama_lengkap[0]) # mengambil index ke berapa ,
                                          #dimulai dari 0 
                                          # iklim adha ganteng , 
                                          # jika kita ambil index pertama maka yang terambil yang
                                          # i , karena i dimulai dari 0, 
                                                  
print("index ke -2 : " + nama_lengkap[1]) # jika index 1 , maka yang terambil k  

#jika -1 , maka diambil dari index terakhir ,
#misal iklim adha ganteng maka 
#g, yang terambil
print("index ke -1 : " + nama_lengkap[-1])

#jika -3 maka e yang terambil
print("index ke -3 "+ nama_lengkap[-3])

#bisa pakai sampai (:)
print("index ke [0:3] : " + nama_lengkap[0:4]) # diambil 0 sampai(:) sebelum 4 , jadi ikl
print("index ke [3:7] : " + nama_lengkap[3:8])

print("index ke [0,2,4,6,8,10] : " + nama_lengkap[0:10:2]) # 0 sampai(:) 10 dengan increment 2 ,diloncati 2
                                                            #iklim adha ganteng
                                                            #jadi
                                                            #ilmah


#item paling kecil
print("item paling kecil : "+ min(nama_lengkap)) #paling kecilnya spasi
#itempaling besar
print("item paling besar : " + max(nama_lengkap)) # sesuai abjad , iklim adha ganteng
                                                  # yang paling besar adalah t , sesuai abjad

#ASCII CODE
ascii_code = ord(" ") #mencari ascii code spasi
print("ASCII code untuk spasi adalah " + str(ascii_code))

data = 117
print("char untuk ASCII 117 adalah : "+ chr(data)) # mencari ascii code dari 117 = u


#4. operator dalam bentuk method

data = "otong surotong paraotong"  # ada 6 o 
jumlah = data.count("o")
print("jumlah o pada data adalah : " + data + " = " + str(jumlah))