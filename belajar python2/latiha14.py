jumlah_dapat_diskon = 0
total_semua = 0
pembeli_terbesar = 0

while True:

    input_jumlah_pembeli = input('masukkan jumlah pembeli : ')

    if input_jumlah_pembeli.isdigit():
        jumlah_pembeli = int(input_jumlah_pembeli)

        if jumlah_pembeli > 0:
            break

        else:
            print('tidak boleh kurang darisama dengan 0')

    else:
        print('tidak boleh pakai huruf')    

for ulang in range(1,jumlah_pembeli+1):

    print(f'pembeli ke {ulang}')

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(" ","").isalpha():
            break

        else:
            print('salah memasukkan nama')

    while True:
        input_jumlah_barang = input('masukkan jumlah barang : ')

        if input_jumlah_barang.isdigit():
            jumlah_barang = int(input_jumlah_barang)

            if jumlah_barang >0:
                break

            else:
                print('tidak boleh kurang atau sama 0')

        else:
            print('tidak boleh pakai angka')

    total = 0
    for ulang1 in range(1,jumlah_barang+1):
        print(f'barang ke {ulang1}')

        while True:
            input_jenis_barang = input('masukkan jenis (elektronik / pakaian / makanan ) : ').lower()

            if input_jenis_barang.isalpha():
                
                if input_jenis_barang == 'elektronik':
                    harga = 100
                    total += harga
                    kategori = 'elektronik'
                    break

                elif input_jenis_barang == 'pakaian':
                    harga = 50
                    total += harga
                    kategori = 'pakaian'
                    break

                elif input_jenis_barang == 'makanan':
                    harga = 30
                    total += harga
                    kategori = 'makanan'
                    break

            else:
                print('tidak boleh pakai angka') 

        print(f'brang ke {ulang1} -> {kategori} -> {harga}')

    


    if total >= 200:
        total -= 20
        diskon = 'ada diskon 20 setiap belanja >=200'
        jumlah_dapat_diskon +=1


    elif total <200:
        diskon = 'tidak ada diskon'    

    total_semua += total
    print('\ntotal harga : ')
    print(f'total : {total}, diskon : {diskon}\n\n\n')

    if total > pembeli_terbesar:
        nama_terbesar = nama
        pembeli_terbesar = total


   


print('\n\n---HASIL AKHIR---')
print(f'total penghasilan toko {total_semua}')
print(f'pembeli terbesar {nama_terbesar}, {pembeli_terbesar}')
print(f'total ada diskon {jumlah_dapat_diskon}')
                                           