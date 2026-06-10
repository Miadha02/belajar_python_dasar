while True:
    i_jumlah_game = input('masukkan jumlah game : ')

    if i_jumlah_game.isdigit():
        jumlah_game = int(i_jumlah_game)

        if jumlah_game >0:
            break
        else:
            print('tidak boleh sama 0')

    else:
        print('salah memasukkan input') 

list_game = []
for ulang in range(1,jumlah_game+1):
    print(f'game ke {ulang}')

    while True:
        input_nama_game = input('masukkan nama game : ')

        if input_nama_game.replace(" ",''):
      
            break
        else:
            print('salah memasukkan nama game')

    while True:
        input_genre = input('masukkan genre : ')

        if input_genre.replace(' ','').isalpha():
            break
        else:
            print('salah memasukkan genre')

    game_baru = [input_nama_game,input_genre]
    list_game.append(game_baru)
print('data game')

print('NO    NAMA_GAME      GENRE')

for index,game in enumerate(list_game):
    print(f'{index+1}   {game[0]}  ,{game[1]}')