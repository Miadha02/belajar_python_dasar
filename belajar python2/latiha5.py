while True:
    nama = input('masukkan nama anda : ')

    if nama.replace(" ","").isalpha():
       
        
        berat =0
        while True:
            berat_badan_anda = input('masukkan berat badan anda (kilogram) : ')
            
            if berat_badan_anda.replace(".",(''),1).isdigit():
                berat_badan = float(berat_badan_anda)

                if berat_badan <= 0:
                    print('berat badan tidak boleh kurang dari 0')
                
                elif berat_badan > 0:
                    berat = berat_badan
                    break
                    
            else:
                print('masukkan berat yang benar')

        tinggi = 0
        while True:
            tinggi_badan_anda = input('masukkan tinggi badan anda (m) : ')

            if tinggi_badan_anda.replace(".","",1).isdigit():

                tinggi_badan = float(tinggi_badan_anda)

                if tinggi_badan <= 0:
                    print('tinggi badan tidak boleh kurang dari sama dengan 0 ')

                elif tinggi_badan > 0:
                    tinggi = tinggi_badan
                    break

            else:
                print('masukkan tinggi badan yanng benar !')    



        bmi = berat / (tinggi*tinggi)

        if bmi < 18.5:
            kategori = 'kurus'
            keterangan = 'disarankan menambah asupan gizi'

        elif bmi < 25:
            kategori = 'normal'
            keterangan = 'kondisi tubuhmu ideal'

        elif bmi < 30:
            kategori = 'gemuk'
            keterangan = 'disarankan untuk berolahraga'

        elif bmi >= 30:
            kategori = 'obesitas'
            keterangan = 'disarankan untuk konsultasike dokter'

        print(10*'-','HASIL ANALISIS BMI',10*"-")
        print(f'NAMA : {nama}')        
        print(f'BMI ANDA : {bmi:.2f}')
        print(f'kategori : {kategori}')
        print('\n\nKeterangan : ')
        print(keterangan)

        while True:

            lanjut = input('apakah ingin lanjut (ya/tidak) : ').lower()
            lanjutan = False
            if lanjut.isalpha():
                
                if lanjut == 'ya':
                    print('melanjutkan program')
                    lanjutan = True
                    break

                elif lanjut == 'tidak':
                    print('mengakhiri program')
                    break    

                else:
                    print('salah memasukkan inputan')

            else :
                print('salah memasukkan inputan')       

        if lanjutan:
            print()
            continue

        else :
            break         
                 

    else:
        print('masukkan nama yang benar')    
        