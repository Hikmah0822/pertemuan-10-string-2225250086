
# Fungsi untuk membersihkan dan menormalkan nama
def normalisasi_nama(nama):
    return nama.strip().title()


# Fungsi untuk membuat inisial mahasiswa
def buat_inisial(nama):
    kata = nama.split()
    inisial = ""

    for k in kata:
        inisial += k[0].upper()

    return inisial


# Fungsi untuk menormalkan kode kelas
def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)


# Input data mahasiswa
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Proses normalisasi
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama_bersih)

# Output hasil
print("\nHasil Normalisasi")
print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", jumlah_kata)
print("Inisial     :", inisial)
