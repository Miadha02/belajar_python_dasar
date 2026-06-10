while True:
    i_jumlah_baris = input('masukkan jumla baris : ')

    if i_jumlah_baris.isdigit():
        jumlah_baris = int(i_jumlah_baris)

        if jumlah_baris >0:
            break
        else:print('tidak 0 atau kurang')
    else:print('tidak boleh huruf')

while True:
    i_jumlah_kolom = input('masukkan jumlah kolom : ')

    if i_jumlah_kolom.isdigit():
        jumlah_kolom = int(i_jumlah_kolom)

        if jumlah_kolom >0:
            break
        else:print('tidak boleh 0 atau kurang')
    else:print('tidak boleh huruf')

list_data = []
for ulang1 in range(jumlah_baris):

    baris_kolom = []
    for ulang2 in range(jumlah_kolom):

        while True:
            input_angka = input(f'masukkan angka [{ulang1}] [{ulang2}] : ')

            if input_angka.replace('-','').isdigit():
                angka = int(input_angka)

                if angka >0: break

                else:print('angka tidak 0 atau kuraang') 
            else:print('tidak boleh huruf')
        baris_kolom.append(angka)

    list_data.append(baris_kolom)

print('hasil matrix')

for data in list_data:
    print(data)

for i,data2 in enumerate(list_data):
    print(f'total baris ke {i} = {sum(data2)}')    

for kolom in range(jumlah_kolom):
    total_kolom = 0
    for baris in range(jumlah_baris):
        total_kolom += list_data[baris][kolom]

    print(f'total kolom ke {kolom} = {total_kolom}')

                    