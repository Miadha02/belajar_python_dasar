data = {
    "nama" : "iklil",
    "usia" : 20,
    "negara" : "indonesia",
    "skills" : ["python","c++","javascript"],
    "poin_belajar" : 85,
    "alamat": {
        "kota":"medan",
        "kode_pos": 20221
    }
}


if ("nama" in data and "usia" in data):
    
        if (data["nama"]=="iklil" and data["usia"] > 17) :
            print(f"kamu adalah {data['nama']} , dan usia kamu {data['usia']}")
            print("kamu sudah dewasa")

        elif (data['nama'] != "iklil" and data['usia'] > 17) :
              print(f"nama kamu salah {data['nama']}")

        elif (data['nama'] =="iklil" and data['usia'] < 17) :  
              print("umur anda kurang")

        else : 
              print("data tidak cocok")          
else :
      print("tidak ada nama atau usia")

#2
if "skills" in data :
      
      jumlah_skill = len(data['skills']) 
      skill = data['skills']
      if ("python" in skill and jumlah_skill > 2):
            print("programmer python terdeteksi")
      elif ("python" in skill and jumlah_skill <=2):
            print("baru mulai belajar ya?")
      else :
            print("unknown")
else :
      print("gaada skill di data")                        

#3 
if "poin_belajar" in data :
      poin = data['poin_belajar']

      if (90 <= poin <= 100) :
            print(f"poin kamu adalah {poin}, predikat sangat baik")
      elif (75 <= poin <=90):
            print(f"poin kamu adalah {poin} ,predikat kamu adalah baik")
      elif (0 <= poin <= 75):
            print(f"poin kamu adalah {poin}, predikat kamu cukup")
      else :
            print("salah memasukkan poin")                   

else :
      print("gaada data poin")
      

    
      
      