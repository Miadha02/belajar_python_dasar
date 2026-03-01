#format string

#contoh generic
#string
nama = "marlene"
format_str = f"hello {nama}" # format (f), dan {nama}

print(format_str)

#angka
angka = 2005.5
#kalau dibuat gini maka
# format_str = "angka "+ angka  ,,,maka hasilnya error, karena gaboleh string ketemu float

#pakai cara ini , format
format_str = f"angka = {angka}"
print(format_str)

#boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

#bilangan bulat
angka = 15
format_str = f"bilangan bulat {angka:d}"
print(format_str)

#bilangan ribuan
angka = 200000
format_str = f"bilangan ribuan {angka:,}" #sebelumnya 2000000 ,pakai (,) menjadi 200,000 
print(format_str)

#bilangan desimal
angka = 2005.54321
format_str = f"bilangan desimal {angka:.2f}"      #titik (.) artinya desimalnya 2005(.)4321 
                                                #2f berfungsi menampilkan angka dibelakang koma
                                             #kalau mau menampilkan 2 angka dibelakang koma pakai 2f
print(format_str)

#menampilkan leading zero
angka = 2005.54321
format_str =f"leading zero = {angka:09.3f}" # 9 berfungsi menambahkan 2005.543 menjadi (spasi)2005.543
                                        #0 berfungsi menambahkan 0 didepan 2005.543 menjadi , 02005.543
print(format_str)

#tanda plus(+) , dan minus (-)

angka_plus = 10
angka_minus = -10
format_plus = f"angka plus {angka_plus:+d}" #+ berfungsi mengeluarkan tanda ,
                                            #misal angka minus -10, di keluarkan tanda -10

format_minus = f"angka minus {angka_minus:+.2f}" #+ berfungsi mengeluarkan tanda ,
                                               #misal angka plus 10, dikeluarkan tanda +10
print(format_minus)
print(format_plus)

#formmat persen
persentase = 0.045
format_persen = f"format persen {persentase:2%}" # % fungsinya adalah mempersenkan
                                                    #2 berungsi menampilkan 2 angka dibelakang koma
print(format_persen)

#melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total =RP.{harga*jumlah:,}"
print(format_string)

#format angka lain (binary , octal , hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexa =f"hexadesimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)