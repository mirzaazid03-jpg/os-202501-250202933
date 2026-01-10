
# Laporan Praktikum Minggu [12]
Topik: ["Virtualisasi Menggunakan Virtual Machine"]

---

## Identitas
- **Nama**  : [azid mirza maulana]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan
Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
Membuat dan menjalankan sistem operasi guest di dalam VM.
Mengatur konfigurasi resource VM (CPU, RAM, storage).
Menjelaskan mekanisme proteksi OS melalui virtualisasi.
Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
Virtualisasi
Virtualisasi adalah teknik yang memungkinkan pembuatan lingkungan komputasi virtual yang terisolasi dari sistem fisik. Setiap lingkungan virtual dapat menjalankan sistem operasi dan aplikasi sendiri seolah-olah berjalan pada perangkat keras terpisah.

Virtual Machine
Virtual Machine (VM) adalah representasi perangkat komputer dalam bentuk perangkat lunak yang memiliki CPU, memori, storage, dan perangkat jaringan virtual.


Host OS dan Guest OS
Host OS adalah sistem operasi utama yang berjalan langsung di atas perangkat keras.
Guest OS adalah sistem operasi yang berjalan di dalam virtual machine.

Hypervisor
Hypervisor merupakan lapisan perangkat lunak yang bertugas mengelola dan membagi resource hardware kepada satu atau lebih VM. Contoh hypervisor adalah Oracle VirtualBox dan VMware.

Isolasi dan Keamanan VM
Virtualisasi menyediakan isolasi antar sistem sehingga kegagalan atau serangan pada guest OS tidak langsung memengaruhi host OS. Konsep ini mendukung sandboxing dan hardening sistem operasi.
---

## Langkah Praktikum
1. Menginstal VirtualBox atau VMware pada host OS.
2. Mengaktifkan fitur virtualisasi (VT-x / AMD-V) di BIOS.
3. Membuat VM baru dan memilih OS guest.
4. Mengatur resource awal VM:
CPU: 1–2 core
RAM: 2–4 GB
Storage: minimal 20 GB
5. Melakukan instalasi sistem operasi guest hingga selesai.
6. Mengubah konfigurasi resource dan mengamati performa sistem.
7. Mengambil screenshot setiap tahap penting.

---

## kode perintah
- Mengecek user yang sedang aktif
whoami

- Menampilkan informasi detail kernel dan arsitektur sistem
uname -a

- Menampilkan daftar file di direktori saat ini
ls

- Mengecek penggunaan Memori (RAM) 
free -h



---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil]()

Hasil Instalasi VM

Instalasi sistem operasi guest Ubuntu Linux berhasil dilakukan. Sistem dapat melakukan login dan berjalan dengan normal di dalam virtual machine.

Konfigurasi Resource
Perubahan konfigurasi resource memberikan dampak terhadap performa VM, terutama pada kecepatan respon sistem dan kemampuan menjalankan aplikasi.
---
Konfigurasi	CPU	RAM	Keterangan
Awal	1 Core	2 GB	Sistem berjalan normal namun cukup lambat
Diubah	2 Core	4 GB	Performa sistem lebih responsif

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
- Virtualisasi memungkinkan menjalankan lebih dari satu sistem operasi pada satu perangkat keras.

- Virtual machine mempermudah proses pengujian dan pembelajaran sistem operasi.

- Konfigurasi resource sangat memengaruhi performa guest OS.

- Virtualisasi meningkatkan keamanan melalui isolasi sistem.
---

## Quiz
1. Apa perbedaan antara host OS dan guest OS?
Host OS berjalan langsung pada hardware, sedangkan guest OS berjalan di dalam virtual machine.

2. Apa peran hypervisor dalam virtualisasi?
Hypervisor bertugas mengelola resource hardware dan mendistribusikannya ke virtual machine.

3. Mengapa virtualisasi meningkatkan keamanan sistem?
Karena adanya isolasi antara host dan guest sehingga gangguan pada satu sistem tidak memengaruhi sistem lainnya.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
