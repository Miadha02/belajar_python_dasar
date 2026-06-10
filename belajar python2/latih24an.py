print('='*20)
print('SISTEM HOTEL')
print('='*20)

while True:
    input_jumlah_baris = input('masukkan jumlah baris : ')

    if input_jumlah_baris.isdigit():
        jumlah_baris = int(input_jumlah_baris)

        if jumlah_baris >0:
            break
        else:
            print('tidak boleh 0 atau kurang')
    else:
        print('tidak boleh huruf')        

while True:

    input_jumlah_kolom = input('masukkan jumlah kolom : ')

    if input_jumlah_kolom.isdigit():
        jumlah_kolom = int(input_jumlah_kolom)

        if jumlah_kolom >0:
            break
        else:
            print('tidak boleh 0 atau kurang')
    else:
        print('tidak boleh huruf')

list_kamar = []
list_hotel = []
nomor = 1
for ulang1 in range(jumlah_baris):
    baris = []
    check = []

    for ulang2 in range(jumlah_kolom):
        baris.append(nomor)
        check.append('O')
        nomor +=1
    list_kamar.append(baris)
    list_hotel.append(check)

while True:
    print('''
1.Lihat Denah Hotel
2.Check In
3.Check Out
4.Cari Kamar
5.Statistik Hotel
6.Keluar                    
''')

    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():
            pilih_menu = int(input_pilih_menu)

            if pilih_menu >0 and pilih_menu <=6:
                break
            else:
                print('pilih 1 - 6')
        else:
            print('tidak boleh huruf')

    if pilih_menu == 1:
        print('Denah Hotel')

        print('\nnomor kamar')
        for data in list_kamar:
            for kamar in data:
                print(f'{kamar} ', end='')
            print()    
        
        print('\nStatus Kamar')
        for check_hotel in list_hotel:
            for check_h in check_hotel:
                print(f'{check_h} ', end='')
            print()    

    elif pilih_menu == 2:

        while True:
            input_nomor_kamar = input('masukkan nama kamar : ')

            if input_nomor_kamar.isdigit():

                nomor_kamar = int(input_nomor_kamar)

                if nomor_kamar >0:
                    break
                else:
                    print('tidak boleh 0 atau kurang')
            else:
                print('tidak boleh huruf')
        ketemu = False
        for i, baris in enumerate(list_kamar):
            for j, kamar in enumerate(baris):

                if kamar == nomor_kamar:
                    if list_hotel[i][j] == 'O':
                        list_hotel[i][j] = 'X'
                        print('check in berhasil')
                        ketemu = True
                    else:
                        print('kamar sudah terisi')
                        ketemu = True               
        if ketemu == False:
            print('nomor tidak ada ')               

    elif pilih_menu == 3:
        while True:
            input_nomor_kamar = input('masukkan nama kamar : ')

            if input_nomor_kamar.isdigit():

                nomor_kamar = int(input_nomor_kamar)

                if nomor_kamar >0:
                    break
                else:
                    print('tidak boleh 0 atau kurang')
            else:
                print('tidak boleh huruf')

        ketemu = False
        for i, baris in enumerate(list_kamar):
            for j, kamar in enumerate(baris):

                if kamar == nomor_kamar:
                    if list_hotel[i][j] == 'X':
                        list_hotel[i][j] = 'O'
                        print('check out berhasil')
                        ketemu = True
                    else:
                        print('kamar sudah kosong')
                        ketemu = True               
        if ketemu == False:
            print('nomor tidak ada ')

    elif pilih_menu == 4:
        while True:
            input_nomor_kamar = input('masukkan nama kamar : ')

            if input_nomor_kamar.isdigit():

                nomor_kamar = int(input_nomor_kamar)

                if nomor_kamar >0:
                    break
                else:
                    print('tidak boleh 0 atau kurang')
            else:
                print('tidak boleh huruf')

        ketemu = False
        for i,cari1 in enumerate(list_kamar):
            for j,cari2 in enumerate(cari1):

                if nomor_kamar == cari2 :
                    ketemu = True
                    print('kamar ditemukan')

                    print(f'nomor kamar : {cari2}')
                    print(f'baris : {i+1}') 
                    print(f'kolom : {j+1}')

                    if list_hotel[i][j] == 'O':
                        print('status : kamar kosong')  


                    else:
                        print('status : kamar terisi')     

        if ketemu == False:
            print('kamar tidak ditemukan')         

    elif pilih_menu == 5:
        print('---STATISTIK HOTEL---')

        print(f'total kamar = {jumlah_baris * jumlah_kolom}')

        kamar_kosong = 0
        kamar_terisi = 0

        for data in list_hotel:

            for data1 in data:
                if data1 == 'X':
                    kamar_terisi += 1
                else:
                    kamar_kosong +=1

        print(f'kamar kosong ={kamar_kosong}')
        print(f'kamar terisi : {kamar_terisi}')      

    elif pilih_menu == 6:
        print(f'program selesai') 
        exit()             
                           


                



                


