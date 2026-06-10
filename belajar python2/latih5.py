while True:
    input_jumlah_makanan = input('masukkan jumlah makanan : ')

    if input_jumlah_makanan.isdigit():
        jumlah_makanan = int(input_jumlah_makanan)

        if jumlah_makanan >0:
            break
        else:
            print('tidak boleh kurang atau sama 0')

    else:
        print('tidak boleh huruf')


list_menu = []
total_semua = 0

for ulang in range(1,jumlah_makanan+1):

    print(f'makanan ke {ulang}')

    while True:
        input_nama = input('masukkan nama makanan : ')

        if input_nama.replace(" ","").isalpha():

            break
        else:
            print('tidak boleh pakai angka')

    while True:
        input_harga = input('masukkan harga : ')

        if input_harga.isdigit():  

            harga = int(input_harga)

            if harga >0:
                break

            else:
                print('tidak boleh kurang atau sama 0')

        else:
            print('tidak boleh pakai huruf')

    pesanan = [input_nama,harga]
    list_menu.append(pesanan)


print(f'daftar makanan ')

print('NO    NAMA    MAKANAN    ')

for index,jumlah in enumerate(list_menu):

    print(f'{index}    {jumlah[0]}      {jumlah[1]}')
    
    total_semua+= jumlah[1]
print(f'total semua {total_semua}')    