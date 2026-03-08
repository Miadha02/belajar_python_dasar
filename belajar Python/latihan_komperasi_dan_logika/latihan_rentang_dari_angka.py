# membuat gabungan area rentang dari angka


#+++++3----------10++++++++++
inputUser = float(input("masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10  : "))

#++++++++++3----------------
#memeriksa angka < 3
KurangDari = (inputUser < 3)
print ("Kurang dari 3 = ",KurangDari)

#--------10+++++++
#memeriksa angka > 10
LebihDari = (inputUser > 10)
print("Lebih dari 10 = ",LebihDari)

Correct = KurangDari or LebihDari 
print("angka yang anda masukkan : ",Correct)


#----3++++++10---------
inputUser = float(input("masukkan angka yang lebih besar dari 3 dan kurang dari 10 : "))

#memeriksa angka > 3
LebihDari = (inputUser > 3)
print("lebih dari 3 = ", LebihDari)

#memeriksa angka < 10
KurangDari = (inputUser < 10)
print("kurang dari 10 = ", KurangDari)

Correct = LebihDari and KurangDari # kita pakai and karena angka yang lebih besar dari 3 dan kurang dari 10 
print("angka yang anda masukkan : ", Correct)