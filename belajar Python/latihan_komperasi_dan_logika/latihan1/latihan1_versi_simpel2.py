#latihan 1 versi simpel 2
# ----0++++++5------8++++11-----

inputUser = float(input("masukkan angka \n\n lebih dari 0 \n dan kurang dari 5 \n \n atau \n\n lebih dari 8 dan \n kurang dari 11 : "))

correct = (0 < inputUser < 5) or (8 < inputUser < 11)  
print(correct)