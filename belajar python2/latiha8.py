saldo = 0
set = 0
while True:

    print(f'''
    ---ATM------------ 
    1). SET SALDO AWAL
    2). CEK SALDO
    3). SETOR UANG
    4). TARIK UANG
    5). KELUAR                              

    ''')
    
    while True:
        pilih_menu = input('masukkan angka yang mau dipilih : ')

        if pilih_menu.isdigit():
            pilih = int(pilih_menu)

            if pilih < 1 or pilih > 5:
                print('tidak boleh kurang dari sama dengan 0 atau lebih dari 5')

            
            elif pilih ==1:                
                if set >= 1:
                    print('tidak boleh pakai 2 kali')
                while 1 > set:

                    while True:
                        set_saldo_awal = input('masukkan set saldo awal : ')

                        if set_saldo_awal.replace(".","").isdigit():

                            set_saldo = float(set_saldo_awal)

                            if set_saldo <= 0:
                                print('tidak boleh kurang dari sama 0 ')

                            elif set_saldo >0:
                                saldo += set_saldo
                                set +=1
                                print('saldo bertambah')
                                
                                break   

                            else:
                                print('salah')

                        else:
                            print('tidak boleh huruf')   
                    

                            
            elif pilih == 2:
                print(f'saldo anda {saldo}')
                continue   

            elif pilih == 3:

                if set >=1:

                    while True:
                        input_setor_uang = input('masukkan jumlah setor uang : Rp.')

                        if input_setor_uang.replace(".","").isdigit():

                            setor_uang = float(input_setor_uang)

                            if setor_uang <= 0:
                                print('tidak boleh kurang dari atau sama 0')

                            elif setor_uang >0:
                                print(f'berhasil setor uang :{setor_uang}')
                                saldo += setor_uang          
                                break                  
                            
                            else:
                                print('salah memasukkan')

                        else:
                            print('tidak boleh pakai huruf')     

                elif set == 0:
                    print('kamu harus set saldo awal dulu')
                                        
            
            elif pilih == 4:

                if saldo > 0:
                    print(f'saldo anda {saldo}')
                    while True:
                            input_tarik_uang = input('masukkan tarik uang : ')

                            if input_tarik_uang.replace(".","").replace("-","").isdigit():
                                
                                tarik_uang = float(input_tarik_uang)

                                if tarik_uang <= 0:
                                    print('tidak boleh kurang atau sama 0')
                                    break

                                if tarik_uang > saldo:
                                    kurang = saldo - tarik_uang
                                    print(f'saldo anda kurang : {kurang}')
                                    break

                                elif tarik_uang <= saldo:
                                    saldo -= tarik_uang
                                    print(f'tarik uang berhasil Rp.{tarik_uang}, sisa saldo Rp.{saldo}')
                                    break

                                else:
                                    print('salah memasukkan')

                            else:
                                print('tidak boleh pakai agka')        
                else:
                    print('saldo anda 0 , tidak bisa tarik uang')            

            elif pilih == 5:
                print('KELUAR DARI BANK')
                break

        else:
            print('kamu harus memasukkan angka ')


    if pilih ==5:
        break        