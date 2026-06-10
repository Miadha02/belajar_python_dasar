while True:
    input_jumlah_buah = input('masukkan jumlah buah : ')

    if input_jumlah_buah.isdigit():
        jumlah_buah = int(input_jumlah_buah)

        if jumlah_buah >0:
            break

        else:
            print('tidak boleh kurang atau sama 0')

    else:
        print('tidak boleh huruf')
list_buah = []
for i in range(1,jumlah_buah+1):

    print(f'buah ke {i}')

   
    while True:  
        input_buah = input(f'masukkan buah ke {i} : ')
        
        if input_buah.isalpha():
            list_buah.append(input_buah)
            break
        else:
            print('salah')

print('hasil')
for index,buah in enumerate(list_buah):
    print(f'no  ke {index+1}. buah {buah}')
