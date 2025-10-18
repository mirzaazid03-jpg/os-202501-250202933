
# Laporan Praktikum Minggu [3]
Topik: ["Manajemen File dan Permission di Linux"]

---

## Identitas
- **Nama**  : [azid mirzamaulana] 
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan
tujuan praktikum minggu ini.  
mahasiswa mampu:
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
1. Pengantar Sistem Berkas Linux
Sistem operasi Linux memiliki sistem berkas (file system) yang digunakan untuk mengatur, menyimpan, dan mengelola data pada perangkat penyimpanan. Setiap objek di Linux—baik itu file, direktori, atau perangkat—dianggap sebagai file.
2. Konsep Dasar Izin File (File Permissions)
Setiap file di Linux memiliki tiga jenis izin utama:

Read (r) : Mengizinkan membaca isi file. Pada direktori, izin ini memungkinkan melihat daftar isi direktori.

Write (w) : Mengizinkan mengubah isi file. Pada direktori, izin ini memungkinkan menambah, menghapus, atau mengganti nama file di dalamnya.

Execute (x) : Mengizinkan menjalankan file sebagai program. Pada direktori, izin ini mengizinkan pengguna untuk masuk (cd) ke direktori tersebut.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-10-15%20204523.png)
Perintah ls -l  digunakan untuk menampilkan daftar file dan direktori dalam format panjang (long listing format).
![screenshot hasil](./screenshots/Screenshot%202025-10-16%20002111.png)
contoh tex -rw-r--r-- 1 azid staff  1240 Oct 15 09:10 laporan.txt
-rwxr-xr-- 1 azid staff  2048 Oct 15 09:00 program.sh
drwxr-xr-x 2 azid staff  4096 Oct 14 17:20 Documents
drwxrwxr-x 3 azid staff  4096 Oct 14 17:25 Downloads
-rw-rw-r-- 1 azid staff   980 Oct 13 20:45 data.csv
drwxr-xr-t 5 azid staff  4096 Oct 13 21:00 /tmp
![screenshot hasil](./screenshots/Screenshot%202025-10-16%20002857.png)
# Membuat file baru
$ touch script.sh

# Melihat izin awal file
$ ls -l script.sh
-rw-r--r-- 1 azid staff 0 Oct 15 10:00 script.sh

# Memberikan izin eksekusi kepada pemilik
$ chmod u+x script.sh

# Cek lagi izin file
$ ls -l script.sh
-rwxr--r-- 1 azid staff 0 Oct 15 10:01 script.sh

# Menambahkan izin tulis untuk grup
$ chmod g+w script.sh

# Cek hasilnya
$ ls -l script.sh
-rwxrw-r-- 1 azid staff 0 Oct 15 10:02 script.sh

# Menghapus izin baca untuk others
$ chmod o-r script.sh

# Hasil akhir
$ ls -l script.sh
-rwxrw---- 1 azid staff 0 Oct 15 10:03 script.sh
- 

---

## Kesimpulan
Manajemen File dan Permission di Linux
1. Pengantar Manajemen File di Linux

Sistem operasi Linux merupakan sistem berbasis multiuser dan multitasking, artinya banyak pengguna dapat mengakses sistem secara bersamaan tanpa saling mengganggu. Karena itu, pengelolaan file (file management) menjadi aspek yang sangat penting agar data setiap pengguna tetap aman dan terorganisasi.

Manajemen file di Linux mencakup segala proses yang berkaitan dengan pembuatan, penyimpanan, pengaturan, penghapusan, serta pemberian hak akses terhadap file dan direktori. Dalam Linux, semua hal dianggap sebagai file, termasuk perangkat keras seperti disk, printer, bahkan proses sistem.

Struktur penyimpanan file di Linux bersifat hierarkis, dimulai dari direktori akar (/) sebagai level tertinggi. Dari root tersebut, terdapat banyak subdirektori seperti /home, /etc, /bin, /usr, dan sebagainya. Misalnya, direktori /home digunakan untuk menyimpan data pengguna, sementara /etc berisi file konfigurasi sistem.

2. Sistem Hak Akses (Permission)

Agar keamanan sistem tetap terjaga, Linux menggunakan sistem permission untuk mengatur siapa yang dapat membaca, menulis, atau menjalankan suatu file. Setiap file atau direktori memiliki tiga jenis hak akses utama:

Read (r) → memberi izin membaca isi file atau melihat daftar isi direktori.

Write (w) → memberi izin mengubah isi file atau menambah/menghapus file dalam direktori.

Execute (x) → memberi izin menjalankan file sebagai program atau script.

Selain itu, Linux membagi pengguna menjadi tiga kategori:

User (u) → pemilik file.

Group (g) → kelompok pengguna yang memiliki hak tertentu.

Others (o) → pengguna lain di luar pemilik dan grup.

Contoh permission:

-rwxr-xr--


Penjelasan:

Karakter pertama - menunjukkan jenis file (file biasa).

Tiga karakter pertama rwx → hak akses pemilik (user).

Tiga karakter berikut r-x → hak akses grup.

Tiga karakter terakhir r-- → hak akses untuk others.

Artinya, pemilik dapat membaca, menulis, dan menjalankan file; grup hanya dapat membaca dan menjalankan; sementara pengguna lain hanya dapat membaca.

3. Perintah Dasar Manajemen File

Linux menyediakan banyak perintah untuk mengelola file. Beberapa perintah dasar yang sering digunakan adalah:

ls → menampilkan daftar file.

cp → menyalin file atau direktori.

mv → memindahkan atau mengganti nama file.

rm → menghapus file.

mkdir → membuat direktori baru.

rmdir → menghapus direktori kosong.

touch → membuat file baru kosong.

Contoh:

mkdir tugas
cd tugas
touch laporan.txt
ls -l


Perintah di atas membuat direktori bernama tugas, masuk ke dalamnya, membuat file baru bernama laporan.txt, lalu menampilkan daftar file dengan format panjang.

4. Mengatur Permission dengan chmod

Perintah chmod (change mode) digunakan untuk mengubah hak akses file atau direktori.
Ada dua cara penulisan dalam chmod:

Simbolik

chmod u+x file.sh
chmod g-w file.txt
chmod o=r file.txt


Penjelasan:

u+x → menambahkan izin eksekusi untuk user.

g-w → menghapus izin tulis untuk grup.

o=r → memberikan izin baca untuk others.

Numerik (Oktal)
Masing-masing izin memiliki nilai:

r = 4

w = 2

x = 1

Jadi, kombinasi rwx bernilai 7 (4+2+1).
Contoh:

chmod 755 file.sh


Artinya:

User: 7 → rwx

Group: 5 → r-x

Others: 5 → r-x

5. Mengatur Kepemilikan File dengan chown dan chgrp

Selain chmod, Linux juga memiliki perintah:

chown → mengubah pemilik file.

chgrp → mengubah grup file.

Contoh:

chown azid script.sh
chgrp staff script.sh


Perintah di atas menjadikan pengguna azid sebagai pemilik file, dan grup staff sebagai grup pemiliknya.

6. Pentingnya Manajemen File dan Permission

Manajemen file dan permission di Linux berfungsi menjaga:

Keamanan data → hanya pengguna yang berhak dapat mengakses file tertentu.

Kestabilan sistem → mencegah modifikasi tidak sah terhadap file sistem.

Kolaborasi antar pengguna → dengan sistem grup, beberapa pengguna bisa bekerja bersama dengan hak akses yang sesuai.

Selain itu, administrator sistem (root) memiliki kendali penuh terhadap semua file dan dapat menyesuaikan izin untuk kebutuhan keamanan atau konfigurasi server.

---

## Quiz
1. [Apa fungsi dari perintah chmod?]  
   **Fungsi utama chmod adalah:

Mengatur atau mengubah izin akses (read, write, execute) pada file atau direktori untuk user, group, dan others di sistem Linux.

Dengan chmod, administrator atau pemilik file dapat mengontrol keamanan sistem dan mencegah akses tidak sah terhadap file.**  
2. [Apa arti dari kode permission rwxr-xr--?]
   **rwx	user (pemilik)	Pemilik file dapat membaca, menulis, dan menjalankan file.
r-x	group	Anggota grup hanya dapat membaca dan menjalankan, tetapi tidak bisa menulis/mengubah file.
r--	others	Pengguna lain hanya bisa membaca file. Tidak dapat menulis atau mengeksekusi.**  
3. [Jelaskan perbedaan antara chown dan chmod.]  
   **🔹 chmod (Change Mode)

 Mengubah izin (permissions) dari sebuah file atau direktori.

Dengan chmod, bisa menentukan siapa yang bisa membaca (read), menulis (write), atau menjalankan (execute) file.

Fokusnya pada hak akses.

🔹 chown (Change Owner)

yaitu Mengubah kepemilikan (ownership) dari file atau direktori.

Dengan chown,bisa menentukan siapa pemilik (user) dan grup (group) dari file tersebut.

Fokusnya pada siapa yang memiliki file, bukan apa yang boleh dilakukan terhadap file itu.**  

 chmod = mengatur “apa yang boleh dilakukan terhadap file”.
 chown = mengatur “siapa yang memiliki file”.

## Refleksi Diri
Tuliskan secara singkat:
- cukup menguji mental pikiran 
- memperdalam materi dari sumber manapun

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
