list_kursi = []

print('='*20)
print('SISTEM BIOSKOP')
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

for ulang in range(jumlah_baris):
    data_baris = []
    for ulang1 in range(jumlah_kolom):
        data_baris.append('O')

    list_kursi.append(data_baris)

while True:
    print('\n====================')
    print(f'''
    1.Lihat Kursi
    2.Pesan Kursi
    3.Batalkan Kursi
    4.Statistik Kursi
    5. Keluar
    ''')    

    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():

            pilih_menu = int(input_pilih_menu)

            if pilih_menu >0 and pilih_menu <=5:
                break
            else:
                print('tidak boleh 0 atau kurang dan lebih dari 5')

        else:
            print('tidak boleh huruf')      

    if pilih_menu ==1:

        print('\n jumlah kursi yang tersedia')
        for data in list_kursi:
            for data1 in data:
                print(data1, end=' ')
            print()          

    elif pilih_menu ==2 :
        print('pesan kursi')

        while True:
            input_baris_menu = input('masukkan baris : ')

            if input_baris_menu.isdigit():
                baris_menu = int(input_baris_menu)

                if baris_menu >=0 and baris_menu <jumlah_baris:
                    break
                else:
                    print('baris tidak tersedia')
            else:
                print('tidak boleh huruf')    

        while True:
            input_kolom_menu = input('masukkan kolom : ')

            if input_kolom_menu.isdigit():

                kolom_menu = int(input_kolom_menu)

                if kolom_menu >=0 and kolom_menu < jumlah_kolom:
                    break
                else:
                    print('kolom tidak tersedia')
            else:
                print('tidak boleh huruf')


        if list_kursi[baris_menu][kolom_menu] == 'O' :

            list_kursi[baris_menu][kolom_menu] = 'X'
            print('kursi berhasil diubah')
             

        else:
            print('kursi sudah diisi')    

        for data in list_kursi:

            for data1 in data:
                print(data1, end=' ')
            print()  

    elif pilih_menu == 3:

        print('batalkan pesanan')

        while True:

            input_baris_hapus = input('masukkan baris yang ingin dihapus : ')

            if input_baris_hapus.isdigit():

                baris_hapus = int(input_baris_hapus)

                if baris_hapus >=0 and baris_hapus < jumlah_baris:
                    break
                else:
                    print('kolom tidak tersedia')
            else:
                print('tidak boleh huruf')        

        while True:

            input_kolom_hapus = input('masukkan kolom yang ingin dihapus : ')

            if input_kolom_hapus.isdigit():
                kolom_hapus = int(input_kolom_hapus)

                if kolom_hapus >=0 and kolom_hapus <jumlah_kolom:
                    break
                else:
                    print('kolom tidak tersedia')

            else:
                print('tidak boleh huruf')

        if list_kursi[baris_hapus][kolom_hapus] == 'X':

            list_kursi[baris_hapus][kolom_hapus] = 'O'

            print('kursi berhasil dibatalkan/dihapus')  

        else:
            print('kursi sudah kosong')  

        for data in list_kursi:

            for data1 in data:
                print(data1, end=' ')
            print()     


    elif pilih_menu == 4:

        total_kursi = jumlah_baris * jumlah_kolom

        kursi_terisi = 0
        kursi_kosong = 0

        for data in list_kursi:

            for data1 in data:

                if data1 == 'X':
                    kursi_terisi +=1

                else:
                    kursi_kosong +=1

        print('----statistik kursi -----')

        print(f'total kursi = {total_kursi}')
        print(f'kursi_terisi = {kursi_terisi}')
        print(f'kursi kosong = {kursi_kosong}')

    elif pilih_menu == 5:
        print('program selesai') 
        exit()   

            
