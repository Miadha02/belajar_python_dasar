print('Menghitung seberapa kuat password')
while True:

    password = input('masukkan password : ')

    skor=0

    if len(password)>= 8:
        skor +=2
        print('panjang sudah cukup ')

    else:
        print('panjang belum cukup')    


    ada_kecil = False

    for huruf in password:
        if huruf.islower():
            ada_kecil = True
    if ada_kecil:
        skor +=1
        print('ada huruf kecil')
    else:
        print('tidak ada huruf kecil')            

    ada_besar = False
    for huruf in password:
        if huruf.isupper():
            ada_besar = True

    if ada_besar :
        skor +=1
        print('ada huruf besar')

    else:
        print('tidak ada huruf besar')



    ada_angka = False
    for angka in password:
        if angka.isdigit():
            ada_angka = True

    if ada_angka :
        skor+=1
        print('ada angka ')

    else :
        print('tidak ada angka')

    simbol = '!@#$%^&*()_+|}{|/>.<,:;"~'
    ada_simbol = False
    for huruf in password:
        if huruf in simbol:
            ada_simbol = True

    if ada_simbol:
        skor+=1
        print('ada simbol!')        
    else:
        print('tidak ada simbol')

    if 'password' in password.lower() or 'admin' in password.lower() or '123456' in password.lower():
        skor -=2
        print('mengandung kata umum')

    ulang = False
    for i in range(len(password)-2):
        if password[i] == password[i+1] == password[i+2]:
            ulang = True

    if ulang:
        skor -=1
        print('ada karakter berulang')    


    if skor <=2:
        kategori = 'lemah'

    elif skor <=5:
        kategori = 'sedang'

    else:
        kategori = 'kuat'                

    print('hasil analisis password')
    print(f'password : {password}') 
    print(f'skor : {skor}')
    print(f'kategori : {kategori}')   
    
    while True:
        lanjut = input('apa ingin lanjut (ya/tidak)')
        
        if lanjut.isalpha():
            if lanjut == 'ya':
                print('program dilanjutkan')

                break

            elif lanjut == 'tidak':
                print('program di hentikan')
                break    
            else:
                print('salah masukkan input')

        else:
            print('salah masukkan perintah') 

    if lanjut == 'ya':
        continue

    elif lanjut == 'tidak':
        break
