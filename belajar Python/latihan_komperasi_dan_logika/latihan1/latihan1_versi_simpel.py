#latihan 1 versi simpel
# ----0++++++5------8++++11-----

inputUser = float(input("masukkan angka \n\n lebih dari 0 \n dan kurang dari 5 \n \n atau \n\n lebih dari 8 dan \n kurang dari 11 : "))

correct = ((inputUser > 0)and(inputUser < 5)) or ((inputUser>8)and (inputUser<11))
print(correct)


