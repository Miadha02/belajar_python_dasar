print('='*20)
print('SISTEM BIOSKOP')
print('='*20)
list_kursi = []
list_kursi1 = []
while True:
    input_jumlah_baris = input('masukkan jumlah baris : ')

    if input_jumlah_baris.isdigit():
        jumlah_baris = int(input_jumlah_baris)

        if jumlah_baris >0:
            break
        else:
            print('tidak boleh kurang dari 1')
    else:
        print('tidak boleh huruf')

while True:
    input_jumlah_kolom = input('masukkan jumlah kolom : ')

    if input_jumlah_kolom.isdigit():
        jumlah_kolom = int(input_jumlah_kolom)

        if jumlah_kolom >0:
            break
        else:
            print('tidak boleh kurang dari 1')
    else:
        print('tidak boleh huruf')

for i in range(jumlah_baris):
    baris = []
    baris1 = []

    for j in range(jumlah_kolom):
        kursi = chr(65 +i) + str(j + 1)
        kursi1 = 'O'

        baris1.append(kursi1)
        baris.append(kursi)
    list_kursi.append(baris)
    list_kursi1.append(baris1)

while True:

    print(f'''
1.Lihat Denah Bioskop
2.Pesan Kursi
3.Batalkan Pesanan
4.Cari Kursi
5.Statistik Bioskop
6.Keluar''')
    
    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():

            pilih_menu = int(input_pilih_menu)

            if pilih_menu > 0 and pilih_menu <=6:
                break
            else:
                print('hanya 1 - 6')
        else:
            print('tidak boleh huruf')


    if pilih_menu == 1:
        print('----DENAH BIOSKOP----')

        for data1 in list_kursi:

            for data2 in data1:
                print(data2, end='  ')
            print('')         

        print('\n\n')

        for data3 in list_kursi1:
            for data4 in data3:
                print(data4, end='  ')
            print()

    elif pilih_menu == 2:
        ketemu = False

        input_nomor_kursi = input('masukkan nomor kursi : ').upper()

        for i,data1 in enumerate(list_kursi):

            for j,data2 in enumerate(data1):

                if data2 == input_nomor_kursi:

                    if list_kursi1[i][j] == 'O':
                        list_kursi1[i][j] = 'X'
                        print('pemesanan berhasil')
                        ketemu = True

                    else:
                        print('kursi sudah terisi')  
                        ketemu = True  

        if ketemu == False:
            print('kursi tidak ditemukan : ')


    elif pilih_menu == 3:
        ketemu = False

        input_nomor_kursi = input('masukkan nomor kursi : ').upper()

        for i,data1 in enumerate(list_kursi):

            for j,data2 in enumerate(data1):

                if data2 == input_nomor_kursi:

                    if list_kursi1[i][j] == 'X':
                        list_kursi1[i][j] = 'O'
                        print('pembatalan berhasil')
                        ketemu = True

                    elif list_kursi1[i][j] == 'O':
                        print('kursi sudah kosong')
                        ketemu = True    

        if ketemu == False:
            print('kursi tidak ditemukan : ')

    elif pilih_menu == 4:

        input_nomor_kursi = input('masukkan nomor kursi : ').upper()
        ketemu = False
        for i,data1 in enumerate(list_kursi):

            for j, data2 in enumerate(data1):

                if input_nomor_kursi == data2:
                    ketemu = True

                    print(f'nomor kursi : {list_kursi[i][j]}')
                    print(f'baris : {i+1}')
                    print(f'kolom : {j+1}')

                    if list_kursi1[i][j] == 'O':
                        print(f'Status : kosong')

                    else:
                        print('status : terisi')       

        if ketemu == False:
            print('kursi tidak ditemukan')       

    elif pilih_menu == 5 :

        kursi_terisi = 0
        kursi_kosong = 0
        list_ramai = []

        for i,data1 in enumerate(list_kursi1):
            total_kursi_terisi = 0

            for j,data2 in enumerate(data1):

                if data2 == 'O':
                    kursi_kosong +=1


                else:
                    kursi_terisi +=1
                    total_kursi_terisi += 1

            list_ramai.append(total_kursi_terisi)

        total_kursi = jumlah_kolom * jumlah_baris
        persentase = (kursi_terisi/total_kursi) * 100

        print(f'total kursi : {total_kursi}')
        print(f'kursi terisi : {kursi_terisi}')
        print(f'kursi kosong : {kursi_kosong}')
        print(f'persentase terisi : {persentase:.1f} %')

        for i, jumlah in enumerate(list_ramai):
            print(f'{chr(65+i)} : {jumlah} kursi terisi')

        terbesar = max(list_ramai)
        index_terbesar = list_ramai.index(terbesar)
        print(f'baris paling ramai : {chr(65+index_terbesar)}')
        print(f'jumlah kursi terisi : {terbesar}')

    elif pilih_menu == 6:
        print('program berhenti')
        exit()    



                  






