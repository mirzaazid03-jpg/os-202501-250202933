
# Laporan Praktikum Minggu [4]
Topik: [Manajemen Proses dan Pengguna di Linux]

---

## Identitas
- **Nama**  : [azid mirza maulana]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan 
Setelah menyelesaikan tugas ini, siswa mampu:

Menjelaskan konsep proses dan user dalam sistem operasi Linux.
Menampilkan daftar proses yang sedang berjalan dan statusnya.
Menggunakan perintah untuk membuat dan mengelola pengguna.
Menghentikan atau mengontrol proses tertentu menggunakan PID.
Menjelaskan hubungan antara manajemen pengguna dan keamanan sistem.  
> 

---

## Dasar Teori
Membuat dan mengatur proses (manajemen proses).
Mengelola pengguna, grup, serta hak akses pengguna.
Menampilkan, menghentikan, dan mengontrol proses yang sedang berjalan.
menerjemahkan konsep manajemen pengguna dengan keamanan sistem operasi.
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
whoami
id
groups
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-10-23%20152104.png)
![Screenshot hasil](./screenshots/Screenshot%202025-10-23%20152744.png)
![screenshot hasil](./screenshots/Screenshot%202025-10-23%20162632.png)
![screenshot hasil](./screenshots/Screenshot%202025-10-23%20192600.png)
![screenshot hasil](./screenshots/Screenshot%202025-10-23%20195051.png)
## Analisis
- 1. Perintah [whoami] dijalankan oleh pengguna "mirzaazid03".
Perintah [id] dijalankan yang menampilkan informasi pengguna sama.
Perintah [top] dijalankan untuk menampilkan proses-proses yang sedang berjalan dengan statistik penggunaan CPU, memori, dan proses secara rinci.
- 2. Perintah sleep 1000 & dijalankan untuk mengeksekusi sleep selama 1000 detik di background.
Perintah ps aux | grep sleep digunakan untuk melihat proses yang mengandung kata "sleep".
Dua proses "sleep infinity" milik root berjalan.
Proses "sleep 1000" milik pengguna mirzaazid03 dengan PID 1289 berjalan.
Proses grep untuk mencari sleep juga muncul di output.
Perintah kill 1289 dijalankan dengan benar dan proses sleep dengan PID 1289 berhasil dihentikan (terminated).
- 3. PID: Process ID, yaitu nomor unik yang diberikan sistem untuk setiap proses yang berjalan.
USER: Nama user (pengguna) yang menjalankan proses tersebut.
%CPU: Persentase penggunaan CPU oleh proses tersebut dibandingkan dengan seluruh total CPU yang tersedia.
%MEM: Persentase penggunaan memori fisik (RAM) oleh proses tersebut dibandingkan dengan total memori sistem.
COMMAND: Nama perintah atau executable yang dijalankan oleh proses tersebut.
- 4. 1. bash
 shell utama  (terminal mengetik perintah).
PID 1 menunjukkan bahwa proses root dari sesi Cloud Shell.
 2. dockerd dan containerd
dockerd(248) adalah daemon utama Docker — yang mengatur semua container.
containerd(281) adalah subproses yang menangani eksekusi container.
Baris {containerd}(293) dst adalah thread internal dari Docker.
 3. logger(26)
Ini adalah proses kecil yang bertugas untuk mencatat log sistem Cloud Shell (logging internal).
 4. python(25)
Menandakan bahwa ada proses Python yang sedang dijalankan oleh sistem.
 5. editor-proxy(283)
 adalah proses yang menjembatani antara Cloud Shell Editor (di browser) dan terminal back-end di server Google Cloud.
 6. runuser(504) → sh(506) → node(519)
Ini menunjukkan rantai proses:
runuser menjalankan sesi shell (sh) dengan user (mirzaazid03).
Dari sh(506) muncul proses node(519) — ini biasanya untuk Cloud Shell Editor, karena editor-nya berbasis Node.js.
node(1244) adalah child process tambahan dari Node.js utama, mungkin untuk menjalankan plugin atau service tambahan.
---

## Kesimpulan
Manajemen proses di Linux merupakan fungsi utama yang mengatur pembuatan, penjadwalan, eksekusi, dan memastikan proses secara efisien dan adil menggunakan algoritma seperti Completely Fair Scheduler (CFS).
manajemen pengguna di Linux mengatur hak akses dan tingkat hak istimewa pengguna, terutama melalui akun root yang memiliki hak istimewa penuh untuk mengelola sistem. Pengguna root dapat melakukan semua tindakan administratif tanpa batasan, sementara pengguna biasa dibatasi berdasarkan hak akses yang diberikan. 
---

## Quiz
1. [Apa fungsi dari proses init atau systemd dalam sistem Linux?]  
   **Jawaban:**  fungsi utama proses init atau systemd adalah:
1. Menjadi proses pertama yang dijalankan setelah kernel Linux selesai booting.
2. Menginisialisasi sistem dengan menjalankan skrip atau layanan sesuai runlevel atau target.
3. Mengelola proses-proses lain sebagai induk proses utama di sistem Linux.
4. menunjuk sistem mencapai keadaan yang dapat digunakan oleh pengguna dan aplikasi.
Fungsi ini sangat penting agar sistem Linux dapat berjalan dengan lancar sejak proses booting hingga shutdown.​


2. [Apa perbedaan antara killdan killall?]
   **Jawaban:** -Perintah kill bekerja dengan menargetkan satu proses berdasarkan nomor ID proses (PID) spesifik. Jadi, untuk menggunakan kill, harus mengetahui PID dari proses yang ingin dihentikan. Kill hanya akan menghentikan proses tertentu yang memiliki PID tersebut.
-perintah killall menargetkan semua proses yang memiliki nama proses tertentu. Dengan killall, dapat menghentikan sekaligus semua proses instance yang berjalan dengan nama yang sama tanpa harus mengetahui PID mereka satu per satu.
3. [Mengapa pengguna root memiliki hak istimewa di sistem Linux?]  
   **Jawaban:**  Pengguna root memiliki hak istimewa di sistem Linux karena akun root adalah akun superuser yang memiliki akses tertinggi dan tanpa batasan pada sistem. Hak istimewa ini memungkinkan pengguna root untuk melakukan segala tindakan administratif dan konfigurasi sistem yang tidak dapat dilakukan oleh pengguna biasa. Root dapat menginstal atau menghapus perangkat lunak, mengonfigurasi pengaturan sistem, mengelola akun pengguna lain, mengakses dan memodifikasi semua file, serta mengendalikan seluruh sistem operasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
