list_barang = []

while True:

    print('='*20)
    print('   CRUD DATA TOKO     ')
    print('='*20)

    print(f'''
    1. Tambah Barang
    2. Lihat Barang
    3. Update Barang
    4. Hapus Barang
    5. Cari Barang
    6. Total Semua Stok
    7. Keluar
                       
    ''')

    while True:
        input_pilih_menu = input('pilih menu : ')

        if input_pilih_menu.isdigit():
            pilih_menu = int(input_pilih_menu)

            if pilih_menu >0 and pilih_menu <=7:
                break

            else:
                print('tidak boleh 0 atau kurang , dan tidak boleh kurang sama dengan 7')

        else:
            print('tidak boleh huruf') 

    if pilih_menu == 1:
        list_item = []
        input_nama_barang = input('masukkan nama barang : ').lower()

        while True:
            input_harga_barang = input('masukkan harga barang : Rp.')

            if input_harga_barang.replace('.','').replace(',','').isdigit():

                harga_barang = int(input_harga_barang)

                if harga_barang >=100:
                    break
                else:
                    print('harga tidak boleh < 100')
            else:print('tidak boleh huruf')

        while True:
            input_stok_barang = input('masukkan stok barang : ')

            if input_stok_barang.isdigit():
                stok_barang = int(input_stok_barang)

                if stok_barang >0:
                    break
                else:
                    print('stok barang tidak boleh 0 atau kurang')
            else:
                print('tidak boleh huruf')

        list_item =[input_nama_barang,harga_barang,stok_barang]

        list_barang.append(list_item)

        print('data berhasil ditambahkan ')


    elif pilih_menu == 2:

        if len(list_barang) > 0:
            for index,barang in enumerate(list_barang):
                print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}')

        else:
            print('harus isi dulu nomor 1')
    
    elif pilih_menu == 3:    

        if len(list_barang) >0:
            for index,barang in enumerate(list_barang):
                print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}')


            while True:

                input_nomor_barang = input('pilih no barang : ') 

                if input_nomor_barang.isdigit():

                    nomor_barang = int(input_nomor_barang) 
                    index = nomor_barang - 1
                    break

                else:
                    print('tidak boleh huruf')

            if index < len(list_barang):

                
                input_nama_baru = input('masukkan nama baru : ').lower()

                while True:
                    input_harga_baru = input('masukkan harga baru : ')

                    if input_harga_baru.replace('.','').replace(',','').isdigit():

                        harga_baru = int(input_harga_baru)

                        if harga_baru >100:
                            break
                        else:
                            print('tidak boleh kurang dari 100')

                    else:
                        print('tidak boleh huruf')


                while True:
                    input_stok_baru = input('masukkan jumlah stok baru : ')

                    if input_stok_baru.isdigit():

                        stok_baru = int(input_stok_baru)

                        if stok_baru >0:
                            break
                        else:
                            print('stok tidak boleh 0 atau kurang')


                list_barang[index][0] = input_nama_baru
                list_barang[index][1] = harga_baru
                list_barang[index][2] = stok_baru

                print('data berhasil diubah ')      

                for index,barang in enumerate(list_barang):
                    print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}')            

        else:
            print('harus pilih nomor 1 dulu ')        

    elif pilih_menu == 4:

        if len(list_barang) >0:
            for index,barang in enumerate(list_barang):
                print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}') 


            while True:
                input_hapus = input('pilih nomor yang mau di hapus : ')

                if input_hapus.isdigit():
                    hapus = int(input_hapus)
                    index = hapus -1
                    break
                
                else:
                    print('tidak boleh huruf')

            if index < len(list_barang):

                list_barang.pop(index)

                print('data berhasil diubah ')
                for index,barang in enumerate(list_barang):
                    print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}') 

                if len(list_barang) <1:
                    print('list barang mu kosong , segera diisi')      
            
            else:
                print('nomor kamu melebihi list')

        else:
            print('harus pilih nomor 1 dahulu')      

    elif pilih_menu == 5:

        if len(list_barang)>0:
            for index,barang in enumerate(list_barang):
                print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}') 


            
            input_cari = input('masukkan nama yang mau dicari : ')
            ketemu = False

            for i,data in enumerate(list_barang):

                if input_cari in data[0]:

                    print('ditemukan')
                    print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}') 
                    ketemu = True

            if ketemu == False:
                print('data tidak ditemukan ')        
                   
        else:
            print('harus pilih nomor 1 dahulu')

    elif pilih_menu == 6:
        if len(list_barang)>0:
            total_stok = 0
            for index,barang in enumerate(list_barang):
                print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}') 
                total_stok += barang[2]

           
            print(f'total stok : {total_stok}')    

        else:
            print('harus pilih nomor 1 dahulu')    

    elif pilih_menu ==7:
        print('program berhenti')
        exit()        

        


            




                                    
                    




         
                    





                            


