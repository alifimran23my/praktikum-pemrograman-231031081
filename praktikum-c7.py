import os
os.system('clear')

pw = "Mhs_ith2023"
a = True
limit = 3
i = 0

while a:
    i += 1
    pwd = input("Masukkan password: ")
    if pwd == pw:
        print("Selamat anda Berhasil Login ")
        a = False
    else:
        if i < limit:
            print("Password salah! coba lagi.")
            print(f"Kesempatan anda tersisa {limit-1} kali")
            a = True    
        else:
            print("Kesempatan habis!!")
            a = False