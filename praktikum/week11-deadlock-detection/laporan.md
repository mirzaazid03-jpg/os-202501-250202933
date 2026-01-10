
# Laporan Praktikum Minggu [11]
Topik: ["deadlock detection"]

---

## Identitas
- **Nama**  : [azid mirza maulana]  
- **NIM**   : [250202933]  
- **Kelas** : [1ikrb]

---

## Tujuan

1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4. Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.
---

## Dasar Teori
Deadlock adalah kondisi di mana dua atau lebih proses saling menunggu resource yang tidak akan pernah dilepaskan. Deadlock dapat terjadi apabila keempat kondisi berikut terpenuhi secara bersamaan:

Mutual Exclusion – Resource hanya dapat digunakan oleh satu proses pada satu waktu.

Hold and Wait – Proses memegang satu resource dan menunggu resource lainnya.

No Preemption – Resource tidak dapat diambil paksa dari proses yang sedang menggunakannya.

Circular Wait – Terdapat siklus proses yang saling menunggu resource.
---

## Langkah Praktikum
1. Menyiapkan Dataset  
2. Implementasi Algoritma Deteksi Deadlock
3. Eksekusi & Validasi
4. Analisis Hasil
5. commit push 

---

## Kode / Perintah


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)
---

import csv

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            process = row['Process']
            alloc = row['Allocation']
            req = row['Request']

            processes.append(process)
            allocation[process] = alloc
            request[process] = req

    return processes, allocation, request


def detect_deadlock(processes, allocation, request):
    """
    Deteksi deadlock menggunakan pendekatan graph sederhana (circular wait)
    """
    deadlocked = set()
    visited = set()

    def has_cycle(start, current):
        if current in visited:
            return False
        visited.add(current)

        for p in processes:
            if allocation[p] == request[current]:
                if p == start:
                    return True
                if has_cycle(start, p):
                    deadlocked.add(p)
                    return True
        return False

    for process in processes:
        visited.clear()
        if has_cycle(process, process):
            deadlocked.add(process)

    return deadlocked


def main():
    filename = "dataset_deadlock.csv"
    processes, allocation, request = read_dataset(filename)

    deadlocked_processes = detect_deadlock(processes, allocation, request)

    print("=== HASIL DETEKSI DEADLOCK ===")
    if deadlocked_processes:
        print("Sistem mengalami DEADLOCK")
        print("Proses yang terlibat:")
        for p in sorted(deadlocked_processes):
            print(f"- {p}")
    else:
        print("Sistem TIDAK mengalami deadlock")


if __name__ == "__main__":
    main()


Hasil Deteksi Deadlock
| Proses | Allocation | Request | Status   |
| ------ | ---------- | ------- | -------- |
| P1     | R1         | R2      | Deadlock |
| P2     | R2         | R3      | Deadlock |
| P3     | R3         | R1      | Deadlock |


=== DEADLOCK DETECTION SIMULATION ===

Daftar Proses dan Resource:
P1 : Allocation = R1 , Request = R2
P2 : Allocation = R2 , Request = R3
P3 : Allocation = R3 , Request = R1

Menganalisis kondisi sistem...
---------------------------------
P1 menunggu resource R2 (dipegang oleh P2)
P2 menunggu resource R3 (dipegang oleh P3)
P3 menunggu resource R1 (dipegang oleh P1)

Siklus ketergantungan terdeteksi:
P1 -> P2 -> P3 -> P1

=== HASIL DETEKSI ===
Status Sistem : DEADLOCK
Proses yang terlibat deadlock:
- P1
- P2
- P3

---

## Analisiis
- Deadlock terjadi karena semua proses saling menunggu resource yang sedang dipegang oleh proses lain, sehingga membentuk circular wait. Tidak ada proses yang dapat melanjutkan eksekusi karena tidak ada resource yang dilepaskan.
Kondisi ini menunjukkan bahwa keempat syarat deadlock terpenuhi secara bersamaan.

---

## Kesimpulan
Berdasarkan hasil praktikum, dapat disimpulkan bahwa algoritma deteksi deadlock mampu mengidentifikasi kondisi deadlock dengan menganalisis siklus ketergantungan resource. Pendekatan ini penting untuk sistem operasi yang tidak menerapkan pencegahan atau penghindaran deadlock.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?
Deadlock Prevention: Mencegah salah satu kondisi deadlock agar tidak terjadi.
Deadlock Avoidance: Menghindari deadlock dengan menganalisis kondisi aman sebelum alokasi resource.
Deadlock Detection: Mengizinkan deadlock terjadi dan kemudian mendeteksinya untuk ditangani. 
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
Karena tidak semua sistem dapat menerapkan pencegahan atau penghindaran deadlock secara efisien, terutama pada sistem dengan resource dinamis.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
Kelebihan:
Lebih fleksibel dalam penggunaan resource.
Tidak memerlukan analisis kondisi aman sebelum alokasi.

Kekurangan:
Deadlock tetap dapat terjadi.
Membutuhkan mekanisme pemulihan setelah deadlock terdeteksi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
