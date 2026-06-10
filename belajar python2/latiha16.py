
while True:
    input_jumlah_karyawan = input('masukkan jumlah karyawan : ')

    if input_jumlah_karyawan.isdigit():

        jumlah_karyawan = int(input_jumlah_karyawan)

        if jumlah_karyawan > 0:
            break
        else:
            print('tidak boleh kurang atau sama 0')

    else:
        print('tidak boleh pakai huruf')

for ulang in range(1,jumlah_karyawan+1):

    print(f'karyawan ke {ulang}')

    while True:
        nama = input('masukkan nama : ')

        if nama.replace(" ","").isalpha():
            break
        else:
            print('tidak boleh pakai huruf')

    while True:
        input_jam_kerja = input('masukkan jam kerja : ')

        if input_jam_kerja.isdigit():
            jam_kerja = int(input_jam_kerja)

            if jam_kerja >=0:
                break

            else:
                print('tidak boleh pakai huruf')        

    while True:
        input_jenis = input('masukkan jenis (tetap / kontrak) : ').lower()

        if input_jenis.isalpha():
            if input_jenis =='tetap':
                gaji = 200
                break

            elif input_jenis == 'kontrak':
                gaji = 100
                break

            else:
                print('salah memilih')

        else:
            print('tidak boleh pakai angka')               

    if jam_kerja <= 40:
        total_gaji = gaji * jam_kerja

    elif jam_kerja > 40:
       gaji_normal = gaji * jam_kerja
       normal = jam_kerja - 40
       total_gaji = gaji_normal + normal

       

    if total_gaji >=1000:
        total_gaji -= 100 

    print(f'nama {nama} : -> {total_gaji}')             