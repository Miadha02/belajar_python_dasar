#++++0------5++++8----11++++++

InputUser = float(input("masukkan kurangdari 0 atau (lebihdari 5 dan kurang dari 8) atau lebih dari 11 : "))

hasil = (InputUser < 0) or (5 < InputUser < 8) or (InputUser > 11)
print(hasil)