
print("="*20)
print('SISTEM GUDANG')
print('='*20)

list_barang = []
while True:
    print('''Daftar Perintaah
    1.Tambah Barang
    2.Lihat Barang
    3.Barang Masuk
    4.Barang Keluar
    5.Cari Barang
    6.Statistik Gudang
    7.Hapus Barang
    8.Keluar
    ''')

    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():
            pilih_menu = int(input_pilih_menu)

            if pilih_menu >0 and pilih_menu <=8:
                break
            else:
                print('hanya 1 - 8 ')

        else:
            print('tidak boleh huruf')

    if pilih_menu ==1:
        print('Tambah Barang')
        list_tambah = []

        nama_barang = input('masukkan nama barang : ').lower()

        while True:
            input_stok_awal = input('masukkan stok awal : ')

            if input_stok_awal.isdigit():

                stok_awal = int(input_stok_awal)

                if stok_awal >=0:
                    break
                else:
                    print('tidak boleh kurang dari 0')
            else:
                print('tidak boleh huruf')

        list_tambah =[nama_barang,stok_awal]

        list_barang.append(list_tambah)

    elif pilih_menu == 2:

        print('Lihat Barang')

        if len(list_barang) >0:
            for i,data in enumerate(list_barang):

                print(f'{i+1}. nama : {data[0]}   | stok: {data[1]}')  

        else:
            print('harus mengisi nomor 1')                          

    elif pilih_menu == 3:
        print('data barang masuk' )
        if len(list_barang) >0:
            for i,data in enumerate(list_barang):

                print(f'{i+1}. nama : {data[0]}   | stok: {data[1]}')  

            while True:
                input_pilih_barang = input('pilih barang : ')

                if input_pilih_barang.isdigit():

                    pilih_barang = int(input_pilih_barang)
                    pilih = pilih_barang -1
                    if   pilih_barang >=0 and pilih_barang <= len(list_barang) :
                        break
                    else:
                        print('data tidak ditemukan')
                else:
                    print('tidak boleh huruf')        

            while True:
                input_barang_masuk = input('masukkan jumlah barang masuk : ')

                if input_barang_masuk.isdigit():

                    barang_masuk = int(input_barang_masuk)

                    if barang_masuk >0:
                        list_barang[pilih][1] += barang_masuk
                        break
                    else:
                        print('tidak boleh kurang dari 0 atau 0')
                else:
                    print('tidak boleh huruf') 
            print('barang berhasil di masukkan')

            print('data barang masuk diperbahurui')
            for i,data in enumerate(list_barang):

                print(f'{i+1}. nama : {data[0]}   | stok: {data[1]}')
        else:
            print('harus mengisi nomor 1') 

    elif pilih_menu == 4:
        print('data barang keluar')
        if len(list_barang) >0:
            for i,data in enumerate(list_barang):

                print(f'{i+1}. nama : {data[0]}   | stok: {data[1]}')  

            while True:
                input_pilih_barang = input('pilih barang : ')

                if input_pilih_barang.isdigit():

                    pilih_barang = int(input_pilih_barang)
                    pilih = pilih_barang -1
                    if   pilih_barang >=0 and pilih_barang <= len(list_barang) :
                        break
                    else:
                        print('data tidak ditemukan')
                else:
                    print('tidak boleh huruf')        

            while True:
                input_barang_keluar = input('masukkan jumlah barang keluar : ')

                if input_barang_keluar.isdigit():

                    barang_keluar = int(input_barang_keluar)

                    if barang_keluar >0 and barang_keluar <= list_barang[pilih][1]:
                        list_barang[pilih][1] -= barang_keluar
                        break
                    else:
                        print('tidak boleh kurang dari 0 atau kurang atau barang melebihi list')
                else:
                    print('tidak boleh huruf') 
            print('barang berhasil di masukkan')

            print('data barang keluar')
            for i,data in enumerate(list_barang):

                print(f'{i+1}. nama : {data[0]}   | stok: {data[1]}')
        else:
            print('harus mengisi nomor 1') 
            
    elif pilih_menu == 5:

        if len(list_barang) >0:
            print('cari barang')
            ketemu = False
            nama_barang = input('masukkan nama barang : ').lower()

            for i,data in enumerate(list_barang):
                
                if nama_barang == data[0]:
                    print('barang ditemukan')
                    print(f'nama {data[0]} | stok : {data[1]}')
                    ketemu = True

            if ketemu == False:
                print('barang tidak ditemukan')    
        else:
            print('harus mengigi nomor 1')

    elif pilih_menu == 6:
        if len(list_barang) >0:
            print('---STATISTIK GUDANG ---')

            total_stok = 0
            list_stok = []

            for data in list_barang:
                total_stok += data[1]

                list_stok.append(data[1])

            terbesar = max(list_stok)
            terkecil = min(list_stok)


            print(f'totsl jenis barang : {len(list_stok)}')
            print(f'total semua stok : {total_stok}')    
            print(f'terbesar = {terbesar}')
            print(f'terkecil : {terkecil}')
              
        else:
            print('harus mengigi nomor 1')
        
    elif pilih_menu == 7 :
        if len(list_barang) >0:
            for i,data in enumerate(list_barang):

                print(f'{i+1}. nama : {data[0]}   | stok: {data[1]}')  

            while True:
                input_hapus_barang = input('pilih barang yang mau dihapus : ')

                if input_hapus_barang.isdigit():
                    i_hapus_barang = int(input_hapus_barang)
                    hapus_barang = i_hapus_barang -1

                    if hapus_barang >= 0 and hapus_barang <=len(list_barang):
                        list_barang.pop(hapus_barang)
                        break
                    else:
                        print(f'data tidak ditemukan')
                else:
                    print('tidak boleh huruf')

            print('data telah dihapus')
            for i,data in enumerate(list_barang):

                print(f'{i+1}. nama : {data[0]}   | stok: {data[1]}')      
        else: 
            print('harus mengisi nomor 1 ')    

    elif pilih_menu == 8:
        print('PROGRAM SELESAI')
        exit()        