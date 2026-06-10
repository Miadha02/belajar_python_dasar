while True:
    input_jumlah_siswa = input('masukkan jumlah siswa : ')

    if input_jumlah_siswa.isdigit():
        jumlah_siswa = int(input_jumlah_siswa)

        if jumlah_siswa >0:
            break
        else:
            print('tidak boleh 0 atau kurang')

    else:
        print('tidak boleh angka')



list_data = []
hasil_nilai = 0
for ulang in range(1,jumlah_siswa+1):

    print(f'siswa ke {ulang}')

    while True:
        nama = input('masukkan nama anda : ')

        if nama.replace(" ","").isalpha():
            break
        else:
            print('tidak boleh pakai angka')


    while True:
        input_nilai = input('masukkan nilai : ')

        if input_nilai.isdigit():
            nilai = int(input_nilai)

            if nilai > 0:
                break

            else:
                print('tidak boleh 0 atau kurang')

        else:
            print('tidak boleh huruf')


    siswa = [nama,nilai]
    list_data.append(siswa)


print('---Data Siswa----')

print('NO    NAMA     NILAI')

for index,data in enumerate(list_data):
    print(f'{index}     {data[0]}    {data[1]}')

    hasil_nilai += data[1]

print(f'total nilai {hasil_nilai}')

    