
# Laporan Praktikum Minggu [14]
Topik: [Penyusunan Laporan Praktikum Format IMRAD]

---

## Identitas
- **Nama**  : [azid mirza maulana]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan
1. Menyusun laporan praktikum dengan struktur ilmiah (Pendahuluan–Metode–Hasil–Pembahasan–Kesimpulan).
2. Menyajikan hasil uji dalam bentuk tabel dan/atau grafik yang jelas.
3. Menuliskan analisis hasil dengan argumentasi yang logis.
4. Menyusun sitasi dan daftar pustaka dengan format yang konsisten.
5. Mengunggah draft laporan ke repositori dengan rapi dan tepat waktu.

---

## Dasar Teori
Laporan IMRAD digunakan untuk merangkum praktikum-praktikum sebelumnya (mis. scheduling, page replacement, deadlock detection, VM/Docker) agar hasil uji dapat dipahami, direplikasi, dan dievaluasi secara akademik.


---

## Langkah Praktikum
1. Menentukan Topik Laporan.  
2. Menyiapkan Bahan
3. Menulis Laporan dengan Struktur IMRAD
4. Menyajikan Tabel/Grafik
5. Sitasi dan Daftar Pustaka
6. Commit & Push Draft

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
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?]    
   **Jawaban:**  Format IMRAD membuat laporan praktikum lebih ilmiah karena memandu penulis menyusun konten secara sistematis: mulai dari latar belakang (Introduction), prosedur (Methods), data mentah (Results), hingga analisis (Discussion). Struktur ini memudahkan evaluator menilai kelengkapan, objektivitas, dan alur logika tanpa membaca ulang secara acak
2. [Apa perbedaan antara bagian Hasil dan Pembahasan?]  
   **Jawaban:**  Bagian Hasil hanya menyajikan data objektif seperti tabel waktu CPU test (5.2s tanpa limit vs 28.4s dengan limit) atau screenshot docker stats, tanpa interpretasi.
Bagian Pembahasan menganalisis mengapa hasil tersebut terjadi, misalnya CPU melambat karena cgroups membatasi shares ke 0.5 core, dan memori gagal akibat OOM killer
3. [Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?]  
   **Jawaban:**  Sitasi membuktikan klaim berbasis bukti eksternal, seperti "cgroups menegakkan limit Docker", sehingga laporan praktikum terlihat kredibel meski sederhana. Daftar pustaka memungkinkan verifikasi dan menghindari plagiarisme, bahkan untuk tugas mahasiswa, karena membangun tradisi ilmiah. Tanpa ini, laporan hanya catatan pribadi, bukan dokumen akademis.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
