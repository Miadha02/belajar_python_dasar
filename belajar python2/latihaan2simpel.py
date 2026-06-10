#------0++++5-----8+++++11------
InputUser = float(input("masukkan nilai (lebih dari 0 dan kurang dari 5) atau (lebih dari 8 dan kurang dari 11) :"))

hasil = (0 < InputUser < 5) or (8 < InputUser <11)
print(hasil)