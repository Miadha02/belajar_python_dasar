import datetime as dt

tahun_lahir = int(input("masukkan tahun lahir : "))
bulan_lahir = int(input("masukkan bulan lahir : "))
tanggal_lahir = int(input('masukkan tanggal lahir : '))

lahir = dt.date(tahun_lahir,bulan_lahir,tanggal_lahir)
print(f"tanggal lahir : {lahir}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}, hari {hari_ini:%A}")

hari_hitung = hari_ini - lahir
print(f"sudah hidup hari : {hari_hitung}")

tahun_hitung = hari_hitung.days // 365
print(f"umur tahun : {tahun_hitung} tahun")

jam_hidup = hari_hitung.days * 24
print(jam_hidup)

berapa_menit = jam_hidup * 60
print(berapa_menit)

berapa_detik = berapa_menit * 60
print(berapa_detik)

