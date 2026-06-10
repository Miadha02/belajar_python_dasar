#program list buku
#data_buku = [['judul buku','penulis'],[],[]]
list_buku = []
while True:

    print('masukkan data nbuku')
    judul = input('masukkan judul buku : ')
    penulis = input('masukkan penulis : ')

    buku_baru = [judul,penulis]
    print(buku_baru)

    list_buku.append(buku_baru)
    print(list_buku)

    print('NO.     judul  penulis')
    for index,buku in enumerate(list_buku):
        print(f'{index}    {buku[0]}    {buku[1]}')