#latihan 1
# ----0++++++5------8++++11-----

inputUser = float(input("masukkan angka \n\n lebih dari 0 \n dan kurang dari 5 \n \n atau \n\n lebih dari 8 dan \n kurang dari 11 : "))

#lebih dari > 0
lebihdari = (inputUser > 0)
print("lebih dari 0 : ", lebihdari)

#kurang dari < 5
kurangdari = (inputUser < 5)
print ("kurang dari 5 : ", kurangdari)

#dan
correct1 = lebihdari and kurangdari
print("hasil dari lebihdari 0 dan kurang dari 5 : ",correct1)

#lebih dari 8
lebihdari = (inputUser > 8)
print("hasil dari lebih dari = ", lebihdari)

# kurang dari 11
kurangdari = (inputUser < 11)
print("hasil kurang dari 11 : ",kurangdari)

#dan
correct2 = lebihdari and kurangdari
print("hasil lebih dari 8 dan kurang dari 11 : ",correct2)

#or 
correct3 = correct1 or correct2
print("hasil dari lebih dari 0 dan kurang dari 5 atau lebih dari 8 dan  kurang dari 11 : ",correct3)


