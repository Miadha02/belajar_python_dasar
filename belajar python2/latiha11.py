
while True:

    jumlah_barang = input('masukkan jumlah barang : ')

    if jumlah_barang.isdigit():
        barang = int(jumlah_barang)
        if barang <=0:
            print('tidak boleh kurang atau kurang dari sama 0')

        elif barang > 0:
            break
        else:
            print('salah')

    else:
        print('tidak boleh pakai huruf')

total = 0
for cabang in range(1,barang+1):
    print(f'barang ke {cabang}')

    while True:
        input_masukkan_harga = input('masukkan harga : ')

        if input_masukkan_harga.isdigit():

            masukkan_harga = int(input_masukkan_harga)

            if masukkan_harga > 0:
                harga = masukkan_harga
                total += harga
                break

            else:
                print('tidsk boleh kurang dari 0')

        else:
            print('tidak boleh pakai huruf')

print(f'total belanja {total}')

                


