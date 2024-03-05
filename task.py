class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

# Membuat objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Putri Suri Anjani", "A 2021", "Pendidikan Komputer", "FKIP", "Pramuka", "Kalimantan Timur")

# Menampilkan nilai atribut objek
print("Nilai atribut mahasiswa1:")
print("Nama:", mahasiswa1.nama)
print("Kelas:", mahasiswa1.kelas)
print("Prodi:", mahasiswa1.prodi)
print("Fakultas:", mahasiswa1.fakultas)
print("Tempat Tinggal:", mahasiswa1.tempat_tinggal)
print("Asal:", mahasiswa1.asal)


