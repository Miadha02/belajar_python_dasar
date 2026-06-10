while True:
    input_jumlah_angka = input('masukkan jumlah angka : ')

    if input_jumlah_angka.isdigit():
        jumlah_angka = int(input_jumlah_angka)

        if jumlah_angka >0:
            break
        else:
            print('tidak boleh kurang dari 0')

    else:
        print('tidak boleh huruf') 


list_data =[]
for ulang1 in range(1,jumlah_angka+1):
    while True:
        input_angka = input(f'masukkan angka ke {ulang1} : ')

        if input_angka.replace('-','').isdigit():
            angka = int(input_angka)

            if angka > 0:
                list_data.append(angka)
                break
            else:
                print('tidak boleh 0 atau kurang')

        else:
            print('tidak boleh angka')

for data in list_data:
    print(data)
print(list_data)
total = sum(list_data)
print(f'hasil : {total}')