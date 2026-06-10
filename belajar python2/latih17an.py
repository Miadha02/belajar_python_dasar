while True:
    i_jumlah_siswa = input('masukkan jumlah siswa : ')

    if i_jumlah_siswa.isdigit():
        jumlah_siswa = int(i_jumlah_siswa)

        if jumlah_siswa >0:
            break
        else:
            print('tidak boleh 0 atau kurang')
    else:
        print('tidak boleh huruf')


while True:
    i_jumlah_mapel = input('masukka jumlah mapel : ')

    if i_jumlah_mapel.isdigit():
        jumlah_mapel = int(i_jumlah_mapel)

        if jumlah_mapel >0:
            break
        else:print('tidak boleh 0 atau kurang')
    else:
        print('tidak boleh huruf')

list_data = []
for ulang1 in range(jumlah_siswa):
    print(f'siswa ke {ulang1+1}')

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(' ','').isalpha():
            break

        else:
            print('tidak boleh huruf')

    nilai_mapel =[]
    for ulang2 in range(jumlah_mapel):
        while True:
            input_nilai = input(f'masukkan nilai mapel ke {ulang2+1} : ')

            if input_nilai.isdigit():
                nilai = int(input_nilai)

                if nilai >0:
                    break
                else:print('tidak boleh 0 atau kurang') 
            else:print('tidak boleh huruf')
        nilai_mapel.append(nilai)

    list_sementara = [nama,nilai_mapel]    
        

    list_data.append(list_sementara)

print('data siswa')



for data in list_data:
    print(f'{data[0]} : {data[1]}')
    total = sum(data[1])
    print(f'total = {total}')

    if total > 100:
        print('status : lulus')

    else:
        print('status :tidak lulus')    

    print('\n\n')

            
