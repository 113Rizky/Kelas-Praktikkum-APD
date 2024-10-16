def nama_fungsi():
   print ("ini adalah fungsi di Python")
nama_fungsi()

   
# Membuat fungsi dengan parameter (panjang, lebar)
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print ("Luas persegi panjang:", luas)
# Pemanggilan fungsi luas_persegi_panjang
luas_persegi_panjang(4, 6)


# Contoh Program mengembalikan hasil fungsi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
hasil = luas_persegi(4)


def mhs(nama, nim, **arr):
    print(nama)
    print(nim)
    print(arr)
    
    
def data(kumpulan):
    print(kumpulan)
    
value = [1,2,3,4]
data(value)


def mhs(nama1, nama2, nama3):
    print(nama1)

    
mhs(nama3= "ucupp", nama2= "saipul", nama1= "michael")