tertinggi = 0
while True:
    input_jumlah_mahasiswa = input('masukkan jumlah mahasiswa : ')

    if input_jumlah_mahasiswa.isdigit():
        jumlah_mahasiswa = int(input_jumlah_mahasiswa)

        if jumlah_mahasiswa <=0:
            print('tidak boleh 0 atau kurang')

        elif jumlah_mahasiswa >0:
            break
        
        else:
            print('salah')

    else:
        print('tidak boleh huruf')

total_rata = 0
jumlah_lulus = 0
for ulang in range(1,jumlah_mahasiswa+1):
    print(f'mahasiswa ke {ulang}')

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(" ","").isalpha():
            break

        else:
            print('tidak boleh angka')

    while True:
        input_jumlah_nilai = input('masukkan jumlah nilai : ')

        if input_jumlah_nilai.isdigit():
            jumlah_nilai = int(input_jumlah_nilai)

            if jumlah_nilai <=0:
                print('tidak boleh 0 atau kurang')

            elif jumlah_nilai >0:
                break
            
            else:
                print('salah')
        else:
            print('tidak boleh huruf')

    jumlah_nilai_nya = 0
    for ulang1 in range(1,jumlah_nilai+1):
        while True:
            nilai_ke = input(f'masukkan nilai ke {ulang1} : ')

            if nilai_ke.isdigit():
                nilai = int(nilai_ke)

                if nilai <0:
                    print('tidak boleh kurang dari 0')

                elif nilai >= 0:
                    jumlah_nilai_nya += nilai
                    break    
            else:
                print('salah memasukkan nilai') 

    rata =jumlah_nilai_nya /jumlah_nilai
    if rata > tertinggi:
        tertinggi = rata
        nama_tertinggi = nama
    if rata >= 85:
        grade = 'A'
        jumlah_lulus +=1

    elif rata >= 70:
        grade = 'B'
        jumlah_lulus +=1

    elif rata >= 60:
        grade = 'C'
        jumlah_lulus +=1

    elif rata<60:
        grade = 'D'

    total_rata += rata
    print(f'nama : {nama} -> rata rata : {rata:.2f} -> grade : {grade}')    

total_rata = total_rata / jumlah_mahasiswa

print('---HASIL AKHIR ---')
print(f'TOTAL RATA RATA KELAS : {total_rata}')
print(f'jumlah lulus : {jumlah_lulus}')
print(f'nilai {nama_tertinggi} tertinggi :  {tertinggi}')

                        