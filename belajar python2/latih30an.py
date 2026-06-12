print('''
========================
SISTEM RUMAH SAKIT
========================
''')

while True:
    input_jumlah_baris = input('masukkan jumlah lantai : ')

    if input_jumlah_baris.isdigit():
        jumlah_baris = int(input_jumlah_baris)

        if jumlah_baris >0:
            break
        else:
            print('tidak boleh kurang dari 1')
    else:
        print('tidak boleh huruf')

while True:
    input_jumlah_kolom = input('masukkan jumlah kamar per lantai : ')

    if input_jumlah_kolom.isdigit():
        jumlah_kolom = int(input_jumlah_kolom)

        if jumlah_kolom >0:
            break
        else:
            print('tidak boleh kurang dari 1')

    else:
        print('tidak boleh huruf')

list_nomor_kamar = []
list_status_kamar = []
list_nama_pasien = []
list_lama_rawat = []
for i in range(jumlah_baris):

    baris_nomor_kamar = []
    baris_status_kamar = []
    baris_nama_pasien = []
    baris_lama_rawat = []
    for j in range(jumlah_kolom):
        nomor_kamar = chr(65+i) + str(j +1)
        status_kamar = 'O'
        nama_pasien = '-'
        lama_rawat = 0

        baris_nomor_kamar.append(nomor_kamar)
        baris_status_kamar.append(status_kamar)
        baris_nama_pasien.append(nama_pasien)
        baris_lama_rawat.append(lama_rawat)

    
    list_nomor_kamar.append(baris_nomor_kamar)
    list_status_kamar.append(baris_status_kamar)
    list_nama_pasien.append(baris_nama_pasien)
    list_lama_rawat.append(baris_lama_rawat)

while True:

    print('''
1.LIHAT RUMAH SAKIT
2.RAWAT INAP PASIEN
3.PASIEN PULANG
4.CARI PASIEN
5.PINDAH KAMAR
6.STATISTIK RUMAH SAKIT
7.PASIEN TERLAMA
8.TUKAR KAMAR DUA PASIEN
9.KELUAR
''')
    
    
    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():
            pilih_menu = int(input_pilih_menu)

            if pilih_menu >0 and pilih_menu <= 9:
                break
            else:
                print('hanya 1 - 9')
        else:
            print('tidak boleh huruf')

    if pilih_menu == 1:

        print('-----DATA RUMAH SAKIT ------')

        print('NOMOR KAMAR')

        for ulang in list_nomor_kamar:
            for ulang1 in ulang:
                print(ulang1,end=' ')
            print()

        print('\nSTATUS')

        for ulang2 in list_status_kamar:
            for ulang3 in ulang2:
                print(ulang3, end='  ')
            print()

        print('\nNAMA PASIEN')

        for ulang4 in list_nama_pasien:
            for ulang5 in ulang4:
                print(ulang5, end='  ')
            print()

        print('\nLAMA RAWAT')

        for ulang6 in list_lama_rawat:
            for ulang7 in ulang6:
                print(ulang7,end='  ')
            print()


    elif pilih_menu == 2:

        no_kamar = input('nomor kamar : ').upper()
        ketemu_kamar = False

        for i,data in enumerate(list_nomor_kamar):

            for j,data1 in enumerate(data):

                if data1 == no_kamar:
                        
                    if list_status_kamar[i][j] == 'O':    

                        nama_pasien_rawat = input('masukkan nama pasien : ').upper()
                        
                        while True:
                            input_lama_rawat_pasien = input('lama rawat : ')

                            if input_lama_rawat_pasien.isdigit():
                                lama_rawat_pasien = int(input_lama_rawat_pasien)

                                if lama_rawat_pasien >0 :
                                    break
                                else:
                                    print('tidak boleh kurang dari 1')
                            else:
                                print('tidak boleh huruf')

                        list_status_kamar[i][j] = 'X'
                        list_nama_pasien[i][j] = nama_pasien_rawat
                        list_lama_rawat[i][j] = lama_rawat_pasien
                        print('\nrawat inap berhasil')
                        ketemu_kamar = True
                        break

                    else:
                        print('KAMAR SUDAH ADA ORANG')
                        ketemu_kamar = True
                        break
        
        if ketemu_kamar == False:
            print('data kamar tidak tersedia')

    elif pilih_menu == 3:

        pasien_pulang = input('nomor kamar : ').upper()
        ketemu_pulang = False

        for i,pulang in enumerate(list_nomor_kamar):

            for j,pulang1 in enumerate(pulang):

                if pulang1 == pasien_pulang:

                    if list_status_kamar[i][j] == 'X':

                        list_status_kamar[i][j] ='O'
                        list_nama_pasien[i][j] = '-'
                        list_lama_rawat[i][j] = 0
                        print('\n PASIEN PULANG BERHASIL')
                        ketemu_pulang = True
                        break

                    else:
                        print('KAMAR PASIEN MEMANG SUDAH KOSONG')
                        ketemu_pulang = True
                        break

        if ketemu_pulang == False:
            print('DATA KAMAR TIDAK TERSEDIA')


    elif pilih_menu == 4:

        nama_pasien_cari = input('nama pasien : ').upper()
        ketemu_cari_pasien = False

        for i,nama in enumerate(list_nama_pasien):

            for j,nama1 in enumerate(nama):
                
                if nama1 == nama_pasien_cari:
                    print('\nPASIEN DITEMUKAN')

                    print(f'nama : {nama1}')
                    print(f'kamar : {list_nomor_kamar[i][j]}')
                    print(f'lantai : {list_nomor_kamar[i][j][0]}')
                    print(f'nomor : {list_nomor_kamar[i][j][1]}')
                    print(f'lama rawat : {list_lama_rawat[i][j]}')

                    ketemu_cari_pasien = True

        if ketemu_cari_pasien == False:
            print('DATA PASIEN TIDAK DITEMUKAN')            


    elif pilih_menu == 5:

        kamar_asal = input('kamar asal : ').upper()
        ketemu_pindah = False

        for q,kamar0 in enumerate(list_nomor_kamar):

            for w,kamar1 in enumerate(kamar0):

                if kamar1 == kamar_asal:

                    if list_status_kamar[q][w] == 'X':

                        kamar_tujuan = input('kamar tujuan : ').upper()

                        for e,kamar2 in enumerate(list_nomor_kamar):

                            for r,kamar3 in enumerate(kamar2):

                                if kamar3 == kamar_tujuan:

                                    if list_status_kamar[e][r] == 'O':
                                        
                                        list_status_kamar[e][r] = list_status_kamar[q][w]
                                        list_status_kamar[q][w] = 'O'

                                        list_nama_pasien[e][r] = list_nama_pasien[q][w]
                                        list_nama_pasien[q][w]= '-'

                                        list_lama_rawat[e][r] = list_lama_rawat[q][w]
                                        list_lama_rawat[q][w] = 0

                                        print('pindah kamar berhasil')
                                        ketemu_pindah = True
                                        break
                                        

                                    else:
                                        print('kamar sudah terisi, coba pilih kamar lain ')
                                        ketemu_pindah = True
                                        break

                    else:
                        print('kamar sudah kosong , tidak bisa dipindah')
                        ketemu_pindah = True
                        break
        
        if ketemu_pindah == False:
            print('DATA KAMAR TIDAK TERSEDIA')

    elif pilih_menu == 6:
        print('----STATISTIK RUMAH SAKIT ------')

        total_kamar = jumlah_baris * jumlah_kolom

        kamar_terisi = 0
        kamar_kosong = 0
        pasien_jumlah = 0
        list_jumlah_pasien = []

        for p,stat in enumerate(list_status_kamar):
            jumlah_pasien = 0

            for l,stat1 in enumerate(stat):

                if stat1 == 'O':
                    kamar_kosong +=1

                else:
                    kamar_terisi +=1   
                    pasien_jumlah += 1
                    jumlah_pasien +=1

            list_jumlah_pasien.append(jumlah_pasien)

        print(f'total kamar : {total_kamar}')
        print(f'kamar terisi : {kamar_terisi}')
        print(f'kamar kosong : {kamar_kosong}')


        persentase_terisi = (kamar_terisi / total_kamar) * 100
        
        print(f'persentase terisi : {persentase_terisi}')


        for h,jlh_pasien in enumerate(list_jumlah_pasien):
            print(f'{chr(65 + h)}. {jlh_pasien} pasien')               
        
        pasien_max = max(list_jumlah_pasien)
        index_max = list_jumlah_pasien.index(pasien_max)

        print(f'lantai paling ramai : {chr(65 + index_max)}')
        print(f'jumlah pasien : {pasien_max}')

        pasien_min = min(list_jumlah_pasien)
        index_min = list_jumlah_pasien.index(pasien_min)
        
        print(f'lantai paling sepi : {chr(65 + index_min)}')
        print(f'jumlah pasien : {pasien_min}')

        total_lama_rawat = 0
        for lama_rpasien in list_lama_rawat:

            for rpasien in lama_rpasien:

                total_lama_rawat += rpasien

        print(f'total_lama rawat : {total_lama_rawat}') 

    elif pilih_menu == 7:

        terbesar = 0

        for i,rawat_pasien1 in enumerate(list_lama_rawat):

            for j,rawat_pasien2 in enumerate(rawat_pasien1):

                if rawat_pasien2 > terbesar:

                    terbesar = rawat_pasien2

                    nama_terbesar = list_nama_pasien[i][j]
                    kamar_terbesar = list_nomor_kamar[i][j]

        if terbesar >0:
            print('----PASIEN TERLAMA----')

            print(f'nama_terbesar : {nama_terbesar}')
            print(f'kamar : {kamar_terbesar}')
            print(f'lama rawat : {terbesar}')

        else:
            print('BELUM ADA PASIEN YANG DIRAWAT')


    elif pilih_menu == 8:
        ketemu_change = False

        kamar_pertama = input('kamar pertama : ').upper()

        for x,pertama in enumerate(list_nomor_kamar):

            for y,kedua in enumerate(pertama):

                if kedua == kamar_pertama:

                    if list_status_kamar[x][y] == 'X':

                        kamar_kedua = input('kamar kedua : ')

                        for c,ketiga in enumerate(list_nomor_kamar):

                            for v,keempat in enumerate(ketiga):

                                if keempat == kamar_kedua:

                                    if list_status_kamar[c][v] == 'X':

                                        list_nama_pasien[x][y],list_nama_pasien[c][v] = list_nama_pasien[c][v],list_nama_pasien[x][y]
                                        list_lama_rawat[x][y],list_lama_rawat[c][v] = list_lama_rawat[c][v],list_lama_rawat[x][y]

                                        print('kamar berhasil ditukar')
                                        ketemu_change = True
                                        break

                                    else:
                                        print('kamar masih kosong')
                                        ketemu_change = True
                                        break    

                    else:
                        print('kamar masih kosong')
                        ketemu_change = True
                        break


        if ketemu_change == False:
            print('data kamar tidak ditemukan !')


    elif pilih_menu == 9:
        print('program dihentikan')
        exit()                    

                





            

    








                               




