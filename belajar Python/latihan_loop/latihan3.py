sisi = 5
count = 1

for i in range (count,sisi +1,+1):
    spasi = sisi -i
    print(" "*spasi+"*"*i)

#kalau pake while
while True :
    
    spasi = sisi - count
    print(" "*spasi+"*"* count)
    count +=1
    if(count > sisi):
        break




