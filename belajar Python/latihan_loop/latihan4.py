#segitiga sama 

sisi = 10
count = 1

for i in range(count,sisi +1):
    spasi = sisi - i
    bintang = (2 * i) -1
    print(" "*spasi+"*"*bintang)

while True :    
    spasi = sisi - count
    bintang = (2 * count) -1
    print(" "*spasi+"*"*bintang)
    count +=1

    if (count > sisi):
        break


#segitiga sama terbalik
sisi = 10
count = 1

for i in range(sisi,count -1,-1):
    spasi = sisi - i # loop 10-10 , 10-9,10-8
    bintang = (2 * i) -1 
    print(" "*spasi+"*"*bintang)


sisi = 10
i = sisi
count = 1
while True:
    spasi = sisi - i
    bintang = (2 * i) -1

    print(" "*spasi+"*"*bintang)
    
    i -= 1
    if (i < count):
        break