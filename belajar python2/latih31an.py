print('''
=============================
SISTEM BANDARA INTERNASIONAL
=============================      
''')

while True:
    input_jumlah_baris = input('masukkan jumlah baris : ')

    if input_jumlah_baris.isdigit():
        jumlah_baris = int(input_jumlah_baris)

        if jumlah_baris > 0:
            break
        else:
            print('tidak boleh kurang dari 1')
    else:
        print('tidak boleh huruf')

while True:

    input_jumlah_kolom = input('masukkan jumlah kolom : ')

    if input_jumlah_kolom.isdigit():
        jumlah_kolom = int(input_jumlah_kolom)

        if jumlah_kolom > 0:
            break
        else:
            print('tidak boleh kurang dari 1')

    else:
        print('tidak boleh huruf')


list_letak_kursi = []
list_letak_status = []
list_letak_nama = []
list_letak_tujuan = []
list_letak_bagasi = []

for baris1 in range(jumlah_baris):
    baris_letak_kursi =[]
    baris_letak_status = []
    baris_letak_nama = []
    baris_letak_tujuan = []
    baris_letak_bagasi = []

    for kolom in range(jumlah_kolom):
        kolom_letak_kursi = chr(65 + baris1) + str(kolom + 1)
        kolom_letak_status = 'O'
        kolom_letak_nama = '-'
        kolom_letak_tujuan = '-'
        kolom_letak_bagasi = 0

        baris_letak_kursi.append(kolom_letak_kursi)
        baris_letak_status.append(kolom_letak_status)
        baris_letak_nama.append(kolom_letak_nama)
        baris_letak_tujuan.append(kolom_letak_tujuan)
        baris_letak_bagasi.append(kolom_letak_bagasi)

    list_letak_kursi.append(baris_letak_kursi)
    list_letak_status.append(baris_letak_status)
    list_letak_nama.append(baris_letak_nama) 
    list_letak_tujuan.append(baris_letak_tujuan)
    list_letak_bagasi.append(baris_letak_bagasi)


while True:
    print('''
1.Lihat Data Pesawat
2.Check In Penumpang
3.Boarding Batal
4.Cari Penumpang
5.Pindah Kursi
6.Tukar Kursi Dua Penumpang
7.Statistik Pesawat
8.Penumpang Bagasi Terberat
9.Tujuan Terpopuler
10.Keluar
''')
    

    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():
            pilih_menu = int(input_pilih_menu)

            if pilih_menu >0 and pilih_menu <= 10:
                break
            else:
                print('hanya 1 - 10')
        else:
            print('tidak boleh huruf')


    if pilih_menu == 1:
        print('---DATA PESAWAT----')

        print('\n---KURSI---')
        for data_kursi in list_letak_kursi:
            for data_kursi1 in data_kursi:
                print(data_kursi1, end= '  ')
            print()

        print('\n---STATUS---')
        for data_status in list_letak_status:
            for data_status1 in data_status:
                print(data_status1, end='  ')
            print()

        print('\n---NAMA---')
        for data_nama in list_letak_nama:
            for data_nama1 in data_nama:
                print(data_nama1, end='  ')
            print()

        print('\n---TUJUAN----')
        for data_tujuan in list_letak_tujuan:
            for data_tujuan1 in data_tujuan:
                print(data_tujuan1,end='  ')
            print()

        print('\n---BAGASI----')
        for data_bagasi in list_letak_bagasi:
            for data_bagasi1 in data_bagasi:
                print(data_bagasi1, end='  ')
            print()

    elif pilih_menu == 2:

        checkin_kursi = input('kursi : ').upper()
        ketemu_checkin = False

        for i,check_kursi in enumerate(list_letak_kursi):

            for j,check_kursi1 in enumerate(check_kursi):

                if check_kursi1 == checkin_kursi:

                    if list_letak_status[i][j] == 'O':

                        while True:
                            checkin_nama = input('nama : ').upper()

                            if checkin_nama.replace(' ','').isalpha():
                                break
                            else:
                                print('tidak boleh angka')

                        while True:
                            checkin_tujuan = input('tujuan : ').upper()

                            if checkin_tujuan.replace(' ','').isalpha():
                                break
                            else:
                                print('tidak boleh angka ')

                        while True:
                            i_checkin_bagasi = input('bagasi : ')

                            if i_checkin_bagasi.isdigit():
                                checkin_bagasi = int(i_checkin_bagasi)

                                if checkin_bagasi >0 and checkin_bagasi <= 100:
                                    break
                                else:
                                    print('hanya 1 - 100 kg')

                            else:
                                print('tidak boleh huruf')
                                        
                        list_letak_status[i][j] = 'X'
                        list_letak_nama[i][j] = checkin_nama
                        list_letak_tujuan[i][j] = checkin_tujuan
                        list_letak_bagasi[i][j] = checkin_bagasi

                        print('Check in Berhasil ')
                        ketemu_checkin = True
                        break

                    else:
                        print('kursi sudah terisi , mohon pilih kursi yang lain')    
                        ketemu_checkin = True
                        break        

        if ketemu_checkin == False:
            print('DATA KURSI TIDAK DITEMUKAN ')

    elif pilih_menu == 3:

        kursi_batal = input('kursi : ').upper()
        ketemu_batal = False

        for i,batal_kursi in enumerate(list_letak_kursi):

            for j,batal_kursi1 in enumerate(batal_kursi):

                if batal_kursi1 == kursi_batal :

                    if list_letak_status[i][j] == 'X':

                        list_letak_status[i][j] = 'O'
                        list_letak_nama[i][j] = '-'
                        list_letak_tujuan[i][j] = '-'
                        list_letak_bagasi[i][j] = 0

                        print('boarding dibatalkan ')
                        ketemu_batal = True
                        break

                    else:
                        print('Kursi memang sudah kosong')
                        ketemu_batal = True
                        break

        if ketemu_batal == False:
            print('DATA KURSI TIDAK DITEMUKAN')

    elif pilih_menu == 4:

        nama_cari = input('nama : ').upper()
        ketemu_cari = False

        for i,cari_nama in enumerate(list_letak_nama):

            for j,cari_nama1 in enumerate(cari_nama):

                if cari_nama1 == nama_cari:
                    print('\n---DATA DITEMUKAN---')

                    print(f'nama : {cari_nama1}')
                    print(f'kursi : {list_letak_kursi[i][j]}')
                    print(f'tujuan : {list_letak_tujuan[i][j]}')
                    print(f'bagasi : {list_letak_bagasi[i][j]}')

                    ketemu_cari = True
                    break
                    
        if ketemu_cari == False:
            print('DATA NAMA TIDAK DITEMUKAN')

                        
    elif pilih_menu == 5:

        kursi_awal = input('kursi awal : ').upper()
        ketemu_pindah = False

        for a,pindah in enumerate(list_letak_kursi):
            
            for b,pindah1 in enumerate(pindah):

                if pindah1 == kursi_awal:

                    if list_letak_status[a][b] == 'X':
                        
                        kursi_tujuan = input('kursi tujuan : ').upper()

                        for c,tujuan1 in enumerate(list_letak_kursi):

                            for d, tujuan2 in enumerate(tujuan1):

                                if tujuan2 == kursi_tujuan:

                                    if list_letak_status[c][d] == 'O':
                                        list_letak_status[a][b], list_letak_status[c][d] = list_letak_status[c][d] , list_letak_status[a][b]
                                        list_letak_nama[a][b], list_letak_nama[c][d] = list_letak_nama[c][d] , list_letak_nama[a][b]
                                        list_letak_tujuan[a][b], list_letak_tujuan[c][d] = list_letak_tujuan[c][d], list_letak_tujuan[a][b]
                                        list_letak_bagasi[a][b] , list_letak_bagasi[c][d] = list_letak_bagasi[c][d], list_letak_bagasi[a][b]

                                        print('pindah kursi berhasil')
                                        
                                        ketemu_pindah = True
                                        break

                                    else:
                                        print('kursi sudah ada yang menempati, tidak bisa pindah') 
                                        ketemu_pindah = True   
                                        break

                    else:
                        print('kursi masih kosong, tidak bisa dipindah')   
                        ketemu_pindah = True
                        break 

        if ketemu_pindah == False:
            print('data kursi tidak ditemukan')            


    elif pilih_menu == 6:
        kursi_pertama = input('kursi pertama : ').upper()
        ketemu_pindah = False

        for i,kp1 in enumerate(list_letak_kursi):

            for j,kp2 in enumerate(kp1):

                if kp2 == kursi_pertama:

                    if list_letak_status[i][j] == 'X':

                        kursi_kedua = input('kursi kedua : ').upper()

                        for k,kk1 in enumerate(list_letak_kursi):

                            for l,kk2 in enumerate(kk1):

                                if kk2 == kursi_kedua:

                                    if list_letak_status[k][l] == 'X':

                                        list_letak_status[i][j], list_letak_status[k][l] = list_letak_status[k][l] , list_letak_status[i][j]
                                        list_letak_nama[i][j], list_letak_nama[k][l] = list_letak_nama[k][l] , list_letak_nama[i][j]
                                        list_letak_tujuan[i][j], list_letak_tujuan[k][l] = list_letak_tujuan[k][l], list_letak_tujuan[i][j]
                                        list_letak_bagasi[i][j] , list_letak_bagasi[k][l] = list_letak_bagasi[k][l], list_letak_bagasi[i][j]

                                        print('KURSI BERHASIL DI TUKAR ')

                                        ketemu_pindah = True
                                        break

                                    else:
                                        print('kursi masih kosong')
                                        ketemu_pindah = True
                                        break
                    else:
                        print('kursi masih kosong ') 
                        ketemu_pindah = True
                        break

        if ketemu_pindah == False:
            print('data kursi tidak ditemukan ')

    elif pilih_menu == 7:
        print('-------STATISTIK PESAWAT---------\n')

        total_kursi = jumlah_baris * jumlah_kolom

        kursi_terisi = 0
        kursi_kosong = 0
        list_jumlah = []

        for i,stat1 in enumerate(list_letak_status):
            jumlah_penumpang_total = 0

            for j,stat2 in enumerate(stat1):

                if stat2 == 'X':
                    kursi_terisi += 1
                    jumlah_penumpang_total += 1

                else:
                    kursi_kosong += 1

            list_jumlah.append(jumlah_penumpang_total)

        print(f'total kursi : {total_kursi}')
        print(f'kursi terisi : {kursi_terisi}')
        print(f'kursi kosong : {kursi_kosong}')

        for i,jlh_list in enumerate(list_jumlah):

            print(f'{chr(65+i)}. {jlh_list} penumpang')

        jumlah_max = max(list_jumlah)
        index_max = list_jumlah.index(jumlah_max)

        jumlah_min = min(list_jumlah)
        index_min = list_jumlah.index(jumlah_min)

        print(f'baris paling ramai : {chr(65+ index_max)}')
        print(f'jumlah penumpang = {jumlah_max}\n')
        
        print(f'baris paling sepi : {chr(65+index_min)}')
        print(f'jumlah penumpang : {jumlah_min}')


    elif pilih_menu == 8:
        terberat = 0

        for i,data1 in enumerate(list_letak_bagasi):

            for j,data2 in enumerate(data1):

                if data2 > terberat:

                    terberat = data2

                    nama_terbesar = list_letak_nama[i][j]
                    kursi_terbesar = list_letak_kursi[i][j]
                    bagasi_terbesar = list_letak_bagasi[i][j]

        if terberat > 0:
            print(f'PENUMPANG BAGASI TERBERAT')
            print(f'nama : {nama_terbesar}')
            print(f'kursi : {kursi_terbesar}')
            print(f'bagasi terbesar : {bagasi_terbesar}')

        else:
            print('belum ada data')   

    elif pilih_menu == 9:

        list_tujuan_populer = []

        for i,tujuan1 in enumerate(list_letak_tujuan):

            for j,tujuan2 in enumerate(tujuan1):

                if tujuan2 != '-':

                    list_tujuan_populer.append(tujuan2)

        if len(list_tujuan_populer) >0 :

            modus = max(set(list_tujuan_populer), key=list_tujuan_populer.count)
            print(f'TUJUAN POPULER \n')

            print(f'Tujuan : {modus}')

            jlh_pen = list_tujuan_populer.count(modus)
            print(f'jumlah penumpang : {jlh_pen}')

        else:
            print('data masih kosong')                

    elif pilih_menu == 10:
        print('program berakhir')
        exit()
    



