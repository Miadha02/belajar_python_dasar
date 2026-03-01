#1. cara membuat string

data = "ini adalah string"
print(data)

print(type(data))

'''
cara membuat string
1. dengan menggunakan single quote '.....'
2. dengan menggunakan double quote "....."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"halo apakabars?"') 
print("'halo,apakabars?'")
print("ini adalah hari jum'at ")

#2. Menggunakan tanda \
print('mari shalat jum\'at') # kalau tidak pakai \ maka error
print('g\'day , isn\'t it')

#backslash
print("C:\\user\\Ucup") # dibaca C:\user\ucup

#tab
print("ucup \t otong, jauhan") # di tab

#backspace
print("ucup \botong ") # menghapus jarak , jadi ucupotong

#newline
print("baris pertama \n baris kedua") # meng enter newline , lf -> line feed ,dipakai oleh unix , macos,linux
print("baris pertama \r baris kedua") # cr : carriage return , dipakai oleh commodore , acorn , lisp
print("baris pertama \r\n baris kedua") #crlf : line feed carriage return, dipakai oleh windows

# 3. String literal atau raw

#hati-hati
print("C:\new folder") # akan salah pathnya

print("c:\\new folder") # ini benar

# menggunakan raw string
print(r"C:\new folder") # dianggap string semua , semua akan di print

#multiline literal string
print(""" 
Nama : iklim
kelas : 3 sd
""")

#multiline literal string dan RAW
print(r""" 
nama : iklim
kelas : 3\sd
      Website : www.iklim.com/newID
""")