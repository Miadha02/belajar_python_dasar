#latihan konversi satua temperature

#program konversi celcius ke satuan lain

print("PROGRAM KONVERSI TEMPERATURE \n ")

celcius = float(input('masukkan suhu dalam Celcius: '))
print("suhu adalah : ", celcius, "Celcius")

#Reamur
reamur = (4/5) * celcius
print("suhu adalah : ", reamur , "reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius ) + 32
print("suhu adalah : ", fahrenheit , "fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu adalah : ", kelvin, "kelvin")