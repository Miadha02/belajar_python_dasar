#latihan 2 versi simpel
#++++0-----5+++++8----11++++++++

inputUser = float(input("masukkan angka kurang dari 0 atau (lebih dari 5 dan kurang dari 8) atau lebih dari 11 : "))

correct = (inputUser < 0 or (inputUser > 5 and inputUser <8) or inputUser > 11 )

print(correct)