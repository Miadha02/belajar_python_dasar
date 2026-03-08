#musim 

bulan = input("masukkan bulan untuk musim : ").lower()

musim_gugur = ['september', 'oktober', 'november']
musim_dingin = ['desember','januari','februari']
musim_semi = ['maret','april','mei']
musim_panas = ['juni','juli','agustus']


if (bulan in musim_gugur):
    print(f"bulan {bulan} , adalah musim gugur, bulan bulannya {" , ".join(musim_gugur)}")

elif (bulan in musim_dingin):
    print(f"bulan {bulan}, adalah musim dingin, bulan bulannya {musim_dingin}")

elif(bulan in musim_semi):
    print(f"bulan {bulan}, adalah musim semi , bulan bulannya {musim_semi}")

elif(bulan in musim_panas):
    print(f"bulan {bulan},adalah musim panas , bulan bulannya {musim_panas}")

else :
    print("kamu salah masukkan bulan ")

print("program selesai")