word = "noelaja"
guess = ""
Attempts = 6

print ("selamat datang di permainan tebak tebakan hangman")
print ("Anda memiliki 6 kesempatan untuk menebak kata yang benar")

while Attempts > 0:
    correct = 0

    for char in word :
        if char in guess:
            print (char, end=" ")
            correct += 1
        else:
            print ("_ ", end="")
    print()

    if correct == len(word):
        print ("\nSelamat, Anda Menang!")
        break


    user_guess = input("Masukkan 1 huruf yang benar: ").lower()

    if len(user_guess) != 1 or not user_guess.isalpha():
        print ("input tidak valid, masukkan 1 huruf saja.")
        continue

    if user_guess in guess:
        print ("Anda sudah menebak huruf ini sebelumnya.\n")
        continue

    guess += user_guess

    if user_guess not in word:
        Attempts -= 1
        print ("Huruf salah! Anda memiliki kesempatan tersisa. , Attemps \n")
    else: ("Huruf benar!\n")

    if Attempts == 0:
        print ("Maaf, Anda Kalah! Kata yang benar adalah:", word)