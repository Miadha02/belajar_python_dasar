harga = 0

while True:

    while True:

        input_jumlah_pembeli = input('masukkan jumlah pembeli : ')

        if input_jumlah_pembeli.isdigit():
            
            jumlah_pembeli = int(input_jumlah_pembeli)

            if jumlah_pembeli > 0:
                break

            elif jumlah_pembeli <= 0:
                print('tidak boleh kurang atau sama 0')

        else:
            print('tidak boleh pakai huruf')


    for hitung in range(1,jumlah_pembeli+1):

        print(f'pembeli ke {hitung}')

        while True:
            input_nama = input('masukkan nama : ')

            if input_nama.replace(" ","").isalpha():
                break

            else:
                print('salah memasukkan nama')

        while True:
            input_jumlah_menu = input('masukkan jumlah menu : ')

            if input_jumlah_menu.isdigit():
                jumlah_menu = int(input_jumlah_menu)

                if jumlah_menu > 0:
                    break

                elif jumlah_menu <= 0:
                    print('tidak boleh kurang dari atau sama 0')

                else:
                    print('salah memasukkan input')        
            
            else:
                print('tidak boleh pakai huruf')

        total =0
        for jumlah in range(1,jumlah_menu+1):

            print(f'menu ke {jumlah}')
            while True:
                input_jenis = input('masukkan jenis (makanan/minuman) : ').lower()

                if input_jenis.isalpha():

                    if input_jenis == 'makanan':
                        jenis = 'makanan'
                        harga_jenis = 15000
                        break

                    elif input_jenis == 'minuman':
                        jenis = 'minuman'
                        harga_jenis = 5000
                        break 

                    else:
                        print('salah memasukkan kategori makanan')       
                else:
                    print('tidak boleh pakai huruf')        

            while True:
                input_jumlah_jenis = input('masukkan jumlah : ')

                if input_jumlah_jenis.isdigit():

                    jumlah_jenis = int(input_jumlah_jenis)

                    if jumlah_jenis >0 :
                        break

                    elif jumlah_jenis <=0:
                        print('tidak boleh kurang atau sama 0')

                    else:
                        print('salah memasukkan inputan')    

                else:
                    print('tidak boleh pakai huruf')    

            total += harga_jenis * jumlah_jenis 

        if total >= 50000:
            total -= 5000
            diskon = 'diskon lebih dari 50000'
                

        elif total <50000:
            diskon = 'tidak dapat diskon kurang dari 50000'

        harga += total
    
        print(f"nama {input_nama} : Rp.{total}")
    print('---HASIL----')

    print(f'total semua : Rp.{harga}')
    break

            
