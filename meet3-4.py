# Meminta input dari pengguna
alas = int(input("Masukkan alas persegi panjang: "))
tinggi = int(input("Masukkan tinggi persegi panjang: "))

# Mengecek apakah input valid (lebih dari 0)
if alas > 0 and tinggi > 0:
    # Menghitung luas
    luas = alas * tinggi
    print(f"\nLuas persegi panjang adalah: {luas:.2f}\n")

    # Menampilkan bentuk persegi panjang dengan bintang
    print("Gambar persegi panjang:")
    for i in range(tinggi):  # tinggi = jumlah baris
        print('*' * alas)    # alas = jumlah bintang per baris

else:
    print("Alas dan tinggi harus lebih dari 0!")
