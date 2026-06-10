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

        if jumlah_kolom > 0:
            break
        else:print('salah memasukkan angka')
    else:
        print('tidak boleh huruf')

list_data = []
for ulang1 in range(jumlah_baris):
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

    list_data.append(baris)    

print('hasil matrix')

for data in list_data:
    print(data)

while True:
    input_dicari = input('masukkan angka yang dicari : ')
    if input_dicari.isdigit():
        cari = int(input_dicari)
        break
    else:print('tidak boleh huruf')

ketemu = False
for i,cari1 in enumerate(list_data):

    for j,cari2 in enumerate(cari1):

        if cari2 == cari:
            print(f'angka ditemukan di [{i}] [{j}]')
            ketemu = True
            
            
if ketemu == False:
    print(f'angka {cari} : data not found')    

