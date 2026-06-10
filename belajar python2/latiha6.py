while True:

    jumlah_mahasiswa_nya = input('masukkan jumlah mahasiswa : ')

    if jumlah_mahasiswa_nya.isdigit():
        jumlah_mahasiswa = int(jumlah_mahasiswa_nya)

        if jumlah_mahasiswa > 0:
            for jumlah in range(1,jumlah_mahasiswa+1):
                print(f'mahasiswa ke {jumlah}')

                while True:
                    nama = input('masukkan nama anda : ')

                    if nama.replace(" ","").isalpha():
                        break
                        
                    else:
                        print('nama kamu salah')    


                while True:
                    jumlah_nilai_input = input('masukkan jumlah nilai : ')

                    if jumlah_nilai_input.isdigit():
                        jumlah_nilai = int(jumlah_nilai_input)

                        if jumlah_nilai >0:
                            break
                        
                        else:
                            print('harus lebih dari 0')

                    else:
                        print('salah memasukkan jumlah nilai')        

                total_nilai = 0
                for j in range(1,jumlah_nilai + 1):
                    while True:
                        nilai_input = input(f'nilai ke {j} : ')

                        if nilai_input.isdigit():
                            nilai = int(nilai_input)

                            if 0<= nilai <= 100:
                                total_nilai += nilai
                                break
                            else:
                                print('nilai harus 0 - 100') 

                        else:
                            print('input kamu salah')

                rata = total_nilai / jumlah_nilai                               

                print('\n hasil')
                print(f'nama {nama}')
                print(f'rata -rata {rata:.2f}')
            break    
        else:
            print('kurang dari 0')            



    else:
        print('kamu salah masukkan jumlah mahasiswa')    

