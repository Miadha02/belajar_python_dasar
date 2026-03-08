#Fahrenheit ke satuan lain

fahrenheit = float(input("masukkan suhu dalam fahrenheit : "))
print("suhu adalah : ", fahrenheit , "fahrenheit")

#fahrenheit ke celcius 
celcius = (5/9)*(fahrenheit - 32 )
print("suhu adalah : ", celcius , "celcius")

#Fahrenheit ke reamur
reamur = (4/9)* (fahrenheit - 32 )
print("suhu adalah : ", reamur,"reamur")

#fahrenheit ke kelvin
kelvin = celcius + 273
print("suhu adalah : ", kelvin, "kelvin")