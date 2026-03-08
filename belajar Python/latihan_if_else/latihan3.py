usia_saya = 20

usia_kamu = int(input("masukkan usia anda : "))

if (usia_saya > usia_kamu):
    beda = usia_saya - usia_kamu
    print(f'''saya lebih tua {usia_saya}, daripada kamu {usia_kamu},
dan kita beda : {beda} tahun''')

elif (usia_kamu > usia_saya) :
    beda_kamu = usia_kamu - usia_saya
    print(f'''kamu lebih tua {usia_kamu}, daripada saya {usia_saya}
dan kita beda {beda_kamu} tahun ''')
