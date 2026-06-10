while True:
    i_ukuran_matrik = input('masukkan ukuran matrix : ')

    if i_ukuran_matrik.isdigit():
        ukuran_matrik = int(i_ukuran_matrik)

        if ukuran_matrik >0:
            break
        else:print('tidak boleh 0 atau kurang')
    else:
        print('tidak boleh huruf')

list_data = []
range_kolom = 3
for baris in range(ukuran_matrik):
    sementara = []
    for kolom in range(range_kolom):
        while True:
            input_angka = input(f'masukkan angka [{baris}] [{kolom}]: ')

            if input_angka.replace('-','').isdigit():
                angka = int(input_angka)
                break
            else:print('tidak boleh huruf')
    
        sementara.append(angka)
    list_data.append(sementara)

print('hasl matrik')

for data in list_data:
    print(data)

for kolomnya in range(range_kolom):
    total = 0
    for barisnya in range(ukuran_matrik):
        total += list_data[barisnya][kolomnya]
      
    print(f'totalnya {kolomnya}:{total} ')    
