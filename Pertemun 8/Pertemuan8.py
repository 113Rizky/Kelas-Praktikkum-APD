angka = int(input("Masukkan angka: "))
print(angka)

# index error
angka = [1,2,3,4]

for i in angka:
    print(i[5])
print(angka[5])


# key error
sosmed = {
    "ig": "@rizky",
    "fb": "rzky"
}

print(sosmed["wa"])


#input “Hello”


try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input yang anda masukkan bukan angka")
except IndexError:
    print("Input yang anda masukkan lebih dari range") 
    

try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input yang anda masukkan bukan angka")
else:
    print(f"Angka yang kamu input: {angka}")
finally:
    print("Program selesai")
    
    
try:
    nama = input("Hello, what's your name? ")
    if len(nama) > 5:
        raise ValueError("Nama tidak boleh lebih dari 5 karakter")
except ValueError as e:
    print(e)