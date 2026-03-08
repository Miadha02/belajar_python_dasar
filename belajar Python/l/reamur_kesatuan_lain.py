#reamur ke satuan lain
print("REAMUR KE SATUAN LAIN")
reamur = float(input("masukkan nilai suhu dalam reamur : "))

print("suhu adalah : ", reamur ,"reamur")

#reamur ke celcius
celcius = (5/4) * reamur
print("suhu adalah ", celcius , "celcius")

#reamur ke fahrenheit
fahrenheit = ((9/5)*celcius) + 32
print("suhu adalah fahrenheit : ", fahrenheit, "fahrenheit")

#reamur ke kelvin
kelvin = ((5/4) * reamur ) + 273
print("suhu adalah : ", kelvin, "kelvin")