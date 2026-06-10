while True:

    while True:

        nama_peminjam = input('masukkan nama peminjam : ').lower()

        if nama_peminjam.replace(" ",'').isalpha():

            print(f'selamat datang  {nama_peminjam} ') 
            break
        else :
            print('kamu salah memasukkan input')

    while True:
        kategori_peminjam = input('masukkan kategori peminjam (umum/mahasiswa) : ').lower()

        if kategori_peminjam.isalpha():
            
            if kategori_peminjam == 'umum':
                kategori = 'umum'
                diskon = 1000
                break

            elif kategori_peminjam == 'mahasiswa':    
                kategori = 'mahasiswa'
                diskon = 2000
                break

            else:
                print('kamu salah memasukkan inputan yang benar')

        else :
            print('kamu salah input')    

    while True:
        jumlah_buku_dipinjam = input('masukkan jumlah buku yang mau ')        

        if jumlah_buku_dipinjam.isdigit():
            jumlah_buku = int(jumlah_buku_dipinjam)
            

            if jumlah_buku <= 0:
                print('tidak boleh dari 0 atau kurang')

            
            elif jumlah_buku > 0:
                break


        else:
            print('kamu salah memasukkan jumlah buku')    

    harga = 0
    for i in range(1,+jumlah_buku+1):
        while True:
            check_keterlambatan = input(f'apakah buku ke {i} terlambat? (ya/tidak)')

            if check_keterlambatan.isalpha():

                if check_keterlambatan == 'ya':
                    terlambat_berapa_hari = input(f'terlambat berapa hari buku ke {i} : ')
                    if terlambat_berapa_hari.isdigit():
                        terlambat_hari = int(terlambat_berapa_hari)

                        if terlambat_hari <=3:
                            print('kalau terlambat kurang dari sama dengan 3 , gratis')
                            break

                        elif terlambat_hari > 3:
                            harga += terlambat_hari * 5000 -(diskon)
                            break

                        elif terlambat_hari < 0:
                            print(f'kamu gak terlambat lah kalau {terlambat_hari}')
                            break

                    else:
                        print('kamu salah memasukkan input')
                        continue

                elif check_keterlambatan == 'tidak':
                    print(f'buku ke {i} tidak terlambat')
                    break

                else:
                    print('kamu salah memasukkan input')

            else:
                print('kamu salah memasukkan input')        
            

    print(f'kamu meminjam buku sebanyak {jumlah_buku}')
    print(f'total semua bukunya = {harga}')

    while True:
        keluar = input('apakah ingin keluar (ya/tidak) : ').lower()

        if keluar.isalpha():
            if keluar=='ya':
                print('kamu keluar dari progeam')
                break

            elif keluar == 'tidak':
                print('melanjutkan program')
                break

            else:
                print('kamu salah memasukkan program')
                continue

        else:
            print('kamu salah memasukkan program')
            break    

    if keluar=='ya':
        break        

    elif keluar == 'tidak':
        continue



