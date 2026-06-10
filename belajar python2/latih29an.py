print('===================')
print('SISTEM PARKIR MALL')
print('===================')

while True:

    i_umlah_baris = input('masukkan jumlah baris : ')

    if i_umlah_baris.isdigit():
        jumlah_baris = int(i_umlah_baris)

        if jumlah_baris >0:
            break
        else:
            print('tidak boleh kurang dari 1')
    else:
        print('tidak boleh huruf ')

while True:

    i_jumlah_kolom = input('masukkan jumlah kolom : ')

    if i_jumlah_kolom.isdigit():
        jumlah_kolom = int(i_jumlah_kolom)

        if jumlah_kolom >0:
            break
        else:
            print('tidak boleh kurang dari 1')
    else:
        print('tidak boleh huruf')

list_parkir_angka = []
list_parkir_huruf = []
list_tempat_parkir_mobil = []
for i in range(jumlah_baris):
    baris_angka = []
    baris_huruf = []

    for j in range(jumlah_kolom):

        jumlah_parkir_angka = chr(65 + i) + str(j + 1)
        jumlah_parkir_huruf = 'O'
        baris_angka.append(jumlah_parkir_angka)
        baris_huruf.append(jumlah_parkir_huruf)       
    list_parkir_angka.append(baris_angka)
    list_parkir_huruf.append(baris_huruf)

while True:
    print('''\n
1.Lihat Area Parkir
2.Parkir Kendaraan
3.Kendaraan Keluar
4.Cari Slot
5.Pindah Slot
6.Statistik Parkir
7.Cari Plat Nomor
8.Keluar ''')
    
    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():
            pilih_menu = int(input_pilih_menu)
            
            if pilih_menu >0 and pilih_menu <=8:
                break
            else:
                print('hanya 1 - 8')
        else:
            print('tidak boleh huruf')

    if pilih_menu == 1:

        print('====AREA PARKIR===')

        for data in list_parkir_angka:

            for data1 in data:
                print(data1,end='  ')
            print()

        print('\n===AREA PARKIR KOSONG===')

        for data2 in list_parkir_huruf:

            for data3 in data2:
                print(data3,end='  ')
            print()

    elif pilih_menu == 2:
        masukkan_slot = input('masukkan slot : ').upper()
        ketemu = False
        
        for i,data in enumerate(list_parkir_angka):

            for j,data1 in enumerate(data):

                if data1 == masukkan_slot:

                    if list_parkir_huruf[i][j] == 'O':
                        while True:
                            masukkan_plat = input('masukkan plat : ').upper()

                            if len(masukkan_plat) == 8:

                                list_parkir_huruf[i][j] = 'X'
                                tempat_parkir_mobil = [data1,masukkan_plat]
                                list_tempat_parkir_mobil.append(tempat_parkir_mobil)
                                print('parkir berhasil')


                                ketemu = True
                                break
                            else:
                                print('plat harus 8 digit')
                        break

                    else:
                        print('tempat parkir sudah terisi')
                        ketemu = True
                        break

        if ketemu == False:
            print('tempat parkir tidak ditemuukan ')

    elif pilih_menu == 3:
        masukkan_slot = input('masukkan slot keluar : ').upper()
        ketemu_keluar = False

        for i,data1 in enumerate(list_parkir_angka):

            for j,data2 in enumerate(data1):

                if data2 == masukkan_slot:

                    if list_parkir_huruf[i][j] == 'X':
                        
                        list_parkir_huruf[i][j] = 'O'

                        for i,data3 in enumerate(list_tempat_parkir_mobil):

                            if data3[0] == masukkan_slot:
                                list_tempat_parkir_mobil.pop(i)
                                print('parkir berhasil keluar')
                                ketemu_keluar = True
                                break
                    else:
                        print('tempat parkir memang sudah kosong')
                        ketemu_keluar = True
                        break    

        if ketemu_keluar == False:
            print('data parkir tidak ditemukan')            

    elif pilih_menu == 4:
        masukkan_slot = input('masukkan slot : ')
        ketemu_cari = False

        for i,data1 in enumerate(list_parkir_angka):
            
            for j,data2 in enumerate(data1):

                if data2 == masukkan_slot:
                    print('slot ditemukan')

                    print(f'lantai : {chr(65+i)}')
                    print(f'nomor : {str(j+1)}')

                    

                    if list_parkir_huruf[i][j] == 'X':
                        status = 'terisi'
                        print(f'status : {status}')
                        
                        for i,data3 in enumerate(list_tempat_parkir_mobil):

                            if data3[0] == masukkan_slot:
                                print(f'plat : {data3[1]}')
                                ketemu_cari = True
                                break

                    else:
                        status = 'kosong'
                        print(f'status : {status}')
                        ketemu_cari = True
                        break        

        if ketemu_cari == False:
            print('data parkir tidak ditemukan')                 

    elif pilih_menu == 5:
        slot_asal = input('slot asal : ').upper()
        ketemu_pindah = False

        for i,data1 in enumerate(list_parkir_angka):

            for j,data2 in enumerate(data1):

                if data2 == slot_asal:

                    if list_parkir_huruf[i][j] == 'X':
                        parkir = list_parkir_huruf[i][j]
                       
                        slot_tujuan = input('slot tujuan : ').upper()

                        for k,data3 in enumerate(list_parkir_angka):

                            for l,data4 in enumerate(data3):

                                if data4 == slot_tujuan:

                                    if list_parkir_huruf[k][l] == 'O':
                                        
                                        list_parkir_huruf[k][l] = parkir
                                        list_parkir_huruf[i][j] = 'O'
                                        print('slot berhasil dipindahkan')
                                        ketemu_pindah = True
                                        
                                        for m,data5 in enumerate(list_tempat_parkir_mobil):

                                            if data5[0] == slot_asal:
                                                data5[0] = slot_tujuan 
                                                ketemu_pindah = True
                                                break

                                    else:
                                        print('slot tujuan sudah terisi')
                                        ketemu_pindah = True
                                        break
                    else:
                        print('slot asal kosong')
                        ketemu_pindah = True
                        break
        if ketemu_pindah == False:
            print('data parkir tidak ditemukan ')            

    elif pilih_menu == 6:

        total_slot = jumlah_baris * jumlah_kolom

        slot_terisi = 0
        slot_kosong = 0
        list_total_kendaraan = []

        for ulang in list_parkir_huruf:

            list_total_kendaraan_ulang = 0
            for ulang1 in ulang:

                if ulang1 == 'O':
                    slot_kosong +=1

                else:
                    slot_terisi +=1
                    list_total_kendaraan_ulang +=1

            list_total_kendaraan.append(list_total_kendaraan_ulang)

        persentase = (slot_terisi /total_slot)  * 100   

        print(f'total slot : {total_slot}')
        print(f'slot kosong : {slot_kosong}')
        print(f'slot terisi : {slot_terisi}')
        print(f'persentase terisi: {persentase:.1f} %')

        for v,kendaraan in enumerate(list_total_kendaraan):
            print(f'{chr(65 + v)} : {kendaraan} kendaraan')

        terbesar = max(list_total_kendaraan)
        index_terbesar = list_total_kendaraan.index(terbesar)

        print(f'lantai paling ramai : {chr(65 + index_terbesar)}')
        print(f'jumlah kendaraan : {terbesar}')  

        terkecil = min(list_total_kendaraan)
        index_terkecil = list_total_kendaraan.index(terkecil)

        print(f'lantai paling sepi : {chr(65 + index_terkecil)}')
        print(f'jumlah kendaraan : {terkecil}')


    elif pilih_menu == 7:
        masukkan_plat = input('masukkan plat : ')
        ketemu_plat = False

        for plat in list_tempat_parkir_mobil:

            if plat[1] == masukkan_plat:

                print(f'plat : {plat[1]}')
                print(f'slot : {plat[0]}')

                print(f'lantai : {plat[0][0]}')
                print(f'nomor : {plat[0][1]}')     
                ketemu_plat = True
                break

        if ketemu_plat == False:
            print('plat tidak ditemukan')

    elif pilih_menu == 8:
        print('program berakhir')
        exit()             
        
                    


                                       
                            
                            

    