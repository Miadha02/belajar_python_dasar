tipe_buku = input('''TIPE BUKU :
1). Novel (Rp.80.000 / buku)
2). Edukasi (Rp.120.000 / buku)
3). Komik (Rp.40.000 / buku)
Masukkan nomor type buku yang mau dibeli : ''').lower()

if tipe_buku.isdigit():
    tipe = int(tipe_buku)
    if (0 < tipe <=3 ): 

        if (tipe == 1):
            harga = 80000
            nama_buku = 'novel'
            print(f'kamu memilih tipe buku novel , harganya {harga:,}')

        elif(tipe == 2):
            harga = 120000    
            nama_buku = 'edukasi'
            print(f'kamu memilih tipe buku edukasi , harganya {harga:,}')
        elif(tipe ==3):
            harga = 40000
            nama_buku = 'komik'
            print(f'kamu memlih tipe buku komik , harganya {harga:,}')

        if harga > 0:
            jumlah_buku = input('masukkan jumlah buku yang mau di beli : ')

            if jumlah_buku.isdigit():
                jumlah_buku_diambil = int(jumlah_buku)
                jumlah_harga = jumlah_buku_diambil * harga
                print(f"kamu membeli buku {nama_buku} sebanyak {jumlah_buku} , totalnya {jumlah_harga:,}")

                if jumlah_buku_diambil > 5:
                    jumlah_harga = jumlah_harga - (jumlah_harga *0.10)
                    print(f"kamu dapat diskon karena membeli lebih dari 5 buku , total {jumlah_harga}")

                check_member = input("apakah ada member (ya/tidak): ").lower()

                if check_member.isalpha():

                    if check_member == 'ya':
                        if jumlah_harga >= 300000:
                            jumlah_harga -= 25000
                            print(f'kamu dapat diskon karena belanjaan lebih dari Rp 300.000 totalnya :{jumlah_harga}')

                        else:
                            print('yah belanjaan mu kurang dari 300 ribu , tidak dapat diskon member !')

                    check_kupon = input('masukkan kode kupon : ').lower()

                    if check_kupon == 'diskon20':
                        jumlah_harga -= 20000
                        print(f'kamu dapat diskon kupon 20000')    

                    else:
                        print(f'yah kamu tidak dapat diskon total :{jumlah_harga}')        

                    print(f'''--Ringkasan pembelian---  
                    Tipe buku = {nama_buku} x {jumlah_buku}
                    Total semuanya (setelah diskon dll) : {max(0,jumlah_harga):,}'''.upper())

                    if jumlah_harga > 1000000:
                        print(' transaksi mu terlalu besar , lakukan dikasir')
                            
            else:
                print('salah memasukkan jumlah buku ! ')        

    else:
        print('kamu salah atau melebihi nomor !')    
