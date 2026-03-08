saldo = 100

print(f'''---Menu ATM---
      1. check saldo
      2. Tarik Tunai
      3. keluar ''')

while True :
    pilih_menu = int(input("pilih menu : "))

    if ((pilih_menu) == 1):
        print(f"saldo anda {saldo}")
    
    elif(pilih_menu == 2):
        tarik_tunai = int(input("masukkan jumlah tarik tunai : "))
        
        if (tarik_tunai > saldo):
            print("saldo tidak cukup")

        elif(tarik_tunai < saldo):
            saldo -= tarik_tunai
            print(f"penarikan berhasil, sisa saldo = {saldo}")

        else :
            print("salah masukkan nilai")

    elif(pilih_menu == 3):    
        print("keluar")
        break   
    else :
        print("salah masuk input")
        continue            
