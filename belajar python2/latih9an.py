list_angka = []
for ulang1 in range(2):
    print(f'baris ke {ulang1}')

    baris = []
    for ulang2 in range(2): 
        while True:
            input_angka = input(f'masukkan angka [{ulang1}] [{ulang2}] : ')

            if input_angka.replace("-",'').isdigit():
                angka = int(input_angka)
                break
            else:
                print('tidak boleh huruf')

        baris.append(angka)

    list_angka.append(baris)

total = 0
tidak_genap = []
print('hasil matrix')

for data in list_angka:
    print(data)

    for angka in data:
        if angka %2==0:
            total += angka

        else:
            tidak_genap.append(angka)

print(f'total = {total}')
for ganjil in tidak_genap:
    print(f'angka {ganjil} tidak genap')
                

