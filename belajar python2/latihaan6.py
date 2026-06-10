'''
++++++0-------10+++++++20---------30++++40-------50+++++++

1. angka tidak boleh angka -13
2. Tidak boleh kelipatan 5
3. jika angka 555 dan 888 langsung true
'''

InputUser = int(input('masukkan angka : '))
hasil = ((((InputUser < 0) or (10 < InputUser <20) or (30 < InputUser <40) or InputUser >50) and (InputUser %5!=0)) or (InputUser == 555 or InputUser == 888)) and InputUser != -13
print(hasil)
