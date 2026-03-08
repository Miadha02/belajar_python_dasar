sisi = 7
count = 1
for i in range(sisi):
    print("*"* count)
    count += 1


#segitiga terbalik
sisi = 1
count = 7
while True :
    print("*"*count)
    count -= 1

    if(count < sisi):
        break

#segitiga 123

sisi = 7
count = 1
while True :
    print(str(count)*count)
    count +=1

    if (count > sisi):
        break

#segitiga for
sisi = 7
for i in range(1,sisi + 1,+1):
    print("*" * i)

#segitia terbalik for    
sisi = 1
count = 7
for i in range (count,sisi -1,-1):
    print("*"* i)


#tes
total = 0
for i in range (0,101):
   total = total + i
print(total)

sisi = 5
for i in range (0,sisi +1):
    print(str(i)*i)

sisi = 5
count = 1
while True :
    print("*"*count)
    count +=1    

    if (count > sisi):
        break

sisi = 5
count = 1
while True :
    print("*"*sisi)
    sisi -= 1

    if(sisi < count):
     break