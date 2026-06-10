#kalkulator sederhana 
angka1 = input('masukkan angka 1 : ')

if angka1.replace(".","",1).isdigit():

    angka11 = float(angka1)

    angka2 = input("masukkan angka 2 : ")

    if angka2.replace(".","",1).isdigit():
        angka22 = float(angka2)

        operator = input("masukkan operator (+,-,/,*): ")

        if operator == '-':
            hasil = angka11 - angka22
            print(f'hasilnya {hasil}')

        elif operator == '*':
            hasil = angka11 * angka22
            print(f"hasilnya {hasil}")

        elif operator == "/":

            if angka22 == 0:
                print(f'error , tidak bisa dibagi 0')

            else:
                hasil = angka11 / angka22
                print(f"hasilnya {hasil:.2f}")

        elif operator == "+":
            hasil = angka11 + angka22   
            print(f"hasilnya {hasil}")     

        else :
            print('salah masukkan inputan')
    else:
        print('kamu salah masukkan angka')    
    
else:
    print(f"kamu salah masukkan angka {angka1}")    


print('end of program')
