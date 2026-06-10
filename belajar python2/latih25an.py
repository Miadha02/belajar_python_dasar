list_data = []
while True:

    print(f'''
1.TAMBAH BUKU
2.LIHAT BUKU
3.PINJAM BUKU
4.KEMBALIKAN BUKU
5.CARI BUKU
6.STATISTIK
7.KELUAR    ''')

    
    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():
            pilih_menu = int(input_pilih_menu)

            if pilih_menu >0 and pilih_menu <=7:
                break
            else:
                print('harus 1 - 7')
        else:
            print('tidak boleh huruf')


    if pilih_menu == 1:
        list_buku = []
        nama_buku = input('masukkan nama buku : ').lower()

        while True:
            input_jumlah_buku = input('masukkan jumlah buku : ')

            if input_jumlah_buku.isdigit():
                jumlah_buku = int(input_jumlah_buku)

                if jumlah_buku >0:
                    break
                else:
                    print('tidak boleh 0 atau kurang')

            else:
                print('tidak boleh huruf')

        list_buku = [nama_buku,jumlah_buku]

        list_data.append(list_buku)

    elif pilih_menu == 2:

        if len(list_data)>0:

            for i,data in enumerate(list_data):
                print(f'{i+1}. {data[0]} | {data[1]}')

        else:
            print('harus mengisi nomor 1 ')                


    elif pilih_menu == 3:

        if len(list_data) >0:
            for i,data in enumerate(list_data):
                print(f'{i+1}. {data[0]} | {data[1]}')

            while True:
                input_pilih_buku = input('pilih buku : ')

                if input_pilih_buku.isdigit():

                    pilih_buku = int(input_pilih_buku)

                    index = pilih_buku -1

                    if index >=0 and index < len(list_data):
                        break
                    else:
                        print('nomor tidak tersedia')

            while True:
                input_jumlah_pinjam = input('masukkan jumlah pinjam : ')

                if input_jumlah_pinjam.isdigit():
                    jumlah_pinjam = int(input_jumlah_pinjam)

                    if jumlah_pinjam <= list_data[index][1]:
                        list_data[index][1] -= jumlah_pinjam

                        print('buku berhasil di pinjam')

                        break
                    else:
                        print('buku tidak cukup')
                else:
                    print('tidak boleh huruf')            
            
        else:
            print('harus mengisi nomor 1 ')   

    elif pilih_menu == 4:
        if len(list_data) >0:
            for i,data in enumerate(list_data):
                print(f'{i+1}. {data[0]} | {data[1]}')

            while True:
                input_buku_kembali = input('pilih_buku : ')

                if input_buku_kembali.isdigit():
                    buku_kembali = int(input_buku_kembali)

                    indexnya = buku_kembali -1

                    if indexnya >=0 and index < len(list_data):
                        break
            while True:
                input_jumlah_kembali = input('masukkan jumlah kembali : ')

                if input_jumlah_kembali.isdigit():

                    jumlah_kembali = int(input_jumlah_kembali)

                    if jumlah_kembali >0:
                        list_data[indexnya][1] += jumlah_kembali 
                        print('d=buku berhasil dikembalukan')
                        break            
                    else:
                        print('tidak boleh 0 atau kurang')
                else:
                    print('tidak boleh huruf')
        else:
            print('harus mengisi nomor 1 ')            


    elif pilih_menu == 5:
        if len(list_data) >0:
            ketemu = False
            cari_buku = input('masukkan nama buku : ').lower()

            for data in list_data:

                if data[0] == cari_buku:
                    print('buku ditemukan')
                    print(f'nama {data[0]}')
                    print(f'stok : {data[1]}')
                    ketemu = True

            if ketemu == False:
                print('buku tidak ditemukan ')     

        else:
            print('harus mengisi nomor 1')        

    elif pilih_menu == 6:
        if len(list_data) >0:
            print('---STATISTIK PERPUSTAKAAN---')

            print(f'total judul buku : {len(list_data)}')
            total_stok = 0
            stok_terbesar = 0
            stok_terkecil = 0

            for data in list_data:

                total_stok += data[1]

                if data[1] > stok_terbesar :
                    stok_terbesar = data[1]

                else:
                    stok_terkecil = data[1]

            print(f'total stok : {total_stok}')

            print(f'stok terbesar : {stok_terbesar}')
            print(f'stok terkecil : {stok_terkecil}') 
        else:
            print('harus mengisi nomor 1')         

    elif pilih_menu == 7:
        print('program selesai')
        exit()
                      





