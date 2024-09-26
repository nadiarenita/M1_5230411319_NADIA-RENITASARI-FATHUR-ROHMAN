import math

def hitung_luas_persegi(sisi):
    return sisi*sisi

def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang*lebar

def hitung_luas_lingkaran(radius):
    return math.pi*(radius**2)


#contoh 

sisi_persegi = 5
panjang_persegi_panjang = 6
lebar_persegi_panjang = 4
radius_lingkaran = 3


print("luas persegi:", hitung_luas_persegi(sisi_persegi))
print("luas persegi panjang", hitung_luas_persegi_panjang(panjang_persegi_panjang,lebar_persegi_panjang))
print("luas lingkaran:", hitung_luas_lingkaran(radius_lingkaran))
