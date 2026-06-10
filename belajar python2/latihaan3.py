#++++0------5++++8----11++++++

InputUser = float(input("masukkan kurangdari 0 atau (lebihdari 5 dan kurang dari 8) atau lebih dari 11"))

kurangdari0 = (InputUser <0)
print(kurangdari0)

lebihdari5 = (InputUser > 5)
print(lebihdari5)
kurangdari8 = (InputUser < 8)
print(kurangdari8)
gabungan1 = lebihdari5 and kurangdari8

lebihdari11 = (InputUser > 11)
print(lebihdari11)

gabungan = kurangdari0 or gabungan1 or lebihdari11
print(gabungan)