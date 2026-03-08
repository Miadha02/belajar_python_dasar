data = {
    "username" : input("masukkan username : "),
    "password" : input("masukkan password : "),
    "kode_akses": int(input("masukkan kode akses : "))
}

if(data['username']== "iklil" or data["username"]== "IKLIL") : 

    panjang_pass = len(data['password'])
    
    if(panjang_pass >=6):
        
        if(data["kode_akses"] % 2 == 0):
            print("login berhasil")

        else:
            print("kode akses harus genap")
    else :
        print("panjang password tidak boleh kurang dari 6")
else :
    print("username salah")    