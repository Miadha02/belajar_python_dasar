#latihan 2
#++++0-----5+++++8----11++++++++

inputUser = float(input("masukkan angka kurang dari 0 atau (lebih dari 5 dan kurang dari 8) atau lebih dari 11 : "))

#kurang dari 0
kurangdari = (inputUser < 0)
print("kurang dari 0 = ",kurangdari)

#lebih dari 5
lebihdari = (inputUser > 5)
print("lebih dari 5 = ", lebihdari)

#kurang dari 8
kurangdari8 = (inputUser < 8)
print("kurang dari 8 = ",kurangdari8)

#dan
correct1= lebihdari and kurangdari8
print("correct 1 = ",correct1)

lebihdari11 = (inputUser > 11)
print("lebih dari 11 = ",lebihdari11)

correct2 = kurangdari or correct1 or lebihdari11

print("hasil semua = ", correct2)

