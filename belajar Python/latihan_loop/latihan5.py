rahasia = 8
nyawa = 3
while True :
    print(f"sisa nyawa : {nyawa}")
    tebakan = int(input("masukkan tebakan : "))

    

    if tebakan == rahasia :
        print(f"kamu berhasil menebak {rahasia}")
        break
    
    
    else :
        print("salah angka")   
        nyawa -= 1

    if nyawa == 0:
        print("Game over")
        break         