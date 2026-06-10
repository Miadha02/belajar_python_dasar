while True:
    input_jumlah_hewan = input('masukkan jumlah hewan : ')

    if input_jumlah_hewan.isdigit():
        jumlah_hewan = int(input_jumlah_hewan)

        if jumlah_hewan >0:
            break
        else:
            print('tidak boleh kurang sama 0')

    else:
        print('tidak boleh pakai huruf')

list_hewan = []
for ulang in range(1,jumlah_hewan+1):

    while True:
        hewan_ke = input(f'masukkan hewan ke {ulang} : ')

        if hewan_ke.isalpha():
            list_hewan.append(hewan_ke)
            break
        else:
            print('tidak boleh pakai angka')


print('----daftar kucing----') 

for index,hewan in enumerate(list_hewan):
    print(f'{index+1}. {hewan}')

total_hewan = len(list_hewan)
print(f'total hewan : {total_hewan}')