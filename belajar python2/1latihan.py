import datetime as dt

tanggal = int(input('tanggal : '))
bulan = int(input('bulan : '))
tahun = int(input('tahun : '))

tanggallahir = dt.date(tahun,bulan,tanggal)
print(f'tanggal lahir anda : {tanggallahir}')
tanggal_hariini = dt.date.today()
print(f'hari ini : {tanggal_hariini:%A}')

harilahir = tanggal_hariini - tanggallahir
print(f"hari setelah lahir : {harilahir}")

tahunlahir = harilahir.days // 365
print(f'umur anda : {tahunlahir}')

bulansetelah = (harilahir.days % 365) // 30
print(f'bulan sisa : {bulansetelah}')

setelahtahun = dt.date(tanggal_hariini.year,bulan,tanggal)

setelahnya = setelahtahun - tanggal_hariini
print(setelahnya)