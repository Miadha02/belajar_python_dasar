#kalkulator sederhana

print(30*"=")
print("kalkulator sederhana".center(30))
print(30*"=")

angka1 = float(input("masukkan angka 1 : "))
operator = input("operator + , - * / : ")
angka2 = float(input("masukkan angka 2 : "))

if operator == "+":
    hasil = angka1 + angka2
    print(f'hasilnya {hasil}'.upper())
elif operator == '-':
    hasil = angka1 - angka2
    print(f"hasil {hasil}".upper())

elif operator == '*':
    hasil = angka1 * angka2
    print(f"hasil {hasil}".upper())

elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasil {hasil}".upper())

else:
    print("kamu salah masukkan input")

