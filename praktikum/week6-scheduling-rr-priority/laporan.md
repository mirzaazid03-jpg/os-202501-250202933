
# Laporan Praktikum Minggu [6]
Topik: ["Penjadwalan CPU – Round Robin (RR) dan Penjadwalan Prioritas"]

---

## Identitas
- **Nama**  : [azid mirza maulana]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan
Setelah menyelesaikan tugas ini, siswa mampu:

Menghitung waktu tunggu dan waktu penyelesaian pada algoritma RR dan Prioritas.
Menyusun tabel hasil perhitungan dengan benar dan sistematis.
Membandingkan performa algoritma RR dan Prioritas.
Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan proses eksekusi.
Kesimpulan menarik mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
Hitung waktu tunggu dan waktu penyelesaian untuk algoritma RR dan Prioritas.
Sajikan hasil perhitungan dan Gantt Chart.
Bandingkan kinerja dan jelaskan pengaruh waktu kuantum serta prioritas.

---

## Langkah Praktikum
1. Siapkan Data Proses
2. Eksperimen 1 – Round Robin (RR)

Gunakan waktu kuantum (q) = 3.
Hitung waktu tunggu dan waktu penyelesaian untuk setiap proses.
Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).
| P1 | P2 | P3 | P4 | P1 | P3 | ...
0    3    6    9   12   15   18  ...
Catat sisa waktu burst tiap putaran.
3. enjadwalan Prioritas (Non-Preemptive)

Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
Lakukan perhitungan manual untuk:
WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]
Buat tabel perbandingan hasil RR dan Prioritas.
4. Analisis Variasi Waktu Quantum (Opsional)

Ubah quantum menjadi 2 dan 5.
Amati perubahan nilai rata-rata waktu tunggu dan waktu penyelesaian .
Buat tabel perbandingan efek kuantum .

---


## Hasil Eksekusi
![screenshot hasil](./screenshots/Screenshot%202025-11-13%20161623.png)
experimen 1 perhitungan round robin(RR)
```
| P1 | P2 | P3 | P4 | P1 | P3 | ...
0    3    6    9   12   15   18  ...
```

![screenshot hasil](./screenshots/Screenshot%202025-11-13%20162006.png)
Eksperimen 2 penjadwalan prioritas

WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]

![screenshot hasil](./screenshots/Screenshot%202025-11-13%20163747.png)

---

## Analisis
- RR adil tapi tergantung quantum Round Robin memberikan waktu CPU bergantian ke semua proses. Jika quantum terlalu kecil, sering ganti proses jadi lambat. Kalau terlalu besar, mirip antrian biasa.
Priority lebih cepat proses penting Proses dengan prioritas tinggi jalan dulu, bikin proses penting cepat selesai. Tapi proses prioritas rendah bisa kelamaan nunggu (starvation).
Quantum pengaruh besar di RR Quantum kecil bikin proses sering berhenti-berhenti, jadi lama. Quantum besar bikin proses cepat selesai tapi bisa kurang responsif.
Priority lebih efisien, RR lebih adil Priority lebih cepat secara rata-rata, cocok buat tugas penting. RR lebih cocok buat sistem yang butuh keadilan semua proses.
Kesimpulan: pilih sesuai kebutuhan Pakai RR kalau ingin semua proses dapat giliran. Pakai Priority kalau ada proses yang harus didahulukan, tapi perlu cara supaya proses kecil tidak kelamaan menunggu.


---

## Kesimpulan
Round Robin unggul dalam keadilan dan respons cepat, cocok untuk sistem multi-user.
Sedangkan Penjadwalan Prioritas lebih efisien dan cocok untuk sistem dengan tingkat kepentingan berbeda, namun perlu mekanisme aging agar proses prioritas rendah tidak diabaikan.

---

## Quiz
1. [Apa perbedaan utama antara Round Robin dan Penjadwalan Prioritas?]  
   **Jawaban:**  Round Robin menjalankan proses secara berurutan dengan waktu eksekusi terbatas (time quantum) yang sama untuk setiap proses tanpa memperhatikan prioritas proses. Algoritma ini bertujuan memberikan keadilan dan mencegah kelaparan karena semua proses mendapat jatah waktu yang sama secara bergilir.
   Penjadwalan Prioritas menjalankan proses berdasarkan tingkat prioritas yang diberikan ke setiap proses. Proses dengan prioritas lebih tinggi eksekusi terlebih dahulu. Prioritas dapat bersifat internal (ditentukan oleh sistem) atau eksternal (berdasarkan kebutuhan waktu, pembayaran, atau pentingnya proses).
2. [Apa pengaruh besar/kecilnya waktu kuantum terhadap kinerja sistem?]  
   **Jawaban:** 
   -   Waktu penempatan yang terlalu kecil menyebabkan pergantian frekuensi konteks (context switching) yang sangat sering.
  -  Waktu penempatan yang terlalu besar membuat satu proses dapat mendominasi CPU untuk waktu yang lama, sehingga proses lain harus menunggu lebih lama.
- Dengan penempatan waktu yang optimal, Round Robin dapat mencapai keseimbangan antara efisiensi CPU dan keadilan dalam pembagian waktu eksekusi antar proses. 
3. [Mengapa algoritma Prioritas dapat menyebabkan kelaparan ?]  
   **Jawaban:**  karena proses dengan prioritas rendah bisa terus-menerus tertunda tanpa eksekusi jika terus ada proses dengan prioritas lebih tinggi yang datang atau memonopoli sumber daya.
   Hal ini terjadi karena dalam penjadwalan berbasis prioritas, sistem selalu memilih proses dengan prioritas tertinggi yang siap dieksekusi, sehingga proses berprioritas rendah jarang atau bahkan tidak pernah mendapat kesempatan untuk berjalan.

---

## Refleksi Diri
Tuliskan secara singkat:
- masih bingung dengan cara menghitung RR dan rumus/cara menghitungnya di exel

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
