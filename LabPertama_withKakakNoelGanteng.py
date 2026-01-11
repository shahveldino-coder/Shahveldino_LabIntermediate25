print ("Bermain tebak kata")
print ("clue : kata rahasia ada di judul repo")

katarahasia ="noelganteng"
index = 0
while True:
    Var1 = input("Tebak satu huruf :")
    if len(Var1) == 1 and Var1[0] == katarahasia[index]:
        print ("Benar, lanjut ke huruf berikutnya")
        index += 1
    else:
        print("Tebakan anda salah, coba lagi")

    if index == len(katarahasia)  :
        print ("selamat tebakan anda benar")
        break


