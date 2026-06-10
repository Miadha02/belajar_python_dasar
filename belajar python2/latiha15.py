
rata_semua = 0
while True:
    input_jumlah_siswa = input('masukkan jumlah siswa : ')

    if input_jumlah_siswa.isdigit():

        jumlah_siswa = int(input_jumlah_siswa)

        if jumlah_siswa >0:
            break

        else:
            print('tidak boleh kurang dari 0 atau sama')

    else:
        print('tidak boleh pakai huruf')

for ulang in range(1,jumlah_siswa+1):

    print(f'siswa ke {ulang}')

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(" ","").isalpha():
            break

        else:
            print('salah memasukkan nama')
    
    
    while True:
        input_jumlah_nilai = input('masukkan jumlah nilai : ')

        if input_jumlah_nilai.isdigit():
            jumlah_nilai = int(input_jumlah_nilai)

            if jumlah_nilai > 0:
                break

            else:
                print('tidak boleh kurang dari 0')

        else:
            print('tidak boleh pakai huruf')
    
    total_nilai = 0
    for ulang1 in range(1,jumlah_nilai+1):
        while True:
            input_nilai = input(f'masukkan nilai ke {ulang1} : ')

            if input_nilai.isdigit():
                nilai = int(input_nilai)

                if nilai >0:
                    total_nilai += nilai

                    break

                else:
                    print('kurang dari 0 atau sama ') 
 
            else:
                print('tidak boleh pakai huruf')


    rata_rata = total_nilai / jumlah_nilai
    
    if rata_rata >=85:
        grade = 'A'

    elif rata_rata >= 70:
        grade = 'B'

    elif rata_rata >= 60:
        grade = 'C'

    elif rata_rata <60:
        grade = 'D'            
    print(f'nama {nama} -> rata rata :{rata_rata} -> grade : {grade}')

    rata_semua += rata_rata 

rata_semua = rata_semua / jumlah_siswa

print('---HASIL AKHIR ---')
print(f'rata semua {rata_semua}')              



