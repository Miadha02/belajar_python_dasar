list_ps = []
while True:

    print('='*20)
    print('  SISTEM RENTAL PS')
    print('='*20,'\n')
    print(f'''1.Tambah PS
2.Lihat Data PS
3.Rental Ps
4.Kembalikan PS
5.Cari PS
6.Statistik Rental
7.Hapus PS
8.Keluar
    ''')
    
    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():

            pilih_menu = int(input_pilih_menu)

            if pilih_menu > 0 and pilih_menu <=8:
                break
            else:
                print('input tidak sesuai')
        else:
            print('tidak bileh huruf')

    if pilih_menu == 1:

        input_nama_ps = input('masukkan nama ps : ')
        status = 'kosong'
        rental = 0
        data_ps = [input_nama_ps,status,rental]

        list_ps.append(data_ps)

    elif pilih_menu == 2:

        if len(list_ps) >0:

            for i,data in enumerate(list_ps):
                print(f'{i+1}. | {data[0]}  | status : {data[1]} | rental : {data[2]}')

        else:
            print('harus mengisi nomor 1 dahulu')            

    elif pilih_menu == 3:

        if len(list_ps) >0:
            for i,data in enumerate(list_ps):
                print(f'{i+1}. | {data[0]}  | status : {data[1]} | rental : {data[2]} jam')

            while True:
                input_pilih_ps = input('pilih ps : ')

                if input_pilih_ps.isdigit():

                    pilih_ps = int(input_pilih_ps)

                    index = pilih_ps -1

                    if index >= 0 and index < len(list_ps):
                        break
                    else:
                        print('data tidak ditemukan')
                else:
                    print('tidak boleh pakai huruf')

            while True:
                input_lama_rental = input('masukkan lama rental : ')

                if input_lama_rental.isdigit():

                    lama_rental = int(input_lama_rental)

                    if lama_rental >0:
                        list_ps[index][2] += lama_rental 
                        list_ps[index][1] = 'dipakai'
                        break
                    else:
                        print('tidak boleh 0 atau kurang')
                else:
                    print('tidak boleh huruf')
        else:
            print('harus mengisi nomor 1 dahulu')   

    elif pilih_menu == 4:
        if len(list_ps) >0:
            for i,data in enumerate(list_ps):
                print(f'{i+1}. | {data[0]}  | status : {data[1]} | rental : {data[2]} jam')

            while True:
                input_pilih_kembali = input('pilih ps yang ingin dikembalikan : ')

                if input_pilih_kembali.isdigit():

                    pilih_kembali = int(input_pilih_kembali)

                    index = pilih_kembali -1

                    if index >= 0 and index < len(list_ps):

                        if list_ps[index][1] == 'dipakai':
                            list_ps[index][1] = 'kosong'
                            list_ps[index][2] = 0
                            print('ps berhasil dikembalikan')
                            break
                        
                        else:
                            print('ps memang kosong')
                            break
                    else:
                        print('data tidak ditemukan')            

                else:
                    print('tidak boleh huruf')                                
        else:
            print('harus mengisi nomor 1 dahulu')

    elif pilih_menu == 5:
        if len(list_ps) >0:
            
            cari_ps = input('masukkan nama ps : ')
            ketemu = False

            for data in list_ps:

                if cari_ps == data[0]:
                    print('data ditemukan')
                    print(f'nama {data[0]}')
                    print(f'status {data[1]}')
                    print(f'rental {data[2]}')
                    ketemu = True


            if ketemu == False:
                print('data tidak ditemukan')

        else:
            print('harus mengisi nomor 1 dahulu')

    elif pilih_menu == 6:
        if len(list_ps) >0:
            print('----STATISTIK RENTAL---') 

            total_jam_rental = 0
            ps_kosong = 0
            ps_dipakai = 0
            for data in list_ps:

                total_jam_rental += data[2]

                if data[1] == 'kosong':
                    ps_kosong += 1
                else:
                    ps_dipakai += 1

            print(f'total ps = {len(list_ps)}')
            print(f'ps dipakai : {ps_dipakai}')
            print(f'ps kosong : {ps_kosong}')
            print(f'total jam rental : {total_jam_rental}')
        else:
            print('harus mengisi nomor 1 dahulu')    

    elif pilih_menu == 7:
        if len(list_ps) >0:
            for i,data in enumerate(list_ps):
                print(f'{i+1}. | {data[0]}  | status : {data[1]} | rental : {data[2]} jam')

            while True:
                input_ps_hapus = input('pilih ps yang ingin dihapus : ')

                if input_ps_hapus.isdigit():

                    ps_hapus = int(input_ps_hapus) 

                    index = ps_hapus -1

                    if index >=0 and index < len(list_ps):

                        list_ps.pop(index)
                        print('data berhasil dihapus')
                        break

                    else:
                        print('data tidak ditemukan')
                else:
                    print('tidak boleh huruf')
        else:
            print('harus mengisi nomor 1 dahulu')      

    elif pilih_menu == 8:
        print('program dihentikan') 
        exit()                     





                        