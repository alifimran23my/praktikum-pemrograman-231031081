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
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek←-
) )

test = 'rud '
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek←-
) )

test = 'bac '
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek←-
) )


