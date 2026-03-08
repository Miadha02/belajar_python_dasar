import datetime as dtime

print("\nsilahkan masukan tanggal ,bulan dan tahun lahir anda ")
tanggal = int(input("tanggal : "))
bulan = int(input("bulan   : "))
tahun = int(input("tahun   : "))

tanggal_lahir = dtime.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"hari nya adalah {tanggal_lahir:%A}")

hari_ini = dtime.date.today()
print(f"hari ini : {hari_ini}")
umur = hari_ini - tanggal_lahir


umur_tahun = umur.days // 365
print(f"umur anda adalah : {umur}")
print(f"umur anda adalah : {umur_tahun} tahun")

tanggal_berikut_ultah = dtime.date(hari_ini.year , bulan , tanggal)
selisih = tanggal_berikut_ultah - hari_ini 
print(f"tanngal berikut : {selisih}")
