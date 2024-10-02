# nama = ["shandy",106,True,
#         ["yuyun",145]3.96
#         [123,ALVITO,False,3.66]
#         "reyhan"]
# print(nama[4])

# matkul = ["APD",
#           "PTI",
#           "WEB",
#           "jarkom",
#           "BASDAT",
#           "strukdat",
#           "PTI",
#           "KALKULUS"
# ]
# print(matkul[6])


makanan = ["Bakso","sate","soto","nasi goreng","cumi goreng","ayam bakar","mie ayam"]
# print("Sebelum: ")
# print(makanan[1:2])
# makanan.append("Nasi Goreng")
# print("Sesudah: ")
# makanan.clear()
# print(makanan)
# del makanan[5]
# data = makanan.pop(5)
# print(makanan)
# print(data)
# print(makanan)
# makanan.insert(2,"Nasi Goreng")
# makanan[0] = ["AYAM","BEBEK"]
# print(makanan)


# minuman = ["teh","susu","kopi","josu","EsTeler","soda"]
# print("sebelum")
# print(minuman)
# del minuman[2]
# print("sesudah")
# print(minuman)
# minuman[4] = "air putih"
# print(minuman)
# minuman.insert(0,"jus tomat")
# print(minuman)


# makanan = ["ayam","ikan",["bakso","soto","sate","ikan","bebek"],
#            ["teh","kopi","air"]]
# for i in makanan : 
    # print(i, end=" ")
    # if isinstance(i,list):
    #     for j in i :
    #     print(j)
    # else:
    #     print(i)
    # for i in makanan :
    #     for j in i : 
    #         print(j)
        
    
# tuple


akuns = []

while True:
    print("Halo! selamat datang di aplikasi catatan")
    print("Silahakn Pilih 'Daftar akun'jika belum buat akun, dan jika sudah memeiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("_________________________")
    opsi = input("Pilih opsi: ")
    print(" ")
    
    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username: #Memeriksa apakah username sudah ada
                akuna = True
                break
        if akuna: 
            print("Nama SUdah Terpakai Untuk Registrasi Silahakan Coba Lagi")
        else: 
            Password = input("Password: ")
            akuns.append([Username, Password, []]) #Simpan username, password, dan catatan (sebagai list kosong)
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")
            
            