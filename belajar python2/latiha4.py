print('---check kekuatan password---'.upper())

percobaan = 0

while percobaan < 3:

    password = input('masukkan password yang mau di check kekuatannya : ')

    skor=0
    simbol = "!@#$%^&*()_+=|][}{><.,]"
    ada_besar= False
    ada_kecil = False
    ada_angka = False
    ada_simbol = False

    for huruf in password:

        if huruf.islower():
            ada_kecil = True

        if huruf.isupper():
            ada_besar = True

        if huruf.isdigit():
            ada_angka = True

        if huruf in simbol:
            ada_simbol = True

    if len(password) >= 8:   
        skor +=2         

    if ada_kecil:
        skor+=1        

    if ada_besar:
        skor+=1

    if ada_angka:
        skor +=1

    if ada_simbol:
        skor +=2

    if 'password' in password.lower() or 'admin' in password.lower() or '123456' in password:
        skor -=2

    ulang = False
    for i in range(len(password)-2):
        if password[i] == password[i+1] == password[i+2]:
            ulang = True

    if ulang:
        skor -= 1

    if skor <=2:
        kategori = 'lemah'

    elif skor <=5:
        kategori = 'sedang'                    
    
    else:
        kategori = 'kuat'

    print('\n\n ---Hasil analisis---')
    print(f'password : {password}')
    print(f'Skor : {skor}') 
    print(f'kategori : {kategori}')

    print('\n alasan : ')
    if len(password)>= 8:
        print('password sudah dari 8 karakter : skor + 2')
    else:
        print('password kurang dari 8 karakter')

    if ada_besar:
        print('ada huruf besar : skor +1')                 
    else:
        print('tidak ada huruf besar')

    if ada_kecil:
        print('ada huruf kecil : skor +1')              

    else:
        print('tidak ada huruf kecil  ')

    if ada_angka:
        print('ada angka : skor + 1')   

    else:
        print('tidak ada angka') 

    if ada_simbol:
        print('ada simbol : skor + 2')
    else:
        print('tidak ada simbol')

    if 'password' in password.lower() or 'admin' in password.lower() or '123456' in password:
        print('mengandung kata umum')

    else:
        print('tidak ada karakter umum')
    if ulang:
        print('mengandung karakter berulang') 

    else:
        print('tidak ada karakter berulang')    


    if percobaan == 3:
        print('terlalu banyak percobaan ') 
        break  
    if kategori == 'lemah':
      
        percobaan +=1
        print('coba lagi sampai bisa ')
        continue



    if percobaan == 3:
        print('terlalu banyak percobaan ') 
        break      

    while True:
        lanjut = input('apa ingin lanjut (ya/tidak) : ')
        lanjutan = False
        if lanjut.isalpha():
            if lanjut =='ya':
                print('program dilanjutkan')
                lanjutan = True
                break
            
            elif lanjut =='tidak':
                print('program dihentikan')
                break
            
            else:
                print('salah memasukkan input')
        else:
            print('salah memasukkan input')

    if lanjutan:
        continue

    else:
        break                