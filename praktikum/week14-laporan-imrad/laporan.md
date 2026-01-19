
# Laporan Praktikum Minggu [14]
Topik: [Penyusunan Laporan Praktikum Format IMRAD]

---

## Identitas
- **Nama**  : [azid mirza maulana]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Judul
CPU Scheduling – FCFS dan SJF
---

## Pendahuluan
Penjadwalan CPU merupakan salah satu komponen penting dalam sistem operasi yang berfungsi untuk menentukan urutan eksekusi proses di dalam prosesor. Algoritma penjadwalan yang berbeda dapat menghasilkan performa sistem yang berbeda pula, terutama dalam hal waktu tunggu (waiting time) dan waktu penyelesaian (turnaround time).
Pada praktikum ini, dilakukan pengujian dua algoritma penjadwalan CPU, yaitu First Come First Served (FCFS) dan Shortest Job First (SJF). Tujuan dari praktikum ini adalah untuk membandingkan kinerja kedua algoritma tersebut berdasarkan parameter waktu tunggu rata-rata dan waktu penyelesaian rata-rata, serta mengevaluasi kesesuaiannya dengan teori penjadwalan CPU

---
## Rumusan masalah
- Bagaimana perbandingan kinerja algoritma FCFS dan SJF dalam hal average waiting time dan average turnaround time?
- Algoritma mana yang lebih efisien untuk meminimalkan waktu tunggu proses?
- Apa trade-off yang harus dipertimbangkan dalam memilih algoritma scheduling?

## Tujuan
1. Mengimplementasikan algoritma CPU scheduling FCFS dan SJF
2. Menganalisis kinerja kedua algoritma berdasarkan waiting time dan turnaround time
3. Memahami karakteristik, kelebihan, dan kekurangan masing-masing algoritma
4. Membandingkan hasil implementasi dengan teori yang ada

## Metode (Methods)
- Sistem Operasi: Windows 10
- Bahasa Pemrograman: Python
- Tools: Visual Studio Code


## Deskripsi Algoritma
1. First-Come, First-Served (FCFS)
FCFS adalah algoritma scheduling non-preemptive yang paling sederhana. Proses dilayani berdasarkan urutan kedatangan (arrival time). Proses yang datang lebih awal akan dieksekusi terlebih dahulu hingga selesai.

2. Shortest Job First (SJF)
SJF adalah algoritma scheduling yang memilih proses dengan burst time terpendek untuk dieksekusi terlebih dahulu. Algoritma ini dapat bersifat preemptive atau non-preemptive. Dalam praktikum ini, digunakan SJF non-preemptive.


## Langkah Eksperimen
1. Persiapan Data
- Definisikan dataset proses dengan arrival time dan burst time
- Validasi input data
2. Implementasi FCFS
- Urutkan proses berdasarkan arrival time
- Hitung completion time untuk setiap proses
- Hitung waiting time dan turnaround time
- Hitung metrik rata-rat
3. Implementasi SJF
- Simulasikan waktu eksekusi
- Pada setiap waktu, pilih proses dengan burst time terpendek yang sudah datang
- Hitung completion time untuk setiap proses
- Hitung waiting time dan turnaround time
- Hitung metrik rata-rata
4. Analisis
- Bandingkan hasil kedua algoritma
- Identifikasi kasus terbaik dan terburuk
- Dokumentasikan



## Hasil Eksekusi
- skenario normal
 Hasil Scheduling dengan FCFS (Dataset 1)
![Screenshot hasil](./screenshots/Hasil%20Scheduling%20dengan%20FCFS%20(Dataset%201).png)
Waktu Tunggu Rata-rata: 11,0 ms
Waktu Pemrosesan Rata-rata: 16,6 ms
Total Waktu Penyelesaian: 28 ms
Pemanfaatan CPU: 100%

 Hasil Scheduling dengan SJF (Dataset 1)
![Screenshot hasil](./screenshots/hasi%20scheduling%20dengan%20SJF%20(dataset%201).png)
Waktu Tunggu Rata-rata: 7,6 ms
Waktu Pemrosesan Rata-rata: 13,2 ms
Total Waktu Penyelesaian: 28 ms
Pemanfaatan CPU: 100%

Hasil Eksperimen Dataset 2 (Convoy Effect Test)
Hasil Scheduling dengan FCFS (Dataset 2)
![Screenshot hasil](./screenshots/Hasil%20Scheduling%20dengan%20FCFS%20(Dataset%202).png)
Waktu Tunggu Rata-rata: 16,0 ms
Waktu Pemrosesan Rata-rata: 26,0 ms
Total Waktu Penyelesaian: 30 ms
Pemanfaatan CPU: 100%

![Screenshot hasil](./screenshots/Hasil%20Scheduling%20dengan%20SJF%20(Dataset%202).png)
Waktu Tunggu Rata-rata: 16,0 ms
Waktu Pemrosesan Rata-rata: 26,0 ms
Total Waktu Penyelesaian: 30 ms
Pemanfaatan CPU: 100%

---
## psuedocode 

***FCFS***

Algorithm FCFS(processes):
    Sort processes by arrival_time
    current_time = 0
    
    For each process in processes:
        If current_time < process.arrival_time:
            current_time = process.arrival_time
        
        process.start_time = current_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = completion_time - arrival_time
        process.waiting_time = turnaround_time - burst_time
        
        current_time = process.completion_time
    
    Calculate average_waiting_time
    Calculate average_turnaround_time
    
    Return results
    

***SJF***

Algorithm SJF(processes):
    current_time = 0
    completed = 0
    ready_queue = []
    
    While completed < total_processes:
        Add all processes with arrival_time <= current_time to ready_queue
        
        If ready_queue is empty:
            current_time = next_arrival_time
            Continue
        
        Select process with minimum burst_time from ready_queue
        
        process.start_time = current_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = completion_time - arrival_time
        process.waiting_time = turnaround_time - burst_time
        
        current_time = process.completion_time
        completed += 1
        Remove process from ready_queue
    
    Calculate average_waiting_time
    Calculate average_turnaround_time
    
    Return results
    

## pembahasan
- 1 Efisiensi SJF dalam Meminimalkan Waiting Time
Hasil eksperimen menunjukkan bahwa SJF secara signifikan lebih baik dalam meminimalkan average waiting time. Pada dataset 1, SJF menghasilkan AWT 7.6 ms dibanding FCFS dengan 11.0 ms, menunjukkan improvement sebesar 30.9%. Ini sesuai dengan teori yang menyatakan bahwa SJF adalah algoritma optimal untuk meminimalkan average waiting time [1].
Keunggulan SJF terlihat jelas pada proses P4 dan P5 yang memiliki burst time pendek. Pada FCFS, P4 harus menunggu 18 ms, sedangkan pada SJF hanya 3 ms. Ini terjadi karena SJF memprioritaskan proses pendek, mencegah proses tersebut menunggu proses panjang yang datang lebih awal.

- .2 Convoy Effect pada FCFS
Dataset 2 dirancang khusus untuk mendemonstrasikan convoy effect, fenomena di mana banyak proses pendek harus menunggu satu proses panjang selesai. Pada kasus ini, P2 dan P3 yang masing-masing hanya membutuhkan 3 ms harus menunggu P1 (24 ms) selesai terlebih dahulu, menghasilkan waiting time yang sangat tinggi (23 ms dan 25 ms).
Menariknya, pada dataset 2, SJF menghasilkan hasil yang sama dengan FCFS. Ini terjadi karena ketika P1 mulai dieksekusi pada waktu 0, tidak ada proses lain yang sudah datang. Karena SJF yang diimplementasikan bersifat non-preemptive, P1 harus diselesaikan terlebih dahulu meskipun P2 dan P3 yang lebih pendek datang kemudian.
Ini mengungkap keterbatasan SJF non-preemptive: algoritma ini tidak dapat menginterupsi proses yang sedang berjalan bahkan jika datang proses dengan burst time lebih pendek. Solusinya adalah menggunakan Shortest Remaining Time First (SRTF), varian preemptive dari SJF [2].
---

## Kesimpulan
1. SJF lebih efisien secara global dengan menghasilkan average waiting time 30.9% lebih rendah (7.6 ms) dibanding FCFS (11.0 ms) dan average turnaround time 20.5% lebih rendah pada dataset normal, memvalidasi teori bahwa SJF adalah algoritma optimal untuk meminimalkan average waiting time.
2. Trade-off antara efisiensi dan fairness sangat nyata: SJF mengoptimalkan metrik rata-rata dengan mengorbankan proses individual (P2 mengalami degradasi waiting time 280%), sementara FCFS memberikan fairness yang lebih baik meskipun tidak optimal secara matematis.
3. Convoy effect merupakan masalah signifikan pada FCFS di mana proses pendek dapat mengalami waiting time sangat tinggi ketika harus menunggu proses panjang, namun SJF non-preemptive juga tidak dapat mengatasi masalah ini jika proses panjang sudah mulai dieksekusi.
4. Pemilihan algoritma harus kontekstual: FCFS cocok untuk sistem yang mengutamakan simplicity dan fairness, sementara SJF lebih sesuai untuk sistem dengan banyak proses pendek dan throughput menjadi prioritas, dengan catatan perlu mekanisme tambahan seperti aging untuk mencegah starvation.
5. Implementasi praktis memerlukan modifikasi: Sistem operasi modern tidak menggunakan FCFS atau SJF murni, melainkan kombinasi algoritma dengan mekanisme preemption, priority, dan aging untuk menyeimbangkan efisiensi, fairness, dan responsiveness.



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
