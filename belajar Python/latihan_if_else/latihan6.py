# data diri
orang = {
    "nama_depan": "muhammad iklil ",
    "nama_belakang": "adha",
    "usia" : 20,
    "negara": "indonesia",
    "status": "menikah",
    "skills" : ['javascript',"react","node","mongodb","python"],
    "alamat": {
    "jalan": "gg.subur",
    "nomor": "14 b"
    }
    }

#1. ngecek skill yang urutannya di tengah
if 'skills' in orang :
    tengah = len(orang["skills"]) // 2
    print(f"skill yang ada di tengah {orang["skills"][tengah]}")
else :
    print("gaada ditengah")

#2. mengecek apakah di skill ada python 
if "skills" in orang :

    if "python" in orang['skills'] :
        print("orang ini punya skill python : True")

    else:
        print("gapunya skill python : False")    
else :
    print("ga punya skill : False")

#3. mengecek apakah ada 
if "skills" in orang :
    k = orang["skills"]

    if("react" in k and "node" in k and "mongodb" in k):
        print("orang ini fullstack")

    elif ("javascript" in k and "react" in k):
        print("orang ini front end")

    elif ("node" in k and "python" in k and "mongodb" in k):
        print("orang ini backend")


    else :
        print("unknown tittle")

else :
    print("orang ini ga ada skill")

#4. status menikah 
if orang["status"] == "menikah" and orang["negara"] == "indonesia":

    nama_lengkap = (f"{orang['nama_depan']} {orang['nama_belakang']}")

    print(f"nama {nama_lengkap} tinggal di {orang["negara"]}, dan sudah {orang["status"]}")
