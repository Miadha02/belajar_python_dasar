#membuat gabungan area rentang dari angka

# ++++++3-----------10+++++++

inputUser = float(input("masukkan nilai yang kurang dari 3 atau lebih besar dari 10 : "))

kurangdari = (inputUser <3)
print(kurangdari)

lebihdari = (inputUser > 10)
print(lebihdari)

gabungan = kurangdari or lebihdari
print('hasil',gabungan)


#lebih simpel
kurangdari = (inputUser < 3) or (inputUser > 10)
print('lebihsimpel',kurangdari)


# -------3+++++10-------
#irissan
inputUser = float(input("masukkan lebih dari 3 dan kurang dari 10 : "))

lebihdari = inputUser > 3
print(lebihdari)

kurangdari = inputUser < 10
print(kurangdari)

gabungan = lebihdari and kurangdari
print(gabungan)

#simpel
hasil = (3 < inputUser < 10)
print(hasil)
hasil = (inputUser > 3) and (inputUser <10)
print(hasil)