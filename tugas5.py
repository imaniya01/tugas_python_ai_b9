def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    hasil = sum(angka) / len(angka)
    return round(hasil, 2)

class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        if nilai is None:
            self.nilai = []
        else:
            self.nilai = nilai

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

if __name__ == "__main__":
    
    print(" FUNCTIONS ")
    print(greet("Arifian"))
    print(f"tambah(5, 7) = {tambah(5, 7)}")
    print(f"tambah(10) = {tambah(10)}")
    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([]) = {rata_rata([])}")
    
    print("\n CLASS STUDENT ")
    
    mahasiswa1 = Student(nama="Budi", nim="A123")
    mahasiswa1.tambah_nilai(85.5)
    mahasiswa1.tambah_nilai(90)
    mahasiswa1.tambah_nilai(78)

    mahasiswa2 = Student(nama="Siti", nim="B456")
    mahasiswa2.tambah_nilai(60)
    mahasiswa2.tambah_nilai(65)
    mahasiswa2.tambah_nilai(70)

    daftar_mahasiswa = [mahasiswa1, mahasiswa2]
    
    for i, mhs in enumerate(daftar_mahasiswa, start=1):
        rata_nilai_str = str(mhs.rata_nilai()).replace('.', ',')
        
        print(f"no.{i}")
        print(f"Nama : {mhs.nama}")
        print(f"NIM : {mhs.nim}")
        print(f"Rata-rata : {rata_nilai_str}")
        print(f"Status: {mhs.status()}")
        
        
        if i < len(daftar_mahasiswa):
            print() 
