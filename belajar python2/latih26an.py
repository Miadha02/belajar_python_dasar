list_mobil = []
while True:

    print(f'''
================
SISTEM RENTAL MOBIL
================
1.Tambah Mobil
2.Lihat Mobil
3.Rental Mobil
4.Kembalikan Mobil
5.Cari Mobil
6.Statistik Rental
7. Hapus Mobil
8. Keluar
''')
    
    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():

            pilih_menu = int(input_pilih_menu)

            if pilih_menu > 0 and pilih_menu <=8:
                break
            else:
                print('harus 1 - 8')
        else:
            print('tidak boleh huruf')

    if pilih_menu == 1:
        status = 'tersedia'
        rental = 0
        while True:
            nama_mobil = input('masukkan nama mobil : ').lower()

            if len(nama_mobil) > 2:
                break
            else:
                print('nama mobil tidak boleh kurang dari 2')

        tambah_mobil = [nama_mobil,status,rental]
        list_mobil.append(tambah_mobil)

        print('mobil berhasil ditambahkan')
    
    elif pilih_menu == 2:

        if len(list_mobil)>0:

            for i,data in enumerate(list_mobil):
                print(f'{i+1}. {data[0]} | {data[1]}  | total rental : {data[2]} jam')
        else:
            print('harus mengisi nomor 1')    

    elif pilih_menu == 3:
        if len(list_mobil) >0:
            for i,data in enumerate(list_mobil):
                print(f'{i+1}. {data[0]} | {data[1]}  | total rental : {data[2]} jam')

            while True:
                input_pilih_mobil = input('pilih mobil : ')

                if input_pilih_mobil.isdigit():

                    pilih_mobil = int(input_pilih_mobil)

                    index = pilih_mobil -1

                    if index >=0 and index < len(list_mobil):
                        break

                    else:
                        print('data tidak tersedia')
                else:
                    print('tidak boleh huruf')

            if list_mobil[index][1] == 'tersedia':
                while True:
                    input_lama_rental = input('masukkan lama rental : ')

                    if input_lama_rental.isdigit():
                        lama_rental = int(input_lama_rental)

                        if lama_rental >0:
                            break
                        else:
                            print('tidak boleh kurang dari 1')
                    else:
                        print('tidak boleh huruf')

                list_mobil[index][2] += lama_rental
                list_mobil[index][1] = 'disewa'

                print('mobil berhasil dirental ')   
                for i,data in enumerate(list_mobil):
                    print(f'{i+1}. {data[0]} | {data[1]}  | total rental : {data[2]} jam')                     

            else:
                print('harus memilih mobil yang statusnya tersedia')
        else:
            print('harus mengisi nomor 1')

    elif pilih_menu == 4:
        if len(list_mobil) >0:
            for i,data in enumerate(list_mobil):
                print(f'{i+1}. {data[0]} | {data[1]}  | total rental : {data[2]} jam')

            while True:
                input_pilih_kembali = input('pilih mobil : ')

                if input_pilih_kembali.isdigit():
                  
                    index_kembali = (int(input_pilih_kembali)) -1

                    if index_kembali >=0 and index_kembali < len(list_mobil):
                        break
                    else:
                        print('data tidak ditemukan')
                else:
                    print('tidak boleh huruf ') 

            if list_mobil[index_kembali][1] == 'disewa':
                list_mobil[index_kembali][2] = 0
                list_mobil[index_kembali][1] = 'tersedia'

                print('mobil berhasil dikembalikan')
            else:
                print('mobil masih tersedia , tidak bisa dikembalikan')
        else:
            print('harus mengisi nomor 1')            

    elif pilih_menu == 5:

        if len(list_mobil) >0:
            cari_mobil = input('masukkan nama mobil : ').lower()
            ketemu = False

            for cari in list_mobil:

                if cari_mobil == cari[0]:
                    print('mobil ditemukan')
                    print(f'mobil = {cari[0]}')
                    print(f'status = {cari[1]}')
                    print(f'total rental = {cari[2]}')
                    ketemu = True
                    break

            if ketemu == False:
                print('mobil tidak ditemukan')        

        else:
           print('harus mengisi nomor 1')

    elif pilih_menu == 6:
        if len(list_mobil) > 0:
            
            print('---STATISTIK RENTAL---')
            mobil_tersedia = 0
            mobil_disewa = 0
            total_jam_rental = 0
            list_rental = []
            
            for data in list_mobil:
                total_jam_rental += data[2]
                list_rental.append(data[2])

                if data[1] == 'tersedia':
                    mobil_tersedia += 1

                else:
                    mobil_disewa +=1

            print(f'total mobil = {len(list_mobil)}')
            print(f'mobil tersedia = {mobil_tersedia}')
            print(f'mobil disewa = {mobil_disewa}')
            print(f'total jam rental = {total_jam_rental} jam')
            print(f'rental terbesar = {max(list_rental)} jam')
            print(f'rental terkecil = {min(list_rental)} jam')

            for data in list_mobil:

                if data[2] == max(list_rental):
                    print(f'mobil rental terbesar : {data[0]} ({max(list_rental)} jam)')
                    break

            for data1 in list_mobil:
                if data1[2] == min(list_rental):
                    print(f'mobil rental terkecil : {data1[0]} ({min(list_rental)} jam)')  
                    break 
        else:
            print('harus mengisi nomor 1')        

    elif pilih_menu == 7:
        if len(list_mobil) >0:
            for i,data in enumerate(list_mobil):
                print(f'{i+1}. {data[0]} | {data[1]}  | total rental : {data[2]} jam') 

            while True:
                input_pilih_hapus = input('pilih mobil yang ingin dihapus : ')

                if input_pilih_hapus.isdigit():

                    index_hapus = (int(input_pilih_hapus)) -1

                    if index_hapus >=0 and index_hapus < len(list_mobil):
                        break
                    else:
                        print('data tidak ditemukan')
                else:
                    print('tidak boleh huruf')        

            list_mobil.pop(index_hapus)

            print('mobil berhasil dihapus ')            
        else:
            print('harus mengisi nomor 1')    

    elif pilih_menu == 8:
        print('program dihentikan') 
        exit()       
                   

           