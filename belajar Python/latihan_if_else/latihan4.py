#nilai ujian

nilai = float(input("masukkan nilai anda : "))

if (90 <= nilai <= 100 ) :
    print(f"nilai kamu {nilai}, kamu dapat A ")

elif (80 <= nilai <= 89) :
    print(f"nilai kamu {nilai}, kamu dapat B")

elif(70 <= nilai <= 79):
    print(f"nilai kamu {nilai}, kamu dapat C")

elif (60 <= nilai <= 69):
    print(f"nilai kamu {nilai}, kamu dapat D ")

elif (0 <= nilai <=59) :
    print(f"nilai kamu {nilai}, kamu dapat E")

else :
    print("kamu salah masukkan nilai")

print("program selesai")