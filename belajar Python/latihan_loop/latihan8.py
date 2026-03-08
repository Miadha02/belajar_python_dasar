target = 100

while True :
    tabungan_input = input("masukkan tabungan atau 'keluar' : ")

    if tabungan_input == "keluar":
        break
    
    tabungan = int(tabungan_input)
    if(tabungan < target):
        
        target -= tabungan
        print(f'kamu memasukkan tabungan {tabungan}')
        print(f"sisa target {target}")


    elif (tabungan >= target):
        print("kamu berhasil")
        hasil = tabungan - target
        print("tabungannya lebih",hasil)
        break

    else :
        print("salah")
        continue