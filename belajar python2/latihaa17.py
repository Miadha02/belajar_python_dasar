harga = 0
barang = 0
while True:
    jumlah_barang = input('masukkan jumlah barang : ')

    if jumlah_barang.isdigit():
        jumlah = int(jumlah_barang)

        if jumlah > 0:
            break
        else:
            print('salah')

    else:
        print('salah')    

for ulang in range(1,jumlah+1):
    print(f'barang ke {ulang}')

    while True:
        nama = input('masukkan nama barang')

        if nama.isalpha():
            break
        else:
            print('salah')

    while True:
        input_harga = input('masukkan harga : ')

        if input_harga.isdigit():
            harga_barang = int(input_harga)

            if harga_barang >0:
                barang += harga_barang
                harga += harga_barang
                break

            else:
                print('salah')

if harga >100000:
    diskon = harga * 0.1
    harga = harga - diskon

print('---HASIL---')
print(f'total belanja sebelum diskon : {barang}')
print(f'total diskon : {diskon}')
print(f'total semuanya : {harga}')
