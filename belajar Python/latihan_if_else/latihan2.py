#if else usia mengemudi

usia = int(input('masukkan usia anda : '))

if (usia < 18) : 
    butuh_berapa_tahun = 18 - usia
    print(f"usia kamu :{usia} kamu belum bisa")
    print(f"kamu butuh {butuh_berapa_tahun} tahun lagi")

elif (usia > 18) :
    print(f"usia kamu :{usia} , kamu sudah bisa")   
