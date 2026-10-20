
# Pertemuan 10 - String dan Pengolahan Teks

Nama: Hikmah Azizah

NIM: 2225250086

Kelas: 3B

## Tujuan
Mengolah dan menormalisasi data teks menggunakan string
Python, seperti strip(), title(), upper(), split(), dan join().

## Cara Menjalankan
Jalankan setiap latihan menggunakan terminal VS Code.

Contoh:
python latihan/01_dasar_string.py

Untuk tugas normalisasi:
python tugas/normalisasi_data_mahasiswa.py

## Algoritma
1. Menerima input nama dan kode kelas.
2. Menghapus spasi berlebih pada nama dan mengubahnya
   menjadi title case.
3. Memisahkan nama menjadi beberapa kata.
4. Membuat inisial dari huruf pertama setiap kata.
5. Mengubah kode kelas menjadi huruf besar dan mengganti
   pemisah spasi dengan tanda hubung.
6. Menghitung jumlah kata dan menampilkan hasilnya.

## Test Case

| Input Nama | Input Kode | Hasil Inisial | Status |
|---|---|---|---|
| aan hendrayana | pmat a 2026 | AH | Lulus |
| fATHIYYAH mUTHMAINNAH | kelas b | FM | Lulus |
| BUDI | pmtk 01 | B | Lulus |
| siti nur aisyah | kelas c | SNA | Lulus |

Catatan: Status diisi setelah program benar-benar diuji.

## Refleksi
Saya belajar menggunakan method string untuk membersihkan
dan menormalkan teks. Salah satu masalah yang ditemukan
adalah spasi berlebih. Masalah tersebut diperbaiki dengan
menggunakan strip(), split(), dan join().

## Sumber
Materi Algoritma dan Pemrograman Pertemuan 10.
Bantuan: dokumentasi resmi Python tentang tipe data string.
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
