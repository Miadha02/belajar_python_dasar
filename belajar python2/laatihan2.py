#------0++++5-----8+++++11------

InputUser = float(input('masukkan nilai (lebih dari 0 dan kurang dari 5) atau (lebih dari 8 dan kurang dari 11) : '))

lebihdari0 = (InputUser > 0)
print(lebihdari0)
kurangdari5 = (InputUser < 5)
print(kurangdari5)
gabungan1 = lebihdari0 and kurangdari5
print(gabungan1)

lebihdari8 = (InputUser > 8)
print(lebihdari8)
kurangdari11 = (InputUser < 11)
print(kurangdari11)

gabungan2 = lebihdari8 and kurangdari11
print(gabungan2)

gabungan = gabungan1 or gabungan2
print(gabungan)



