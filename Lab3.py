def tampil_kata(kunci, terbuka):
    hasil = ""
    for i in range(len(kunci)):
        if terbuka[i] == True:
            hasil = hasil + kunci[i]
        else:
            hasil = hasil + "_"

        if i < len(kunci) - 1:
            hasil = hasil + " "
    return hasil


def game_tebak(kunci):
    nyawa = 5
    terbuka = [False for i in range(len(kunci))]

    while nyawa > 0:
        teks = tampil_kata(kunci, terbuka)
        print("Kata :", teks)
        print("Nyawa :", nyawa)

        huruf = input("Masukkan huruf: ")

        ketemu = False
        for i in range(len(kunci)):
            if kunci[i] == huruf:
                terbuka[i] = True
                ketemu = True

        if ketemu == True:
            print("Huruf ditemukan!")
        else:
            nyawa = nyawa - 1
            print("Huruf tidak ada!")

        if "_" not in teks:
            print("Kata :", teks)
            print("Selamat, kamu menang!")
            break

    if nyawa == 0:
        print("Game selesai, kamu kalah!")


game_tebak("Noels")
