print("="*20)
print('SYSTEM PARKIR')
print('='*20)

list_parkir = []
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

for loop_baris in range(jumlah_baris):

    baris = []

    for loop_kolom in range(jumlah_kolom):
        baris.append('O')

    list_parkir.append(baris)

#ya
for i,data in enumerate(list_parkir):
    print(f'baris ke {i} :', end=" ")
    for data1 in data:
        print(data1, end=' ')
    print(' ')    

while True:
    print('='*20)
    print('DAFTAR PERINTAH')
    print(f'''1.Lihat Parkiran
    2.Parkir Mobil
    3.Keluar Mobil
    4.Statistik Parkiran
    5.Cari Mobil
    6.Keluar Program
    ''')
    print('='*20)
    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():

            pilih_menu = int(input_pilih_menu)

            if pilih_menu >0 and pilih_menu <= 6:
                break
            else:
                print('tidak boleh 0 atau kurang dan tidak boleh lebih dari sama dengan 6')
        else:
            print('tidak boleh huruf')        

    if pilih_menu ==1:
        print('---PARKIRAN---')        
        for i,data in enumerate(list_parkir):
            print(f'baris ke {i} :', end=" ")
            for data1 in data:
                print(data1, end=' ')
            print(' ')   

    elif pilih_menu == 2:
        print(f'parkir mobil')

        while True:
            input_baris_parkir = input('masukkan baris parkir : ')

            if input_baris_parkir.isdigit():
                baris_parkir = int(input_baris_parkir)

                if baris_parkir >=0 and baris_parkir < jumlah_baris:
                    break
                else:print('baris tidak tersedia')
            else:
                print('tidak boleh huruf')

        while True:
            input_kolom_parkir = input('masukkan kolom parkir : ')

            if input_kolom_parkir.isdigit():
                kolom_parkir = int(input_kolom_parkir)

                if kolom_parkir >=0 and kolom_parkir < jumlah_kolom:
                    break
                else:print('kolom tidak tersedia')
            else:
                print('tidak boleh huruf')                        

        if list_parkir[baris_parkir][kolom_parkir] == 'O':
            list_parkir[baris_parkir][kolom_parkir] = 'M'

            print('parkir telah diperbaharui')

            for i,data in enumerate(list_parkir):
                print(f'baris ke {i} :', end=" ")
                for data1 in data:
                    print(data1, end=' ')
                print(' ') 

        else:
            print('parkir sudah diisi')
    elif pilih_menu == 3:
        print('KELUAR MOBIL')

        while True:
            input_baris_keluar = input('masukkan baris keluar : ')

            if input_baris_keluar.isdigit():

                baris_keluar = int(input_baris_keluar)

                if baris_keluar >=0 and baris_keluar < jumlah_baris:
                    break
                else:
                    print('baris tidak tersedia')
            else:
                print('tidak boleh huruf')

        while True:
            input_kolom_keluar = input('masukkan kolom keluar : ')

            if input_kolom_keluar.isdigit():

                kolom_keluar = int(input_kolom_keluar)

                if kolom_keluar >=0 and kolom_keluar < jumlah_kolom:
                    break
                else:
                    print('kolom tidak tersedia') 
            else:
                print('tidak boleh huruf')

        if list_parkir[baris_keluar][kolom_keluar] == 'M':

            list_parkir[baris_keluar][kolom_keluar] = 'O'

            print('parkiran sudah dihapus')    

            for i,data in enumerate(list_parkir):
                print(f'baris ke {i}:', end=" ")

                for data1 in data:
                    print(data1, end=' ')
                print(' ')
        else:
            print('parkir kosong')        

    elif pilih_menu == 4:
        print('STATISTIK PARKIRAN')

        jumlah_parkir = jumlah_baris * jumlah_kolom
        jumlah_terisi = 0
        jumlah_kosong = 0

        for data in list_parkir:

            for data1 in data:
                if data1 == 'O':
                    jumlah_kosong += 1
                else:
                    jumlah_terisi += 1

        print(f'JUMLAH PARKIRAN : {jumlah_parkir}')
        print(f'JUMLAH TERISI : {jumlah_terisi}')
        print(f'JUMLAH KOSONG : {jumlah_kosong}')                        

    elif pilih_menu == 5:
        print('CARI MOBIL')

        ketemu = False
        for i,data in enumerate(list_parkir):
            for j,data1 in enumerate(data):

                if data1 == 'M':
                    print(f'Mobil ditemukan di baris : {i} , kolom : {j}')
                    ketemu = True    

        if ketemu == False:
            print('tidak ada mobil')

    elif pilih_menu == 6:
        print('PROGRAM SELESAI')
        exit()        