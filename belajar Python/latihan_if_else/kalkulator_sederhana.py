#kalkulator sederhana if else

print(10*"=")
print("kalkulator sederhana")
angka1 = float(input("masukkan angka 1 : "))
angka2 = float(input("masukkan angka 2 : "))
operator = input("masukkan operator (+,-,*,/) : ")

if (operator =="+"):
    print(angka1 + angka2) #bisa gini
    hasil = angka1 + angka2  #bisa juga gini
    print(f"hasilnya adalah : {hasil}")

elif (operator =="-") :
    print(angka1 - angka2)
    hasil = angka1 - angka2
    print(f"hasilnya adalah {hasil}")

elif (operator =="*"):
    print(angka1*angka2)
    hasil = angka1 * angka2
    print(f"hasil adalah :{hasil} ")

elif(operator == "/"):
    print(angka1/angka2)
    hasil = angka1 * angka2
    print(f"hasil adalah : {hasil}")

else : 
    print("salah memasukkan operator")

print("program selesai")