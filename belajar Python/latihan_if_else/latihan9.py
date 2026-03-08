#soal 
#siapa yang dapat kda skor tertinggi
#siapa yang dapat mvp menang dan mvp kalah
#jika 10 <= skor <=20  maka silver
#jika > 20 maka gold

#kawan
friend ={

    "friend_1": {
        "kill" : int(input("player 1 jumlah kill : ")),
        "assist" : int(input("player 1 assist : ")),
        "death" : int(input("player 1 death : ")),
    },

     "friend_2": {
        "kill": int(input("player 2 kill : ")),
        "assist": int(input("player 2 assist : ")),
        "death" : int(input("player 2 death : "))
    },
    "friend_3":{
        "kill" : int(input("player 3 kill : ")),
        "assist": int(input("player 3 assist : ")),
        "death": int(input("player 3 death : "))
    }
}

enemy = {

    "enemy_1":{
        "kill" :int(input("enemy 1 kill : ")),
        "assist":int(input("enemy 1 assist : ")),
        "death":int(input("enemy 1 death : "))
    },
    "enemy_2":{
        "kill" : int(input("enemy 2 kill : ")),
        "assist" : int(input("enemy 2 assist : ")),
        "death":int(input("enemy 2 death : "))
    },
    "enemy_3":{
        "kill": int(input("enemy 3 kill : ")),
        "assist":int(input("enemy 3 assist")),
        "death":int(input("enemy 3 death"))
    }
}

winner = {
   "winner" : input("masukkan pemenang antara friend atau enemy : ").lower()
}

parameter_kill = 2
parameter_assist = 1
parameter_death = -1


#menghitung kda
#skor friend
skor_f1 = (friend["friend_1"]["kill"] * parameter_kill) + (friend["friend_1"]["assist"] * parameter_assist) + (friend["friend_1"]["death"] * parameter_death)
skor_f2 = (friend["friend_2"]["kill"] * parameter_kill) + (friend["friend_2"]["assist"] * parameter_assist) + (friend["friend_2"]["death"] * parameter_death)
skor_f3 = (friend["friend_3"]["kill"] * parameter_kill) + (friend["friend_3"]["assist"] * parameter_assist) + (friend["friend_3"]["death"] * parameter_death)

#skor enemy
skor_e1 = (enemy['enemy_1']["kill"] * parameter_kill) + (enemy['enemy_1']['assist'] * parameter_assist) + (enemy['enemy_1']['death'] * parameter_death)
skor_e2 = (enemy['enemy_2']["kill"] * parameter_kill) + (enemy['enemy_2']['assist'] * parameter_assist) + (enemy['enemy_2']['death'] * parameter_death)
skor_e3 = (enemy['enemy_3']["kill"] * parameter_kill) + (enemy['enemy_3']['assist'] * parameter_assist) + (enemy['enemy_3']['death'] * parameter_death)

print("\n\n",5*"="," hasil pertandingan ",5*"=","\n")
if (winner['winner']=="enemy"):
    print("pemenang adalah enemy\n")

elif (winner['winner']=='friend'):
    print("pemenang adalah friend \n")  

print(5*"="," Player kda ",5*"=")
print("===friend===")
print(f"friend 1 kda : {skor_f1}")
print(f"friend 2 kda : {skor_f2}")
print(f"friend 3 kda : {skor_f3}")

print("\n===enemy===")
print(f"enemy 1 kda : {skor_e1}")
print(f"enemy 2 kda : {skor_e2}")
print(f"enemy 3 kda : {skor_e3}")


#siapa yang dapat mvp menang dan mvp kalah
print("============")
print(" siapa yang mvp menang dan mvp kalah : \n")

#friend
if (skor_f2 < skor_f1 > skor_f3) :
    if (skor_f1 >= 20):
        print("friend 1 medali gold")
    
    elif (10 <= skor_f1 <=20):
        print("friend 1 medali perak")

    else:
        print("friend 1 medali bronze")        

    if(winner['winner']=='enemy'):
        print("friend mvp kalah")
    elif(winner['winner'] == 'friend'):
        print("friend mvp menang")
    else :
        print("")        

elif (skor_f1 < skor_f2 > skor_f3):
    if(skor_f2 >= 20):
        print("friend 2 medali gold")
    elif(10 <= skor_f2 <= 20):
        print("friend 2 : medali perak")

    else:
        print("friend 2 medali bronze")        

    if(winner['winner']=='friend'):
        print("friend 2 mvp menang")
    elif(winner['winner']=='enemy'):
        print("friend 2 mvp kalah")    

    else : 
        print("")

elif (skor_f1 < skor_f3 > skor_f2):
    if(skor_f3 >= 20):
        print("friend 3 medali gold")
    if(10 <= skor_f3 <=20):
        print("friend 3 medali perak")
    else :
        print("friend 3 medali bronze")

    if(winner['winner']=='friend'):
        print("friend 3 mvp menang")
    elif(winner['winner']=='enemy'):
        print("friend 3 mvp kalah")   
    else :
        print("") 

else :
    print("ada yang salah")

#enemy
print("=====","\n")
if (skor_e2 < skor_e1 > skor_e3):

    if(skor_e1 >= 20):
        print("enemy 1 medali gold")

    elif(10 <= skor_e1 <= 20):
        print("enemy 1 medali perak")
    else :
        print("enemy 1 bronze")    

    if(winner['winner']=='friend'):
        print("enemy 1 mvp kalah")
    elif(winner['winner']=='enemy'):
        print('enemy 1 mvp menang')

elif (skor_e1 <= skor_e2 >= skor_e3):
    if(skor_e2 >=20):
        print("enemy 2 medali gold")
    elif(10 <= skor_e2 <= 20):
        print("enemy 2 medali perak")
    else :
        print("enemy 2 bronze")

    if(winner['winner']=='friend'):
        print("enemy 2 mvp kalah")    

    elif(winner['winner']=='enemy'):
        print("enemy 2 mvp menang")

elif (skor_e1 <= skor_e3 >= skor_e2) :
    if(skor_e3 >=20):
        print("enemy 3 medali gold")
    elif(10 <= skor_e3 <=20):
        print("enemy 3 medali perak")
    else :
        print("enemy 3 medali bronze")

    if(winner['winner']=='friend'):
        print("enemy 3 mvp kalah ")
    elif(winner['winner']=='enemy'):
        print("enemy 3 mvp menang") 

else :
    print("ada yang salah")               
#jika < 5 maka silver
#jika > 5 maka gold

