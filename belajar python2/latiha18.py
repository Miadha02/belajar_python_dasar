total_semua_pembeli = 0

while True:
    input_jumlah_pembeli = input('jumlah pembeli : ')

    if input_jumlah_pembeli.isdigit():
        jumlah_pembeli = int(input_jumlah_pembeli)

        if jumlah_pembeli > 0:
            break
        else:
            print('salah')
    else:
        print('salah')

for ulang in range(1,jumlah_pembeli+1):

    print(f'pembeli ke {ulang}') 

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(' ',"").isalpha():
            break
        else:
            print('salah')               
    
        
    while True:
        input_jumlah_beli = input('masukkan jumlah barang : ')

        if input_jumlah_beli.isdigit():
            jumlah_beli = int(input_jumlah_beli)

            if jumlah_beli > 0:
                break
            else:
                print('salah')
        else:
            print('salah')        

    total_1 = 0
    for ulang1 in range(1,jumlah_beli+1):
        print(f'barang ke {ulang1}') 

        while True:
            nama = input('masukkan nama barang : ') 

            if nama.isalpha():
                break
            else:
                print('salah')

        while True:
            input_harga_barang = input('masukkan harga : ')

            if input_harga_barang.isdigit():
                harga_barang = int(input_harga_barang)

                if harga_barang > 0:
                    break
                else:
                    print('salah')

            else:
                print('salah')

        
        while True:
            input_barang_jumlah = input('masukkan jumlah barang : ') 

            if input_barang_jumlah.isdigit():
                barang_jumlah = int(input_barang_jumlah)

                if barang_jumlah > 0:
                    total = harga_barang * barang_jumlah
                    break
                else:
                    print('salah')
            else:
                print('salah')           

        total_1 += total

        if total_1 >=100000:
            total_1 = total_1 - (total_1 * 0.1)
            diskon = 'diskon 10%'

        else:
            diskon = 'tidak ada diskon'
    total_semua_pembeli += total_1
    print(f'total {nama} {total_1} diskon : {diskon}')

print(f'total semua {total_semua_pembeli} ')


