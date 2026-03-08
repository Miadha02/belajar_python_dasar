import datetime as dtime

print("masukkan umur anda : ")

umur = int(input("umur anda : "))

print(umur)

hari_ini = dtime.date.today()
print(hari_ini)
sudah_hidup_selama = umur * 365

print(f"kamu sudah hidup selama : {sudah_hidup_selama}")
 
jam = sudah_hidup_selama * 24
print(f"jam = , {jam}")

menit = jam * 60
print(f"menit : {menit}")

detik = menit * 60
print(f"detik : {detik}")