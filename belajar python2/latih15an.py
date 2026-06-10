while True:
    input_jumlah_baris = input('masukkan jumlah baris : ')

    if input_jumlah_baris.isdigit():
        jumlah_baris = int(input_jumlah_baris)

        if jumlah_baris >0:
            break
        else:print('tidak boleh 0 atau kurang')
    else:print('tidak boleh huruf')

while True:
    input_jumlah_kolom = input('masukkan jumlah kolom : ')

    if input_jumlah_kolom.isdigit():
        jumlah_kolom = int(input_jumlah_kolom)

        if jumlah_kolom >0:
            break
        else:print('tidak boleh 0 atau kurang')
    else:print('tidak boleh huruf')

list_data = []
for ulang1 in range(jumlah_baris):
    baris = []
    for ulang2 in range(jumlah_kolom):
        while True:
            input_angka = input(f'masukkan angka [{ulang1}] [{ulang2}]: ')

            if input_angka.replace('-','').isdigit():
                angka = int(input_angka)
                break
            else:print('salah memasukkan angka')    

        baris.append(angka) 
    list_data.append(baris)

print('hasil matrix')
for data in list_data:
    print(data)

for kolomnya in range(jumlah_kolom):

    total_ya = 0
    terbesar = list_data[0][kolomnya]
    for barisnya in range(jumlah_baris):
        total_ya += list_data[barisnya][kolomnya]

        if list_data[barisnya][kolomnya] > terbesar:
            terbesar = list_data[barisnya][kolomnya]
            
    print(f'total kolom {kolomnya} : {total_ya}')    

    print(f'terbesar = {terbesar}')
