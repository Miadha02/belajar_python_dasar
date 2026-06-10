sisi = 10
count =1

#for
for i in range(sisi):
    print("*"*count)
    count +=1
print('akhir dari for')
#while
count = 1
while True:
    print("*"*count)
    count +=1

    if count > sisi:
        break


print('akhir dari while')    

#segitiga ganjil
print("=======")
count = 1
while True :
    
    if count %2 == 0:
        count +=1
        continue
    
    else :
        print("*"*count)
        count +=1

    if count > sisi:
        print('akhir dari segitiga') 
        break
print("akhir dari program")


#segitiga sama kaki 
spasi = 5
count =1
sisi = 10
while True:
    if count %2 == 0:
        count +=1
        continue

    else :
        print(" "*spasi,"*"*count)
        count +=1
        spasi -= 1

    if count > sisi:

        break    

#segitiga sama kaki terbalik
spasi = 1
count = 10
sisi = 1

while True:
    if count %2 == 0:
        count -=1
        continue

    else:
        print(" "*spasi,"*"*count)
        spasi +=1
        count -=1
    
    if count < sisi:
        print("akhir dari segitiga")
        break



listcoba = [[1,2,3,4,5],[5,6,7,8,9]]

for data in listcoba:
    
    for data1 in data:
        print(data1,end=' ')
    print()    

for data3 in listcoba:
    print(data3[1])

