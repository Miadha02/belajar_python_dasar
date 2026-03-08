total_belanja = 0

while True :
    input_user = input("masukkan harga barang (atau ketik selesai) : ")

    if input_user == "selesai" :
        break
    
    

    if input_user.isdigit():
        harga = int(input_user)
        total_belanja += harga

    else :
        continue
    

print("="*5)
print(f"total yang harus dibayar : {total_belanja}")        