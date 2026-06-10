while True:
    i_jumlah_baris = input('masukkan jumlah baris : ')

    if i_jumlah_baris.isdigit():
        jumlah_baris = int(i_jumlah_baris)

        if jumlah_baris > 0:
            break
        else:
            print('tidak boleh 0 atau kurang')

    else:
        print('tidak boleh pakai huruf')        

while True:
    i_jumlah_kolom = input('masukkan jumlah kolom : ')

    if i_jumlah_kolom.isdigit():
        jumlah_kolom = int(i_jumlah_kolom)

        if jumlah_kolom >0:
            break
        else:
            print('tidak boleh 0 atau kurang')

    else:
        print('tidak boleh pakai hururf') 


list_angka = []
for ulang1 in range(jumlah_baris):
    print(f'baris ke {ulang1}')

    baris = []
    for ulang2 in range(jumlah_kolom):
        while True:
            input_angka = input(f'masukkan angka [{ulang1}] [{ulang2}] : ')

            if input_angka.replace("-",'').isdigit():
                angka = int(input_angka)
                break
            else:
                print('tidak boleh huruf')  

        baris.append(angka)

    list_angka.append(baris)

print(f'hasil matrix')

total_semua = 0
total_genap = []
total_ganjil =[]
total_hasil_genap = 0
total_hasil_ganjil = 0
for data in list_angka:
    print(data)

    for angka in data:
        total_semua += angka
        if angka%2==0:
            total_genap.append(angka)

        else:
            total_ganjil.append(angka)

print(f'total semua : {total_semua}')
print(f'angka genap : {total_genap}')
for genap in total_genap :
    total_hasil_genap += genap
print(f'total hasil genap : {total_hasil_genap}')


print(f'total_ganjil : {total_ganjil}')
for ganjil in total_ganjil:
    total_hasil_ganjil += ganjil

print(f'total hasil ganjil : {total_hasil_ganjil}')    



