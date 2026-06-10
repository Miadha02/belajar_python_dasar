while True:
    input_jumlah_penonton = input('masukkan jumlah penonton : ')

    if input_jumlah_penonton.isdigit():
        jumlah_penonton = int(input_jumlah_penonton)

        if jumlah_penonton >0:
            break
        else:
            print('tidak boleh kurang dari 0 atau sama')

    else:
        print('tidak boleh pakai huruf')

harga_semua = 0
for ulang in range(1,jumlah_penonton+1):

    print(f'penonton ke {ulang}')

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(" ","").isalpha():
            break
        else:
            print('salah memaasukkan nama')

    while True:  
        input_jumlah_tiket = input('masukkan jumlah tiket : ')

        if input_jumlah_tiket.isdigit():
            jumlah_tiket = int(input_jumlah_tiket)

            if jumlah_tiket > 0:
                break

            else:
                print('tidak boleh kurang atau sama 0')
        else:
            print('tidak boleh huruf')   

    harga = 0
    for ulang1 in range(1,jumlah_tiket+1):

        print(f'tiket ke {ulang1}')

        while True:
            jenis_tiket = input('masukkan jenis tiket (vip / regular / ekonomi) : ').lower()

            if jenis_tiket.isalpha():

                if jenis_tiket == 'vip':
                    harga_tiket = 5000
                    harga += harga_tiket
                    break
                elif jenis_tiket == 'regular':
                    harga_tiket = 3000
                    harga += harga_tiket
                    break

                elif jenis_tiket == 'ekonomi':
                    harga_tiket = 2000
                    harga += harga_tiket
                    break

                else:
                    print('salah memilih jenis tiket')

            else:
                print('tidak boleh pakai angka')
        
    harga_semua += harga

    print(f'nama : {nama} -> membeli : {jumlah_tiket} tiket -> harga : {harga}  ')   

print(f'harga semua {harga_semua} ')

