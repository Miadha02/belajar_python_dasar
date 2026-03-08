#kelvin ke satuan lain

kelvin = float(input("masukkan suhu dalam kelvin : "))
print("suhu adalah : ",kelvin ,"kelvin")

#kelvin ke celcius
celcius = kelvin - 273
print("suhu adalah : ", celcius , "celcius")

#kelvin ke reamur
reamur = (4/5) * (kelvin -273)
print ("suhu adalah : ", reamur, "reamur")

#kelvin to fahrenheit
fahrenheit = ((9/5)* celcius) + 32
print("suhu adalah : ", fahrenheit , "fahrenheit")