# date and time

import datetime as dtime

hari_ini = dtime.date.today()
print(hari_ini)

print(f"Hari ini adalah hari = {hari_ini:%A}")         

tanggal = dtime.date(2026,3,11)
print(tanggal)
print(f"hari ini adalah hari = {tanggal:%A}")

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
