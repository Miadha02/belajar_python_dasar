if pilih_menu == 4:

        if len(list_barang) >0:
            for index,barang in enumerate(list_barang):
                print(f'{index+1}. nama barang : {barang[0]}, harga {barang[1]} , stok {barang[2]}') 