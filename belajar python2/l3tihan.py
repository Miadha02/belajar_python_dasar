#kasir

nama = input('masukkan nama penonton : ').lower()

if nama.replace(" ","").isalpha():
    print(f"selamat datang di bioskop {nama}")

    umur = input('masukkan umur anda : ')

    if umur.isdigit():
        umur_penonton = int(umur)

        tiket = input("masukkan type ticket (reguler(100000) / vip(500000)) : ").lower()

        if tiket=='reguler':
            harga = 100000
            print(f"harga tiket reguler : {harga}")

        elif tiket == 'vip':
            harga = 500000
            print(f"harga tiket vip : {harga}")

        else:
            harga = 0
            print("salah masukkan tipe tiket")

        if harga > 0:
            if (0 < umur_penonton < 12):
                harga -= (harga*0.20)
                print(f"harga diskon anak anak {harga}")

            elif (12 <= umur_penonton <= 18):
                harga -= (harga *0.10)
                print(f"harga diskon pelajar {harga}")

            elif(umur_penonton>60):
                harga -= (harga*0.15)
                print(f"harga diskon lansia {harga}")

            if 'wibu' in nama:
                print(f'kamu dapat diskon {nama} Rp.50.000')
                harga -= 50000

        print(f"Total yang harus di bayar : Rp {harga:,}")   
             
    else:
        print("umur gaboleh pakai huruf")
else:
    print("nama gaboleh pakai angka")