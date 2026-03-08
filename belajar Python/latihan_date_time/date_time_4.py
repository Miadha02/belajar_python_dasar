import datetime as dtime

print("masukkan ")
tanggal = int(input("tanggal : "))
bulan   = int(input("bulan : "))
tahun = int(input("tahun : "))

tanggal_lahir = dtime.datetime(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah {tanggal_lahir}")
print(f"harinya adalah : {tanggal_lahir:%A}")

sekarang = dtime.datetime.now()

selisih = sekarang - tanggal_lahir 

print(f"selisih = {selisih.days}")