
list_angka = []
for ulang in range(2):
    print(f'baris ke {ulang}')

    baris = []
    for ulang1 in range(2):
        while True:
            input_angka = input(f'masukkan angka [{ulang}] [{ulang1}] : ')

            if input_angka.replace('-','').isdigit():
                angka = int(input_angka)
                break

            else:
                print('tidak boleh huruf')

        baris.append(angka)
    list_angka.append(baris)

total = 0
print('---hasil matrix---')
for data in list_angka:  #[1,2]
    print(data)
    
    for angka in data: #[1]
        total += angka



print(f'total{total}')


