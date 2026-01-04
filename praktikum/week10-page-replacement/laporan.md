
# Laporan Praktikum Minggu [10]
Topik: ["Manajemen Memori – Page Replacement FIFO & LRU"]

---

## Identitas
- **Nama**  : azid mirza maulana  
- **NIM**   : 250202933 
- **Kelas** : 1ikrb

---

## Tujuan
1. Mengimplementasikan algoritma FIFO dan LRU.
2. Menghitung jumlah page fault.
3. Membandingkan performa kedua algoritma.


---

## Dasar Teori
1. Page replacement adalah mekanisme penggantian halaman di memori utama ketika
terjadi page fault dan tidak tersedia frame kosong.
2. FIFO mengganti halaman yang pertama kali masuk ke memori tanpa
memperhatikan frekuensi penggunaan
3. LRU mengganti halaman yang paling lama tidak digunakan berdasarkan riwayat
akses.
---

## Langkah Praktikum
1. Dataset Uji
Reference string:
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
Jumlah frame: 3

2. Alur Program
1.Membaca reference string.
2.Mensimulasikan FIFO dan LRU.
3.Menghitung page hit dan page fault.
4.Menampilkan hasil ke terminal.

3. Hasil Simulasi

| Algoritma | Page Fault | Keterangan |
|---------|------------|-----------|
| FIFO | 10 | Kurang efisien |
| LRU | 9 | Lebih optimal |


---
## kode perintah
def read_reference_string(filename):
    with open(filename, 'r') as file:
        return [int(x.strip()) for x in file.read().split(',')]


def fifo_page_replacement(ref, frames):
    memory = []
    page_faults = 0
    index = 0

    print("\n=== FIFO Page Replacement ===")
    for page in ref:
        if page in memory:
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[index] = page
                index = (index + 1) % frames
        print(f"Page {page} -> {memory} ({status})")

    return page_faults


def lru_page_replacement(ref, frames):
    memory = []
    recent = {}
    page_faults = 0
    time = 0

    print("\n=== LRU Page Replacement ===")
    for page in ref:
        time += 1
        if page in memory:
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda p: recent[p])
                memory[memory.index(lru_page)] = page
        recent[page] = time
        print(f"Page {page} -> {memory} ({status})")

    return page_faults


if __name__ == "__main__":
    reference_string = read_reference_string("reference_string.txt")
    frames = 3

    fifo_faults = fifo_page_replacement(reference_string, frames)
    lru_faults = lru_page_replacement(reference_string, frames)

    print("\n=== HASIL AKHIR ===")
    print(f"FIFO Page Faults : {fifo_faults}")
    print(f"LRU  Page Faults : {lru_faults}")





---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)
=== FIFO Page Replacement ===
Page 7 -> [7] (FAULT)
Page 0 -> [7, 0] (FAULT)
Page 1 -> [7, 0, 1] (FAULT)
Page 2 -> [2, 0, 1] (FAULT)
Page 0 -> [2, 0, 1] (HIT)
Page 3 -> [2, 3, 1] (FAULT)
Page 0 -> [2, 3, 0] (FAULT)
Page 4 -> [4, 3, 0] (FAULT)
Page 2 -> [4, 2, 0] (FAULT)
Page 3 -> [4, 2, 3] (FAULT)
Page 0 -> [0, 2, 3] (FAULT)
Page 3 -> [0, 2, 3] (HIT)
Page 2 -> [0, 2, 3] (HIT)

=== LRU Page Replacement ===
Page 7 -> [7] (FAULT)
Page 0 -> [7, 0] (FAULT)
Page 1 -> [7, 0, 1] (FAULT)
Page 2 -> [2, 0, 1] (FAULT)
Page 0 -> [2, 0, 1] (HIT)
Page 3 -> [2, 0, 3] (FAULT)
Page 0 -> [2, 0, 3] (HIT)
Page 4 -> [4, 0, 3] (FAULT)
Page 2 -> [4, 0, 2] (FAULT)
Page 3 -> [4, 3, 2] (FAULT)
Page 0 -> [0, 3, 2] (FAULT)
Page 3 -> [0, 3, 2] (HIT)
Page 2 -> [0, 3, 2] (HIT)

=== HASIL AKHIR ===
FIFO Page Faults : 10
LRU  Page Faults : 9

---

## Analisis
Analisis
LRU menghasilkan page fault lebih sedikit karena mempertimbangkan pola
penggunaan halaman sebelumnya, sedangkan FIFO tidak memperhatikan hal tersebut.


---

## Kesimpulan
1. FIFO mudah diimplementasikan namun kurang efisien.
2. LRU memberikan performa lebih baik pada sebagian besar kasus.
3. Pemilihan algoritma page replacement memengaruhi kinerja sistem.


---

## Quiz
 **1. Perbedaan utama FIFO dan LRU?**  
FIFO berdasarkan urutan masuk halaman, sedangkan LRU berdasarkan penggunaan terakhir.

**2. Mengapa FIFO dapat menyebabkan Belady’s Anomaly?**  
Karena FIFO tidak mempertimbangkan pola penggunaan halaman.

**3. Mengapa LRU lebih baik dari FIFO?**  
Karena LRU memanfaatkan prinsip locality of reference.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
