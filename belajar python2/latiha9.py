hari = 1
harga = 0
while True:

    print(f'hari ke {hari}')   

    while True:
        input_jumlah_kendaraan = input('masukkan jumlah kendaraan : ')

        if input_jumlah_kendaraan.isdigit():
            jumlah_kendaraan = int(input_jumlah_kendaraan)

            if (jumlah_kendaraan <= 0  or jumlah_kendaraan >10):
                print('kendaraan tidak boleh kurang atau sama dengan 0')

            elif jumlah_kendaraan > 0:
                break

            else:
                print('salah memasukkan jumlah')

        else:
            print('tidak boleh pakai huruf')

    for ulang in range(1,jumlah_kendaraan+1):
        while True:
            print(f'kendaraan ke {ulang}')

            input_jenis = input('masukkan jenis kendaraan (motor /mobil) : ').lower()

            if input_jenis.isalpha():

                if input_jenis =='mobil':
                    jenis = 'mobil'
                    harga_parkir = 5000
                    break
                    
                elif input_jenis == 'motor':    
                    jenis = 'motor'
                    harga_parkir = 2000
                    break

                else:
                    print('pilih antara (mobil / motor)')
            else:
                print('tidak boleh pakai angka')    

        while True:
            input_lama_parkir = input('masukkan lama parkir (jam): ')

            if input_lama_parkir.isdigit():
                lama_parkir = int(input_lama_parkir)

                if lama_parkir <= 0:
                    print('tidak boleh kurang atau sama 0')
                

                elif lama_parkir > 0 :
                    lama = lama_parkir
                    break    

                else:
                    print('sakah memasukkan input')
            else:
                print('tidak boleh pakai huruf')    

       
        #kita satukan dulu 
        total_kendaraan = harga_parkir * lama
    
        while True:        
            
            input_member = input('apakah ada member (ya/tidak) : ').lower()

            if input_member.isalpha():
                if input_member == 'ya':
                    total_kendaraan = total_kendaraan -(total_kendaraan * 0.20)
                    diskon = '20%'
                    break

                elif input_member == 'tidak':
                    diskon = '0%'
                    break    
                
                else:
                    print('salah memasukkan input')

            else:
                print('tidak boleh pakai angka')   



        harga += total_kendaraan    #baru kita +++ kan

    print(f'---HASIL HARI ke {hari} ----')
    for hasil in range(1,ulang+1):
        print(f'kendaraan ke{hasil} -> {jenis} -> {harga_parkir} * {lama} * {diskon}')

    print(f'totalnya : {harga}')    
    
    while True:
        isLanjut = input('apakah ingin lanjut ? (ya /tidak) : ').lower()

        if isLanjut.isalpha():
            if isLanjut == 'ya':
                break

            elif isLanjut == 'tidak':
                break
                
            else:
                print('salah pilih ya atau tifsk')
        else:
            print('salah ')

    if isLanjut == 'ya':
        hari +=1
        continue

    else:
        break        
    
        
        

                 
                




