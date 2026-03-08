# continue , pass

#pass , berfungsi sebagai dummy , tidak akan di eksekusi

angka = 0

while angka < 5:
    angka += 1
    if angka == 3 :
        pass # tidak akan dieksekusi

    print(angka)

#continue
print("=====continue====")
angka = 0
print(f"angka sekarang {angka}")

while angka <5 :
    angka +=1
    print(f"angka sekarang { angka}") # aksi 1

    if angka == 3:
        print("nice")
        continue # ini akan membuat loop meloncat ke step selanjutnya , aksi ke 2 di lewati                   
    print("whassup") # aksi 2

print("finishe")