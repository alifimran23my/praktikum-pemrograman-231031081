# Tugas buat program tebak angka 1 sampai 10 dengan batas kesempatan 3 kali.berikan pesan "kesempatan anda terisisa x kali"          
import os 
import random as rd
os.system('cls')

angka = [1,2,3,4,5,6,7,8,9,10]
com = rd.choice(angka)
a = True
limit = 3
i = 0

while a:
    i +=1
    pilih = input('masukan pilihan:')
    if pilih == com:
         print(f"pilihan anda benar yaitu {angka} \n")
         a = True
    else:
        if i < limit:
            print('tebakan anda salah!coba lagi.')
            print(f'kesempatan anda tersisa {limit-i} kali')
            a = True
        else:
            print('kesempatan anda habis')
            a = False