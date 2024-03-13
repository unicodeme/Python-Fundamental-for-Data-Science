# fungsi untuk menghitung luas persegi panjang
def hitung_luas(panjang, lebar):
  luas = panjang * lebar
  return luas

# fungsi untuk menghitung keliling persegi panjang
def hitung_keliling(panjang, lebar):
  keliling = panjang * lebar
  return keliling

panjang = 5
lebar   = 3

luas_persegi_panjang = hitung_luas(panjang, lebar)
keliling_persegi_panjang = hitung_keliling(panjang, lebar)
print("Luas persegi panjang", luas_persegi_panjang)
print("Keliling persegi panjang", keliling_persegi_panjang)