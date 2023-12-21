import os
os.system('clear')

a = True

while a:
    pilih = input ("Apakah ingin melanjutkan? [y/n]")
    if pilih == "y":
        print("Terimah Kasih!")
        a = False
    elif pilih == "n":
        print("Sampai Jumpa")
        a = False
    else:
        print("Jangan Aneh Deh 😒")    