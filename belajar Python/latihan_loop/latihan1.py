#latihan membuat segitiga

sisi = 4

#1 menggunakan for
#dummy variable
count = 1
for i in range(sisi):
    print("*"*count) # * kali 1
    count += 1  #diulangi mterus ditambah + 1 = 2 ,3 ,4 . sampai sisi = 4
print("akhir dari for")


#2.menggunakan while
#while
print("\nawal dariwhile")
sisi = 4
count = 1

while count <= sisi:
    print("*"*count)
    count +=1

    if (count > sisi):
        break

print("akhir dari while")
count = 1

print("awal while")


#3 hanya ganjil saja
sisi = 4
count = 1
while True:    
    #jika count % 2 , maka hasilnya ganjil , 1 mod 2 = 1 , mod = sisa bagi
    if (count % 2):
        print("*"*count)
        count += 1
    else :
        count += 1
        continue 

    if (count > sisi):
        break

#segitiga sama kaki

sisi = 15
count = 1
spasi = int(sisi / 2)
while True:
    if(count % 2):
        print(" "*spasi,"+"*count)
        spasi -=1
        count += 1

    else :
        count += 1
        
        continue
    if (count > sisi):
        break    

#segitiga sama kaki terbalik
count = 5
spasi = 0
while True:
    
    if(count % 2):
        print(" "*spasi,"+"*count)
        spasi +=1
        count -= 1
    else :
        count -= 1    
    if (count < 1):
        break

           
