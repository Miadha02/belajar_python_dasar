jenis_kendaraan = input('masukkan jenis kendaraan (mobil, 5000) / (motor),2000) : ').lower()

if jenis_kendaraan.isalpha():

    if jenis_kendaraan == 'mobil':
        harga = 5000

    elif jenis_kendaraan == 'motor':
        harga = 2000

    if harga > 0:
        berapa_jam = input('masukkan berapa jam parkir : ')
        if berapa_jam.isdigit():
            jam = int(berapa_jam)
            harga_berapa_jam = harga * jam
            print(f'harga parkir selama {jam} jam = {harga_berapa_jam:,}')

            if jam > 5:
                harga_berapa_jam = harga_berapa_jam - (harga_berapa_jam * 0.15)
                print(f'kamu dapat diskon 15% karena sudah lebih dari 5 jam  = {harga_berapa_jam}')


            plat_nomor = input('masukkan plat nomor : ')
            if plat_nomor.replace(" ","").isalnum():
                if '8' in plat_nomor:
                    harga_berapa_jam = harga_berapa_jam - 2000
                    print(f'kamu dapat diskon Rp.2000 karena adaa nomor 8 : {harga_berapa_jam}')

                elif '8' not in plat_nomor:
                    print(f'kamu tidak dapat diskon plat , karena tidak ada angka 8 di platmu')


            else:
                print('kamu salah masukkan plat !')        

            member = input('apakah ada member (ya / tidak) : ').lower()

            if member.isalpha():
                if member == 'ya':
                    harga_berapa_jam -= 5000
                    print(f"kamu punya member , dapat diskon 5000 {harga_berapa_jam}")

                elif member == 'tidak':
                    print('tidak memiliki member')
                
                else:
                    print('kamu salah memasuki input ')    

            print(f"jumlah biaya parkir selama {berapa_jam} = Rp. {harga_berapa_jam:,}")
            if jam > 24 :
                print('mobil kamu akan diderek karena melebihi 24 jam')

print('end of program ')


