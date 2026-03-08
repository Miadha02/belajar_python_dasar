#contoh 1
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang {angka}")

    if angka == 3:
        print("nice")
        break     # otomatis berhenti saat angka 3
    print("wassup")

print("cukup finish")

#contoh 2
data_int = int(input("hitung sampai ="))
angka = 0

while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_int : # jika kita menginput data_int 5 , maka keluar 5 kali
        print("nice!")
        break

    print("wassup!")
print("cukup finish ")    