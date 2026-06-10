'''
++++++0------10++++++20-----30++++

angka tidak boleh -5 dan 15
angka tidak boleh kelipatan 100

jika angka 1000 maka langsung true
'''

InputUser = float(input("masukkan angka : "))

hasil = ((InputUser < 0 or (10 <InputUser < 20) or InputUser > 30 ) and (InputUser != -5 and InputUser !=15 and InputUser % 100 != 0)) or InputUser == 1000
print(hasil)
