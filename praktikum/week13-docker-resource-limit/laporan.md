
# Laporan Praktikum Minggu [13]
Topik: [Docker – Resource Limit (CPU & Memori)]

---

## Identitas
- **Nama**  : [azid mirza maulana]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan
1 Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2 Membangun image dan menjalankan container.
3 Menjalankan container dengan pembatasan CPU dan memori.
4 Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5 Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
1. Membuat Dockerfile sederhana untuk menjalankan aplikasi/skrip.
2. Menjalankan container dengan pembatasan resource (CPU dan memori).
3. Mengamati dampak pembatasan resource melalui output program dan monitoring sederhana.

---

## Langkah Praktikum
1. Persiapan Lingkungan [Pastikan Docker terpasang dan berjalan & Verifikasi]
2. Membuat Aplikasi/Skrip Uji
3. Membuat Dockerfile 
4. Menjalankan Container Tanpa Limit
5. Menjalankan Container Dengan Limit Resource
6. Monitoring Sederhana
7. Commit & Push

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
1. [Mengapa container perlu dibatasi CPU dan memori?]  
   **Jawaban:Container dibatasi untuk mencegah satu container mengonsumsi semua sumber daya host, yang bisa menyebabkan crash sistem atau starvation container lain. Cgroups di Linux kernel menegakkan batas ini.**  
2. [Apa perbedaan VM dan container dalam konteks isolasi resource?]  
   **Jawaban:VM isolasi penuh dengan hypervisor (guest OS terpisah, overhead tinggi), sementara container gunakan namespaces dan cgroups untuk isolasi proses ringan pada kernel host yang sama (efisien tapi kurang kuat secara hardware).**  
3. [Apa dampak limit memori terhadap aplikasi boros memori?]  
   **Jawaban:Aplikasi gagal alokasi (MemoryError/OOM kill), proses dihentikan kernel sebelum host kehabisan memori; tanpa limit, bisa crash seluruh host.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
