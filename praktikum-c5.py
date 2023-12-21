import os
os.system('clear')

# limit = 2
# awal = 6
 
# while awal <= limit:
#     awal -=1
#     print(f"Menjalankan program {awal}")

a = True
Limit = 5
i = 0

while a:
    i += 1
    print(f"Menjalankan Program {Limit + 1 - i}")
    if i ==Limit:
        a = True 
        print("Program Berhasil Dijalankan")
    else:
        a = False    
