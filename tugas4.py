import time

print("### Sistem Manajemen Perpustakaan Mini ###\n")

INFO_PERPUSTAKAAN = ('Perpustakaan Cerdas', 'Surabaya', 2020, 'ID-SUB-01')
nama_perpus, kota, _, kode_cabang = INFO_PERPUSTAKAAN 
print(f"Selamat datang di {nama_perpus} ({kode_cabang}) di kota {kota}!")

pustakawan = {
    'nama': 'Andi Wijaya',
    'id': 'P001',
    'status': 'Aktif'
}
print(f"Pustakawan bertugas: {pustakawan['nama']} (ID: {pustakawan['id']})")

inventaris_buku = [
    {'id': 'BK001', 'judul': 'Laskar Pelangi', 'penulis': 'Andrea Hirata', 'tahun': 2005, 'tags': {'fiksi', 'inspiratif', 'novel'}},
    {'id': 'BK002', 'judul': 'Bumi Manusia', 'penulis': 'Pramoedya Ananta Toer', 'tahun': 1980, 'tags': {'fiksi', 'sejarah', 'klasik'}},
    {'id': 'BK003', 'judul': 'Cantik Itu Luka', 'penulis': 'Eka Kurniawan', 'tahun': 2002, 'tags': {'fiksi', 'magical realism', 'sejarah'}},
    {'id': 'BK004', 'judul': 'Filosofi Teras', 'penulis': 'Henry Manampiring', 'tahun': 2018, 'tags': {'non-fiksi', 'filsafat', 'self-help'}},
    {'id': 'BK005', 'judul': 'Sapiens', 'penulis': 'Yuval Noah Harari', 'tahun': 2011, 'tags': {'non-fiksi', 'sejarah', 'sains'}},
    {'id': 'BK006', 'judul': 'Gadis Kretek', 'penulis': 'Ratih Kumala', 'tahun': 2012, 'tags': {'fiksi', 'sejarah', 'romance'}},
]

print(f"\nJumlah buku saat ini: {len(inventaris_buku)} judul.")
print("-" * 40)
time.sleep(1) 


print("\n### Proses Pembaruan Inventaris Buku ###\n")
print(f"Inventaris sebelum pembaruan: {[b['judul'] for b in inventaris_buku]}")

buku_baru = {'id': 'BK007', 'judul': 'Laut Bercerita', 'penulis': 'Leila S. Chudori', 'tahun': 2017, 'tags': {'fiksi', 'sejarah', 'politik'}}
inventaris_buku.append(buku_baru)
print(f"\n[APPEND] Buku '{buku_baru['judul']}' telah ditambahkan.")

buku_donasi = [
    {'id': 'BK008', 'judul': 'Atomic Habits', 'penulis': 'James Clear', 'tahun': 2018, 'tags': {'non-fiksi', 'self-help'}},
]
inventaris_buku.extend(buku_donasi)
print(f"[EXTEND] {len(buku_donasi)} buku donasi telah ditambahkan.")

buku_diperbaiki = inventaris_buku.pop()
print(f"[POP] Buku '{buku_diperbaiki['judul']}' diambil untuk diperbaiki.")

buku_hilang = next((buku for buku in inventaris_buku if buku['id'] == 'BK002'), None)
if buku_hilang:
    inventaris_buku.remove(buku_hilang)
    print(f"[REMOVE] Buku '{buku_hilang['judul']}' dihapus dari data karena hilang.")

print(f"\nInventaris setelah pembaruan: {[b['judul'] for b in inventaris_buku]}")
print(f"Total buku sekarang: {len(inventaris_buku)} judul.")
print("-" * 40)
time.sleep(1)


print("\n### Analisis Genre Antar Buku ###\n")
buku_a = inventaris_buku[0] 
buku_b = inventaris_buku[4] 

print(f"Membandingkan genre '{buku_a['judul']}' dengan '{buku_b['judul']}'...")
print(f"Genre '{buku_a['judul']}': {buku_a['tags']}")
print(f"Genre '{buku_b['judul']}': {buku_b['tags']}")

genre_sama = buku_a['tags'].intersection(buku_b['tags'])
semua_genre = buku_a['tags'].union(buku_b['tags'])
genre_unik_a = buku_a['tags'].difference(buku_b['tags'])
genre_eksklusif = buku_a['tags'].symmetric_difference(buku_b['tags'])

print(f"\nIntersection (Genre yang sama): {genre_sama or 'Tidak ada'}")
print(f"Union (Semua genre gabungan): {semua_genre}")
print(f"Difference (Genre unik di '{buku_a['judul']}'): {genre_unik_a}")
print(f"Symmetric Difference (Genre yang tidak beririsan): {genre_eksklusif}")
print("-" * 40)
time.sleep(1)

print("\n### Pembuatan Laporan ###\n")

buku_modern = [
    f"{buku['judul']} ({buku['tahun']})"
    for buku in inventaris_buku if buku['tahun'] >= 2010
]
print("Laporan 1: Buku Terbit >= 2010")
for item in buku_modern:
    print(f"  - {item}")

peta_id_judul = {buku['id']: buku['judul'] for buku in inventaris_buku}
print("\nLaporan 2: Peta ID -> Judul Buku")
print(peta_id_judul)

penulis_unik = {buku['penulis'] for buku in inventaris_buku}
print("\nLaporan 3: Daftar Penulis Unik di Perpustakaan")
print(penulis_unik)
print("-" * 40)
time.sleep(1)


print("\n### Fitur Pencarian Buku ###\n")
judul_dicari = 'Filosofi Teras'

buku_ditemukan = None
for buku in inventaris_buku:
    if judul_dicari.lower() in buku['judul'].lower():
        buku_ditemukan = buku
        break

if buku_ditemukan:
    posisi = inventaris_buku.index(buku_ditemukan)
    print(f"Hasil: Buku '{judul_dicari}' DITEMUKAN!")
    print(f"   - Penulis: {buku_ditemukan['penulis']}")
    print(f"   - Lokasi di rak (indeks): {posisi}")
else:
    print(f"Hasil: Buku '{judul_dicari}' TIDAK DITEMUKAN di inventaris.")

print("\n--- Selesai ---")