print("Nama : Alif imran")
print("NIM : 231031081")
print("Prodi : Sistem Informasi")
print("Tanggal Lahir : 01-01-2004")

#operasi aritmetika
a=7
print('Nilai a=',a)
a=7
a+=1
print('Nilai a+=1 akan menjadi',a)
a=7
a-=1
print('Nilai a-=1 akan menjadi',a)
a=7
a*=2
print('Nilai a*=2 akan menjadi',a)
a=7
a/=2
print('Nilai a/=2 akan menjadi',a)
a=7
a%=2
print('Nilai a%=2 akan menjadi',a)
a=7
a//=2
print('Nilai a//=2 akan menjadi',a)
a=7
a**=2
print('Nilai a**=2 akan menjadi',a)


#OR
b=True
print('Nilai b=',b)
b|=False
print('Nilai b|= False akan menjadi',b)
b=False
print('Nilai b=',b)
b|=False
print('Nilai b|= False akan menjadi',b)

#AND
b=True
print('Nilai b=',b)
b&=False
print('Nilai b&= False akan menjadi ',b)
b=False
print('Nilai b=',b)
b&=False
print('Nilai b&= False akan menjadi ',b)

#XOR
b=True
print('Nilai b=',b)
b^=False
print('Nilai b^=False akan menjadi ',b)
b=False
print('Nilai b=',b)
b^=False
print('Nilai b^=False akan menjadi ',b)

#Shifting
c=0b0100
print('Nilai c=',format(c,'04b'))
c>>=1
print('Nilai c>>=1 akan menjadi ',format(c ,'04b'))
c=0b0100
c<<=1
print('Nilai c<<=1 akan menjadi ',format(c ,'04b'))

a=8#isi dengan ujung NIM
b=13#Ubah dengan hasil jumlah ujung NIM dengan 5
print('==================Besar dari 13')
hasil=a>13
print(a,'>13 adalah',hasil)
hasil=b>13
print(b,'>13 adalah',hasil)

print('==================Kecil dari 13')
hasil=a<13
print(a,'<13 adalah ',hasil)
hasil=b<13
print(b,'<13 adalah ',hasil)

print('==================Besar atau sama dari 13')
hasil=a>=13
print(a,'>=13 adalah',hasil)
hasil=b>=13
print(b,'>=13 adalah',hasil)

print('==================Besar atau sama dari 13')
hasil=a<=13
print(a,'<=13 adalah',hasil)
hasil=b<=13
print(b,'=13 adalah',hasil)

print('==================Sama dengan 13')
hasil=a==13
print(a,'==13 adalah',hasil)
hasil=b==13
print(b,'==13 adalah',hasil)


print('==================Tidak sama dengan 13')
hasil=a!=13
print(a,'!=13 adalah',hasil)
hasil=b!=13
print(b,'!=13 adalah',hasil)

print('=============NOT=============')
a=True
c=not a

print('a adalah a')
print('------c=not a-------NOT')
print('c adalah',c)

print('=============OR=============')
a=True
b=True
c=a or b
print(a,'OR',b,'menjadi',c)

a=True
b=False
c=a or b
print(a,'OR',b,'menjadi',c)

a=False
b=True
c=a or b
print(a,'OR',b,'menjadi',c)

a=False
b=False
c=a or b
print(a,'OR',b,'menjadi',c)

print('=============AND=============')
a=True
b=True
c=a and b
print(a,'AND',b,'menjadi',c)

a=True
b=False
c=a and b
print(a,'AND',b,'menjadi',c)

a=False
b=True
c=a and b
print(a,'AND',b,'menjadi',c)

a=False
b=False
c=a and b
print(a,'AND',b,'menjadi',c)

print('=============XOR=============')
a=True
b=True
c=a^b
print(a,'^',b,'menjadi',c)

a=True
b=False
c=a^b
print(a,'^',b,'menjadi',c)

a=False
b=True
c=a^b
print(a,'^',b,'menjadi',c)

a=False
b=False
c=a^b
print(a,'^',b,'menjadi',c)

print(' ============== IS ')
a=5
b=5
print('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil= a is b
print('a is b = ', hasil )

a =5
b =6
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is b
print ('a is b = ', hasil )

print (' ============== IS NOT ')
a =5
b =5
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is not b
print ('a is not b = ', hasil )

a=5
b=6
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is not b
print ('a is not b = ', hasil )

#TUGAS
#Buat kode untuk masing masing operator berikut
print("=============NAND=============")
print("=============NOR=============")
print("=============NXOR=============")

#jawaban
print("=============NAND=============")
hasil = not(a and a)
print(a, "nand", b, "adalah =",hasil)
hasil = not(a and b)
print(a, "nand", b, "adalah =",hasil)
hasil = not(b and a)
print(b, "nand", b, "adalah =",hasil)
hasil = not(b and b)
print(b, "nand", b, "adalah =",hasil)
print()
print("=============NOR=============")
hasil = not(a or a)
print(a, "nor", a, "adalah =",hasil)
hasil = not(a or b)
print(a, "nor", b, "adalah =",hasil)
hasil = not(b or a)
print(a, "nor", b, "adalah =",hasil)
hasil = not(b or b)
print(a, "nor", b, "adalah =",hasil)
print()
print("=============NXOR=============")
hasil = not(a ^ a)
print(a, "nxor", a, "adalah =",hasil)
hasil = not(a ^ b)
print(a, "nxor", b, "adalah =",hasil)
hasil = not(b ^ a)
print(b, "nxor", a, "adalah =",hasil)
hasil = not(b ^ b)
print(b, "nxor", b, "adalah =",hasil)
print()
print()
print()

print (' ======================= IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

test = 'rud '
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

test = 'bac '
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

print (' ======================= NOT IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek
) )

test = 'rud '
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek
) )

test = 'bac '
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek
) )
#Tugas
#Dengan cara yang sama buat operator in dan not in , ubah nama ←- lengkap menjadi nama masing - masing dengan uji test
test1 = "al"
test2 = "la"
test3 = "a"
test4 = "i"
test5 = "e"
test6 = "o"

#Operator Bitwise
a=1
a +=60
b=1
b+= 90
print("=============================OR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(|)")
hasil=a|b
print("Nilai",a,"|",b,"dalam biner =", format(hasil,"08b"))

print("=============================AND")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(&)")
hasil=a&b
print("Nilai",a,"&",b,"dalam biner =", format(hasil,"08b"))

print("=============================XOR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(^)")
hasil=a^b
print("Nilai",a,"^",b,"dalam biner =", format(hasil,"08b"))

print("=============================NOT")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~a)")
hasil= ~a
print("Nilai ~",a,"dalam biner =", format(hasil,"08b"))

print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~b)")
hasil= ~b
print("Nilai ~",b,"dalam biner =", format(hasil,"08b"))

print("=============================>>")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(>>2)")
hasil= a >> 2
print("Nilai ~",a,"dalam biner =", format(hasil,"08b"))

print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(<<2)")
hasil= b << 2
print("Nilai ~",b,"dalam biner =", format(hasil,"08b"))
print()
#TUGAS
print()
text = '============================= NOT AND'

# Membuat list dari representasi ASCII setiap karakter dalam teks
ascii_values = [ord(char) for char in text]

# Membuat representasi biner dari setiap nilai ASCII
binary_values = [bin(value)[2:].zfill(8) for value in ascii_values]

# Menggabungkan representasi biner menjadi satu string
binary_string = ''.join(binary_values)

print(binary_string)

print()
text = ' ============================= NOT OR '

binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
binary_string = ''.join(binary_values)

print(binary_string)
print()
text = ' ============================= NOT XOR '

binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
binary_string = ''.join(binary_values)

print(binary_string)
print()
text = ' ============================= NOT ( > >2) '

binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
binary_string = ''.join(binary_values)

print(binary_string)
print()
text = ' ============================= NOT ( < <2) '

binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
binary_string = ''.join(binary_values)

print(binary_string)

