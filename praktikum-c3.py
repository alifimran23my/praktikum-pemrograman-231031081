print('PRAKTIKUM 3')
nama='alif imran'
nim='231031081'
meet='Praktikum 3 (string)'
prodi='Sistem Informasi'
email='imranalif015@gmail.com'
ttl='Baringin,01-01-2004'
alamat='Dusun Baringin'
asal='Baringin'
hobi='Bulutangkis'
tinggi='164 cm'

print('-'*50)
strl="alif imran"
a=strl.center(50)
print(a)
strl= "231031081"
a= strl.center(50)
print(a)
print()
print()
strl= 'Praktikum 3(string)'
a=strl.rjust(50)
sp=60
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('/n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-'*sp)

print(f"""\tHallo, nama saya {nama} dengan NIM {nim},ini adalah file {meet}.Terimah kasih.\n""")

print(f"""Biodata saya,
nama\t={nama.upper()}
nim\t={nim}
prodi\t={prodi}
TTL\t={ttl}
Alamat\t={alamat}
Asal\t={asal}
Hobi\t={hobi}
Tinggi\t={tinggi}
""")

# Stat1: Issac duFort Frankel Sir
stat1 = 'duFort Frankel Sir Issac'
result1 = stat1.split()
result1 = result1[-1] + ' ' + ' '.join(result1[:-1])
print(result1)

# Stat2: d F S Issac
stat2 = 'duFort Frankel Sir Issac'
result2 = stat2.split()
result2 = ' '.join([word[0] for word in result2]) + ' ' + result2[-1]
print(result2)

# Stat3: duFort F S I
stat3 = 'duFort Frankel Sir Issac'
result3 = stat3.split()
result3 = ' '.join([word if word == 'duFort' else word[0] for word in result3])
print(result3)

# Stat4: I duFort Frankel Sir
stat4 = 'duFort Frankel Sir Issac'
result4 = stat4.split()
result4 = result4[-1] + ' ' + ' '.join(result4[:-1])
result4 = result4[0] + ' ' + result4[1:]
print(result4)

# Stat5: Issac d F S
stat5 = 'duFort Frankel Sir Issac'
result5 = stat5.split()
result5 = result5[-1] + ' ' + ' '.join(result5[:-1])
result5 = result5[0] + ' ' + result5[1:]
print(result5)

# Stat6: ISSAC D F S
stat6 = 'duFort Frankel Sir Issac'
result6 = stat6.split()
result6 = result6[-1].upper() + ' ' + ' '.join([word[0].upper() for word in result6[:-1]])
print(result6)

# Stat7: duFort Frankel Sir Issac
stat7 = '#duFort Frankel Sir Issac$'
result7 = ''.join([c for c in stat7 if c.isalpha() or c.isspace()])
print(result7)

# Stat8: duFort Frankel Sir Issac
stat8 = '#duFort-Frankel-Sir-Issac$'
result8 = ''.join([c for c in stat8 if c.isalpha() or c.isspace() or c == '-'])
print(result8)

# Stat9: duFort Frankel Sir Issac
stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
result9 = ''.join([c for c in stat9 if c.isalpha() or c.isspace()])
print(result9)

# Stat10: DUFORT FRANKEL SIR ISSAC
stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
result10 = ''.join([c for c in stat10 if c.isalpha() or c.isspace()])
result10 = result10.upper()
print(result10)
