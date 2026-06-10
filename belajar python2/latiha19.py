

while True:
    input_jumlah_pelanggan = input('masukkan jumlah pelanggan : ')

    if input_jumlah_pelanggan.isdigit():
        jumlah_pelanggan = int(input_jumlah_pelanggan)

        if jumlah_pelanggan >0:
            break
        else:
            print('tidak boleh kurang atau sama 0')
    else:
        print('gaboleh pakai huruf')
hasil_semua = 0
terbesar = 0
nama_terbesar = ''
for ulang1 in range(1,jumlah_pelanggan + 1):
    print(f'pelanggan ke {ulang1}')

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(" ","").isalpha():
            break
        else:
            print('tidak boleh pakai angka')

    while True :
        input_jumlah_barang = input('masukkan jumlah barang : ')

        if input_jumlah_barang.isdigit():
            jumlah_barang = int(input_jumlah_barang)

            if jumlah_barang > 0:
                break
            else:
                print('tidak boleh kurang dari 0 atau sama')
        else:
            print('tidak boleh pakai huruf')                

    total_harga = 0
    for ulang in range(1,jumlah_barang+1):
        print(f'barang ke {ulang}')

        
        while True:
            masukkan_jenis = input('masukkan jenis (makanan/minuman/snack): ')

            if masukkan_jenis.isalpha():

                if masukkan_jenis == 'makanan':
                    harga = 2000
                    total_harga += harga
                    break
                
                elif masukkan_jenis == 'minuman':
                    harga = 1000
                    total_harga += harga
                    break

                elif masukkan_jenis == 'snack':
                    harga = 500
                    total_harga += harga 
                    break    

                else:
                    print('salah memasukkan jumlah barang')
            else:
                print('tidak boleh angka')

    if total_harga >= 5000:
        total_harga -= 1000
        diskon = 'dapat diskon 1000'

    elif total_harga >= 3000:
        total_harga -= 500
        diskon = ' dapat diskon 500'

    else:
        diskon = 'tidak dapat diskon'             

    hasil_semua += total_harga       

    if total_harga > terbesar:
        terbesar = total_harga
        nama_terbesar = nama

    print(f'nama {nama} : total_harga : {total_harga} , diskon {diskon}') 

    

print('\nhasil semua')
print(f'total semua {hasil_semua}')   
print(f'nama terbessar = {nama_terbesar} :{terbesar}')         

                