print("--- Silakan Masukkan Data Anda ---")
nama_user = input("Masukkan nama Anda: ")
umur_user_str = input("Masukkan umur Anda: ")

tinggi_user_str = input("Masukkan tinggi badan Anda (contoh: 165.5): ") 

hobi_user_str = input("Masukkan beberapa hobi Anda (pisahkan dengan koma): ")

angka1_str = input("Masukkan angka favorit pertama Anda: ")
angka2_str = input("Masukkan angka favorit kedua Anda: ")

umur_user = int(umur_user_str)
angka1 = int(angka1_str)
angka2 = int(angka2_str)
tinggi_user = float(tinggi_user_str) 

hobi_user = [item.strip() for item in hobi_user_str.split(',')]

print("\nTerima kasih! Data Anda telah kami simpan.")
print("================================================\n")


print("--- 2. Tipe Data Variabel ---")

nama_lengkap = nama_user
print(f"Variabel 'nama_lengkap': '{nama_lengkap}' adalah {type(nama_lengkap)}")

umur = umur_user
print(f"Variabel 'umur': {umur} adalah {type(umur)}")

tinggi_badan = tinggi_user
print(f"Variabel 'tinggi_badan': {tinggi_badan} adalah {type(tinggi_badan)}")

sudah_vaksin = True
print(f"Variabel 'sudah_vaksin': {sudah_vaksin} adalah {type(sudah_vaksin)}")

hobi = hobi_user
print(f"Variabel 'hobi': {hobi} adalah {type(hobi)}")

print("================================================\n")


print(f"--- 3. Manipulasi String untuk Nama '{nama_lengkap}' ---")
salam = "Selamat datang, " + nama_lengkap + "!"
print(f"Hasil penggabungan string: {salam}")
panjang_nama = len(nama_lengkap)
print(f"Panjang nama Anda adalah {panjang_nama} karakter.")
nama_upper = nama_lengkap.upper()
print(f"Nama dalam huruf besar: {nama_upper}")
nama_lower = nama_lengkap.lower()
print(f"Nama dalam huruf kecil: {nama_lower}")
print("================================================\n")


print(f"--- 4. Operasi Matematika untuk Angka {angka1} dan {angka2} ---")
print(f"Penjumlahan (+): {angka1 + angka2}")
print(f"Pengurangan (-): {angka1 - angka2}")
print(f"Perkalian (*):   {angka1 * angka2}")
if angka2 != 0:
    print(f"Pembagian (/):     {angka1 / angka2}")
    print(f"Pembagian Bulat (//): {angka1 // angka2}")
    print(f"Sisa Bagi/Modulus (%): {angka1 % angka2}")
else:
    print("Operasi pembagian tidak dapat dilakukan karena angka kedua adalah 0.")
print("================================================\n")


print("--- 5. Manipulasi List Hobi ---")
print(f"List hobi awal Anda: {hobi}")

if len(hobi) > 0:
    print(f"Hobi pertama Anda (indeks 0) adalah: '{hobi[0]}'")
else:
    print("Anda tidak memasukkan hobi.")

print("\nMenambahkan 'Tidur' ke dalam list...")
hobi.append("Tidur")
print(f"List hobi setelah ditambah: {hobi}")

if len(hobi) > 1:
    print("\nMenghapus item terakhir dari list...")
    hobi_dihapus = hobi.pop()
    print(f"Item yang dihapus: '{hobi_dihapus}'")
    print(f"List hobi final: {hobi}")
print("================================================\n")


print("--- 6. Kalimat Perkenalan ---")
print(f"Halo, nama saya {nama_lengkap} dan umur saya {umur} tahun.")
print("\nProgram selesai.")