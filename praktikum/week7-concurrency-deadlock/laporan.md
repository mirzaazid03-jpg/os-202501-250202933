
# Laporan Praktikum Minggu [7]
Topik: [Sinkronisasi Proses dan Masalah Deadlock]

---

## Identitas
- **Nama**  : [azid mirza maulana]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan
1. Mengidentifikasi empat kondisi penyebab kebuntuan ( mutual exclusion, hold and wait, no preemption,circular wait ).
2. Menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor .
3. Menganalisis dan memberikan solusi untuk kasus kebuntuan.
4. Berkolaborasi dalam waktu untuk menyusun laporan analisis.
5. Menyajikan hasil studi kasus secara sistematis.

---

## Dasar Teori
- Sinkronisasi proses adalah mekanisme pengaturan jalannya beberapa proses yang berjalan secara bersamaan dalam sistem operasi agar tidak terjadi konflik dalam mengakses sumber daya atau data bersama. Sinkronisasi penting untuk menghindari inkonsistensi data yang dapat terjadi karena proses-proses tersebut dapat mengakses dan memodifikasi data secara bersamaan. Mekanisme ini menjamin bahwa proses yang bersaing untuk mengakses ke sumber daya bersama dapat melakukannya secara berurutan dan terkontrol, sehingga menghindari masalah seperti kondisi ras dan ketidakkonsistenan data.
- Masalah deadlock adalah kondisi dimana beberapa proses saling menunggu satu sama lain untuk melepaskan sumber daya yang dibutuhkan, sehingga tidak ada proses yang dapat melanjutkan eksekusinya. Deadlock terjadi bila empat kondisi utama terpenuhi sekaligus, yakni: mutualclusion (satu sumber daya hanya bisa digunakan satu proses pada suatu waktu), hold and wait (proses menahan satu sumber daya sambil menunggu sumber daya lain), no preemption (sumber daya tidak bisa diambil paksa dari proses yang memilikinya), dancircular wait (terdapat siklus menunggu sumber daya antar proses). Pemahaman dan penanganan deadlock memerlukan pengenalan kondisi ini serta penggunaan teknik sinkronisasi seperti semaphore dan monitor untuk mencegah atau mengatasi kebuntuan.

---

## Langkah Praktikum
1.  Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)

- Implementasikan versi sederhana dari masalah Dining Philosophers tanpa mekanisme pencegahan deadlock.
Contoh pseudocode:
while true:
  think()
  pick_left_fork()
  pick_right_fork()
  eat()
  put_left_fork()
  put_right_fork()


Philosopher i (i = 0 to 4):
while true:
    think()  // Filsuf berpikir
    pick_left_fork(i)   // Ambil garpu kiri (fork[i])
    pick_right_fork(i)  // Ambil garpu kanan (fork[(i+1) % 5])
    eat()               // Makan jika kedua garpu tersedia
    put_left_fork(i)    // Lepas garpu kiri
    put_right_fork(i)   // Lepas garpu kanan

- Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).

Simulasi langkah demi langkah untuk 5 filsuf (P0-P4) menunjukkan potensi deadlock
Waktu  | P0          | P1          | P2          | P3          | P4
-------|-------------|-------------|-------------|-------------|-------------
t0     | think       | think       | think       | think       | think
t1     | pick_left(0)| pick_left(1)| pick_left(2)| pick_left(3)| pick_left(4)
t2     | pick_right(0) # tunggu fork[1] | pick_right(1) # tunggu fork[2] | pick_right(2) # tunggu fork[3] | pick_right(3) # tunggu fork[4] | pick_right(4) # tunggu fork[0]
       |             |             |             |             | DEADLOCK!

Pada t2, semua filsuf memegang garpu kiri dan menunggu garpu kanan, membentuk siklus.


- Identifikasi kapan dan mengapa kebuntuan terjadi.

Deadlock terjadi ketika semua 5 filsuf secara bersamaan mengambil garpu kiri lalu mencoba garpu kanan, menyebabkan circular wait. Ini memenuhi 4 kondisi Coffman: mutual exclusion (satu garpu per filsuf), hold and wait (pegang kiri, tunggu kanan), no preemption (garpu tak bisa direbut), dan circular wait (P0→P1→P2→P3→P4→P0). Probabilitas tinggi pada sistem dengan scheduling nondeterministic, di mana timing eksekusi bersamaan memicu kebuntuan permanen kecuali intervensi eksternal
2. Eksperimen 2 – Versi Tetap (Menggunakan Semaphore / Monitor)

Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
Menggunakan semaphore (mutex) untuk mengontrol akses.
Membatasi jumlah filosof yang dapat dimakan secara bersamaan (maks 4).
pengaturan urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).
Analisis hasil modifikasi dan buktikan bahwa kebuntuan telah dihindari.

Modifikasi utama menggunakan semaphore "room" (init=4) untuk membatasi maksimal 4 filsuf mengambil garpu bersamaan, memecah circular wait. Filsuf ke-4 (P4) ambil garpu kanan dulu untuk asimetri tambahan

Semaphore room = 4;  // Maks 4 filsuf bersamaan
Semaphore fork[5] = {1,1,1,1,1};  // Binary semaphore per garpu

Philosopher i (i = 0 to 4):
while true:
    think()
    sem_wait(room)  // Masuk "ruang makan" (maks 4)
    if i == 4:      // Asimetri: P4 ambil kanan dulu
        sem_wait(fork[(i+1)%5])  // pick_right
        sem_wait(fork[i])        // pick_left
    else:
        sem_wait(fork[i])        // pick_left
        sem_wait(fork[(i+1)%5])  // pick_right
    eat()
    sem_post(fork[i])            // put_left
    sem_post(fork[(i+1)%5])      // put_right
    sem_post(room)               // Keluar ruang


    Simulasi Alur Versi Fixed
Waktu  | P0      | P1      | P2      | P3      | P4      | Room | Status
-------|---------|---------|---------|---------|---------|------|-------
t0     | think   | think   | think   | think   | think   | 4    | 
t1     | room↓   | room↓   | room↓   | room↓   | -       | 0    | 4 filsuf masuk
t2     | L0↓ R1↓ | L1↓ R2↓ | L2↓ R3↓ | L3↓ R4↓ | -       | 0    | Semua makan
t3     | eat↑    | eat↑    | eat↑    | eat↑    | -       | 0    | 
t4     | room↑   | room↑   | room↑   | room↑   | room↓   | 1    | P4 masuk, prioritas
ada minimal 1 garpu bebas karena room=4, P4 dapat ambil keduanya.

Bukti Kebuntuan Dihindari
Circular wait dipatahkan karena semaphore room memastikan maksimal 4 filsuf pegang garpu, meninggalkan minimal 1 garpu bebas. Philosopher yang dapat akses room pasti dapat garpu kedua tanpa siklus penuh.​
----

| Kondisi Coffman  | Versi Deadlock | Versi Fixed Solusi          |
| ---------------- | -------------- | --------------------------- |
| Mutual Exclusion | Ya             | Tetap (semaphore binary)    |
| Hold & Wait      | Ya             | Tetap tapi terbatas room=4  |
| No Preemption    | Ya             | Tetap (tidak diubah)        |
| Circular Wait    | Ya             | Tidak- room=4 jamin 1 bebas |

Starvation dicegah oleh fairness semaphore (FIFO queue). Asimetri P4 tambahan kurangi konflik.

----
3. Eksperimen 3 – Analisis Kebuntuan

Menjelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut menyelesaikan pada versi fixed.

Sajikan hasil analisis dalam tabel seperti contoh berikut:

Kondisi Deadlock	Terjadi di Versi Deadlock	Solusi di Versi Fixed
Pengecualian Bersama	Ya (satu garpu hanya satu proses)	Gunakan semaphore untuk mengontrol akses
Tahan dan Tunggu	Ya	Hindari proses menahan lebih dari satu sumber daya
Tidak Ada Pendahuluan	Ya	Tidak ada mekanisme pelepasan paksa
Menunggu Melingkar	Ya	Ubah urutan pengambilan sumber daya

4. Eksperimen 4 – Dokumentasi

Simpan semua diagram, simulasi tangkapan layar, dan hasil diskusi di:
praktikum/week7-concurrency-deadlock/screenshots/
Tuliskan laporan kelompok di laporan.md(format IMRaD singkat: Pendahuluan, Metode, Hasil, Analisis, Diskusi ).

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Eksperimen pertama, 5 filsuf dapat mencapai deadlock permanen saat semua mengambil garpu kiri bersamaan lalu menunggu garpu kanan, memenuhi 4 kondisi Coffman secara penuh. Simulasi alur mengilustrasikan circular wait (P0→F1→P1→F2→...→P4→F0), menyebabkan sistem terkunci total tanpa kemajuan. Hasil ini membuktikan bahaya race condition dan urutan pengambilan sumber daya yang simetris dalam sistem konkuren.​
-ekperimen kedua Modifikasi dengan semaphore room=4 dan asimetri P4 mematahkan circular wait karena selalu ada minimal 1 garpu bebas, memungkinkan progres kontinu. Simulasi menunjukkan 4 filsuf makan bergantian sementara 1 menunggu, menghindari kebuntuan sambil mempertahankan paralelisme maksimal. Teknik ini menjamin liveness (tidak ada starvation) melalui fairness semaphore FIFO.​

---

## Kesimpulan
Kesimpulan Eksperimen Sinkronisasi & Deadlock
Eksperimen Dining Philosophers membuktikan bahwa implementasi tanpa sinkronisasi menyebabkan deadlock permanen melalui circular wait saat semua filsuf mengambil garpu kiri bersamaan, memenuhi 4 kondisi Coffman. Modifikasi dengan semaphore room=4 dan asimetri berhasil mematahkan circular wait, menjamin progres kontinu karena selalu ada minimal 1 garpu bebas.​

1.Pencegahan > Deteksi: Mengontrol akses sumber daya (semaphore) lebih efisien daripada recovery deadlock.​

2. Kondisi Kritis: Sinkronisasi esensial untuk hindari race condition di sistem konkuren seperti multi-threading dan database locks.​

3. Praktik Industri: Teknik ini diterapkan di Linux mutex, Java synchronized, dan Web3 smart contract concurrency.​

---

## Quiz
1. [anggapan empat kondisi utama menyebabkan kebuntuan]  
   **Jawaban:**  Empat kondisi utama yang menyebabkan kebuntuan (deadlock) dalam sistem operasi adalah pengecualian bersama (mutual exclusion), tahan dan tunggu (hold and wait), tidak ada preemption (no preemption), serta tunggu melingkar (circular wait). dikenal sebagai kondisi Coffman, harus terjadi secara bersamaan agar kebuntuan muncul, di mana proses saling menunggu sumber daya satu sama lain tanpa kemajuan.
2. [Mengapa sinkronisasi diperlukan dalam sistem operasi?]  
   **Jawaban:**  Sinkronisasi diperlukan dalam sistem operasi untuk mengatur akses bersamaan oleh beberapa proses terhadap sumber daya bersama, sehingga mencegah inkonsistensi data akibat race condition di mana proses saling bertabrakan saat membaca atau menulis data yang sama.​
   1. Mencegah Race Condition
   2. Menjaga Konsistensi Data
   3. Mengatur Urutan Proses
3. [Menjelaskan perbedaan antara semaphore dan monitor .]  
   **Jawaban:**  Semaphore dan monitor merupakan mekanisme sinkronisasi dalam sistem operasi untuk mengelola akses proses ke sumber daya bersama, tetapi semaphore menggunakan variabel integer dengan operasi wait (P) dan signal (V) yang low-level, sedangkan monitor adalah struktur high-level yang menyediakan mutual exclusion otomatis melalui prosedur eksklusif.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
