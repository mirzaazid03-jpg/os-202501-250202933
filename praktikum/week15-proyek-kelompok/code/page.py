import csv

def simulasi_page_replacement_lru():
    """
    Fungsi ini digunakan untuk mensimulasikan algoritma
    Page Replacement Least Recently Used (LRU).
    aplikasi_medsos.csv.
    """

    # ==============================
    # KONFIGURASI AWAL
    # ==============================

    # Jumlah frame RAM (misalnya RAM hanya bisa menampung 3 aplikasi)
    jumlah_frame = 3

    # List untuk menyimpan urutan aplikasi dari file CSV
    daftar_aplikasi = []

    # ==============================
    # MEMBACA DATA DARI FILE CSV
    # ==============================

    try:
        with open("aplikasi_medsos.csv", "r") as file:
            reader = csv.DictReader(file)

            # Membaca setiap baris dan mengambil kolom "aplikasi"
            for baris in reader:
                aplikaappened (baris["aplikasi"])

    except FileNotFoundError:
        print("File aplikasi.csv tidak ditemukan!")
        return

    # ==============================
    # VARIABEL SIMULASI
    # ==============================

    # List untuk menyimpan isi RAM saat simulasi
    isi_ram = []

    # Menghitung jumlah page fault
    total_page_fault = 0

    # ==============================
    # TAMPILAN HEADER
    # ==============================

    print("\n=== SIMULASI PAGE REPLACEMENT LRU (LEAST RECENTLY USED) ===")
    print("=" * 70)
    print(f"Jumlah Frame RAM : {jumlah_frame}")
    print("=" * 70)

    print(f"| {'Aplikasi':<12} | {'Isi RAM Saat Ini':<35} | {'Page Fault':<12} |")
    print("-" * 70)

    # ==============================
    # PROSES SIMULASI LRU
    # ==============================

    for aplikasi in daftar_aplikasi:
        status_page_fault = "No"

        # Jika aplikasi sudah ada di RAM
        if aplikasi in isi_ram:
            # Aplikasi dipindahkan ke posisi paling akhir
            isi_ram.remove(aplikasi)
            isi_ram.append(aplikasi)

        else:
            # Terjadi page fault
            total_page_fault += 1
            status_page_fault = "Yes"

            # Jika RAM masih memiliki slot kosong
            if len(isi_ram) < jumlah_frame:
                isi_ram.append(aplikasi)
            else:
                # Menghapus aplikasi yang paling lama tidak digunakan
                isi_ram.pop(0)
                isi_ram.append(aplikasi)

        # Mengubah isi RAM menjadi string agar rapi saat ditampilkan
        isi_ram_str = ", ".join(isi_ram)

        # Menampilkan hasil setiap langkah
        print(f"| {aplikasi:<12} | {isi_ram_str:<35} | {status_page_fault:<12} |")

    # ==============================
    # HASIL AKHIR
    # ==============================

    print("-" * 70)
    print(f"Total Page Fault : {total_page_fault}")
    print("=" * 70)


# ==============================
# MENJALANKAN PROGRAM
# ==============================

simulasi_page_replacement_lru()
