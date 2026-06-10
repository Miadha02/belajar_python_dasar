while True:

    input_jumlah_mahasiswa = input('masukkan jumlah mahasiswa : ')

    if input_jumlah_mahasiswa.isdigit():
        jumlah_mahasiswa = int(input_jumlah_mahasiswa)

        if jumlah_mahasiswa >0:
            for jumlah in range(1,jumlah_mahasiswa+1):
                    
                print(f'mahasiswa ke {jumlah} ')

                while True:
                    nama = input('masukkan nama : ')

                    if nama.replace(" ",'').isalpha():
                        break

                    else:
                        print('masukkan nama yang sesuai ')

                while True:
                    input_jumlah_nilai = input('masukkan jumlah nilai : ')

                    if input_jumlah_nilai.isdigit():
                        jumlah_nilai = int(input_jumlah_nilai)

                        if jumlah_nilai > 0:
                            break

                        else:
                            print('tidak boleh kurang dari 0')

                    else:
                        print('salah memasukkan input') 

                total_nilai = 0
                for jlh_nilai in range(1,jumlah_nilai+1):
                    while True:
                        nilai_ke = input(f'nilai ke {jlh_nilai} : ')

                        if nilai_ke.isdigit():
                            nilai = int(nilai_ke)

                            if (0 <= nilai <=100):
                                total_nilai += nilai
                                break

                            else:
                                print('tidak boleh kurang dari 0 atau lebih dari 100')

                        else:
                            print('salah memasukkan nilai')

                rata = total_nilai / jumlah_nilai

                if rata >= 85:
                    kategori = 'A'

                elif rata >= 70:
                    kategori = 'B'

                elif rata >= 60:
                    kategori = 'C'

                elif rata < 60 :
                    kategori = 'D'

                    


                print(10*"-",'HASIL',10*"-")
                print(f'NAMA : {nama}')
                print(f'rata - rata : {rata:.2f}')    
                print(f'GRADE : {kategori}')       
                print('\n\n\n')    

        else:
            print('salah masukkan jumlah mahasiswa')    

        while True:
            lanjut = input('apa ingin lanjut (ya/tidak) : ').lower()

            if lanjut.isalpha():

                if lanjut == 'ya':
                    break

                elif lanjut == 'tidak':
                    break
                else:
                    print('salah masukkan input')

            else:
                print('salah memasukkan input')       

    else:
        print('salah masukkan jumlah mahasiswa')    
        continue

    if lanjut =='ya':                   
        continue

    else:
        print('end of program')
        break   

        