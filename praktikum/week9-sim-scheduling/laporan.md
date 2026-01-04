
# Laporan Praktikum Minggu [9]
Topik: ["Simulasi Algoritma Penjadwalan CPU"]

---

## Identitas
- **Nama**  : [Azid mirza maulan]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
>1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.


---

## Dasar Teori
Bagaimana cara mengimplementasikan algoritma FCFS dan SJF dalam bentuk program?

Bagaimana hasil simulasi dibandingkan dengan perhitungan manual?

Apa kelebihan dan keterbatasan simulasi penjadwalan CPU?
---

## Langkah Praktikum
1. Menyiapkan Dataset

Buat dataset proses minimal berisi:

Proses	Arrival Time	Burst Time
P1	0	6
P2	1	8
P3	2	7
P4	3	3

Implementasi Algoritma

Program harus:

- Menghitung waiting time dan turnaround time.
Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
Menampilkan hasil dalam tabel.
Eksekusi & Validasi

- Jalankan program menggunakan dataset uji.
Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.
Simpan hasil eksekusi (screenshot).
Analisis

- Jelaskan alur program.
Bandingkan hasil simulasi dengan perhitungan manual.
Jelaskan kelebihan dan keterbatasan simulasi.
Commit & Push

- git add .
git commit -m "Minggu 9 - Simulasi Scheduling CPU"
git push origin main

---

---

## Hasil Eksekusi
hail simulasi algoritma FCFS
![Screenshot hasil](./screenshots/Screenshot%202026-01-01%20204156.png)

---

## Analisis
- Hasil simulasi dengan perhitungan dengan program seperti ini lebih effisien dan minim kesalahan dalam perhitungan.

---

## Kesimpulan
- lebih Cepat
- lebih akurat
- Bisa untuk dataset besar atau dengan jumlah Proses yang lebih banyak

**Kekurangan simulasi ini**

- Tidak bisa berjalan secara real-time
Belum mendukung preemtive scheduling

---

## Quiz
1. [Mengapa simulasi diperlukan untuk menguji algoritma scheduling?]  
   **Simulasi memungkinkan pengujian algoritma secara cepat, akurat, dan konsisten terutama untuk dataset besar.**  
2. [Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?]  
   **Perhitungan manual lebih rentan kesalahan dan memakan waktu, sedangkan simulasi bersifat otomatis.**  
3. [Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.]  
   **FCFS lebih mudah karena hanya bergantung pada urutan waktu kedatangan proses.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
