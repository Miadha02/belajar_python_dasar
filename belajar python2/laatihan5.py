'''
#------0++++10----20++++30-----

angka harus genap
tidak boleh angka 24
jika angka 777 langsung true
'''
InputUser = float(input("masukkan angka : "))

hasil = (((0 < InputUser <10 or (20 < InputUser <30)) and (InputUser %2==0)) and (InputUser !=24)) or (InputUser == 777)
print(hasil) 