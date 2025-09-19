import numpy as np
import pandas as pd
import os
np.random.seed(42)

if __name__ == "__main__":
    
    print("="*5, " NUMPY ", "="*5)

    nilai_ujian = np.random.randint(50, 101, size=10)
    
    rata_rata = np.mean(nilai_ujian)
    median = np.median(nilai_ujian)
    standar_deviasi = np.std(nilai_ujian)
    nilai_min = np.min(nilai_ujian)
    nilai_max = np.max(nilai_ujian)

    print(f"Data Nilai: {nilai_ujian}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Median: {median}")
    print(f"Standar Deviasi: {standar_deviasi:.2f}")
    print(f"Nilai Minimal: {nilai_min}")
    print(f"Nilai Maksimal: {nilai_max}\n")

    print("="*5, " PANDAS ", "="*5)

    data = {
        'nama': [f'Mahasiswa_{i+1}' for i in range(10)],
        'nim': [f'202511{i:03d}' for i in range(10)],
        'nilai': nilai_ujian
    }
    df = pd.DataFrame(data)

    df['status'] = np.where(df['nilai'] >= 70, "LULUS", "TIDAK LULUS")

    print("Tampilan 5 baris pertama DataFrame:")
    print(df.head())
    print("\n")

    nama_file = "ringkasan_tugas.txt"
    
    with open(nama_file, 'w') as f:
        f.write("=== Ringkasan Statistik NumPy ===\n")
        f.write(f"Rata-rata: {rata_rata:.2f}\n")
        f.write(f"Median: {median}\n")
        f.write(f"Standar Deviasi: {standar_deviasi:.2f}\n")
        f.write(f"Nilai Minimal: {nilai_min}\n")
        f.write(f"Nilai Maksimal: {nilai_max}\n\n")
        
        f.write("=== Ringkasan DataFrame Pandas ===\n")
        f.write(f"Jumlah Total Data: {len(df)} baris\n")
        status_counts = df['status'].value_counts()
        f.write(f"Jumlah Lulus: {status_counts.get('LULUS', 0)}\n")
        f.write(f"Jumlah Tidak Lulus: {status_counts.get('TIDAK LULUS', 0)}\n")

    print(f"File '{nama_file}' berhasil dibuat dengan ringkasan awal.\n")

    class GradeBook:
        def __init__(self, df: pd.DataFrame):
            self.df = df

        def average(self) -> float:
            return self.df['nilai'].mean()

        def pass_rate(self, threshold: float = 70.0) -> float:
            lulus_count = (self.df['nilai'] >= threshold).sum()
            total_count = len(self.df)
            return (lulus_count / total_count) * 100 if total_count > 0 else 0.0

        def save_summary(self, path: str):
            with open(path, 'a') as f: 
                f.write("\n=== Ringkasan dari Objek GradeBook ===\n")
                f.write(str(self)) 
                f.write(f"Tingkat Kelulusan: {self.pass_rate():.2f}%\n")

        def __str__(self) -> str:
            return (f"GradeBook berisi {len(self.df)} data mahasiswa.\n"
                    f"Rata-rata nilai keseluruhan: {self.average():.2f}")

    print("="*10, " OOP: GRADEBOOK ", "="*10)

    gradebook_obj = GradeBook(df)

    print(gradebook_obj)  
    
    print(f"Rata-rata dari method: {gradebook_obj.average():.2f}")
    print(f"Tingkat kelulusan dari method: {gradebook_obj.pass_rate():.2f}%")

    gradebook_obj.save_summary(nama_file)
    print(f"Ringkasan dari GradeBook telah ditambahkan ke '{nama_file}'.")