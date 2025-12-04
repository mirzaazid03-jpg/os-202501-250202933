
# Laporan Praktikum Minggu [5]
Topik: ["Penjadwalan CPU – FCFS dan SJF"]

---

## Identitas
- **Nama**  : Azid mirza maulana
- **NIM**   : 250202933
- **Kelas** : 1ikrb

---

## Tujuan
Setelah menyelesaikan tugas ini, siswa mampu:

Menghitung waktu tunggu dan waktu penyelesaian untuk algoritma FCFS dan SJF.
Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
Membandingkan kinerja FCFS dan SJF berdasarkan hasil analisis.
Menjelaskan kelebihan dan kekurangan masing-masing algoritma.
Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.

---

## Dasar Teori
1. Hitung waktu tunggu dan waktu penyelesaian dari minimal 2 skenario FCFS dan SJF.
2. Sajikan hasil perhitungan dalam tabel perhitungan (FCFS vs SJF).
3. Analisis kelebihan dan kelemahan tiap algoritma.

---

## Langkah Praktikum
1. Siapkan Data Proses.  
2.  Eksperimen 1 – FCFS (Siapa cepat dia dapat)
Urutkan proses berdasarkan Waktu Kedatangan .
Hitung nilai berikut untuk setiap proses:
Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
Turnaround Time (TAT) = WT + Burst Time
Hitung rata-rata Waiting Time dan Turnaround Time.
Buat Gantt Chart sederhana:
| P1 | P2 | P3 | P4 |
0    6    14   21   24
3.  Eksperimen 2 – SJF (Pekerjaan Terpendek Pertama)
Urutkan proses berdasarkan Burst Time terpendek (dengan memperhatikan waktu datang).

Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.

Bandingkan hasil FCFS dan SJF pada tabel berikut:

Algoritma	Rata-rata Waktu Tunggu	Rata-rata Waktu Penyelesaian	Kelebihan	Kekurangan
FCFS	...	...	Sederhana dan mudah diterapkan	Tidak efisien untuk proses yang panjang
SJF	...	...	Optimal untuk job pendek	Menyebabkan kelaparan pada pekerjaan yang panjang

4. Eksperimen 3 – Visualisasi Spreadsheet (Opsional)

Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
Kolom: Kedatangan, Meledak, Mulai, Menunggu, Berbalik, Selesai.
Gunakan rumus dasar penjumlahan/subtraksi.
Tangkapan layar hasil perhitungan dan penyimpanan di:
praktikum/week5-scheduling-fcfs-sjf/screenshots/

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
Turnaround Time (TAT) = WT + Burst Time
| P1 | P2 | P3 | P4 |
0    6    14   21   24
praktikum/week5-scheduling-fcfs-sjf/screenshots/
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-11-06%20233701.png)
![screenshot hasil](./screenshots/Screenshot%202025-11-06%20234919.png)

---

## Analisis
- SJF lebih unggul ketika proses-proses memiliki variasi waktu eksekusi yang besar, karena memberi prioritas pada pekerjaan singkat → menurunkan rata-rata waktu tunggu.

- FCFS lebih unggul dalam lingkungan yang stabil dan adil, karena tidak menimbulkan starvation (semua proses dilayani sesuai urutan kedatangan). 

---

## Kesimpulan
SJF menghasilkan waktu tunggu dan waktu penyelesaian rata-rata yang lebih kecil dibanding FCFS, sehingga lebih efisien untuk beban kerja campuran. Namun, FCFS tetap relevan untuk sistem yang menuntut keadilan dan kesederhanaan.

---

## Quiz
1. [Apa perbedaan utama antara FCFS dan SJF]
   **Jawaban:**  FCFS menekankan urutan kedatangan (sederhana tapi tidak efisien).
SJF menekankan waktu eksekusi terpendek (lebih efisien tapi kurang adil untuk proses besar).
Perbedaan utama antara FCFS (First Come, First Served) dan SJF (Shortest Job First) terletak pada cara sistem operasi menentukan urutan eksekusi proses di CPU.
2. [Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum]  
   **Jawaban:**  SJF menghasilkan rata-rata waktu tunggu minimum karena setiap proses pendek diselesaikan lebih awal, sehingga total waktu menunggu semua proses menjadi paling kecil secara keseluruhan.
3. [Apa kelemahan SJF jika diterapkan pada sistem interaktif]  
   **Jawaban:**1.  Sulit mengetahui burst time sebelumnya.	SJF membutuhkan informasi tentang lama waktu eksekusi tiap proses (CPU burst) untuk menentukan siapa yang terpendek. Di sistem interaktif, waktu eksekusi sulit diprediksi karena tiap pengguna memberikan input berbeda-beda dan tidak teratur.
2. Bisa menyebabkan starvation (kelaparan proses).	Proses panjang mungkin tidak pernah dijalankan kalau selalu ada proses pendek baru yang datang.
 Dalam sistem interaktif, ini sangat buruk karena proses pengguna tertentu bisa menunggu tanpa batas waktu.
3. Tidak cocok untuk sistem real-time atau respons cepat.	Sistem interaktif butuh respon cepat untuk semua pengguna, bukan hanya proses pendek. SJF bisa memperlambat respon bagi pengguna dengan proses sedikit lebih panjang.
4. Kurang adil (unfair scheduling).	Pengguna dengan proses besar selalu kalah prioritas terhadap proses pendek. Dalam sistem interaktif, ini menyebabkan pengalaman pengguna tidak seimbang.
5. Overhead perhitungan estimasi burst time.	Untuk menerapkan SJF dalam sistem nyata, OS harus mengestimasi burst time tiap proses menggunakan rumus atau rekaman eksekusi sebelumnya.
 Ini menambah kompleksitas dan beban sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
bagian paling menantang dalam praktikum minggu ke 5 ini adalah belum mengetahui tenteng pengoprasian exel/spreedset. 
- Bagaimana cara Anda mengatasinya?  
dengan mencari tutorial pembelajaarn/pengerjaan untuk mengoprasikan exel

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
