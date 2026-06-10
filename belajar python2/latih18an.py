list_game = []
while True:
    keluar = True
    print('='*20)
    txt = 'CRUD DATA GAME'
    x = txt.center(20)
    print(x)
    print('='*20)
    
    print(f'''
    1.Nambah Game 
    2.Lihat Game
    3.Updte Game
    4.Hapus Game
    5.Keluar
    ''')

    
    while True:
        pilih_menu = input('pilih menu : ')

        if pilih_menu.isdigit():
            pilih = int(pilih_menu)

            if pilih >0 and pilih <=5:

                if pilih == 1:
                    while True:
                        tambah_nama_game = input('masukkan nama game : ').lower()

                        if len(tambah_nama_game) >2:
                            break
                        else:
                            print('tidak boleh 1 huruf')

                    while True:
                        tambah_genre_game = input('masukkan genre game : ').lower()

                        if len(tambah_genre_game) >2:
                            break
                        else:
                            print('tidak boleh 0-2 huruf atau angka')

                    list_tambah_game = [tambah_nama_game,tambah_genre_game]      

                    list_game.append(list_tambah_game)

                    print('data berhasil ditambahkan \n')


                elif pilih == 2:

                    if len(list_game) >0:
                        
                        for i,data in enumerate(list_game):
                            print(f'{i+1}. {data[0]} {data[1]}')

                        print('\n')    

                    else:
                        print('tidak ada game , mohon diisi terlebih dahulu')    

                elif pilih == 3:
                    if len(list_game) >0:
                        
                        for i,data in enumerate(list_game):
                            print(f'{i+1}. {data[0]} - {data[1]} ')

                        
                        input_update_game = int(input('silahkan pilih yang mana mau di update : '))

                        index = input_update_game -1

                        if index < len(list_game):

                            while True:
                                input_game_baru = input('masukkan nama game baru : ')

                                if len(input_game_baru) >2:
                                    break
                                else:
                                    print('tidak boleh terdiri dari 1 huruf / angka')

                            while True:
                                input_genre_baru = input('masukkan genre game baru : ')

                                if len(input_genre_baru) >2:
                                    break
                                else:
                                    print('judul game tidak boleh terdiri dari 1 angka/huruf')

                            list_game[index][0] = input_game_baru
                            list_game[index][1] = input_genre_baru 

                            print('data berhasil diubah')
                            print(f'{i+1}. {list_game[index][0]} - {list_game[index][1]}\n')

                            print('list game sekarang')
                            for i,updategame in enumerate(list_game):
                                print(f'{i+1}. {updategame[0]} - {updategame[1]}')
                                                

                        else:
                            print('kamu salah input')
                                
                    else:
                        print('tidak ada game, mohon diisi terlebih dahulu')          

                elif pilih == 4:

                    if len(list_game) >0:
                        
                        for i,datahapus in enumerate(list_game):
                            print(f'{i+1}. {datahapus[0]} - {datahapus[1]}')

                        while True:

                            input_hapus = int(input('pilih yang mana mau dihapus : '))

                            index = input_hapus -1
      

                            if index <len(list_game):

                                list_game.pop(index)
                                print('data berhasil dihapus')
                                break

                            else:
                                print('nomor tidak ada')    


                              

                    else:
                        print('tidak ada game, mohon diisi terlebih dahulu ')                          


                elif pilih == 5:
                    keluar = True
                    break      

            else:
                print('tidak boleh kurang sama dengan 0 atau lebih dari 5')

    if keluar == True:
        break
