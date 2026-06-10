while True:
    input_jumlah_siswa = input('masukkan jumlah siswa : ')

    if input_jumlah_siswa.isdigit():
        jumlah_siswa = int(input_jumlah_siswa)

        if jumlah_siswa > 0:
            break
        else:
            print('tidak boleh 0 atau kurang')

    else:
        print('tidak bolrh huruf')

list_data = []
list_nilai = []
for ulang1 in range(1,jumlah_siswa+1):

    
    print(f'siswa ke {ulang1}')

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(' ','').isalpha():
           break

        else:
            print('tidak boleh angka')

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

    list =[nama,nilai]                        
    list_data.append(list)
    list_nilai.append(list[1])



print('---DATA SISWA ---')
total =0
for index,data in enumerate(list_data):
    print(f'{index+1}. {data[0]} = {data[1]}')

    total += data[1]

terbesar = max(list_nilai)
terkecil = min(list_nilai)
print(f'total = {total}')
print(f'terbesar {terbesar}')
print(f'terkecil : {terkecil}')