total = 0
total_makanan = 0
total_minuman = 0
while True:

    input_jumlah_item = input('masukkan jumlah item : ')

    if input_jumlah_item.isdigit():
        jumlah_item = int(input_jumlah_item)

        if jumlah_item <= 0:
            print('tidak boleh 0 atau kurang')

        elif jumlah_item >0:
            break    
    else:
        print('tidak boleh pakai huruf')

for jumlah in range(1,jumlah_item+1):
    print(f'item ke {jumlah}')

    while True:
        input_jenis_nya = input('masukkan jenis (makanan/minuman) : ').lower()

        if input_jenis_nya.isalpha():

            if input_jenis_nya == 'makanan':
                harga = 10000
                kategori = 'makanan'
                total += harga
                total_makanan += harga
                break

            elif input_jenis_nya == 'minuman':
                harga = 5000
                kategori = 'minuman'
                total += harga
                total_minuman += harga
                break

            else:
                print('salah memilih')

        else:
            print('tidak boleh pakai angka')


print('---HASIL---')
print(f'total makanan : {total_makanan}')
print(f'total minuman : {total_minuman}')
print(f'total semua {total}')
