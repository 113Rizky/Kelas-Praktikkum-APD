# cuaca = "cerah"

# if cuaca == "mendung":
#     print("diam dirumah")
# elif cuaca == "cerah" :
#     print("keluar rumah")
# else:
#     print("hari ini mendung") 
    
# nama = str(input("Masukkan Nama Anda : "))
# print(nama)

umur = int(input("Masukkan umur anda : "))
if umur > 0:
    if umur <= 10:
         print("Umur Anda termasuk kategori anak-anak")
    elif umur <= 18:
        print("Umur anda termasuk kategori remaja")
    elif umur <= 35:
        print("Umur anda termasuk kategori dewasa")
    elif umur <= 65:
        print("Umur anda termasuk kategori paruh baya")
else:
    print("Umur anda termasuk kategori tua")
    
    
nim = int(input("Masukkan nim:"))

if nim >= 1 and nim <= 50 :
    if nim >= 1 and nim <= 25 : 
       print("Kelas A'2")
    else :
        print("Kelas A'2")
elif nim >= 51 and nim <= 100 :
    if nim >= 51 and nim <= 75 :
        print("Kelas B'2")
    else :
        print("Kelas B'2")
elif nim >= 101 and nim <= 121 :
    if nim >= 101 and nim <= 110 :   
        print("Kelas C'1")
    else :
        print("Kelas C'2") 
else :
    print("Anda Bukan Mahasiswa Informatika 24")
    
nim = int(input("Masukkan nim: "))
hasil = "Kelas A" if nim >= 1 and nim <= 50 else "Kelas B" if nim >= 51 and nim <= 100 else "Kelas C" if nim >= 101 and nim <=121 else "mahasiswa siluman"
print(hasil)                      